import Calu
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow


class MyApp(QMainWindow, Calu.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Calu.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.calx_tax_button.clicked.connect(self.CalulateTax)

    def CalulateTax(self):
        price = int(self.price_box.toPlainText())
        tax = self.tax_rate.value()
        total_price = price + ((tax / 100) * price)
        total_price_string = str(total_price)
        self.results_window.setText(total_price_string)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MyApp()

    MainWindow.show()

    sys.exit(app.exec_())
