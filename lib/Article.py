
class Article:
    pass
    all_articles = []

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all_articles.append(self)

    @property
    def author(self):
        from Author import Author
        add_author = Author(f'{self.author}')
        return add_author

    @property
    def magazine(self):
        return self._magazine

    @property
    def title(self):
        return self._title

    @classmethod
    def all(cls):
        return cls.all_articles

    @classmethod
    def articles(cls, author):
        return [article for article in cls.all_articles if article.author == author]
