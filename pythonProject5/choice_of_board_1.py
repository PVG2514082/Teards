from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, a):
        a.setObjectName("Form")
        a.resize(611, 443)
        a.setStyleSheet("#Form {\n"
"    background: #2f353b;\n"
"}")
        self.c = QtWidgets.QWidget(a)
        self.c.setGeometry(QtCore.QRect(10, 10, 571, 524))
        self.c.setObjectName("verticalLayoutWidget")
        self.d = QtWidgets.QVBoxLayout(self.c)
        self.d.setContentsMargins(2, 2, 2, 2)
        self.d.setObjectName("vlayout_main")
        self.s = QtWidgets.QPushButton(self.c)
        self.s.setObjectName("button_create_board")
        self.d.addWidget(self.s)
        self.t = QtWidgets.QScrollArea(self.c)
        self.t.setStyleSheet("#scroll_area_items {\n"
"    background-color: transperent;\n"
"}")
        self.t.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.t.setFrameShadow(QtWidgets.QFrame.Plain)
        self.t.setWidgetResizable(True)
        self.t.setObjectName("scroll_area")
        self.u = QtWidgets.QWidget()
        self.u.setGeometry(QtCore.QRect(0, 0, 567, 491))
        self.u.setStyleSheet("#scroll_area_widget_container {\n"
"    background: #2f353b;\n"
"}")
        self.u.setObjectName("scroll_area_widget_container")
        self.c_2 = QtWidgets.QWidget(self.u)
        self.c_2.setGeometry(QtCore.QRect(20, 20, 521, 361))
        self.c_2.setObjectName("verticalLayoutWidget_2")
        self.v = QtWidgets.QVBoxLayout(self.c_2)
        self.v.setContentsMargins(0, 0, 0, 0)
        self.v.setObjectName("vlayout_items")
        self.t.setWidget(self.u)
        self.d.addWidget(self.t)
        self.retranslateUi(a)
        QtCore.QMetaObject.connectSlotsByName(a)

    def retranslateUi(self, a):
        r = QtCore.QCoreApplication.translate
        a.setWindowTitle(r("Form", "Terds"))
        self.s.setText(r("Form", "Добавить доску"))