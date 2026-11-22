"""Synthetic demonstration only. No human reviewers, LLM calls or real MLR outcomes."""
import numpy as np, pandas as pd
from sklearn.metrics import cohen_kappa_score, confusion_matrix, brier_score_loss, roc_auc_score
from sklearn.linear_model import LogisticRegression
rng=np.random.default_rng(20261122)
n=600
# Synthetic case-mix with 30% unacceptable cases; 3 domain strata.
category=np.resize(np.array(['evidence_support','qualification','context']), n)
rng.shuffle(category)
y=np.zeros(n,dtype=int)
for c in np.unique(category):
 idx=np.flatnonzero(category==c)
 y[rng.choice(idx, size=round(len(idx)*0.3),replace=False)]=1
# judge raw scores are simulated, with domain-specific limitations and noise
z=rng.normal(0,1,n)+ np.where(y==1,1.15,-1.15)
z+=np.select([category=='evidence_support',category=='qualification',category=='context'],[-0.55,-0.15,0.30],default=0)
raw=1/(1+np.exp(-z))
# first 300 development; remainder held out. Only calibrate on dev.
train=np.arange(n)<300
model=LogisticRegression().fit(raw[train].reshape(-1,1), y[train])
cal=model.predict_proba(raw.reshape(-1,1))[:,1]
pred_raw=(raw>=0.5).astype(int)
pred_cal=(cal>=0.35).astype(int) # illustrative cost-sensitive cutoff, NOT tuned on test
# Selective policy: defer borderline estimated risk to hypothetical perfect expert for workload count only.
defer=(cal>=0.20)&(cal<0.60)
# Do NOT count deferred as auto correct; evaluate auto decisions conditional on coverage.
def metrics(y,p):
 tn,fp,fn,tp=confusion_matrix(y,p,labels=[0,1]).ravel()
 return {'n':len(y),'TP':int(tp),'FN':int(fn),'FP':int(fp),'TN':int(tn),'accuracy':(tp+tn)/len(y),'kappa':cohen_kappa_score(y,p),'sensitivity':tp/(tp+fn),'specificity':tn/(tn+fp),'false_acceptance_rate':fn/(tp+fn)}
rows=[]
for label,mask,pred in [('General judge',~train,pred_raw),('Calibrated/risk cutoff',~train,pred_cal),('Auto-only selective',(~train)&(~defer),pred_cal)]:
 r=metrics(y[mask],pred[mask]);r['configuration']=label;rows.append(r)
res=pd.DataFrame(rows).set_index('configuration')
print(res.to_string(float_format=lambda f: f'{f:.3f}'))
print('holdout_count',sum(~train),'holdout_deferral_count',sum((~train)&defer),'coverage',sum((~train)&(~defer))/sum(~train))
print('holdout Brier raw',round(brier_score_loss(y[~train],raw[~train]),4),'cal',round(brier_score_loss(y[~train],cal[~train]),4))
print('holdout auc',round(roc_auc_score(y[~train],raw[~train]),4))
df=pd.DataFrame({'id':[f'SYN-{i+1:04d}' for i in range(n)],'case_type':category,'reference_unacceptable':y,'simulated_raw_judge_score':raw.round(5),'calibrated_score':cal.round(5),'split':np.where(train,'development','test'),'general_judge_flag':pred_raw,'calibrated_flag':pred_cal,'defer_to_expert':defer.astype(int)})
df.to_csv('synthetic_cases.csv',index=False)
res.to_csv('simulation_results.csv')
