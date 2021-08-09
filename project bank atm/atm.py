class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

#Your balance (fixed amount)
    def check_balance(self):
        print("Your balance is 50000")

#withdrawling your money from your fixed amount
    def withdrawl(self,amount):
        new_amount = 50000 - amount
        print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))


def main():
    #questions for the card and pin numbers
    Card_number = input("insert your card number:- ")
    pin_number  = input("enter your pin number:- ")

#creating a new user profile
    new_user =  Atm(Card_number ,pin_number)

    #giving the option to choose the enquiry or withdrawl
    print("Choose your activity ")
    print("1.Balance Enquriy   2.withdrawl")
    activity = int(input("enter activity number :- "))

    if (activity == 1):
        #creating a path when the user chooses 1 to check their balance
        new_user.check_balance()
        #creating the path when the user chooses 2 to choose their withdrawl
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        new_user.withdrawl(amount)
    else:
        #error message when the user uses a different number rather than 1 or 2
        print("enter a valid number")


if __name__ == "__main__":
    main()
