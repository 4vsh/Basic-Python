class car:

    def __init__(self, name, model, year, color, top_speed, site, credit):
        print(f"Welcome to {name} info dashboard @{site} | © {credit} 2024.")
        self.name = "Name: "+name
        self.model = "Model Number: "+model
        self.year = "Released Year: "+year
        self.color = "Color: "+color
        self.top_speed = "Top Speed: "+top_speed

    def sale(self):
        print(f"{self.name} is in sale :) ")
        print("+-------------------+\n")
    def notinsale(self):
        print(f"{self.name} is not in sale :(")
        print("+-------------------+\n")





porsche = car("Porsche", "9/11", "2019", "Black-blue", "495kph", "porsche.com", "Porsche")

print(porsche.name)
print(porsche.model)
print(porsche.year)
print(porsche.color)
print(porsche.top_speed)

porsche.notinsale()

ford = car("BMW", "BMW XR 200", "2009", "darkBlue", "255kph", "bmw.com", "BMW")
print(ford.name)
print(ford.model)
print(ford.year)
print(ford.color)
print(ford.top_speed)

ford.sale()

print("Thanks for visiting here in our shop :)")
#thank you :)