from typing import Any


class Author:
    def __init__(self, name):
        if (type(name) is (str)):
            self._name = name
        else:
             print("Name must be String!")

    @property
    def name(self):
        return self._name

a1 = Author("n1")
a2 = Author("n2")
a3 = Author("n3")
a4 = Author("n4")
a5 = Author("n5")
a6 = Author("n6")
a7 = Author("n7")

###!!!!----> check name() delverable <----!!!!###
# print(a7.name)