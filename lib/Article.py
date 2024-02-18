from Author import Author
from Magazine import Magazine


class Article:
    pass
    all_articles = []
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all_articles.append({
            "author": author.name,
            "magazine": {magazine._name: magazine._category},
            "title": title
        })
    
    def author(self):
        return Article.all_articles[0].get("author")
    
    def magazine(self):
        return Article.all_articles[0].get("magazine")

    def title(self):
        return self._title

    @classmethod
    def articles(author):
        pass
        author_articles = []
        for article in Article.all_articles:
            for value in article.value():
                if value == author.name:
                    author_articles.append(article)
        return author_articles
    
    @classmethod
    def all(cls):
        return cls.all_articles

    # def show_all(cls):
    #     print([Article.all])


# alex = Author("alex")
# mag = Magazine("Unix devs", "software")
# A1 = Article(alex, mag, "100 tips for devs")
# print(A1.author())
# print(A1.magazine())

if __name__ == "__main__":
    alex = Author("alex")
    mag = Magazine("Unix devs", "software")

    A1 = Article(alex, mag, "100 tips for devs")

    alexa = Author("alex")
    mag = Magazine("Unix", "flamingo")

    A1 = Article(alex, mag, "ai birds")

    print("Title of A1:", A1.title())
    print("All Articles:", Article.all())
    print(alex.articles())




