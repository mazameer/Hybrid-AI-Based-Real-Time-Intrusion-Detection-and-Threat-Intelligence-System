# Hybrid AI-Based Real-Time Intrusion Detection and Threat Intelligence System

## Overview
This project is an AI-based intrusion detection system that monitors network traffic in real-time and identifies malicious activities such as DoS attacks, scanning, and suspicious behavior.

## Features
- Real-time network traffic monitoring
- Machine learning-based attack detection
- Attack classification (DoS, Scan, Suspicious)
- IP blocking mechanism
- Dashboard visualization

## Technologies Used
- Python
- Machine Learning (Random Forest, Deep Learning)
- Flask
- HTML, CSS (Frontend)
- SQLite

## Project Structure
- backend/ → Core logic and ML models
- frontend/ → Dashboard UI
- attack_simulator.py → Simulates attacks

## How to Run
```bash
pip install -r requirements.txt
python backend/app.py