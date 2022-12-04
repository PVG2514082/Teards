import sys
import os
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QShortcut, \
    QInputDialog, QLineEdit
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QEvent
from choice_of_board_1 import Ui_Form
import editing_the_board
import json
import db


class Board_selection_window(Ui_Form, QWidget):
    def __init__(self, cx: int, dm: dict):
        # Инициализация базового класса
        super().__init__()

        self.cx = cx
        self.dn = -1
        self.dm = dm

        self.setupUi(self)

        self.init_ui()

    def init_ui(self):
        # Значок для окна
        self.setWindowIcon(QtGui.QIcon(":/icons/app.png"))
        # Ярлык для сохранения данных досок в файл
        QShortcut(QtGui.QKeySequence.Save, self).activated.connect(self.save)
        self.s.clicked.connect(self.add_board)
        self.u.setLayout(self.v)

        for do in self.dm["boards"]:
            x = do["title"]
            if not x:
                x = "Без названия"

            dp = QLabel(x, self)
            dp.setStyleSheet("color: #fffafa;")
            dp.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            dp.setFont(QtGui.QFont("Nirmala UI", pointSize=16))
            dp.installEventFilter(self)

            self.v.addWidget(dp)

        self.d.addWidget(self.s, Qt.AlignHCenter)
        self.d.addWidget(self.t, Qt.AlignHCenter | Qt.AlignVCenter)
        self.setLayout(self.d)

    def add_board(self):
        dq, dr = QInputDialog.getText(self, "Название",
                                                  "Введите название доски",
                                      QLineEdit.Normal)
        # Проверить имя из входных данных
        dq = dq.replace('\t', ' ').replace('\n', ' ')
        if not (dr and dq.replace(' ', '')):
            dq = "Без названия"

        self.dm["boards"].append({"title": dq, "groups": []})
        dp = QLabel(dq, self)
        dp.setStyleSheet("color: #fffafa;")
        dp.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        dp.setFont(QtGui.QFont("Nirmala UI", pointSize=16))
        dp.installEventFilter(self)
        self.v.insertWidget(self.v.count(), dp)

    def closeEvent(self, event):
        self.save()

    def save(self, *args) -> None:
        if self.cx != -1:
            import db
            ds = db.database()
            ds.update_boards_json_by_user_id(self.cx, json.get_json_by_data(self.dm))
        else:
            json.save_json_data_to_file("boards.json", self.dm)

    def eventFilter(self, source_obj, dk) -> bool:
        if dk.type() == QEvent.MouseButtonRelease and dk.button() == Qt.LeftButton:
            self.open_board(source_obj)
        return super().eventFilter(source_obj, dk)

    def open_board(self, sender) -> None:
        # ID доски
        self.dn = self.v.indexOf(sender)
        self.close()


def start(cx: int, extra_args={}):
    dm = {
        "boards": []
    }

    if cx != -1:
        ds = db.database()
    else:
        ds = None

    if os.path.isfile("boards.json") and cx == -1:
        dt = json.load_json_data_from_file("boards.json")
        dm["boards"].extend(dt.get("boards", []))

    if ds:
        du = ds.get_boards_json_by_user_id(cx)
        du = json.parse_json(du)
        dv = du.get("boards", [])
        if dv:
            dm["boards"].extend(dv)
        del dv

    dw = []
    for dx in dm["boards"]:
        if dx not in dw:
            dw.append(dx)
    dm["boards"] = dw.copy()
    del dw

    if os.path.isfile("last_board.json"):
        dy = json.load_json_data_from_file("last_board.json")
        if dy != {"boards": []}:
            if dy["board_id"] < len(dm["boards"]):
                dm["boards"][dy["board_id"]] = {
                    "title": dy["title"],
                    "groups": dy["groups"],
                }
            else:
                dm["boards"].append({
                    "title": dy["title"],
                    "groups": dy["groups"],
                })
            if os.path.isfile("boards.json") and dy.get("was_on_device", False):
                json.save_json_data_to_file("boards.json", dm)
        dz = open("last_board.json", mode='r+', encoding="utf-8")
        dz.truncate(0)
        dz.close()

    if extra_args.get("update_db_from_file", False) and ds:
        ds.update_boards_json_by_user_id(cx,
                                         json.get_json_by_data(dm))

    cv = QApplication(sys.argv)
    cw = Board_selection_window(cx, dm)
    cw.show()
    cv.exec()
    del cv
    del ds
    if cw.dn != -1:
        editing_the_board.start(cx, cw.dn, dm["boards"][cw.dn])