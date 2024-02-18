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
        return [article for article in self._articles]


    @classmethod
    def all(cls):
        return cls.all_authors
    
    def topic_areas(self, magazine):
        pass


class Magazine:

    all_magazines = []        
    _authors = []


    def __init__(self, name, category):
        if isinstance(name, str):
            self._name = name
            self._category = category
            self._articles = []
            Magazine.all_magazines.append(self)
        else:
            print("Name must be a string!")


    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    @classmethod
    def all(cls):
        return cls.all_magazines
    
    def add_article(self, author, title):
        from Article import Article
        new_article = Article(author, self, title)
        Article.all_articles.append(new_article)
        self._articles.append(new_article)
        return new_article

    @classmethod
    def contributing_authors(cls):
        _authors =  [author for magazine in cls.all_magazines for author in magazine.contributors()]
        cls._authors = _authors
        return cls._authors
    
    def contributors(self):
        return list(set(article.author for article in self._articles))
    
    @classmethod
    def article_titles(cls):
        return [article.title() for magazine in cls.all_magazines for article in magazine._articles]
    
    

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
        return self._author

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



