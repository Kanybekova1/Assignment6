from bmiait import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow,QMessageBox, QApplication


class BMIApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.calculateButton.clicked.connect(self.calculate_bmi)
        self.setFixedSize(500, 400)
        self.setStyleSheet("background-color: #F5F5F5;")
        self.actionExit.triggered.connect(self.close)
        self.actionClear.triggered.connect(self.clear_fields)
        self.actionAbout.triggered.connect(self.show_about)

    def calculate_bmi(self):
        try:
            height = float(self.heightInput.text())
            weight = float(self.weightedit.text())
            height = height /100

           

            bmi = round((weight / (height ** 2)), 1)
            self.label.setText(str(bmi))

        
            if bmi < 18.5:
                category = "Underweight"
                color = "blue"
            elif 18.5 <= bmi < 25:
                category = "Normal weight"
                color = "green"
            elif 25 <= bmi < 30:
                category = "Overweight"
                color = "orange"
            else:
                category = "Obese"
                color = "red"

            self.label.setStyleSheet(f"color: {color}; font-weight: bold;")
            self.label.setText(f"{bmi:.2f} ({category})")

        except ValueError:
            self.label.setText("Invalid Input")

    def clear_fields(self):
        """Clear input fields and reset label."""
        self.weightedit.clear()
        self.heightInput.clear()
        self.label.setText("BMI Result")
        self.label.setStyleSheet("color: black;")

    def show_about(self):
        """Display an about message."""
        QMessageBox.information(self, "About", 
        'How to Use the BMI Calculator:\n\n'
        '1️. Enter your weight in kilograms (kg) in the "Weight" field.\n'
        '2️. Enter your height in centimeters (cm) in the "Height" field.\n'
        '3️. Click "Calculate" to compute your BMI (Body Mass Index).\n'
        '4️. The result will be displayed with a color indicator:\n'
        '   - 🟡 Underweight (<18.5)\n'
        '   - 🟢 Normal (18.5 – 24.9)\n'
        '   - 🟠 Overweight (25 – 29.9)\n'
        '   - 🔴 Obese (≥30)\n'
    )
        self.actionAbout.triggered.connect(self.show_help)
    
    def exit_app(self):
        reply = QMessageBox.question(self, "Exit", "Are you sure you want to exit?", 
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                    QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
                QApplication.quit() 
        self.actionExit.triggered.connect(self.exit_app)



        