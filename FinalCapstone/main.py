#Change Return Program - The user enters a cost and then the amount of money given. 
#The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.
from changeMachine import *

def main():
    userAmount = float(input('What do you want to calculate change for?: $'))
    check = changeMachine(userAmount)
    check.calculate()
    check.results()

if __name__ == '__main__':
    main()