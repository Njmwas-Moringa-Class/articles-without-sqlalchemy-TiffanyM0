from Author import *
from Magazine import *


class Article:
    pass
    all = []
    # Article __init__(author, magazine, title)
    # An article is initialized with an author as an Author object, a magazine as a Magazine object, and title as a string.
    # An article cannot change its author, magazine, or title after it is has been initialized.
    # Article title()
    # Returns the title for that given article
    # Article all()
    # Returns an list of all Article instances
    def __init__(self, Author, magazine, title):
        self.author = Author
        self.magazine = magazine
        self.title = title
        Article.add_to_all(self)

    @classmethod
    def add_to_all(cls, author, magazine, title):
        cls.all.append(author)
        cls.all.append(magazine)
        cls.all.append(title)
    def show_all(cls):
        print([Article.all])


