# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\prana\OneDrive\Desktop\Documents\My Files\Projects\Procrastinator\time_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(453, 99)
        self.window_7 = QtWidgets.QFrame(Form)
        self.window_7.setGeometry(QtCore.QRect(10, 10, 431, 41))
        self.window_7.setStyleSheet("QFrame {\n"
"    border: 1px solid;\n"
"    border-radius: 5px;\n"
"    border-bottom-color: rgb(222, 169, 151);\n"
"border-right-color: rgb(222, 169, 151);\n"
"border-left-color: rgb(222, 169, 151);\n"
"    border-top-color: rgb(222, 169, 151);\n"
"}")
        self.window_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.window_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.window_7.setObjectName("window_7")
        self.frame_grip_7 = QtWidgets.QFrame(self.window_7)
        self.frame_grip_7.setGeometry(QtCore.QRect(490, 270, 19, 19))
        self.frame_grip_7.setStyleSheet("QFrame {\n"
"border-radius: 10px;\n"
"}")
        self.frame_grip_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_grip_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_grip_7.setObjectName("frame_grip_7")
        self.project_name = QtWidgets.QLineEdit(self.window_7)
        self.project_name.setGeometry(QtCore.QRect(170, 11, 151, 20))
        self.project_name.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    background-color: rgb(252, 252, 252);\n"
"    color: #edb4a1;\n"
"    padding: 2px;\n"
"    padding-bottom: 5px;    \n"
"    font: 63 8pt \"Cascadia Code SemiBold\";\n"
"}")
        self.project_name.setInputMask("")
        self.project_name.setObjectName("project_name")
        self.frame_3 = QtWidgets.QFrame(self.window_7)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 61, 21))
        self.frame_3.setStyleSheet("QFrame {\n"
"border: 1px solid;\n"
"border-radius: 6px;\n"
"border-top-color: rgb(237, 180, 161);\n"
"border-right-color: rgb(237, 180, 161);\n"
"border-left-color: rgb(237, 180, 161);\n"
"border-bottom-color: rgb(237, 180, 161);\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.stop_bt = QtWidgets.QPushButton(self.window_7)
        self.stop_bt.setGeometry(QtCore.QRect(330, 11, 41, 20))
        self.stop_bt.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    color: rgb(80, 125, 97);\n"
"    background-color: rgb(252, 252, 252);\n"
"    border: 1px solid;\n"
"    border-top-color: rgb(255, 0, 0);\n"
"    border-right-color: rgb(255, 0, 0);\n"
"    border-left-color: rgb(255, 0, 0);\n"
"    border-bottom-color: rgb(255, 0, 0);\n"
"    font: 11pt \"Cascadia Code\";\n"
"    padding-bottom: 2px;\n"
"}\n"
"QPushButton::hover {\n"
"    background-color: rgb(240, 240, 240);\n"
"    border-top-color: rgb(227, 0, 0);\n"
"    border-right-color: rgb(227, 0, 0);\n"
"    border-left-color: rgb(227, 0, 0);\n"
"    border-bottom-color: rgb(227, 0, 0);\n"
"}")
        self.stop_bt.setObjectName("stop_bt")
        self.seconds = QtWidgets.QLineEdit(self.window_7)
        self.seconds.setGeometry(QtCore.QRect(80, 11, 81, 20))
        self.seconds.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    background-color: rgb(252, 252, 252);\n"
"    color: #edb4a1;\n"
"    padding: 2px;\n"
"    padding-bottom: 5px;    \n"
"    font: 63 8pt \"Cascadia Code SemiBold\";\n"
"}")
        self.seconds.setText("")
        self.seconds.setReadOnly(True)
        self.seconds.setObjectName("seconds")
        self.DNALabel_8 = QtWidgets.QLabel(self.window_7)
        self.DNALabel_8.setGeometry(QtCore.QRect(16, -5, 51, 51))
        self.DNALabel_8.setStyleSheet("QLabel {\n"
"    border-radius: 3px;\n"
"    border: 0px;\n"
"    color: #edb4a1;\n"
"    font: 25 13pt \"Cascadia Code Light\";\n"
"}")
        self.DNALabel_8.setObjectName("DNALabel_8")
        self.pause_bt = QtWidgets.QPushButton(self.window_7)
        self.pause_bt.setGeometry(QtCore.QRect(380, 11, 41, 20))
        self.pause_bt.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    color: #edb4a1;\n"
