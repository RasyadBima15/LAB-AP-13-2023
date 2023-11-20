from abc import ABC,abstractmethod

#abstract class
class math_operation(ABC):

    @abstractmethod
    def operator(self):
        pass


#Inheritance
class multiplication(math_operation):
    def __init__(self,v1,v2):
        # Encapsulation
        self._variable_1 = v1
        self._variable_2 = v2
    
    #abstractmethod
    def operator(self):
        print (self._variable_1 * self._variable_2)

    #setter
    def ubahvar(self,var1_baru,var2_baru):
        self._variable_1 = var1_baru
        self._variable_2 = var2_baru

    # getter
    def ambilVariable(self):
        print(self._variable_1)
        print(self._variable_2)

    

class division(math_operation):
    def __init__(self,v3,v4):
        # Encapsulation
        self._variable_3 = v3
        self._variable_4 = v4

    #abstractmethod
    def operator(self):
        print (self._variable_3 / self._variable_4)

    #setter
    def ubahvar(self,var3_baru,var4_baru):
        self._variable_3 = var3_baru
        self._variable_4 = var4_baru

    # getter
    def ambilVariable(self):
        print(self._variable_3)
        print(self._variable_4)


#Polymorphism
#method interface 
def operator_of_math_operation(math_operation):
    math_operation.operator()


#object
# operator1 = multiplication(2,4)
# operator2 = division(8,4)

# #encapsulation object
# operator_of_math_operation(operator1)
# operator_of_math_operation(operator2)



operator1 = multiplication(2,4)
operator1.ubahvar(5,6)
operator1.ambilVariable()