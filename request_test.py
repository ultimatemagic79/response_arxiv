import arxiv


def fetch_arxiv_papers(search_query, keys):
    client = arxiv.Client()
    search = arxiv.Search(query=search_query, max_results=100, sort_by=arxiv.SortCriterion.SubmittedDate)
    papers = []
    for result in client.results(search):
        if any(key in result.title.lower() for key in keys):
            print(result)
            papers.append({"title": result.title, "summary": result.summary, "link": result.pdf_url})
    return papers


keys = ["test-time adaptation", "adversarial"]
papers = fetch_arxiv_papers("cs.CV", keys)
print(papers)
