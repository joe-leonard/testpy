from scraper import fetch_article_links, fetch_article_content
from db_manager import init_db, insert_article
from config import LIST_URLS, REQUEST_DELAY
import time


def main():
    # Initialize the database
    init_db()

    for url in LIST_URLS:
        article_links = fetch_article_links(url)
        for article in article_links:
            print(f"Fetching content for article: {article['Title']}")
            content = fetch_article_content(article['URL'])
            insert_article(article['Title'], content, article['URL'])
        # 延迟以限制请求速率
        time.sleep(REQUEST_DELAY)

if __name__ == "__main__":
    main()
