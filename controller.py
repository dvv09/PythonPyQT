from PyQt5.QtWidgets import QApplication
from model import CalculatorModel
from view import CalculatorView
import sys
class CalculatorController:
    def __init__(self):
        self.app = QApplication([])
        self.model = CalculatorModel()
        self.view = CalculatorView(self)
        self.view.show()

    def run(self):
        return self.app.exec_()

    def calculate(self, expression):
        return self.model.calculate(expression)

if __name__ == '__main__':
    controller = CalculatorController()
    sys.exit(controller.run())
