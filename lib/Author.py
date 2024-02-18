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
        from Article import Article 
        _article = Article(self, magazine, title)
        self._articles.append(_article)
    
    def magazine_contributor(self, magazine):
        from Magazine import Magazine
        _magazine = Magazine(magazine.name, magazine.category)
        self._magazines.append(_magazine)
    
    def magazines(self):
        return self._magazines

    def articles(self):
        return self._articles

    @classmethod
    def all(cls):
        return cls.all_authors
    
    def add_article(self, magazine, title):
        pass
