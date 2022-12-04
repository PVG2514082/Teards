import hashlib
import os
import sqlite3


class AccountNotExists(Exception):
    pass


class IncorrectPassword(Exception):
    pass


class AccountAlreadyExists(Exception):
    pass


class database:
    def __init__(self, filename="users.sqlite"):
        self.a = sqlite3.connect(filename)
        # Некоторые постоянные переменные для работы модуля
        self.b = 32
        self.c = 100000

    def __del__(self):
        self.a.close()

    def is_user_by_id_exists(self, value: int) -> bool:
        # Проверьте, что учетная запись с этим логином не существует
        a = """
                SELECT * FROM users 
                WHERE id = ?
                """
        b = self.a.cursor().execute(a,
                                    (value,)).fetchall()
        return len(b) != 0

    def get_password_hash_with_random_salt(self, e: str) -> bytes:
        c = os.urandom(self.b)
        # Хэш заданного пароля
        d = hashlib.pbkdf2_hmac("sha256",
                                e.encode("utf-8"),
                                c,
                                self.c)
        return c + d

    def get_password_hash_by_salt(self, e: str, c: bytes) -> bytes:
        return hashlib.pbkdf2_hmac("sha256",
                                   e.encode("utf-8"),
                                   c,
                                   self.c)

    def get_user_id_from_db_by_form_data(self, f: str, e: str) -> int:
        # Запрос для получения идентификатора и хэша из учетной записи по заданному логину
        a = """
                SELECT id, password FROM users
                WHERE login = ?
                """
        # Идентификатор и хэш из учетной записи по заданному логину
        g = self.a.cursor().execute(a,
                                    (f,)).fetchone()
        if g is None:
            raise AccountNotExists

        # Потому что db_data[0] - это идентификатор пользователя
        h = g[-1]

        k = h[:self.b]
        m = h[self.b:]
        n = self.get_password_hash_by_salt(e, k)

        # Сравнение паролей
        if n != m:
            raise IncorrectPassword

        return g[0]

    def add_account_to_db(self, f: str, e: str, q='') -> None:
        # Проверьте, что учетная запись с указанным логином не существует
        a = """
                          SELECT id FROM users
                          WHERE login = ?
                          """
        w = self.a.cursor().execute(a,
                                    (f,)).fetchall()
        if w:
            raise AccountAlreadyExists

        a = """
                INSERT INTO users (login, password, boards)
                VALUES (?, ?, ?)
                """
        e = self.get_password_hash_with_random_salt(e)
        self.a.cursor().execute(a,
                                (f,
                                 e,
                                 q))
        self.a.commit()

    def get_boards_json_by_user_id(self, e: int) -> str:
        if not self.is_user_by_id_exists(e):
            raise AccountNotExists

        a = """
                SELECT boards FROM users
                WHERE id = ?
                """
        r = self.a.cursor().execute(a,
                                    (e,)).fetchone()
        return r[0]

    def update_boards_json_by_user_id(self, u: int, n: str) -> None:
        if not self.is_user_by_id_exists(u):
            raise AccountNotExists

        a = """
                UPDATE users
                SET boards = ?
                WHERE id = ?
                """
        self.a.cursor().execute(a,
                                (n, u,))
        self.a.commit()