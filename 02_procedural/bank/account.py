def account_create(number, owner, balance, limit):
    account = {"number": number, "owner": owner, "balance": balance, "limit": limit}
    return account

def deposit_amount(account, amount):
    account["balance"] += amount

def withdraw_amount(account, amount):
    account["balance"] -= amount

def statement(account):
    print("Saldo é {}".format(account["balance"]))