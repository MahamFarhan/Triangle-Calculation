import math
class Triangle:
    __object_count = 0

    def __init__(self, *args):
        if len(args) == 0:
            self.__sidea = 0.1
            self.__sideb = 0.1
            self.__sidec = 0.1
        elif len(args) == 1 and isinstance(args[0], Triangle):
            self.__sidea = args[0].sidea
            self.__sideb = args[0].sideb
            self.__sidec = args[0].sidec
        
        elif len(args) == 1:
            self.__sidea = float(args[0])
            self.__sideb = float(args[0])
            self.__sidec = float(args[0])
        elif len(args) == 2:
            self.__sidea = float(args[0])
            self.__sideb = float(args[0])
            self.__sidec = float(args[1])
        elif len(args) == 3:
            self.__sidea = float(args[0])
            self.__sideb = float(args[1])
            self.__sidec = float(args[2])
        else:
            raise ValueError("Invalid arguments for Triangle constructor")
        
        Triangle.__object_count += 1

    #Properties and setter methods
    @property
    def sidea(self):
        return self.__sidea

    @sidea.setter
    def sidea(self, value):
        self.__validate_side(value)
        self.__sidea = float(value)

    @property
    def sideb(self):
        return self.__sideb

    @sideb.setter
    def sideb(self, value):
        self.__validate_side(value)
        self.__sideb = float(value)

    @property
    def sidec(self):
        return self.__sidec

    @sidec.setter
    def sidec(self, value):
        self.__validate_side(value)
        self.__sidec = float(value)

    def __validate_side(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Side length must be a positive number")

    @classmethod
    #this tells that this method is a class method
    def object_count(cls):
        #it receives the class as the first argument
        #__object_count is a private class variable that counts how many Triangle objects have been created.
        return cls.__object_count

    def perimeter(self):
        return self.__sidea + self.__sideb + self.__sidec

    def is_right_angled(self):
        #sorts the sides to check for the Pythagorean theorem
        sides = sorted([self.__sidea, self.__sideb, self.__sidec])
        #math.isclose is used to compare floating point numbers for equality
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)
    
    def __str__(self):
        return f"Triangle(sidea={self.__sidea}, sideb={self.__sideb}, sidec={self.__sidec})"
        
            
