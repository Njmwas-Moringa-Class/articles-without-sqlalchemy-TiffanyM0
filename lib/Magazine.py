from Article import Article
from Author import Author

class Magazine:
    all_magazines = []
    all_articles=[]
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []
        self._contributors = []
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    @classmethod
    def all(cls):
        return cls.all_magazines

    def contributors(self):
        self._contributors.append(article._author for article in self._articles)
        return [article._author for article in self._articles]

    def add_article(self, article):
        self._articles.append(article)
        Magazine.all_articles.append(article)


    @classmethod
    def find_by_name(cls, name):
        for mag in cls.all_magazines:
            if mag._name == name:
                return mag
        return None

        # def find_match(iterable, name):
        #     return next(
        #         (value for value in iterable if value._name == name),
        #         None
        #     )
    
    @classmethod
    def article_titles(cls, magazine):
        title_list = []
        for article in magazine.all_articles:
            title_list.append(article._title)
        return title_list

    def contributing_authors(self):
        pass
    
