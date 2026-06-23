import sqlite3

def create_database():

    conn = sqlite3.connect("asm.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subdomains(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subdomain TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS live_hosts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        host TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ports(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        host TEXT,
        port INTEGER
    )
    """)

    conn.commit()
    conn.close()


def save_subdomains(subdomains):

    conn = sqlite3.connect("asm.db")
    cursor = conn.cursor()

    for subdomain in subdomains:
        cursor.execute(
            "INSERT INTO subdomains(subdomain) VALUES(?)",
            (subdomain,)
        )

    conn.commit()
    conn.close()


def save_live_hosts(hosts):

    conn = sqlite3.connect("asm.db")
    cursor = conn.cursor()

    for host in hosts:
        cursor.execute(
            "INSERT INTO live_hosts(host) VALUES(?)",
            (host,)
        )

    conn.commit()
    conn.close()


def save_port(host, port):

    conn = sqlite3.connect("asm.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO ports(host, port) VALUES(?, ?)",
        (host, port)
    )

    conn.commit()
    conn.close()