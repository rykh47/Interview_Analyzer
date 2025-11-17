```markdown
# System Flow Diagram

## AI Interview Analyzer - Process Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                        USER INTERFACE                            │
│                      (Streamlit App)                             │
└────────────────────────────┬────────────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │  Input Selection │
                    │  - Audio File    │
                    │  - Text Transcript│
                    └────────┬─────────┘
                             │
                ┌────────────┴────────────┐
                │                         │
                ▼                         ▼
    ┌───────────────────┐    ┌────────────────────┐
    │  Audio File       │    │  Text Transcript  │
    │  Upload           │    │  (Direct Input)   │
    └─────────┬─────────┘    └─────────┬──────────┘
              │                        │
              │                        │
              ▼                        │
    ┌───────────────────┐             │
    │  Audio Processor  │             │
    │  (Whisper STT)    │             │
    └─────────┬─────────┘             │
              │                        │
              └────────────┬───────────┘
                           │
                           ▼
              ┌──────────────────────┐
              │   Text Transcript     │
              │   (Normalized)        │
              └───────────┬───────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ AI Analyzer  │  │  Sentiment   │  │  Keyword     │
│ (Gemini API) │  │  Analyzer    │  │  Extractor   │
│              │  │  (VADER)     │  │              │
└──────┬───────┘  └──────┬───────┘  └──────┬───────┘
       │                 │                  │
       │                 │                  │
       └─────────────────┼──────────────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │  Report Generator    │
              │  - Structure Data    │
              │  - Create Charts     │
              │  - Generate Insights│
              └───────────┬──────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│  Dashboard   │  │  PDF Report  │  │  Visualizations│
│  Display     │  │  Generator   │  │  (Plotly)    │
│  (Streamlit) │  │  (ReportLab) │  │              │
└──────────────┘  └──────┬───────┘  └──────┬───────┘
                         │                  │
                         └────────┬─────────┘
                                  │
                                  ▼
                        ┌──────────────────┐
                        │  Final Output    │
                        │  - Interactive   │
                        │    Dashboard     │
                        │  - PDF Report    │
                        │  - Visualizations│
                        └──────────────────┘
```
