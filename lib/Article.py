
class Article:
    pass
    all_articles = []

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all_articles.append(self)

    @property
    def magazine(self):
        return self._magazine

    @property
    def author (self):
        return self._author
    
    
    @property
    def title(self):
        return self._title

    def all():
        return Article.all_articles

