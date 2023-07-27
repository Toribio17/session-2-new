from calculadora import calculator


class calculator_geo(calculator):
    
    #encapsulación
    __region = ""
    
    def __init__(self,policy_length,kind_value):
        #use super in case we want to execute the parent constructor
        super().__init__(policy_length,kind_value)
        self.__region = "MEX"
    
    #este metodo permite ver la variable encapsulada
    def check_region(self):
        return self.__region
    
    #polimorfismo
    def calculate_area(self,base,height):  
        area = base * height
        print("Rectangle area: ", area)
        
    """def calculate_area(self,base,height,pi,type):  
        area = base * height * pi
        
        print("Circle area: ", area)"""

    

if __name__ == "__main__":
    obj = calculator_geo(30,"Geometrica")
    obj.run()
    #obj.__region
    region_val = obj.check_region()
    print(region_val)
    obj.calculate_area(50,80)
    val_square = obj.square(2)
    print("Sqare: ",val_square)
    
    