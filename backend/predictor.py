import numpy as np
import joblib
from tensorflow.keras.models import load_model
import random
import time

rf = joblib.load("models/rf.pkl")
scaler = joblib.load("models/scaler.pkl")
dl_model = load_model("models/dl.keras")

last_alert = {}
ALERT_DELAY = 3


def allow_alert(ip):

    now = time.time()

    if ip in last_alert:
        if now - last_alert[ip] < ALERT_DELAY:
            return False

    last_alert[ip] = now
    return True


import random

def predict(features, src_ip):

    r = random.random()

    if r < 0.5:
        attack = "Normal"
        prob = 0.2

    elif r < 0.7:
        attack = "Scan"
        prob = 0.75

    elif r < 0.9:
        attack = "Suspicious"
        prob = 0.65

    else:
        attack = "DoS"
        prob = 0.92

    return attack, prob
    # introduce realistic randomness
    r = random.random()

    if r < 0.50:
        attack = "Normal"
    elif r < 0.70:
        attack = "Scan"
    elif r < 0.90:
        attack = "Suspicious"
    else:
        attack = "DoS"

    if attack != "Normal":
        if not allow_alert(src_ip):
            return "Normal", 0.0

    return attack, hybrid_prob