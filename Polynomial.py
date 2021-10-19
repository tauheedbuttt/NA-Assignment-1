"""
Name: Tauheed Butt
Enrollment: 01-134191-068
Class: BSCS-6B
"""

class Polynomial:
    """
    This class creates a polynomial
    Coefficients is of dictionary type where each key key represents variable's
    name and value represents the coefficient of that variable
    Constant represents the constant in the equation
    """
    def __init__(self, coefficients, constant):
        # coefficients is dictionary of coefficients from x1, x2, x3 ... xn
        self.coefficients = coefficients
        self.constant = constant

    def __str__(self):
        result = ""
        for key in self.coefficients:
            result += f"({self.coefficients[key]} {key}) + "
        result += f"({self.constant})"
        return result

    def evaluate(self, values):
        # values is a dictionary consisting of values for x1,x2,x3..xn
        # it will return a value

        # if values provided are less than the actual coefficients
        if len(values) < len(self.coefficients):
            raise ValueError("Number of Values less than Equation")

        result = self.constant
        for var in self.coefficients:
            if var not in values: # raises error if variable not found
                raise ValueError(f"Value for {var} not found")

            result += self.coefficients[var]*values[var]
        return result
