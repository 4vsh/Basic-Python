#similar like inheritance bUT the thing is we also can inherite class from multiple classes

class grandpa:
    name = "Grandpa"
    surname = "Aryal"

    def grand(self):
        print("Yes im from grandpa class 👻")


class father(grandpa):  #father is inheritating (rip spell :/) from grandpa
    name = "Father"     #surname came from grandpa

    def grand(self):
        print("I am father class and i just inherit and change my grandpa's function inside my class hahahaha")
    def father(self):
        print("yes Im father:/")
class son(father):      #son is inheritating (rip spell :/) from father
    name = "Son"        #surname came from grandpa

    def grand(self):
        print("Yea you know who am I, And yeah i inherit my fathers function then change inside it lol ")



print(grandpa.name, grandpa.surname)
print(father.name, father.surname)
print(son.name, son.surname)
print()

myson = son()

#yep!! thats it :)

Father = father()
Grand = grandpa()
Grand.grand()
Father.grand()

myson.grand()

