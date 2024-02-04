from Author import *
from Magazine import *


class Article(Magazine, Author):
    pass
    all_articles = []
    # # Article __init__(author, magazine, title)
    # # An article is initialized with an author as an Author object, a magazine as a Magazine object, and title as a string.
    # # An article cannot change its author, magazine, or title after it is has been initialized.
    # # Article title()
    # # Returns the title for that given article
    # # Article all()
    # # Returns an list of all Article instances
    def __init__(self, author, magazine, title=""):
        self.author = author.name
        self.magazine = magazine.name
        self.title = title
        Article.all_articles.append([author, magazine, title])

    @classmethod
    def all(cls):
        return cls.all_articles

    # def show_all(cls):
    #     print([Article.all])

print(Article.all)


