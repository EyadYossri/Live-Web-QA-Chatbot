<p align="center">
  <img src="Demo/demo.gif" alt="Demo" width="600" />
</p>

# 🤖 GPT Jr — Web QA Chatbot (SerpApi + Pinecone + Gemini)

GPT Jr is an intelligent web-based chatbot that combines **live web search**, **vector storage**, and **AI-powered responses** to deliver up-to-date, context-aware answers — just like ChatGPT, but with real-time information.

---

## 🚀 Features

- 🌐 **Live Web Search** using [SerpApi](https://serpapi.com/)  
- 🧠 **Semantic Search** powered by **SentenceTransformers** + **Pinecone**  
- 💬 **Conversational Interface** built with **Streamlit**  
- 🔎 **Dynamic Knowledge Updates** from real web data  
- ✨ **Gemini Integration** (Google Generative AI) for coherent and detailed answers  
- 📚 **Context Memory** via Pinecone vector store for smarter follow-ups  

---

## 🧩 Tech Stack

| Component | Technology |
|------------|-------------|
| Web UI | Streamlit |
| Web Search API | SerpApi |
| Embeddings | SentenceTransformers (`all-MiniLM-L6-v2`) |
| Vector Database | Pinecone |
| Language Model | Gemini 2.5 Flash |
| Environment Management | python-dotenv |

---

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/EyadYossri/Live-Web-QA-Chatbot.git
   cd Live-Web-QA-Chatbot
   ```
2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up your environment variables:**
   Create a `.env` file in the root of the project and add the following:
   ```
   PINECONE_API_KEY="your-pinecone-api-key"
   PINECONE_INDEX_NAME="your-pinecone-index-name"
   GOOGLE_API_KEY="your-google-api-key"
   SERPER_API_KEY="your-serper-api-key"
   ```
4. **Run the Streamlit app:**
   ```bash
   streamlit run src/app.py
   ```

## 🤗 Hugging Face Spaces

This project is deployed on **Hugging Face Spaces**.  
You can access it here: [https://huggingface.co/spaces/EyadYossri/Live-Web-QA-Chatbot](https://huggingface.co/spaces/EyadU3/Live-Web-QA-Chatbot)

---

## 🟥 Streamlit App

You can also try the **Streamlit version** here:  
[https://live-web-qa-chatbot.streamlit.app](https://live-web-app-chatbot.streamlit.app/)
