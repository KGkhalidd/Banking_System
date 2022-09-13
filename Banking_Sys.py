# Banking System By ~KHAlED GAMAL~
# makes u Create account , login , w=Withdrow , Deposit , Display Balance
# withdraw => taking money ----- deposit => Adding money

from abc import ABCMeta, abstractclassmethod
from random import randint


class Account(metaclass=ABCMeta):

    @abstractclassmethod
    def createAccount():
        return 0

    @abstractclassmethod
    def authenticate():
        return 0

    @abstractclassmethod
    def withdraw():
        return 0

    @abstractclassmethod
    def deposit():
        return 0

    @abstractclassmethod
    def displayBalance():
        return 0


class SavingAccount(Account):
    def __init__(self) -> None:

        # 'key' : [name,balance]
        self.savingAccounts = {}

    def createAccount(self, name, initialDeposit):

        # creating random number '5 digits'
        self.accountNumber = randint(10000, 99999)

        # creating dict the key is the random num and the value is the name and the initial deposit
        self.savingAccounts[self.accountNumber] = [name, initialDeposit]

        # show him that account is created and showing the random number
        print(
            f'\nAccount Creation has been successful!. Ur account number is : {self.accountNumber}\n')
        print('-'*60)
        print('\n')

    def authenticate(self, name, accountNumber):

        # checks if the number exists in the list or not
        if accountNumber in self.savingAccounts.keys():

            # check the name too
            if self.savingAccounts[accountNumber][0] == name:

                # if found
                print('\nAuthentication successful!\n')

                self.accountNumber = accountNumber
                return True
            else:

                # if the name not found
                print('\nAuthentication failed!\n')
                return False
        else:

            # if the account not found
            print('\nAuthentication failed!\n')

            return False

    # taking money

    def withdraw(self, withdrawalAmount):

        # if the money u want to take less than the money in the Bank
        if withdrawalAmount > self.savingAccounts[self.accountNumber][1]:
            print("Ur balance isn't enough\n")

        else:

            # the money in the bank - the money u want to take
            self.savingAccounts[self.accountNumber][1] -= withdrawalAmount
            print('withdrawal was successful\n')

            self.displayBalance()

    # adding money
    def deposit(self, depositAmount):

        # money in the bank + the money u added
        self.savingAccounts[self.accountNumber][1] += depositAmount
        print('Deposit was successful!\n')

        self.displayBalance()

    # display the money in the bank

    def displayBalance(self):
        print(
            f'Available balance : {self.savingAccounts[self.accountNumber][1]}\n')


# creating the object from class
savingAccount = SavingAccount()


print()

# just displaying
while True:

    print('Enter 1 to create a new account : ')
    print('Enter 2 to access an existing account : \n')
    print('Enter 3 to exit.\n')

    userChoice = int(input())

    if userChoice == 1:

        name = input('\nEnter Ur name : \n')
        initialDeposit = int(input('\nEnter the initial deposit : \n'))
        savingAccount.createAccount(name, initialDeposit)

    elif userChoice == 2:

        name = input('\nEnter Ur name : \n')
        accountNumber = int(input('\nEnter ur account Number : \n'))
        authenticationStatus = savingAccount.authenticate(name, accountNumber)

        if authenticationStatus == True:

            while True:

                print('\nEnter 1 to withdraw : ')
                print('Enter 2 to deposit : ')
                print('Enter 3 to display available balance : ')
                print('\nEnter 4 to go back to the previous menu. \n')

                userChoice = int(input())
                print()

                if userChoice == 1:

                    print()
                    print('Enter the withdrawal amount : ')
                    withdrawalAmount = int(input())
                    savingAccount.withdraw(withdrawalAmount)
                    print()

                elif userChoice == 2:

                    print()
                    depositAmount = int(
                        input('\nEnter the deposit Ammount :\n'))
                    savingAccount.deposit(depositAmount)
                    print()

                elif userChoice == 3:
                    print()
                    savingAccount.displayBalance()

                elif userChoice == 4:
                    break

    elif userChoice == 3:
        break
