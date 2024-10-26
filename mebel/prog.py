from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 700)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.core_txt = QtWidgets.QLabel(self.centralwidget)
        self.core_txt.setGeometry(QtCore.QRect(0, 0, 700, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.core_txt.setFont(font)
        self.core_txt.setStyleSheet("color: rgb(0, 0, 0);")
        self.core_txt.setObjectName("core_txt")
        self.btn_count = QtWidgets.QPushButton(self.centralwidget)
        self.btn_count.setGeometry(QtCore.QRect(0, 555, 350, 100))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_count.setFont(font)
        self.btn_count.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.btn_count.setObjectName("btn_count")
        self.width_lbl = QtWidgets.QLabel(self.centralwidget)
        self.width_lbl.setGeometry(QtCore.QRect(0, 50, 230, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.width_lbl.setFont(font)
        self.width_lbl.setStyleSheet("color: rgb(0, 0, 0);")
        self.width_lbl.setObjectName("width_lbl")
        self.lenght_lbl = QtWidgets.QLabel(self.centralwidget)
        self.lenght_lbl.setGeometry(QtCore.QRect(235, 50, 230, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lenght_lbl.setFont(font)
        self.lenght_lbl.setStyleSheet("color: rgb(0, 0, 0);")
        self.lenght_lbl.setObjectName("lenght_lbl")
        self.height_lbl = QtWidgets.QLabel(self.centralwidget)
        self.height_lbl.setGeometry(QtCore.QRect(470, 50, 230, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.height_lbl.setFont(font)
        self.height_lbl.setStyleSheet("color: rgb(0, 0, 0);")
        self.height_lbl.setObjectName("height_lbl")
        self.width = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.width.setGeometry(QtCore.QRect(0, 100, 230, 50))
        self.width.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.width.setObjectName("width")
        self.height = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.height.setGeometry(QtCore.QRect(470, 100, 230, 50))
        self.height.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.height.setObjectName("height")
        self.lenght = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.lenght.setGeometry(QtCore.QRect(235, 100, 230, 50))
        self.lenght.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lenght.setObjectName("lenght")
        self.mat_lbl = QtWidgets.QLabel(self.centralwidget)
        self.mat_lbl.setGeometry(QtCore.QRect(0, 150, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mat_lbl.setFont(font)
        self.mat_lbl.setStyleSheet("color: rgb(0, 0, 0);")
        self.mat_lbl.setObjectName("mat_lbl")
        self.material = QtWidgets.QComboBox(self.centralwidget)
        self.material.setGeometry(QtCore.QRect(0, 180, 230, 70))
        self.material.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.material.setObjectName("material")
        self.door_amount_lbl = QtWidgets.QLabel(self.centralwidget)
        self.door_amount_lbl.setGeometry(QtCore.QRect(235, 150, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.door_amount_lbl.setFont(font)
        self.door_amount_lbl.setStyleSheet("color: rgb(0, 0, 0);")
        self.door_amount_lbl.setObjectName("door_amount_lbl")
        self.door_amount = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.door_amount.setGeometry(QtCore.QRect(235, 180, 230, 70))
        self.door_amount.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.door_amount.setObjectName("door_amount")
        self.ans = QtWidgets.QLabel(self.centralwidget)
        self.ans.setGeometry(QtCore.QRect(350, 555, 300, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.ans.setFont(font)
        self.ans.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.ans.setObjectName("ans")
        self.inside_left = QtWidgets.QCheckBox(self.centralwidget)
        self.inside_left.setGeometry(QtCore.QRect(0, 400, 175, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inside_left.setFont(font)
        self.inside_left.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"selection-color: rgb(0, 85, 0);")
        self.inside_left.setObjectName("inside_left")
        self.inside_bot = QtWidgets.QCheckBox(self.centralwidget)
        self.inside_bot.setGeometry(QtCore.QRect(525, 400, 175, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inside_bot.setFont(font)
        self.inside_bot.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"selection-color: rgb(0, 85, 0);")
        self.inside_bot.setObjectName("inside_bot")
        self.inside_top = QtWidgets.QCheckBox(self.centralwidget)
        self.inside_top.setGeometry(QtCore.QRect(350, 400, 175, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inside_top.setFont(font)
        self.inside_top.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"selection-color: rgb(0, 85, 0);")
        self.inside_top.setObjectName("inside_top")
        self.inside_right = QtWidgets.QCheckBox(self.centralwidget)
        self.inside_right.setGeometry(QtCore.QRect(175, 400, 175, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inside_right.setFont(font)
        self.inside_right.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"selection-color: rgb(0, 85, 0);")
        self.inside_right.setObjectName("inside_right")
        self.inside_lbl = QtWidgets.QLabel(self.centralwidget)
        self.inside_lbl.setGeometry(QtCore.QRect(175, 350, 350, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.inside_lbl.setFont(font)
        self.inside_lbl.setStyleSheet("color: rgb(0, 0, 0);")
        self.inside_lbl.setObjectName("inside_lbl")
        self.door_sys_lbl = QtWidgets.QLabel(self.centralwidget)
        self.door_sys_lbl.setGeometry(QtCore.QRect(0, 250, 230, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.door_sys_lbl.setFont(font)
        self.door_sys_lbl.setObjectName("door_sys_lbl")
        self.door_sys = QtWidgets.QComboBox(self.centralwidget)
        self.door_sys.setGeometry(QtCore.QRect(0, 300, 230, 50))
        self.door_sys.setObjectName("door_sys")
        self.shelf_lbl = QtWidgets.QLabel(self.centralwidget)
        self.shelf_lbl.setGeometry(QtCore.QRect(235, 250, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.shelf_lbl.setFont(font)
        self.shelf_lbl.setObjectName("shelf_lbl")
        self.box_lbl = QtWidgets.QLabel(self.centralwidget)
        self.box_lbl.setGeometry(QtCore.QRect(470, 250, 230, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.box_lbl.setFont(font)
        self.box_lbl.setObjectName("box_lbl")
        self.box_amount = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.box_amount.setGeometry(QtCore.QRect(470, 300, 230, 50))
        self.box_amount.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.box_amount.setObjectName("box_amount")
        self.shelf_amount = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.shelf_amount.setGeometry(QtCore.QRect(235, 300, 230, 50))
        self.shelf_amount.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.shelf_amount.setObjectName("shelf_amount")
        self.answer = QtWidgets.QLabel(self.centralwidget)
        self.answer.setGeometry(QtCore.QRect(650, 555, 50, 100))
        self.answer.setObjectName("answer")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        self.add_function()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "просчёт"))
        self.core_txt.setText(_translate("MainWindow", "Введите параметры"))
        self.btn_count.setText(_translate("MainWindow", "Посчитать результат"))
        self.width_lbl.setText(_translate("MainWindow", "Введите ширину"))
        self.lenght_lbl.setText(_translate("MainWindow", "Введите длину"))
        self.height_lbl.setText(_translate("MainWindow", "Введите высоту"))
        self.mat_lbl.setText(_translate("MainWindow", "Выберите материал двери"))
        self.door_amount_lbl.setText(_translate("MainWindow", "Введите количетсво дверей"))
        self.ans.setText(_translate("MainWindow", "Итоговая стоимость - "))
        self.inside_left.setText(_translate("MainWindow", "Левая стенка"))
        self.inside_bot.setText(_translate("MainWindow", "Нижняя часть"))
        self.inside_top.setText(_translate("MainWindow", "Верхняя часть"))
        self.inside_right.setText(_translate("MainWindow", "Правая стенка"))
        self.inside_lbl.setText(_translate("MainWindow", "Выберите присутствующие части шкафа"))
        self.door_sys_lbl.setText(_translate("MainWindow", "Выберите систему дверей"))
        self.shelf_lbl.setText(_translate("MainWindow", "Введите количество полок"))
        self.box_lbl.setText(_translate("MainWindow", "Введите количество ящиков"))
        self.answer.setText(_translate("MainWindow", ans))


ans = "0"
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
Ui_MainWindow.setupUi(app, MainWindow)
MainWindow.show()
sys.exit(app.exec_())
Ui_MainWindow.setupUi()