import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QFrame, QLabel, QApplication, \
    QVBoxLayout, QHBoxLayout, QSizePolicy, QPlainTextEdit, QLineEdit, \
    QScrollArea, QScrollBar, QColorDialog, QMessageBox
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from icons import ico


class QCard(QWidget):
    def __init__(self, w: int, x='', y=[], z='', aa=None):
        super().__init__(aa)
        self.ab = aa

        self.y = y
        self.x = x
        self.z = z
        self.w = w

        self.init_ui()

    def init_ui(self):
        self.ac = QWidget(self)
        self.ac.setObjectName("card_widget_main")
        self.ac.resize(140, 120)
        self.ac.setMinimumSize(130, 120)
        self.ac.setMaximumSize(260, 260)
        self.ac.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        # Название карточки (доступно для редактирования)
        self.ad = QLineEdit(self.x)
        self.ad.setStyleSheet("""
                                          QLineEdit { 
                                          background:rgba(0, 0, 0, 0);
                                          color: rgba(255, 255, 255, 93%);
                                          border-style: None; }""")
        self.ad.setFont(QtGui.QFont("Nirmala UI", pointSize=10))
        self.ad.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        self.at = QHBoxLayout()
        for ae in self.y:
            af = QWidget()
            af.setMinimumSize(22, 5)
            af.setMaximumHeight(8)
            af.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            af.setStyleSheet("QWidget {background: " + ae + ";}")
            self.at.addWidget(af)
        # Добавление значка удаления в макет с пометками
        self.au = QLabel()
        self.au.setPixmap(QtGui.QPixmap(":/icons/add.png"))
        self.au.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.au.mousePressEvent = self.add_mark
        self.at.addWidget(self.au)
        # Добавление значка удаления в макет с пометками
        self.ar = QLabel()
        self.ar.setPixmap(QtGui.QPixmap(":/icons/delete.png"))
        self.ar.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.ar.mousePressEvent = self.delete_card
        self.at.addWidget(self.ar)

        self.av = QPlainTextEdit(self.z)
        self.av.setStyleSheet("""
                                                QPlainTextEdit { 
                                                margin-top: 0.1em;
                                                margin-bottom: 0.1em;
                                                background:rgba(0, 0, 0, 0%);
                                                color: rgba(255, 255, 255, 79%);
                                                selection-background-color: grey;
                                                border: None; }""")
        self.av.setFont(QtGui.QFont("Nirmala UI", pointSize=10))
        self.av.setWordWrapMode(QtGui.QTextOption.WordWrap)
        self.av.setFrameStyle(QFrame.NoFrame)
        self.av.setAutoFillBackground(False)
        # Палитра для редактирования текста
        aw = QtGui.QPalette()
        aw.setColor(QtGui.QPalette.Highlight, QtGui.QColor(255, 255, 255, 200))
        aw.setColor(QtGui.QPalette.HighlightedText, QtGui.QColor(255, 255, 255, 200))
        self.av.setPalette(aw)

        self.d = QVBoxLayout()
        self.d.setContentsMargins(8, 5, 8, 5)
        self.d.addLayout(self.at)
        self.d.addWidget(self.ad)
        self.d.addWidget(self.av)
        self.d.setStretch(3, 2)
        self.ac.setLayout(self.d)

        self.ax = QVBoxLayout()
        self.ax.addWidget(self.ac)
        self.setLayout(self.ax)
        self.setStyleSheet("""#card_widget_main {
                              padding-top: 0.2em;
                              padding-bottom: 0.2em;
                              background: #413d51;
                              border-style: outset;
                              border-radius: 15px;
                              }
                              #card_widget_main::hover {
                              background: #423c63; 
                              }""")
        self.ay = self.change_focus

    def change_focus(self, *args):
        self.setFocus()

    def add_mark(self, *args):
        if len(self.y) > 2:
            az = QMessageBox(QMessageBox.Information, "Внимание!",
                                  "Достигнут лимит по цветным меткам")
            az.setWindowIcon(QtGui.QIcon(":/icons/app.png"))
            az.exec_()
            return
        # Выбор цвета
        ba = QColorDialog()
        ba.exec_()
        ae = ba.selectedColor()
        # Добавление метки
        self.y.append(ae.name())
        af = QWidget()
        af.setMinimumSize(22, 5)
        af.setMaximumHeight(8)
        af.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        af.setStyleSheet("QWidget {background: " + ae.name() + ";}")
        self.at.insertWidget(1, af)

    def delete_card(self, *args):
        self.ab.remove_card(self)

    def to_dict(self) -> dict:
        return {
                "title": self.x,
                "description": self.z,
                "marks_colors": self.y
        }


