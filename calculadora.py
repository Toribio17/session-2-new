#this is the parent class
import random
import string
# Finding square by using pow method
import operator

class calculator():
    #variables globales
    calculator_kind = ""
    calculator_factory_number = ""
    calculator_policy = ""
    
    def __init__(self,policy_length,kind_value):
       self.calculator_kind = kind_value
       factory = self.calculator_factory_number = random.randint(0,1000)
       policy = self.calculator_policy = self.generate_policies(policy_length)
       print("Calculator kind ",kind_value)
       print("Policy: ",policy)
       print("Factory: ", factory)
       
    def generate_policies(self,length):
        return ''.join(
        random.choices(string.ascii_letters + string.digits,k=length
        )
    )
    
    def sum(self, value_1,value_2):
        sum = value_1 + value_2
        
        return sum
    
    def subtract(self, value_1,value_2):
        subtracts = value_1 - value_2
        return subtracts
    
    def calculate_area(self):
        raise NotImplementedError
    
    def square(self,n):
        square = operator.pow(n, 2)
        return square


    def run(self):
        print("running")

       

if __name__ == "__main__":
    obj = calculator(30,"Test")
    obj.run()
    