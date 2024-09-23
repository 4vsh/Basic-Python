#call multiple methods sequentially

class bike:

    def turn_on(self):
        print("start the engine! ")
        return self
    def drive(self):
        print("Drive the car! ")
        return self

    def brake(self):
        print("Hit break with ")
        return self

    def turn_off(self):
        print("Turn off the engine! ")
        return self

#without method chaining
duke = bike()

duke.drive()                #this is normal right?
print()
                            #using method chaining !!
#same with method chaining method
duke.drive().brake() .turn_off()       #after writing this we have to return self from class functions

print()
duke.turn_on().turn_off()
