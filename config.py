
import pandas as pd

# Read Excel file
df = pd.read_excel('extracted_links.xlsx', engine='openpyxl')

# Get 'URL' column and convert to list
LIST_URLS = df['URL'].tolist()

BASE_URL = "https://www.XXX.com"
REQUEST_DELAY = 5  # Delay between two requests in seconds

# Site-specific scraping configurations
SCRAPING_CONFIG = {
    "article_links_selector": "a.n_itembox",
    "article_title_selector":".itemtit",
    "next_page_selector": 'a.b[title="下一页"]',
    "article_content_selector": 'div.maincontent',
    "remove_tags": ['a', 'img']
}
