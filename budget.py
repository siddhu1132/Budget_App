class Category:

  def __init__(self, name) :

    self.name = name
    self.ledger = list()

  def __str__(self):
    title = f"{self.name:*^30}\n"
    items = ""
    total = 0
    for item in self.ledger:
      items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'

      total += item['amount']

    output = title + items + "Total: " + str(total)
    return output

# Creating a deposit Method and it accepts amount and description.

  def deposit(self, amount, description="") :
    """
    If no description is given, it should default to empty string. The method should append an object to the ledger list in the form of 
        { 'amount' : amount,'description' : description }
    """
    self.ledger.append({"amount" : amount, "description" : description})

  # Creating a Withdrawk Method

  def withdraw(self, amount, description="") :   
    '''
    The amount passed i the ledger should be stored as a negative number. If there are no funds, nothing should be added to ledger.
    If Withdrwal took place, this method should return True, else it returns false.
    '''
    if(self.check_funds(amount)) :  
      self.ledger.append({ "amount" : -amount, "description" : description })      
      return True;
    return False

  # Creating get_balance method

  def get_balance(self) :
    '''
     This Method returns the Current balance of the budget category based on deposits and withdrawals.
    '''
    total_cash = 0 
    for item in self.ledger :
      total_cash += item["amount"]     
    return total_cash

  # Creating Transfer Method
  def transfer(self,amount,category) :
    """
    This Method accepts an amountand another budgetcategory as arguments. This method should return True if the transfer took place, and False otherwise.
    """
    if(self.check_funds(amount)) :
      self.withdraw(amount,"Transfer to " + category.name)
      category.deposit(amount, "Transfer from " + self.name)
      return True
    return False

   # Creating Method to check the funds.

  def check_funds(self,amount):
    '''
    This method accepts an amount as an argument. It returns false if the amount is greater than the balance of budget and returns otherwise.      
    '''
    if(self.get_balance() >= amount) : 
      return True
    return False

  def get_withdrawls(self):
    total = 0
    for items in self.ledger:
      if item["amount"] < 0:
        total += item["amount"]
    return total

def create_spend_chart(categories):
  return None;
