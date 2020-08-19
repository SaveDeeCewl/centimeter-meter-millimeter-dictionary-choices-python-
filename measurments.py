again = 'y'
while again == 'y':


    def centimeter():
        x = float(input("Input centimeter: "))
        print("What do you want to convert ",x," centimeters to?")
        y = str(input("(millimeters/meters):"))
        if y == 'meters':
            print(x," centimeters is", x/100, "meters")
        if y == 'millimeters':
            print(x," centimeters is", x*10, "millimeters")
    def millimeter():
        x = float(input("Input millimeter: "))
        print("What do you want to convert",x," millimeters to?")
        y = str(input("(centimeters/meters):"))
        if y == 'centimeters':
            print(x," millimeters is", x/10, "centimeters")
        if y == 'meters':
            print(x," millimeters is",x/1000, "meters")
    def meter():
        x = float(input("Input meter:"))
        print("What do you want to convert",x," meters to?")
        y = str(input("(millimeter/centimeter):"))
        if y == 'millimeter':
            print(x ," meters is",x*1000,"millimeters")
        if y == 'centimeter':
            print(x, " meter is", x*100,"centimeters")
    dispatcher = {
        'centimeter' : centimeter, 'millimeter' : millimeter, 'meter' : meter
    }
    action = input("(millimeter/centimeter/meter):")
    dispatcher[action]()
    again = input("Go again? (y/n):")
print("bye")



