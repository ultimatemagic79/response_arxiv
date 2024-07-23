import arxiv
from fastapi import FastAPI

app = FastAPI()


def fetch_arxiv_papers(search_query):
    search = arxiv.Search(query=search_query, max_results=5, sort_by=arxiv.SortCriterion.SubmittedDate)
    papers = []
    for result in search.results():
        papers.append({"title": result.title, "summary": result.summary, "link": result.pdf_url})
    return papers


@app.get("/arxiv")
def get_papers(search_query: str):
    papers = fetch_arxiv_papers(search_query)
    return {"papers": papers}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
