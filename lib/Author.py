from Article import Article

class Author:
    all_authors = []

    def __init__(self, name):
        if isinstance(name, str):
            self._name = name
            self._articles = []
            self._magazines = []
            Author.all_authors.append(self)
        else:
            print("Name must be a string!")

    @property
    def name(self):
        return self._name
    
    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        self._articles.append(new_article)
        self._magazines.append(magazine)
        magazine.add_article(new_article)
        return new_article

    def articles(self):
        return self._articles
    
    def magazines(self):
        return self._magazines
    
    def topic_areas(self):
        return [magazine.category for magazine in self._magazines]
    
