import sqlite3

DATABASE_PATH = "articles.db"


def init_db():
    """
    Initializes the SQLite database and creates the required tables if they don't exist.
    """
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS articles (
        `title` varchar(255) NULL,
        `content` text NULL,
        `url` varchar(255) NOT NULL,
        PRIMARY KEY (`url`)
    )
    ''')

    conn.commit()
    conn.close()


def insert_article(title, content, url):
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("""
            INSERT INTO articles (title, content, url)
            VALUES (?, ?, ?);
            """, (title, content, url))
            conn.commit()
        except sqlite3.IntegrityError:
            # This will catch any attempt to insert a duplicate URL
            print(f"Duplicate URL detected: {url}")
