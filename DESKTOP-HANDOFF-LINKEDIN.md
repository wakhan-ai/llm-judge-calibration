# Desktop ChatGPT handoff — LinkedIn Beyond Agreement publishing

**Checkpoint:** 27 November 2026.  
**Goal:** Resume exactly where the web ChatGPT thread stopped, using the desktop app's connected browser / Work mode to publish the prepared LinkedIn research article. This document is a continuity note, not a scientific result or confirmation of publication.

## Immediate action

1. User is attempting to switch from ChatGPT web to desktop because the connected browser needed for LinkedIn publishing is associated with the desktop session, but latest messages are not appearing across devices.
2. Open LinkedIn profile **https://www.linkedin.com/in/wabbasuk/** in the user's connected browser and allow the user to log in if needed.
3. Create a **LinkedIn article** (not merely a feed post) titled: **Beyond Agreement: What Real LLM Judge Experiments Reveal About Evidence, Verification and Risk**.
4. Use the complete research manuscript: [BEYOND-AGREEMENT.md](phase-2-scifact/articles/BEYOND-AGREEMENT.md). Ensure formatted tables, sources and methodological cautions survive adaptation to the LinkedIn editor.
5. Add a cover/hero graphic previously generated in the web conversation. It was saved in that session at `/mnt/data/beyond_agreement_ai_judgment_and_verification.png` (this path may **not** be accessible from desktop; ask for the image to be reattached or regenerate a matching graphic if missing). The image depicts LLM judge, evidence verification and risk in a clean white/blue/teal 16:9 research banner.
6. Include at the end the explicitly prospective **VARE Research Phase II+ — Completing the Missing Evidence Before Publication** research programme: [VARE-PHASE-II-PLUS.md](phase-2-scifact/articles/VARE-PHASE-II-PLUS.md). Present this as **future experiments**, never as already measured findings.
7. The user asked to publish the article and associated announcement, with all GitHub research links and references. Publishing actions should follow connected-browser authorisation and the user's chosen visibility / final confirmation.
8. Once the real LinkedIn article URL exists, **add it back into GitHub** article manuscript, roadmap and README files using the connected GitHub account `wakhan-ai`. Do not guess or invent the LinkedIn URL.

## GitHub source of truth

Repository: **https://github.com/wakhan-ai/llm-judge-calibration** (public).  
Article: https://github.com/wakhan-ai/llm-judge-calibration/blob/main/phase-2-scifact/articles/BEYOND-AGREEMENT.md  
Phase II+ programme: https://github.com/wakhan-ai/llm-judge-calibration/blob/main/phase-2-scifact/articles/VARE-PHASE-II-PLUS.md  
Research folder: https://github.com/wakhan-ai/llm-judge-calibration/tree/main/phase-2-scifact  
Evidence: https://github.com/wakhan-ai/llm-judge-calibration/tree/main/phase-2-scifact/evidence  
Protocol: https://github.com/wakhan-ai/llm-judge-calibration/blob/main/phase-2-scifact/PROTOCOL.md

Both README files and both article markdown files were committed and verified in the web ChatGPT thread. No LinkedIn publishing action has yet been completed.

## Core empirical claims, as reported in repository

- Phase I is **synthetic simulation** (600 records; not real LLM outputs); do not mix with Phase II.
- SciFact 5,183 abstracts, 809 labelled train, 300 labelled dev, 300 unlabelled official test.
- Of 188 dev claims with annotated evidence, top-5 retrieved annotated documents: title-only **115/188** versus title+abstract **168/188** (28.2 percentage-point gain); document retrieval only, not judge success.
- Real model 30-claim pilot (GPT-4.1 Mini): plain, rubric, same-model VARE all false accepted **3/20** non-SUPPORT claims. VARE review load **17/30**, plain **0/30**. More verification did not prevent false accepts.
- 15-claim development verifier follow-up had zero baseline false accepts; therefore no evidence of verifier correction of false acceptance in that sample.
- 41-claim document-disjoint comparison: all methods eight review slots; rubric **2/20** false accepts vs full-abstract Gemini 2.5 Flash verifier **1/20**; correct auto accepts **17/21** vs **18/21** respectively. Only **one** CONTRADICT case; single-case difference, no conclusive superiority.
- 97-claim contradiction-enriched development stress test: 47 CONTRADICT claims, 19 review slots. Plain **0** residual contradiction false accepts, rubric **3**, same-model cited verifier **0**, Gemini Flash full **1**, Gemini Pro full **0**. Pro's performance partly reflects response truncation causing review, not semantic detection. This cohort overlaps evidence documents with training/prior tests, not independent final confirmation.
- Not yet validated: deterministic numerical/endpoint/unit checks, category-specific calibrated risk policies, independent severity costs, evidence-removal stability controls, large fresh grouped holdout or external FEVEROUS benchmark.
- Style for article: natural, technically rigorous and clear; transparent limitations and negative results; avoid exaggeration or regulatory endorsement.

## Proposed LinkedIn accompanying announcement

Following my earlier research on LLM judge calibration, I wanted to move beyond simulated results and examine how actual AI evaluators perform against scientific evidence.

The feedback on my previous articles raised some important questions: Can an evaluator miss serious errors despite performing well overall? Does adding another AI model improve verification? And how do we know when human review is genuinely necessary?

My latest article, **“Beyond Agreement: What Real LLM Judge Experiments Reveal About Evidence, Verification and Risk,”** explores these questions using real model experiments on the public SciFact benchmark.

The findings were interesting, and not always what I expected. Better evidence retrieval made a measurable difference, while adding another verifier did not consistently improve reliability. Some configurations also introduced substantial review overhead.

I've included the research methods, experimental results, limitations and code in the public GitHub repository.

This work also establishes the next research direction, **VARE Research Phase II+**, where I plan to investigate the remaining gaps through further controlled experiments.

The goal is to understand what genuinely makes AI evaluation more reliable, rather than assuming that adding more checks automatically makes it better.

Research and reproducibility: https://github.com/wakhan-ai/llm-judge-calibration

#AIResearch #LLMasAJudge #AIEngineering #TrustworthyAI #AgenticAI

## Desktop sync issue

The user reports that the desktop app does **not** show the latest web-thread messages. ChatGPT's conversational Memory is not guaranteed to mirror a full transcript or update instantly; this GitHub file is the durable task handoff. The desktop session can open this exact URL even if chat sync remains broken.

## Definition of done

LinkedIn article created with banner and references; optional accompanying feed post published; actual LinkedIn article URL captured and GitHub research documentation back-linked. Until then, report publication as pending.
