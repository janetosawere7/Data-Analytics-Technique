def printSummary(bankAccounts,transactionHistory):
    print("Record of Transactions")
    print("Record", end="")

    statement = "{:>10}"
    for customer in bankAccounts:
        print(statement.format(customer), end="")

    print("\n--------------------------------------------", end="")


    len_array = max([len(items) for k, items in transactionHistory.items()])


    for i in range(len_array):
        print("\n",statement.format(i+1), end="")
        for key in transactionHistory:
            print(statement.format(transactionHistory[key][i]), end="")

def createAccount(bankAccounts):
    """A function to create new account and store in dictionary"""
    name = input("Name: ")
    balance = float(input("Initial balance: "))
    bankAccounts[name] = balance

def transaction_func(bankAccounts, transactionHistory, accountName):
    print("\nProcessing ", accountName)
    transactionType = int(input("Transaction type: \n0. Nothing \n1. Deposit \n2. Withdrawal\n: "))
    
    # if transactionType == 0 (Nothing), return null
    if transactionType == 0:
        amount = 0
    else:
        amount = float(input("Amount: "))

        # if transactiontype is withdrawal, make amount negative
        if transactionType == 2:
            amount *= -1

        # update bank account
        bankAccounts[accountName] += amount

    if accountName not in transactionHistory:
        transactionHistory[accountName] = []

    transactionHistory[accountName].append(amount)

    return 
    
def printTransactions(bankAccounts, no_of_account):
    print("Current Balances")
    statement = "{:>10}"
    for customer in bankAccounts:
        print(statement.format(customer), end="")

    print()
    for customer in bankAccounts:
        print(statement.format(bankAccounts[customer]), end="")

if __name__ == "__main__":
    bankAccounts = {}
    transactionHistory = {}
    upnext = 1
    no_of_account = int(input("Number of Account: "))
    while no_of_account >0:
        createAccount(bankAccounts)
        no_of_account -=1

    while upnext != 0:
        for customer in bankAccounts:
            transaction_func(bankAccounts, transactionHistory, customer)
        printTransactions(bankAccounts, no_of_account)
        upnext = int(input("\n0 to exit, any other key to continue: "))

    printSummary(bankAccounts,transactionHistory)