class QGroup(QWidget):
    def __init__(self, ag: int, x='', ah=[], aa=None):
        super().__init__(aa)
        # Название группы
        self.x = x
        # Список карточек в группе
        self.ah = ah
        # Идентификатор текущей группы
        self.ag = ag

        self.init_ui()

    def init_ui(self):
        self.ai = QWidget(self)
        # Название группы
        self.ad = QLineEdit(self.x)
        self.ad.mouseDoubleClickEvent = lambda event: self.ad.selectAll()
        self.ad.focusInEvent = lambda event: None
        self.ad.setStyleSheet("""
                                          QLineEdit { 
                                          margin-right: 8px;
                                          background:rgba(0, 0, 0, 0);
                                          color: rgba(255, 255, 255, 93%);
                                          border-style:None }""")
        self.ad.setFont(QtGui.QFont("Nirmala UI", pointSize=12))
        self.ad.setAlignment(Qt.AlignLeft | Qt.AlignCenter)
        self.ad.setMaxLength(30)

        self.aj = QLabel("+ Добавить ещё одну карточку")
        self.aj.setFont(QtGui.QFont("Nirmala UI", pointSize=10))
        self.aj.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.aj.setStyleSheet("""
                                           QLabel { 
                                           color: rgba(255, 255, 255, 79%);
                                           padding: 4px 4px 4px 4px;
                                           }
                                           QLabel:hover {
                                           background: #252850;                                       
                                           }""")
        self.aj.mousePressEvent = lambda event: self.add_card()

        self.ak = QVBoxLayout()
        self.ak.setSpacing(6)
        for al in self.ah:
            am = QCard(self.ak.count(), al.title, al.marks_colors,
                       al.description, aa=self)
            self.ak.addWidget(am)

        self.t = QScrollArea(self)
        self.t.setFrameStyle(QFrame.NoFrame)
        self.t.setStyleSheet("QScrollArea{background:transparent;}")
        self.t.setAutoFillBackground(False)
        self.an = QWidget()
        self.an.setAutoFillBackground(False)
        self.an.setObjectName("widget_cards_container")
        self.an.setStyleSheet("""#widget_cards_container{
                                                  background:#1d1e33;
                                                  border-style: outset;
                                                  border-radius: 25px;}""")
        self.an.setLayout(self.ak)
        self.t.setWidget(self.an)
        self.t.setWidgetResizable(True)

        self.d = QVBoxLayout()
        self.d.addWidget(self.ad)
        self.d.addWidget(self.t)
        self.d.addWidget(self.aj)
        self.d.setAlignment(self.aj, Qt.AlignLeft | Qt.AlignCenter)
        self.d.setContentsMargins(5, 5, 5, 5)
        self.ai.setLayout(self.d)

        self.ao = QVBoxLayout()
        self.ao.addWidget(self.ai)
        self.setLayout(self.ao)

    def add_card(self, y=[], x="Без названия", z="Без описания") -> None:
        card = QCard(len(self.ah), x=x, y=list(y), z=z, aa=self)
        self.ah.append(card)
        self.ak.addWidget(card)

    def remove_card(self, ap: QCard) -> None:
        if ap in self.ah:
            self.ah.remove(ap)
            self.ak.removeWidget(ap)
            ap.setParent(None)
            self.ak.update()
            del ap

    def to_dict(self) -> dict:
        aq = {
            "title": self.x,
            "cards": []
        }

        for card in self.ah:
            aq["cards"].append(card.to_dict())

        return aq