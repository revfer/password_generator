import sys, sqlite3
from random import choice

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(735, 467)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Dialog.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        Dialog.setAccessibleDescription("")
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Generate_password = QtWidgets.QPushButton(Dialog)
        self.Generate_password.setGeometry(QtCore.QRect(20, 220, 191, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.Generate_password.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        self.Generate_password.setFont(font)
        self.Generate_password.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Generate_password.setMouseTracking(True)
        self.Generate_password.setStyleSheet("background-color: rgb(0, 85, 127);\n"
                                             "color: rgb(255, 255, 255)")
        self.Generate_password.setAutoDefault(True)
        self.Generate_password.setObjectName("Generate_password")
        self.Generate_pas_output = QtWidgets.QLineEdit(Dialog)
        self.Generate_pas_output.setGeometry(QtCore.QRect(20, 150, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Generate_pas_output.setFont(font)
        self.Generate_pas_output.setWhatsThis("")
        self.Generate_pas_output.setStyleSheet("background-color: rgb(0, 85, 127);\n"
                                               "color: rgb(255, 255, 255)")
        self.Generate_pas_output.setInputMask("")
        self.Generate_pas_output.setFrame(True)
        self.Generate_pas_output.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.Generate_pas_output.setReadOnly(True)
        self.Generate_pas_output.setClearButtonEnabled(True)
        self.Generate_pas_output.setObjectName("Generate_pas_output")
        self.add_password = QtWidgets.QPushButton(Dialog)
        self.add_password.setGeometry(QtCore.QRect(230, 230, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        self.add_password.setFont(font)
        self.add_password.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_password.setMouseTracking(True)
        self.add_password.setStyleSheet("background-color: rgb(0, 85, 127);\n"
                                        "color: rgb(255, 255, 255)")
        self.add_password.setAutoDefault(False)
        self.add_password.setDefault(True)
        self.add_password.setFlat(False)
        self.add_password.setObjectName("add_password")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(20, 380, 271, 41))
        self.comboBox.setStyleSheet("background-color: rgb(0, 85, 127);\n"
                                    "color: rgb(255, 255, 255)")
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.User_password_input = QtWidgets.QLineEdit(Dialog)
        self.User_password_input.setGeometry(QtCore.QRect(350, 220, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.User_password_input.setFont(font)
        self.User_password_input.setWhatsThis("")
        self.User_password_input.setStyleSheet("background-color: rgb(0, 85, 127);\n"
                                               "color: rgb(255, 255, 255)")
        self.User_password_input.setInputMask("")
        self.User_password_input.setFrame(True)
        self.User_password_input.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.User_password_input.setReadOnly(False)
        self.User_password_input.setClearButtonEnabled(True)
        self.User_password_input.setObjectName("User_password_input")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 340, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: rgb(255, 255, 255)")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(600, 30, 111, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.spinBox.setFont(font)
        self.spinBox.setMouseTracking(True)
        self.spinBox.setStyleSheet("\n"
                                   "color: rgb(255, 255, 255)")
        self.spinBox.setSuffix("")
        self.spinBox.setPrefix("")
        self.spinBox.setMinimum(8)
        self.spinBox.setMaximum(24)
        self.spinBox.setProperty("value", 12)
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(350, 30, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("\n"
                                   "color: rgb(255, 255, 255)")
        self.label_2.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.checkBox_abc = QtWidgets.QCheckBox(Dialog)
        self.checkBox_abc.setEnabled(True)
        self.checkBox_abc.setGeometry(QtCore.QRect(350, 90, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.checkBox_abc.setFont(font)
        self.checkBox_abc.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_abc.setStyleSheet("\n"
                                        "color: rgb(255, 255, 255)")
        self.checkBox_abc.setChecked(False)
        self.checkBox_abc.setObjectName("checkBox_abc")
        self.checkBox_123 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_123.setGeometry(QtCore.QRect(510, 90, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.checkBox_123.setFont(font)
        self.checkBox_123.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_123.setStyleSheet("\n"
                                        "color: rgb(255, 255, 255)")
        self.checkBox_123.setObjectName("checkBox_123")
        self.servic_input = QtWidgets.QLineEdit(Dialog)
        self.servic_input.setGeometry(QtCore.QRect(20, 30, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.servic_input.setFont(font)
        self.servic_input.setWhatsThis("")
        self.servic_input.setStyleSheet("background-color: rgb(0, 85, 127);\n"
                                        "color: rgb(255, 255, 255)")
        self.servic_input.setInputMask("")
        self.servic_input.setFrame(True)
        self.servic_input.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.servic_input.setReadOnly(False)
        self.servic_input.setClearButtonEnabled(True)
        self.servic_input.setObjectName("servic_input")
        self.checkBox_Aa = QtWidgets.QCheckBox(Dialog)
        self.checkBox_Aa.setEnabled(True)
        self.checkBox_Aa.setGeometry(QtCore.QRect(350, 140, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.checkBox_Aa.setFont(font)
        self.checkBox_Aa.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_Aa.setStyleSheet("\n"
                                       "color: rgb(255, 255, 255)")
        self.checkBox_Aa.setChecked(False)
        self.checkBox_Aa.setObjectName("checkBox_Aa")
        self.checkBox__ = QtWidgets.QCheckBox(Dialog)
        self.checkBox__.setEnabled(True)
        self.checkBox__.setGeometry(QtCore.QRect(510, 140, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.checkBox__.setFont(font)
        self.checkBox__.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox__.setStyleSheet("\n"
                                      "color: rgb(255, 255, 255)")
        self.checkBox__.setChecked(False)
        self.checkBox__.setObjectName("checkBox__")
        self.login_input = QtWidgets.QLineEdit(Dialog)
        self.login_input.setGeometry(QtCore.QRect(20, 90, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.login_input.setFont(font)
        self.login_input.setWhatsThis("")
        self.login_input.setStyleSheet("background-color: rgb(0, 85, 127);\n"
                                       "color: rgb(255, 255, 255)")
        self.login_input.setInputMask("")
        self.login_input.setFrame(True)
        self.login_input.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.login_input.setReadOnly(False)
        self.login_input.setClearButtonEnabled(True)
        self.login_input.setObjectName("login_input")
        self.login_output = QtWidgets.QLineEdit(Dialog)
        self.login_output.setGeometry(QtCore.QRect(350, 350, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.login_output.setFont(font)
        self.login_output.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.login_output.setWhatsThis("")
        self.login_output.setStyleSheet("background-color: rgb(0, 85, 127);\n"
                                        "color: rgb(255, 255, 255)")
        self.login_output.setInputMask("")
        self.login_output.setFrame(True)
        self.login_output.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.login_output.setReadOnly(True)
        self.login_output.setClearButtonEnabled(True)
        self.login_output.setObjectName("login_output")
        self.pass_output = QtWidgets.QLineEdit(Dialog)
        self.pass_output.setGeometry(QtCore.QRect(350, 410, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pass_output.setFont(font)
        self.pass_output.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pass_output.setWhatsThis("")
        self.pass_output.setStyleSheet("background-color: rgb(0, 85, 127);\n"
                                       "color: rgb(255, 255, 255)")
        self.pass_output.setInputMask("")
        self.pass_output.setFrame(True)
        self.pass_output.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.pass_output.setReadOnly(True)
        self.pass_output.setClearButtonEnabled(True)
        self.pass_output.setObjectName("pass_output")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Generate_password.setText(_translate("Dialog", "Generate"))
        self.Generate_pas_output.setText(_translate("Dialog", "Сгенерированный пароль"))
        self.add_password.setText(_translate("Dialog", "Ok"))
        self.User_password_input.setText(_translate("Dialog", "Ввод своего пароля"))
        self.label.setText(_translate("Dialog", "Выберите сервис:"))
        self.label_2.setText(_translate("Dialog", "Выберите кол-во символов:"))
        self.checkBox_abc.setText(_translate("Dialog", "Буквы (abc)"))
        self.checkBox_123.setText(_translate("Dialog", "Цифры (123)"))
        self.servic_input.setText(_translate("Dialog", "Сервис"))
        self.checkBox_Aa.setText(_translate("Dialog", "Регистр (Аа)"))
        self.checkBox__.setText(_translate("Dialog", "Символы (.,!)"))
        self.login_input.setText(_translate("Dialog", "Введите логин"))
        self.login_output.setText(_translate("Dialog", "Логин (номер телефона)"))
        self.pass_output.setText(_translate("Dialog", "Пароль"))


class MyWidget(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.checkBox_abc.toggle()
        self.checkBox_Aa.toggle()
        self.checkBox_123.toggle()

        self.add_password.clicked.connect(self.generation_pass)
        self.Generate_password.clicked.connect(self.generation_pass)
        self.checkBox_abc.clicked.connect(self.generation_pass)
        self.checkBox_Aa.clicked.connect(self.generation_pass)
        self.spinBox.valueChanged.connect(self.generation_pass)

        self.con = sqlite3.connect('pas_db.db')
        self.cur = self.con.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS passwords (login TEXT, password TEXT, service TEXT)')
        self.add_password.clicked.connect(self.add_to_sql)
        self.comboBox.addItems(set(self.get_services_from_sql()))
        self.comboBox.activated[str].connect(self.output_pass)

    # generate password
    def is_num_in(self, a):
        for i in a:
            if i.isdigit():
                return True
        return False

    def is_high_in(self, a):
        return a.lower() == a

    def is_symb_in(self, a):
        for i in a:
            if not i.isdigit() and not i.isalpha():
                return True
        return False

    def gen_words_only(self, kol, is_reg):
        if is_reg:
            c = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        else:
            c = 'qwertyuiopasdfghjklzxcvbnm'
        a = ''
        for i in range(kol):
            a += choice(c)
        if is_reg and self.is_high_in(a):
            return self.gen_words_only(kol, is_reg)
        return a

    def gen_words_num(self, kol, is_reg):
        if is_reg:
            c = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
        else:
            c = 'qwertyuiopasdfghjklzxcvbnm1234567890'
        a = ''
        for i in range(kol):
            a += choice(c)
        if not self.is_num_in(a):
            return self.gen_words_num(kol, is_reg)
        if is_reg and self.is_high_in(a):
            return self.gen_words_num(kol, is_reg)
        return a

    def gen_HARDER_pass(self, kol, is_reg):
        if is_reg:
            c = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM12345678901234567890!@#&()–[{}]:;?/*`~$^+=<>'
        else:
            c = 'qwertyuiopasdfghjklzxcvbnm12345678901234567890!@#&()–[{}]:;?/*`~$^+=<>'
        a = ''
        for i in range(kol):
            a += choice(c)
        if not self.is_num_in(a):
            return self.gen_HARDER_pass(kol, is_reg)
        if is_reg and self.is_high_in(a):
            return self.gen_HARDER_pass(kol, is_reg)
        if not self.is_symb_in(a):
            return self.gen_HARDER_pass(kol)
        return a

    def gen_num_symb_pass(self, kol):
        c = '1234567890!@#&()–[{}]:;?/*`~$^+=<>'
        a = ''
        for i in range(kol):
            a += choice(c)
        if not self.is_num_in(a):
            return self.gen_num_symb_pass(kol)
        if not self.is_symb_in(a):
            return self.gen_num_symb_pass(kol)
        return a

    def gen_num_only(self, kol):
        c = '1234567890'
        a = ''
        for i in range(kol):
            a += choice(c)
        if not self.is_num_in(a):
            return self.gen_num_only(kol)
        return a

    def gen_symb_only(self, kol):
        c = '!@#&()–[{}]:;?/*`~$^+=<>'
        a = ''
        for i in range(kol):
            a += choice(c)
        if not self.is_symb_in(a):
            return self.gen_symb_only(kol)
        return a

    def gen_symb_words(self, kol, is_reg):
        if is_reg:
            c = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#&()–[{}]:;?/*`~$^+=<>'
        else:
            c = 'qwertyuiopasdfghjklzxcvbnm!@#&()–[{}]:;?/*`~$^+=<>'
        a = ''
        for i in range(kol):
            a += choice(c)
        if is_reg and self.is_high_in(a):
            return self.gen_symb_words(kol, is_reg)
        if not self.is_symb_in(a):
            return self.gen_symb_words(kol)
        return a

    def generation_pass(self):
        if self.sender().text() == 'Generate':
            if self.checkBox_abc.isChecked() and \
                    not self.checkBox_123.isChecked() and \
                    not self.checkBox__.isChecked():
                self.Generate_pas_output.setText(self.gen_words_only(self.spinBox.value(),
                                                                     self.checkBox_Aa.isChecked()))
            elif self.checkBox_abc.isChecked() and \
                    self.checkBox_123.isChecked() and \
                    not self.checkBox__.isChecked():
                self.Generate_pas_output.setText(self.gen_words_num(self.spinBox.value(),
                                                                    self.checkBox_Aa.isChecked()))
            elif self.checkBox_abc.isChecked() and \
                    self.checkBox_123.isChecked() and \
                    self.checkBox__.isChecked():
                self.Generate_pas_output.setText(self.gen_HARDER_pass(self.spinBox.value(),
                                                                      self.checkBox_Aa.isChecked()))
            elif not self.checkBox_abc.isChecked() and \
                    self.checkBox_123.isChecked() and \
                    self.checkBox__.isChecked():
                self.Generate_pas_output.setText(self.gen_num_symb_pass(self.spinBox.value()))
            elif not self.checkBox_abc.isChecked() and \
                    self.checkBox_123.isChecked() and \
                    not self.checkBox__.isChecked():
                self.Generate_pas_output.setText(self.gen_num_only(self.spinBox.value()))
            elif not self.checkBox_abc.isChecked() and \
                    not self.checkBox_123.isChecked() and \
                    self.checkBox__.isChecked():
                self.Generate_pas_output.setText(self.gen_symb_only(self.spinBox.value()))
            elif self.checkBox_abc.isChecked() and \
                    not self.checkBox_123.isChecked() and \
                    self.checkBox__.isChecked():
                self.Generate_pas_output.setText(self.gen_symb_words(self.spinBox.value(),
                                                                     self.checkBox_Aa.isChecked()))

    # SQL
    def add_to_sql(self):
        if self.sender().text() == 'Ok':
            login = self.login_input.text()
            pas1 = self.Generate_pas_output.text()
            pas2 = self.User_password_input.text()
            serv = self.servic_input.text()
            if (pas1 == 'Сгенерированный пароль' or pas1 == '') and pas2 != 'Ввод своего пароля' and pas2 != '':
                passw = pas2
                self.User_password_input.setText('')
            elif (pas2 == 'Ввод своего пароля' or pas2 == '') and pas1 != 'Сгенерированный пароль':
                passw = pas1
                self.Generate_pas_output.setText('')
            else:
                return
            self.cur.execute(f'''INSERT INTO passwords(login, password, service)
             VALUES(?, ?, ?)''', (login, passw, serv))
            self.con.commit()
            self.comboBox.addItem(serv)

    def get_log_from_sql(self, ser):
        a = self.cur.execute('SELECT * FROM passwords').fetchall()
        b = []
        for i in a:
            if i[2] == ser:
                b.append(i[0])
        return b

    def get_pass_from_sql(self, ser):
        a = self.cur.execute('SELECT * FROM passwords').fetchall()
        b = []
        for i in a:
            if i[2] == ser:
                b.append(i[1])
        return b

    def get_services_from_sql(self):
        a = self.cur.execute('SELECT * FROM passwords').fetchall()
        return list(map(lambda x: x[2], a))

    def output_pass(self, text):
        self.login_output.setText(';'.join(self.get_log_from_sql(text)))
        self.pass_output.setText(';'.join(self.get_pass_from_sql(text)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
