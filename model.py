class CalculatorModel:
    def calculate(self, expression):
        try:
            result = str(eval(expression))
            return result
        except Exception as e:
            return "Error"
