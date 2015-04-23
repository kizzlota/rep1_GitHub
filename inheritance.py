
class Parent:

    def last_name(self):
        print("Roberts")


class Child:

    def first_name(self):
        print("Bucky")

    def last_name(self):  #override previous method 'last name'
        print("Snitz")


bucky = Child()
bucky.first_name()
bucky.last_name()




class Mario():

    def move(self):
        print('I am moving')

class Shroom():

    def eat_shroom(self):
        print("now i am bid")

class BigMario(Mario, Shroom):
    pass                            # word 'pass' prevents syntax error, than making inheritance
                                    # and then in a new class is nothing to do than inherits

bm = BigMario()
bm.move()
bm.eat_shroom()

print "HW"
