# LangChain URL Summarizer with Groq

Demo video Link :- https://drive.google.com/file/d/1cmlMIaWtHgnmjHN969gJPtIGPIu-e8vL/view?usp=sharing

This Streamlit application allows you to summarize content from YouTube videos or website URLs using LangChain and the Groq LLM. It provides a quick and easy way to get concise summaries of online content.

## Features

* **Summarize YouTube Videos:** Extracts and summarizes the content of YouTube videos.
* **Summarize Website URLs:** Extracts and summarizes the text content of web pages.
* **Groq LLM Powered:** Uses the fast Groq LLM for quick and accurate summarization.
* **Streamlit Interface:** User-friendly web interface for easy interaction.
* **Error Handling:** Robust error handling for invalid URLs and video loading issues.

## Getting Started

### Prerequisites

* Python 3.7+
* A Groq API key (we will get from groq cloud website)

### Installation

1.  **Clone the repository**

2.  **Create a virtual environment **

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**

    ```bash
    streamlit run app.py
    ```

### Usage

1.  **Enter Groq API Key:**
    * In the sidebar, enter your Groq API key.
2.  **Enter URL:**
    * In the main interface, enter the YouTube video URL or website URL you want to summarize.
3.  **Summarize:**
    * Click the "Summarize the content from YT Or Website" button.
4.  **View Summary:**
    * The summarized content will be displayed on the screen.

### Code Explanation

* **`app.py`:**
    * This file contains the Streamlit application and the LangChain summarization logic.
    * It handles URL input, Groq LLM integration, and error handling.
    * It uses `YoutubeLoader` and `UnstructuredURLLoader` to load content.
    * Uses the Langchain `load_summarize_chain` to summarize the data.

### Dependencies

* `streamlit`
* `langchain`
* `langchain-groq`
* `langchain-community`
* `validators`
* `pytube`

### Error Handling

The application includes robust error handling to manage:

* Invalid URLs.
* Issues loading YouTube videos (e.g., unavailable videos, network errors).
* General Exceptions.
