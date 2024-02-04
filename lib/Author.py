from Article import Article

class Author:
    all_authors = []

    def __init__(self, name):
        if isinstance(name, str):
            self._name = name
            self._articles = []
            Author.all_authors.append(self)
        else:
            print("Name must be a string!")

    @property
    def name(self):
        return self._name

    def contribute_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        self._articles.append(new_article)
        return new_article

    def articles(self):
        return self._articles

    @classmethod
    def all(cls):
        return cls.all_authors
