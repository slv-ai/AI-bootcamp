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

def download_paper_pdf(paper_id, save_path):
    paper = client.get(paper_id)
    pdf_content = paper.pdf
    with open(save_path, 'wb') as f:
        f.write(pdf_content)    
    print(f"PDF downloaded and saved to {save_path}")

def main():
    query = "machine learning"
    papers = fetch_arxiv_papers(query, max_results=5)
    for idx, paper in enumerate(papers):
        print(f"Paper {idx+1}: {paper['title']}")
        print(f"Authors: {', '.join(paper['authors'])}")
        print(f"Published: {paper['published']}")
        print(f"URL: {paper['url']}")
        print(f"Categories: {', '.join(paper['categories'])}")
        print(f"Summary: {paper['summary'][:200]}...")  # Print first 200 characters of summary
        print("\n")
        
        # Download the PDF of the first paper as an example
        if idx == 0:
            download_paper_pdf(paper_id=paper['url'].split('/')[-1], save_path='paper1.pdf')