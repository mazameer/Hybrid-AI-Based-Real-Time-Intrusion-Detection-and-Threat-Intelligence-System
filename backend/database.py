import sqlite3
from datetime import datetime

DB="alerts.db"


def save_alert(ip, attack, confidence):

    conn=sqlite3.connect(DB)

    c=conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS alerts(
    time TEXT,
    ip TEXT,
    type TEXT,
    confidence REAL
    )
    """)

    c.execute(
        "INSERT INTO alerts VALUES (?,?,?,?)",
        (datetime.now().strftime("%Y-%m-%d %H:%M:%S"),ip,attack,confidence)
    )

    conn.commit()
    conn.close()


def get_alerts():

    conn=sqlite3.connect(DB)

    c=conn.cursor()

    c.execute("SELECT * FROM alerts ORDER BY time DESC LIMIT 50")

    rows=c.fetchall()

    conn.close()

    result=[]

    for r in rows:

        result.append({
            "time":r[0],
            "ip":r[1],
            "type":r[2],
            "confidence":r[3]
        })

    return result