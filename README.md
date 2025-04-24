# LLM with RAG

This repository implements **Retrieval-Augmented Generation (RAG)** with **Large Language Models (LLMs)**. It focuses on combining knowledge retrieval systems with generative language models to enhance the accuracy and relevance of generated outputs.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)

## Introduction

In this project, we explore the integration of retrieval mechanisms with LLMs for tasks requiring domain-specific knowledge or enhanced context understanding. The approach bridges the gap between static knowledge in pre-trained models and dynamic knowledge retrieval.

## Features

- **Knowledge Retrieval**: Fetch relevant documents from a knowledge base.
- **Augmented Generation**: Use retrieved knowledge to assist language generation.
- **Modular Design**: Easy to adapt and extend for other use cases.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/srivarshini-21/LLM_with_RAG.git
   cd LLM_with_RAG
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

To run the project, you need to add your **Gemini API Key**. Follow these steps:

1. Obtain your Gemini API Key from the Gemini platform.
2. Create a `.env` file in the root directory of the project.
3. Add the following line to the `.env` file:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```
   Replace `your_api_key_here` with your actual Gemini API Key.

## Usage

1. Start the retrieval-augmented generation pipeline:
   ```bash
   python app.py
   ```

3. Customize streamlit in `app.py` as needed.

4. Explore various other models as per your requirements by editing the `rag_pipeline.py`.

5. Try out the RAG model by uploading any PDF file and asking questions related to the PDF to get required answers.
