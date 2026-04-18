# Parallel Chain Architecture

## Process Flow

| Stage | Left Branch | Right Branch |
|-------|-------------|--------------|
| **Input** | Parallel<notes,quiz>Input | |
| **Prompt** | PromptTemplate | PromptTemplate |
| **LLM** | ChatOllama | ChatOllama |
| **Output Parser** | StrOutputParser | StrOutputParser |
| **Combined** | Parallel<notes,quiz>Output | |
| **Final Prompt** | PromptTemplate | |
| **Final LLM** | ChatOllama | |
| **Final Parser** | StrOutputParser | |
| **Result** | StrOutputParserOutput | |