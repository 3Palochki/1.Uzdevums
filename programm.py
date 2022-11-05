admin = open("/Users/ankit/Desktop/PROG-1-GIT/1. uzdevums/admin.txt", "r+")
viesis = open("/Users/ankit/Desktop/PROG-1-GIT/1. uzdevums/viesis.txt", "r+")

# users = str(admin.readlines(10000)) + str(viesis.readlines(10000))
# print(users)

class Admin:
    def __init__(self, name, position, age):
        self.name = name
        self.age = age
        self.position = position
    def printName(self):
        print("Lietotājs " + self.name + " tika izveidots. Viņam ir " + str(self.age) + ", un darbā viņš skaitās kā " + self.position)
    def printAdminQty(self):
        for self.name in admin:
            print("1 Admin")
    def printGuestQty(self):
        for self.name in viesis:
            print("1 Guest")
    def Age(self):
        print("Min age is: " + str(min(36, 28, 33, 21, 30)))
        print("Max age is: " + str(max(36, 28, 33, 21, 30)))
        print("Vid. arit. ir: " + str(int((36 + 28 + 33 + 21 + 30)/5)))

class Guest():
    def __init__(self, name, position, age):
        self.name = name
        self.age = age
        self.position = position
    def printName(self):
        print("Lietotājs " + self.name + " tika izveidots. Viņam ir " + str(self.age) + ", un viņš ir " + self.position)

name1 = Admin("Edvards Siliņš" , "administrātors", 36)
name2 = Admin("Valerijs Dante", "administrātors", 28)
name3 = Admin("Sintija Pūce", "administrātors", 33)
name4 = Admin("Antons Koroļovs", "administrātors", 21)
name5 = Admin("Aleksandrs Runcis", "administrātors", 30)

name1a = Guest("Edvards Siliņš" , "viesis", 36)
name2a = Guest("Valerijs Dante", "viesis", 28)
name3a = Guest("Sintija Pūce", "viesis", 33)
name4a = Guest("Antons Koroļovs", "viesis", 21)
name5a = Guest("Aleksandrs Runcis", "viesis", 30)

name1.printName()
print("----------------------------------------")
name2.printName()
print("----------------------------------------")
name3.printName()
print("----------------------------------------")
name4.printName()
print("----------------------------------------")
name5.printName()
print("----------------------------------------")
print("----------------------------------------")
print("----------------------------------------")
print("----------------------------------------")
name1a.printName()
print("----------------------------------------")
name2a.printName()
print("----------------------------------------")
name3a.printName()
print("----------------------------------------")
name4a.printName()
print("----------------------------------------")
name5a.printName()
print("----------------------------------------")

name1.printAdminQty()
print("----------------------------------------")
name1.printGuestQty()

name1.Age()
