class Author:
    pass
    # Author __init__(name)
    # An author is initialized with a name, as a string.
    # A name cannot be changed after it is initialized.
    # Author name()
    # Returns the name of the autho
    def __init__(self, name):
        if (type(name) is (str)):
            self.name = name
        else:
            print("Name must be String!")

# d = Author("betsy")
# print(d.name)