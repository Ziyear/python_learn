class SweetPotato:
    def __init__(self):
        self.cookLevel = 0
        self.cookString = "生的"
        self.condiments = []

    def __str__(self):
        return "地瓜 状态： %s（%s）作料有：%s" % (self.cookString, self.cookLevel,str(self.condiments))

    def cook(self, cookTime):
        self.cookLevel += cookTime

        if self.cookLevel >= 0 and self.cookLevel < 3:
            self.cookString = "生的"
        elif self.cookLevel >= 3 and self.cookLevel < 5:
            self.cookString = "半生不熟"
        elif self.cookLevel >= 5 and self.cookLevel <= 8:
            self.cookString = "输了"
        elif self.cookLevel > 8:
            self.cookString = "烤糊了"

    def addCondiments(self, condiments):
        self.condiments.append(condiments)


digua = SweetPotato()
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)

digua.cook(1)
print(digua)
digua.cook(1)
digua.addCondiments("大蒜")
print(digua)

digua.cook(1)
print(digua)
