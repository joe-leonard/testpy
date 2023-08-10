import requests
from bs4 import BeautifulSoup
from config import BASE_URL, SCRAPING_CONFIG

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}



def fetch_article_links(list_url):
    """
    Fetches article links from a list page.
    """
    articles = []
    page_num = 1

    while True:
        print(f"Fetching articles from page {page_num} at URL: {list_url}")
        response = requests.get(list_url, headers=HEADERS)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract articles on the current page using the selectors from SCRAPING_CONFIG
        page_articles = soup.select(f'{SCRAPING_CONFIG["article_links_selector"]}')

        articles.extend([
            {
                "Title": a.select_one(f'{SCRAPING_CONFIG["article_title_selector"]}').text.strip(),
                "URL": BASE_URL + a['href']
            }
            for a in page_articles
        ])

        # Check for the next page using the selectors from SCRAPING_CONFIG
        next_page = soup.select_one(f'{SCRAPING_CONFIG["next_page_selector"]}')
        if next_page and next_page['href'] not in list_url:
            list_url = BASE_URL + next_page['href']
            page_num += 1
        else:
            print("Detected the last page, stopping...")
            break

    return articles


def fetch_article_content(article_url):
    """
    Fetches the content of an article.
    """
    response = requests.get(article_url, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract and clean the article content
    content_tag = soup.select_one(f'{SCRAPING_CONFIG["article_content_selector"]}')
    if content_tag:
        # Remove unwanted tags
        for tag in content_tag.find_all(f'{SCRAPING_CONFIG["remove_tags"]}'):
            tag.decompose()

        # Remove class attribute
        if 'class' in content_tag.attrs:
            del content_tag.attrs['class']
    return content_tag.prettify()
