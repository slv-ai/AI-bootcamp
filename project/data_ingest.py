import arxiv
client = arxiv.Client()

def fetch_arxiv_papers(query, max_results=10):  
    search = arxiv.Search(
        query=query,
        max_results = max_results,
        sort_by = arxiv.SortCriterion.SubmittedDate
    )
    results = []
    for result in search.results():
        paper_info = {
            "title": result.title,
            "authors": [author.name for author in result.authors],
            "summary": result.summary,
            "published": result.published,
            "url": result.pdf_url,
            "categories": result.categories
        }
        results.append(paper_info)
    return results