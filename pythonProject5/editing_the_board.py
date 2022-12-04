import sys

from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QShortcut, \
    QMessageBox
from PyQt5 import  QtGui
from PyQt5.QtCore import Qt
from editing_the_board_1 import Ui_Form
from custom_widgets import  QGroup

import choice_of_board

import json


class Board_edit_window(Ui_Form, QWidget):
    def __init__(self, cx: int, cy: int, cz: dict):
        # Инициализация базового класса
        super().__init__()
        self.cx = cx
        self.cy = cy
        self.cz = cz
        self.x = cz["title"]
        self.da = False
        self.dc = {
            "board_id": self.cy,
            "update_db_from_file": False,
        }

        self.setupUi(self)
        # Установите привязки и некоторые стили для виджетов
        self.init_ui()

    def init_ui(self):
        QShortcut(QtGui.QKeySequence.Save, self).activated.connect(self.save)
        # Иконки для навигационной панели
        self.e.setLayout(self.h)
        self.d.setAlignment(self.e, Qt.AlignTop)
        self.h.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        # Иконка сохраниения
        self.dd = QLabel()
        self.dd.setPixmap(QtGui.QPixmap(":/icons/save.png"))
        self.h.addWidget(self.dd)
        self.dd.mousePressEvent = self.save
        # Иконка информации
        self.de = QLabel()
        self.de.setPixmap(QtGui.QPixmap(":/icons/info.png"))
        self.h.addWidget(self.de)
        self.de.mousePressEvent = self.show_info
        # Иконка возвращения на главный экран
        self.df = QLabel()
        self.df.setPixmap(QtGui.QPixmap(":/icons/home.png"))
        self.h.addWidget(self.df)
        self.df.mousePressEvent = self.open_selection_window

        self.dg = QLabel(self.x)
        self.dg.setFont(QtGui.QFont("Nirmala UI", pointSize=14))
        self.dg.setStyleSheet("QLabel{color: #fffafa;}")
        self.h.addWidget(self.dg)
        self.h.setAlignment(self.dg, Qt.AlignHCenter | Qt.AlignVCenter)

        for dh, di in enumerate(self.cz["groups"]):
            current_group = QGroup(dh, di["title"], [])
            for al in di["cards"]:
                current_group.add_card(x=al["title"],
                                       y=al["marks_colors"].copy(),
                                       z=al["description"])
            self.k.insertWidget(self.k.count() - 1, current_group)

        self.i.setLayout(self.k)
        self.d.addWidget(self.g, Qt.AlignHCenter | Qt.AlignVCenter)

        self.o.clicked.connect(self.add_group)
        self.dj = self.set_focus
        self.setFocus()
        self.setWindowIcon(QtGui.QIcon(":/icons/app.png"))
        self.setLayout(self.d)
        self.setMinimumSize(1000, 550)

    def add_group(self):
        di = QGroup(len(self.cz["groups"]), "Без названия", ah=[])
        self.k.insertWidget(self.k.count() - 1, di)
        self.cz["groups"].append(di.to_dict())

    def set_focus(self, dk):
        if dk.button() == Qt.LeftButton:
            self.setFocus()

    def save(self, *args) -> None:
        dl = {
            "title": self.x,
            "board_id": self.cy,
            "groups": [],
            "was_on_device": self.cx == -1
        }
        for i in range(self.k.count() - 1):
            dl["groups"].append(self.k.itemAt(i).widget().to_dict())

        json.save_json_data_to_file("last_board.json", dl)

    def show_info(self, *args) -> None:
        INFO = str("Это раздел с редактированием текстовой доски, вы можете создавать группы,\n" +
               "добавлять карточки внутрь группы.")
        az = QMessageBox(QMessageBox.Information, "Информация", INFO)
        az.setWindowIcon(QtGui.QIcon(":/icons/app.png"))
        az.exec_()

    def open_selection_window(self, *args) -> None:
        self.save()
        self.da = True
        self.dc["update_db_from_file"] = True
        self.close()


def start(cx: int, cy: int, cz):
    cv = QApplication(sys.argv)
    cw = Board_edit_window(cx, cy, cz)
    cw.show()
    cv.exec()
    del cv
    # Открыть окно выбора, если нам это нужно
    if cw.da:
        board_selection.start(cx, cw.dc)