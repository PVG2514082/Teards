from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton
import db
import json
from form_of_login_1 import Ui_main_window
import sys


class Login_form_window(QMainWindow, Ui_main_window):
    def __init__(self):
        # Инициализация базового класса
        super().__init__()

        self.setupUi(self)

        self.ea = False
        # Аргументы для открытия меню выбора доски
        self.eb = []

        self.init_ui()

    def init_ui(self) -> None:
        # Настройка всех значков из файла ресурсов
        self.setWindowIcon(QIcon(":/icons/app.png"))
        self.bm.setPixmap(QPixmap(":/icons/user.png"))
        self.cq.setPixmap(QPixmap(":/icons/user.png"))
        self.bn.setPixmap(QPixmap(":/icons/key.png"))
        self.bt.setPixmap(QPixmap(":/icons/key.png"))
        self.cn.setPixmap(QPixmap(":/icons/key.png"))

        self.be.setAlignment(Qt.AlignJustify | Qt.AlignHCenter)
        self.by.setAlignment(Qt.AlignJustify | Qt.AlignHCenter)
        self.bx.setAlignment(Qt.AlignJustify | Qt.AlignHCenter)
        self.cj.setAlignment(Qt.AlignRight)
        self.bj.setAlignment(Qt.AlignLeft)

        self.bz.setAlignment(self.cd, Qt.AlignHCenter | Qt.AlignCenter)
        self.cj.setAlignment(self.cr, Qt.AlignCenter)
        self.bj.setAlignment(self.bv, Qt.AlignCenter)

        self.bf.setLayout(self.bg)
        self.widget_midle_background.setLayout(self.bz)
        self.cf.setLayout(self.cg)

        self.cr.clicked.connect(self.enter_account)
        self.bv.clicked.connect(self.create_account)
        self.cd.clicked.connect(self.work_offline)
        self.a.ay = lambda event: self.a.setFocus()
        self.cs.ay = lambda event: self.br.setFocus(True)
        self.bw.ay = lambda event: self.lineEdit_login_input.setFocus(True)

        self.a.setFocus()
        self.a.setLayout(self.bd)

    def check_form_field(self, ec: str) -> bool:
        ed = {
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
        }
        for ee in ec.lower():
            if ee not in ed:
                return False
        return len(ec) != 0

    def enter_account(self):
        # Проверка логина и пароля
        ef = self.lineEdit_login_input.text()
        eg = self.cm.text()

        eh = self.check_form_field(ef)
        ei = self.check_form_field(eg)
        # Все возможные случаи ниже
        if not eh:
            self.cq.setPixmap(QPixmap(":/icons/error.png"))
            self.cq.setToolTip("Неверный логин")
            self.cq.setToolTipDuration(5000)
        else:
            self.cq.setPixmap(QPixmap(":/icons/user.png"))
            self.cq.setToolTip('')

        if not ei:
            self.cn.setPixmap(QPixmap(":/icons/error.png"))
            self.cn.setToolTip("Неверный пароль")
            self.cn.setToolTipDuration(5000)
        else:
            self.cn.setPixmap(QPixmap(":/icons/key.png"))
            self.cn.setToolTip('')

        if not ei or not eh:
            return

        ds = db.database()
        try:
            cx = ds.get_user_id_from_db_by_form_data(ef, eg)
        except db.AccountNotExists as e:
            # Настройка значка ошибки и всплывающей подсказки, если что-то пойдет не так
            self.cq.setPixmap(QPixmap(":/icons/error.png"))
            self.cq.setToolTip("Неверный логин")
            return
        except db.IncorrectPassword as e:
            # Настройка значка ошибки и всплывающей подсказки, если что-то пойдет не так
            self.cn.setPixmap(QPixmap(":/icons/error.png"))
            self.cn.setToolTip("Неверный пароль")
            return
        else:
            self.cq.setPixmap(QPixmap(":/icons/user.png"))
            self.cq.setToolTip('')
            self.cn.setPixmap(QPixmap(":/icons/key.png"))
            self.cn.setToolTip('')

        ej = ds.get_boards_json_by_user_id(cx)
        ek = json.load_raw_json_from_file("boards.json")

        if json.can_combine_boards_jsons(json.format_json(ek),
                                         json.format_json(ej)):
            az = QMessageBox(QMessageBox.Information, '',
                                  "На устройстве найдены досоки, а в аккаунте ничего не сохранено\n" +
                                  "Хотите добавить данные в аккаунт?")
            az.setWindowIcon(QIcon(":/icons/app.png"))
            az.setWindowTitle("Terds")
            az.addButton(button_yes := QPushButton("Да", az), QMessageBox.YesRole)
            az.addButton(QPushButton("Нет", az), QMessageBox.NoRole)
            az.exec()

            if az.clickedButton() == button_yes:
                combined_json, combined_boards_data = json.combine_boards_jsons(ek,
                                                                                ej)
                ds.update_boards_json_by_user_id(cx,
                                                 combined_json)
        self.ea = True
        self.eb = [cx]
        self.close()

    def create_account(self) -> None:
        ef = self.br.text()
        eg = self.bq.text()
        el = self.bs.text()
        # Проверка логина и пароля
        eh = self.check_form_field(ef)
        ei = self.check_form_field(eg)
        # Все возможные случаи ниже
        if not eh:
            self.bm.setPixmap(QPixmap(":/icons/error.png"))
            self.bm.setToolTip("Неверный логин")
            self.bm.setToolTipDuration(5000)
        else:
            self.bm.setPixmap(QPixmap(":/icons/user.png"))
            self.bm.setToolTip('')

        if not ei:
            self.bn.setPixmap(QPixmap(":/icons/error.png"))
            self.bn.setToolTip("Неверный пароль")
            self.bn.setToolTipDuration(5000)
        else:
            self.bn.setPixmap(QPixmap(":/icons/key.png"))
            self.bn.setToolTip('')

        if not ei or not eh:
            return

        elif el != eg:
            self.bn.setPixmap(QPixmap(":/icons/error.png"))
            self.bn.setToolTip("Пароли не совпадают")
            self.bn.setToolTipDuration(5000)
            self.bt.setPixmap(QPixmap(":/icons/error.png"))
            self.bt.setToolTip("Пароли не совпадают")
            self.bt.setToolTipDuration(5000)
            return

        ds = db.database()
        try:
            ds.add_account_to_db(ef, eg)
        except db.AccountAlreadyExists as e:
            self.bm.setPixmap(QPixmap(":/icons/error.png"))
            self.bm.setToolTip("Данной аккаунт уже есть")
            self.bm.setToolTipDuration(5000)
            return
        else:
            # Значок пользователя
            self.cq.setPixmap(QPixmap(":/icons/user.png"))
            self.cq.setToolTip('')
            # Значок первого пароля
            self.bn.setPixmap(QPixmap(":/icons/key.png"))
            self.bn.setToolTip('')
            # Значок повторения пароля
            self.bt.setPixmap(QPixmap(":/icons/key.png"))
            self.bt.setToolTip('')

        cx = ds.get_user_id_from_db_by_form_data(ef, eg)
        self.ea = True
        self.eb = [cx]
        self.close()

    def work_offline(self) -> None:
        self.eb = [-1]
        self.ea = True
        self.close()


def start() -> list:
    cv = QApplication(sys.argv)
    cw = Login_form_window()
    cw.show()
    cv.exec()
    return [cw.eb,
            cw.ea]