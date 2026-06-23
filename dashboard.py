from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/")

def home():

    conn = sqlite3.connect("asm.db")

    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM subdomains")
    subdomains = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM live_hosts")
    live_hosts = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM ports")
    ports = cursor.fetchone()[0]

    conn.close()

    return f"""
    <h1>Attack Surface Management Dashboard</h1>

    <h2>Total Subdomains: {subdomains}</h2>

    <h2>Total Live Hosts: {live_hosts}</h2>

    <h2>Total Open Ports: {ports}</h2>
    """

if __name__ == "__main__":
    app.run(debug=True)