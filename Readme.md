# TraceCall-ai

This project automates customer support call quality analysis by converting call recordings into fully structured QA reports, including:

- Agent performance scoring

- Customer sentiment analysis

- Compliance & risk detection

- Timestamp-linked evidence

- Coaching recommendations

- Process improvement insights

It is designed for QA teams, compliance teams, contact centers, and operations leaders who need scalable, consistent, and auditable call reviews.


**Transforming raw calls --> Actionable operational insights.**

## Architecture & Workflow

![CallSense AI Workflow](./workflow.png)

#### Key Design Principles

- Modular & containerized

- Model-agnostic (ASR & LLMs)

- Evidence-based (timestamps for every claim)

- Compliance-aware by design

## Key Capabilities

- 🎙 High-accuracy ASR using **NVIDIA Whisper** (Docker container).

- ⏱ Precise timestamp segmentation (30s timestamps).

- 🤖 Deep conversational analysis using **qwen3-next-80b-a3b-instruct**.

- 📊 Agent performance scoring (0->10).

- 😊 Customer sentiment & satisfaction prediction.

- ⚠ Compliance & operational risk detection.

- 🧾 Audit-ready structured JSON - split information to different teams depending on interest.

- 📝 Executive-ready narrative reports.

- 📧 Automated email delivery to QC teams using **Gmail API**.

## 🎧 Sample Customer Support Call

A real **11:30 mins** customer support call recording used to generate the example QA report:

▶️ **[Customer_Support_Call_1.wav](./Customer_Support_Call_1.wav)**

> This audio file is provided for demonstration purposes and is analyzed automatically by CallSense AI to generate structured QA, sentiment, and compliance insights

## 📄 Sample AI-Generated Call Report

A concise example of an automatically generated QA report produced by CallSense AI:

📄 **[Call*Report_1*(Brief).pdf](<./Call_Report_1_(Brief).pdf>)**


📄 **[Call*Report_2*(Detailed_more_spaced).pdf](<./Call_Report_2_(Detailed_more_spaced).pdf>)**

> This report was generated directly from the sample call audio using the full CallSense AI analysis pipeline.

