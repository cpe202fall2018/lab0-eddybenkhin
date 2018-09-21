def weight_on_planets():
   # write your code here
    earthWeight = input("What do you weigh on Earth? ")
    marsWeight = earthWeight * 0.38
    jupiterWeight = earthWeight * 2.34
    
    print("\nOn Mars you would weigh {0} pounds.".format(marsWeight))
    print("On Jupiter you would weigh {0} pounds.".format(jupiterWeight))
   
   
if __name__ == '__main__':
   weight_on_planets()
