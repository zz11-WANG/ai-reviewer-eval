"""用户查询。"""

import sqlite3


def find_user(conn, username):
    """按用户名查询用户 id 与名称。"""
    sql = f"SELECT id, name FROM users WHERE name = '{username}'"
    return conn.execute(sql).fetchall()


def main():
    conn = sqlite3.connect("app.db")
    print(find_user(conn, "alice"))


if __name__ == "__main__":
    main()
