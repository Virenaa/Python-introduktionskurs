# Jag bekräftar härmed att jag inte kommunicerar med andra personer än kursens lärare under tentans gång.

# Jag är medveten om att fusk i tentan kan leda till disciplinåtgärder.

# Fråga 1

def norway_pandemic():
    
    bosatt = input("Hvor er du bosatt?")
    if bosatt[0].lower() == "v":
        print("Velkommen till Norge!")
        return
    
    full_vaccinerad = input("Er du fullvaksinert?")
    if full_vaccinerad.lower() == "ja":
        print("Velkommen till Norge!")
        return

    karatan = input("Har du gjennomgått koronasykdom de siste seks måndene?")
    if karatan.lower() == "ja":
        print("Velkommen till Norge!")
        return
    else:
        print("Velkommen till Norge, men du må teste deg och sitte i karatene.")
        return 


# Fråga 2

def alter(s):
    newalter = ""
    for i in range(0,len(s),2):
        newalter += s[i+1] + s[i]
    return newalter


def scramble(s):
    first_char = s[0]
    last_char = s[-1]
  
    if len(s) % 2 == 0:
        middle = alter(s[1:-1])
    else:
        middle = alter(s[0:-1])
        first_char = ""

    result = first_char + middle + last_char
    return result


def scrambles(s):
    s_list = s.split()
    scrambled = []
    for word in s_list:
        scrambled.append(scramble(word))
    
    return " ".join(scrambled)
        
# Fråga 3 

class Account:
    def __init__(self, accountnr,balance):
        self.accountnr = accountnr
        self.balance = balance 

    def get_balance(self):
        return self.balance
        
    def set_balance(self,b):
        self.balance = b 

def transfer(account1,account2,amount):
    if amount > account1.get_balance():
        return "not enough money"
    else:
        account1.set_balance(account1.get_balance() - amount)
        account2.set_balance(account2.get_balance() + amount)
        return "OK"

