from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, a):
        a.setObjectName("Form")
        a.resize(902, 704)
        b = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        b.setHorizontalStretch(0)
        b.setVerticalStretch(0)
        b.setHeightForWidth(a.sizePolicy().hasHeightForWidth())
        a.setSizePolicy(b)
        a.setMinimumSize(QtCore.QSize(0, 180))
        a.setStyleSheet("#Form {\n"
"    background: #2f353b;\n"
"}")
        self.c = QtWidgets.QWidget(a)
        self.c.setGeometry(QtCore.QRect(20, 20, 481, 451))
        self.c.setObjectName("verticalLayoutWidget")
        self.d = QtWidgets.QVBoxLayout(self.c)
        self.d.setContentsMargins(0, 0, 0, 0)
        self.d.setObjectName("vlayout_main")
        self.e = QtWidgets.QWidget(self.c)
        b = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        b.setHorizontalStretch(0)
        b.setVerticalStretch(0)
        b.setHeightForWidth(self.e.sizePolicy().hasHeightForWidth())
        self.e.setSizePolicy(b)
        self.e.setMinimumSize(QtCore.QSize(0, 60))
        self.e.setStyleSheet("#widget_navbar {\n"
"    background: #1d1e33;\n"
"}")
        self.e.setObjectName("widget_navbar")
        self.f = QtWidgets.QWidget(self.e)
        self.f.setGeometry(QtCore.QRect(10, 10, 461, 61))
        self.f.setObjectName("horizontalLayoutWidget")
        self.h = QtWidgets.QHBoxLayout(self.f)
        self.h.setContentsMargins(10, 10, 2, 2)
        self.h.setSpacing(10)
        self.h.setObjectName("hlayout_navbar")
        self.d.addWidget(self.e)
        self.g = QtWidgets.QScrollArea(self.c)
        self.g.setStyleSheet("#scroll_area_window {\n"
"    background-color: transperent;\n"
"}")
        self.g.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.g.setWidgetResizable(True)
        self.g.setObjectName("scroll_area_window")
        self.i = QtWidgets.QWidget()
        self.i.setGeometry(QtCore.QRect(0, 0, 479, 383))
        self.i.setStyleSheet("#scroll_area_widget_window {\n"
"    background: #2f353b;\n"
"}")
        self.i.setObjectName("scroll_area_widget_window")
        self.j = QtWidgets.QWidget(self.i)
        self.j.setGeometry(QtCore.QRect(-50, 10, 479, 383))
        self.j.setObjectName("widget")
        self.k = QtWidgets.QHBoxLayout(self.j)
        self.k.setContentsMargins(0, 0, 0, 0)
        self.k.setSpacing(3)
        self.k.setObjectName("hlayout_groups")
        self.m = QtWidgets.QGridLayout()
        self.m.setObjectName("gridLayout_add_button_container")
        n = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.m.addItem(n, 2, 1, 1, 1)
        n_1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.m.addItem(n_1, 0, 1, 1, 1)
        n_2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.m.addItem(n_2, 1, 2, 1, 1)
        n_3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.m.addItem(n_3, 1, 0, 1, 1)
        self.o = QtWidgets.QPushButton(self.j)
        b = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        b.setHorizontalStretch(0)
        b.setVerticalStretch(0)
        b.setHeightForWidth(self.o.sizePolicy().hasHeightForWidth())
        self.o.setSizePolicy(b)
        self.o.setMinimumSize(QtCore.QSize(165, 40))
        self.o.setMaximumSize(QtCore.QSize(165, 55))
        q = QtGui.QFont()
        q.setFamily("Nirmala UI")
        q.setPointSize(10)
        self.o.setFont(q)
        self.o.setStyleSheet("#button_add_group {\n"
"    border-color: #08e8de;\n"
"    border-style: outset;\n"
"    border-radius: 0.625em;\n"
"    \n"
"    padding-left: 0.625em;\n"
"    padding-right: 0.625em;\n"
"    padding-top: 0.3em;\n"
"    padding-bottom:  0.3em;\n"
"\n"
"    color: #fffafa;\n"
"    background-color: #543964;\n"
"}\n"
"\n"
"#button_add_group::hover {\n"
"    background-color: #6c4675;\n"
"    border-color: #6c4675;\n"
"}\n"
"\n"
"#button_add_group:pressed {\n"
"    background-color: #6c4675;\n"
"    border-color: #30d5c8;\n"
"    outline: none;\n"
"}")
        self.o.setObjectName("button_add_group")
        self.m.addWidget(self.o, 1, 1, 1, 1)
        self.k.addLayout(self.m)
        self.g.setWidget(self.i)
        self.d.addWidget(self.g)

        self.retranslateUi(a)
        QtCore.QMetaObject.connectSlotsByName(a)

    def retranslateUi(self, a):
        r = QtCore.QCoreApplication.translate
        a.setWindowTitle(r("Form", "Terds"))
        self.o.setText(r("Form", "Добавить группу"))