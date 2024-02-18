#!/usr/bin/env python3
import ipdb;
from Author import Author
from Article import Article
from Magazine import Magazine

if __name__ == '__main__':
#  WRITE YOUR TEST CODE HERE ###
    alex = Author("alex")
    mag = Magazine("Unix devs", "software")

    A1 = Article(alex, mag, "100 tips for devs")

    JK = Author('J.K')
    J1 = Author('J1')
    J2 = Author('J2')

    disney = Magazine('disney', 'film')

    JK.add_article('harry-poter', 'into the abyss')
    JK.add_article('hoodwinked', 'alice-in-wonderland')

    JK.add_article('disney', 'tangled')
    J1.add_article('disney', 'tangled')
    J2.add_article('disney', 'tangled')

    disney.contributors()
    disney.contributing_authors()
    JK.magazines()


    ipdb.set_trace()
