"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, commission_rate = 0, contracts = 0, salary = 0, hours = 0, hourly_wage = 0, bonus = 0 ): 
        self.name = name
        self.commission_rate = commission_rate
        self.contracts = contracts
        self.salary = salary
        self.hours = hours
        self.hourly_wage = hourly_wage
        self.bonus = bonus
        self.total_pay = 0

    def get_pay(self):
        if self.salary:
            self.total_pay += self.salary

        if self.contracts:
            self.total_pay += self.contracts * self.commission_rate

        if self.hours:
            self.total_pay += self.hours * self.hourly_wage

        if self.bonus:
            self.total_pay += self.bonus

        return self.total_pay



    def __str__(self):

        pay_calc = ""

        if self.salary:
            pay_calc += (f'{self.name} works on a monthly salary of {self.salary}')
        
        else:
            pay_calc += (f'{self.name} works on a contract of {self.hours} hours at {self.hourly_wage}/hour')
            

        if self.contracts:
            pay_calc += (f' and receives a commission for {self.contracts} contract(s) at {self.commission_rate}/contract.')

        elif self.bonus:
            pay_calc += (f' and receives a bonus commission of {self.bonus}.')

        else:
            pay_calc += '.'

        
        pay_calc += (f'  Their total pay is {self.total_pay}.')
        return pay_calc



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', salary=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', hours=100, hourly_wage=25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', salary=3000, contracts=4, commission_rate=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', hours=150, hourly_wage=25, contracts=3, commission_rate=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', salary=2000, bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', hours=120, hourly_wage=30, bonus=600)
