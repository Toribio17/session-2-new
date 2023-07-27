from calculadora import calculator

class calculator_basic(calculator):
    
    #encapsulación
    __region = ""
    
    def __init__(self,policy_length,kind_value):
        #use super in case we want to execute the parent constructor
        super().__init__(policy_length,kind_value)
        self.__region = "USA"
        
        
    #este metodo permite ver la variable encapsulada
    def check_region(self):
        return self.__region
    
    

if __name__ == "__main__":
    obj = calculator_basic(30,"Basic")
    obj.run()
    #obj.__region
    region_val = obj.check_region()
    print(region_val)
    sum = obj.sum(10, 10)
    print("sum: ",sum)
    subs = obj.subtract(50, 30)
    print("Substract: ",subs)
    
    
