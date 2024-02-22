#!/usr/bin/env python3
import ipdb;
from Author import Author
from Magazine import Magazine
from Article import Article

if __name__ == '__main__':
#  WRITE YOUR TEST CODE HERE ###
    # alex = Author("alex")
    # mag = Magazine("Unix devs", "software")

    # A1 = Article(alex, mag, "100 tips for devs")

    # JK = Author('J.K')
    # J1 = Author('J1')
    # J2 = Author('J2')

    # disney = Magazine('disney', 'film')

    # JK.add_article('harry-poter', 'into the abyss')
    # JK.add_article('hoodwinked', 'alice-in-wonderland')

    # JK.add_article('disney', 'tangled')
    # J1.add_article('disney', 'tangled')
    # J2.add_article('disney', 'tangled')

    # disney.contributors()
    # disney.contributing_authors()
    # JK.magazines()

    author1 = Author("Mickey")
    assert author1.name == "Mickey"
    magazine1 = Magazine("Tech Magazine", "Technology")
    assert magazine1.name == "Tech Magazine"
    assert magazine1.category == "Technology"
    author1.add_article(magazine1, "Article 1")

    author2 = Author("Minnie")
    assert author2.name == "Minnie"
    magazine2 = Magazine("Techy", "Technology")
    assert magazine2.name == "Techy"
    assert magazine2.category == "Technology"
    author2.add_article(magazine2, "Article 2")

    assert len(Magazine.all_magazines) == 2
    assert len(Article.all_articles) == 2

    assert len(author2.articles()) == 1
    assert author1.articles()[0].title == "Article 1"

    assert len(author1.magazines()) == 1
    assert author1.magazines()[0].name == 'Tech Magazine'

    Article2 = Article(author1, magazine1, "code fix")
    author1.add_article(magazine2, 'amazing race')
    magazine3 = Magazine('Up', 'Disney')

    author1.add_article(magazine3,'sad movie tings')
    assert magazine3.contributors()[0]._articles[0]._author.name == 'Mickey'
    # assert len(magazine1._articles) == 1
    # assert magazine1._articles[0].title == "Article 1"
    # magazine1.add_article("Article 2")

    # assert len(magazine1.contributors()) == 1
    # assert magazine1.contributors()[0].name == "Mickey"

    # magazine1.add_article(author1, "Article 2")

    # assert Magazine.contributors() == [author1, author2]


    ipdb.set_trace()
