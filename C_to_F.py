def main():

    for i in range(5):
        celsius = eval(input("To receive temperature in degrees Fahrenheit, please input temperature in degrees Celsius: "))

        #print("Temperature is:", celsius, "degrees Celsius")


        fahrenheit = celsius*(9/5) + 32
        print("Temperature is ", fahrenheit, "degrees Fahrenheit")

main()
input("Press <Enter> to quit")

