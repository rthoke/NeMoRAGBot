# NeMoRAGBot

A Retrieval-Augmented Generation (RAG) chatbot powered by NVIDIA's NeMo Guardrails for secure, context-aware, and dynamic conversational AI. This project ensures safety, accuracy, and reliability, making it ideal for customer support, knowledge management, and Q&A systems.

## Features

- **RAG Framework**: Combines retrieval techniques with generative AI for precise and informed responses.
- **NeMo Guardrails**: Ensures conversational safety, adherence to constraints, and improved reliability.
- **Customizable**: Adaptable for various use cases like customer service, education, and interactive knowledge bases.
- **Secure Deployment**: Built with safety-first principles for robust application.

## Requirements

Before running the project, ensure you have the following installed:

- Python >= 3.8
- NVIDIA NeMo toolkit
- Required libraries (install with `requirements.txt`)

## Installation

1. Clone this repository:
   git clone https://github.com/rthoke/NeMoRAGBot.git
   cd NeMoRAGBot
  
2. Install dependencies:
   !pip install -qU nemoguardrails "langchain-chroma>=0.1.2" pypdf langchain-nvidia-ai-endpoints langchain_community PyPDF2 openai requests langchain_community tqdm langchain_nvidia_ai_endpoints  llama-index-embeddings-huggingface

3. To start the vector database , run the following command:
    python3 chroma_db.py

4. To start the chatbot, run the following command:
    python3 rag_nemo.py
   This will run or the terminal. Customize configurations in config.yaml as per your requirements and attached UI as per you need

## Configuration
  Modify the config.yaml file to adjust:
  
  Retrieval settings
  Guardrails (conversation constraints)

   
