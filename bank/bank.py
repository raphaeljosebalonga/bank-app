""" Bank Module """

class Bank(object):
    """ Bank Class """
    def __init__(self):
        self.accounts = {}

    def get_account_balance(self, account_number): # pragma: no cover
        """ Getter Method """
        return self.accounts.get(account_number) # pragma: no cover

    def add_account(self, account):
        """ Setter Method """
        self.accounts[account.account_number] = account.balance
