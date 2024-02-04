from Author import Author
from Magazine import Magazine

class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        self._author = Author
        self._magazine = Magazine
        self._title = title
        Article.all_articles.append({
            "author": author,
            "magazine": magazine,
            "title": title
        })

    def author(self):
        return self._author

    def magazine(self):
        return self._magazine

    def title(self):
        return self._title

    @classmethod
    def articles(cls, author):
        return [article for article in cls.all_articles if article.get("author") == author]

    @classmethod
    def all(cls):
        return cls.all_articles