"background-color: rgb(252, 252, 252);\n"
"    font: 11pt \"Cascadia Code\";\n"
"    padding-bottom: 2px;\n"
"}\n"
"QPushButton::hover {\n"
"    color: rgb(203, 154, 138);\n"
"    background-color: rgb(240, 240, 240);\n"
"}\n"
"QPushButton::disabled {\n"
"    color: rgb(108, 108, 108);\n"
"    background-color: rgb(163, 163, 163);\n"
"}")
        self.pause_bt.setObjectName("pause_bt")
        self.all_tasks = QtWidgets.QPlainTextEdit(Form)
        self.all_tasks.setGeometry(QtCore.QRect(10, 60, 431, 31))
        self.all_tasks.setStyleSheet("             QPlainTextEdit{\n"
"             border: 0px solid;\n"
"             border-color: none;\n"
"             border-radius: 6px;\n"
"             color: #edb4a1;\n"
"             font: 63 8pt \"Cascadia Code SemiBold\";\n"
"             }\n"
"        QScrollBar:vertical {\n"
"            border: 0px solid #dca795;\n"
"            background:white;   \n"
"            margin: 0px 0px 0px 0px;\n"
"               width: 1px;\n"
"        }\n"
"        QScrollBar::handle:vertical {         \n"
"       \n"
"            min-height: 0px;\n"
"              border: 0px solid red;\n"
"            border-radius: 5px;\n"
"            background-color: #dca795;\n"
"        }\n"
"        QScrollBar::add-line:vertical {       \n"
"            height: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line:vertical {\n"
"            height: 0px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"")
        self.all_tasks.setReadOnly(True)
        self.all_tasks.setObjectName("all_tasks")
        self.finishTask = QtWidgets.QPushButton(Form)
        self.finishTask.setGeometry(QtCore.QRect(410, 65, 21, 20))
        self.finishTask.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    color: rgb(80, 125, 97);\n"
"    background-color: rgb(252, 252, 252);\n"
"    border: 1px solid;\n"
"    border-top-color: rgb(102, 252, 91);\n"
"    border-right-color: rgb(102, 252, 91);\n"
"    border-left-color: rgb(102, 252, 91);\n"
"    border-bottom-color: rgb(102, 252, 91);\n"
"    font: 11pt \"Cascadia Code\";\n"
"    padding-bottom: 2px;\n"
"}\n"
"QPushButton::hover {\n"
"    background-color: rgb(240, 240, 240);\n"
"    border-top-color: rgb(97, 234, 84);\n"
"    border-right-color:rgb(97, 234, 84);\n"
"    border-left-color: rgb(97, 234, 84);\n"
"    border-bottom-color:rgb(97, 234, 84)\n"
"}")
        self.finishTask.setObjectName("finishTask")
        self.skipTask = QtWidgets.QPushButton(Form)
        self.skipTask.setGeometry(QtCore.QRect(380, 65, 21, 20))
        self.skipTask.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    color: #edb4a1;\n"
"background-color: rgb(252, 252, 252);\n"
"    font: 11pt \"Cascadia Code\";\n"
"    padding-bottom: 2px;\n"
"}\n"
"QPushButton::hover {\n"
"    color: rgb(203, 154, 138);\n"
"    background-color: rgb(240, 240, 240);\n"
"}\n"
"QPushButton::disabled {\n"
"    color: rgb(108, 108, 108);\n"
"    background-color: rgb(163, 163, 163);\n"
"}")
        self.skipTask.setObjectName("skipTask")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.project_name.setText(_translate("Form", "Project Name"))
        self.stop_bt.setText(_translate("Form", "🛑"))
        self.DNALabel_8.setText(_translate("Form", "Timer"))
        self.pause_bt.setText(_translate("Form", "⏸️"))
        self.all_tasks.setPlainText(_translate("Form", "Task 1:\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""))
        self.finishTask.setText(_translate("Form", "✅"))
        self.skipTask.setText(_translate("Form", "🔙"))
