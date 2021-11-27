class Calculator:
  @staticmethod  
  def add_numbers(num1, num2):
    return num1 + num2

class Calculator_without_sttic_method:
  def add_numbers(self,num1, num2):
    return num1 + num2

if __name__ == "__main__":
    sum = Calculator.add_numbers(5, 7)
    print('Sum:', sum)
    sum = Calculator.add_numbers(15, 17)
    print('Sum:', sum)
