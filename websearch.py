import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def search_web(query, num_results=5):
    url = "https://serpapi.com/search.json"
    params = {
        "q": query,
        "api_key": SERPAPI_KEY,
        "num": num_results
    }

    try:
        data = requests.get(url, params=params).json()
        results = []
        for item in data.get("organic_results", []):
            link = item.get("link")
            snippet = item.get("snippet", "")
            content = fetch_page_text(link) if link else None

            if not content:
                content = snippet  
            if content:
                results.append({"url": link, "content": content})
        return results
    except Exception as e:
        print("Web search failed:", e)
        return []


def fetch_page_text(url):
    try:
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        for script in soup(["script", "style"]):
            script.decompose()
        text = " ".join(soup.stripped_strings)
        return text
    except:
        return ""
