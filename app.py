import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from websearch import search_web
from retriever import add_to_vectorstore, search_similar

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(page_title="GPT Jr", page_icon="🌐", layout="wide")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🤖  GPT Jr  🤖")
st.caption("Ask anything — I’ll search the web and answer with up-to-date info.")

# --- Chat display ---
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

# --- User input box (like ChatGPT) ---
query = st.chat_input("Ask your question here...")

if query:
    # Show user message immediately
    st.chat_message("user").markdown(query)
    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("assistant"):
        with st.spinner("Searching and generating answer..."):
            results = search_web(query)

            if not results:
                answer = "⚠️ Sorry, I couldn’t find relevant results."
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})

            else:
                contents = [r["content"][:3000] for r in results]
                metas = [r["url"] for r in results]
                add_to_vectorstore(contents, metas)
                context_chunks = "\n\n".join(search_similar(query))

                prompt = f"""
                You are an expert AI assistant that writes detailed, informative answers using verified web search content. 
                Your goal is to educate the user with depth, clarity, and real-world examples.

                Instructions:
                - Use the provided web context to write a comprehensive explanation.
                - Expand on key concepts with clear definitions, examples, and applications.
                - If helpful, organize your answer using short paragraphs or bullet points.
                - Base everything strictly on the context; do not make up facts.
                - If information is limited, explain as much as possible from what's available.

                ---
                Context:
                {context_chunks[:8000]}

                User Question:
                {query}

                ---
                Final Answer (well-structured, detailed, and educational):
                """

                model = genai.GenerativeModel("models/gemini-2.5-flash")
                response = model.generate_content(prompt)
                answer = response.text if hasattr(response, "text") else "⚠️ No answer generated."

                # --- Display answer ---
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})

                # --- Display sources below ---
                if metas:
                    st.divider()
                    st.subheader("🔗 Sources")
                    unique_links = list(dict.fromkeys(metas))
                    for url in unique_links:
                        st.markdown(f"- [{url}]({url})")
