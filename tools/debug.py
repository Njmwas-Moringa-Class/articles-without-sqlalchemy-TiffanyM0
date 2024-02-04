#!/usr/bin/env python3
import ipdb;
from lib.Author import Author
from lib.Article import Article
from lib.Magazine import Magazine

if __name__ == '__main__':
#  WRITE YOUR TEST CODE HERE ###
    alex = Author("alex")
    mag = Magazine("Unix devs", "software")

    A1 = Article(alex, mag, "100 tips for devs")

    alexa = Author("alex")
    mag = Magazine("Unix", "flamingo")

    A1 = Article(alex, mag, "ai birds")

    print("Title of A1:", A1.title())
    print("All Articles:", Article.all())
    print(alex.articles())





# DO NOT REMOVE THIS
    ipdb.set_trace()
