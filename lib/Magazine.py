class Magazine:
    pass
    # Magazine blueprint
    def __init__(self, name, category):
        self._name = name
        self._category = category
    
    def getName(self):
        return self._name
    def setName(self, name):
        self._name = name
    def getCategory(self):
        return self._category
    def setCategory(self, category):
        self._category = category
    name = property(getName, setName)
    category = property(getCategory, setCategory)

bridal = Magazine("Bridal", "wedding")
print(bridal.name)
bridal.setName("Kenyan Weddings")

print(bridal.name)


