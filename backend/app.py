from flask import Flask, jsonify
from flask_cors import CORS
import random
import time

app = Flask(__name__)
CORS(app)

alerts = []

ips = [
    "192.168.1.5",
    "192.168.1.10",
    "10.0.0.8",
    "172.16.0.4"
]

attack_types = [
    "Normal",
    "Scan",
    "Suspicious",
    "DoS"
]

def generate_alert():

    attack = random.choices(
        attack_types,
        weights=[50,20,20,10]
    )[0]

    alert = {
        "time": time.strftime("%H:%M:%S"),
        "ip": random.choice(ips),
        "type": attack,
        "confidence": round(random.uniform(0.5,0.99),2)
    }

    alerts.insert(0, alert)

    if len(alerts) > 50:
        alerts.pop()

@app.route("/alerts")
def get_alerts():

    generate_alert()

    return jsonify(alerts)


if __name__ == "__main__":
    print("Server running on http://localhost:5000")
    app.run(debug=True)