from typing import List

import arxiv
from fastapi import FastAPI, Query

app = FastAPI()


def fetch_arxiv_papers(search_query: str, keys: List[str]):
    client = arxiv.Client()
    search = arxiv.Search(query=search_query, max_results=100, sort_by=arxiv.SortCriterion.SubmittedDate)
    papers = []
    for result in client.results(search):
        if any(key in result.title.lower() for key in keys):
            papers.append({"title": result.title, "summary": result.summary, "link": result.pdf_url})
    return papers


@app.get("/arxiv")
def get_papers(search_query: str):
    papers = fetch_arxiv_papers(search_query, keys)
    return {"papers": papers}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
