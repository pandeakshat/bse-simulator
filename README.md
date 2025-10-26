# BSE Simulator

> Interactive academic simulator reproducing Bristol Stock Exchange dynamics.

---

## 📘 Overview

The BSE Simulator recreates the agent-based market model developed by Dave Cliff for the Bristol Stock Exchange. It enables experimentation with market microstructure, trading strategies, and equilibrium formation in a controlled environment. The tool is designed for research, teaching, and conceptual demonstrations of automated trading behavior.

- Type: Streamlit App  
- Tech Stack: Python, Streamlit  
- Status: Completed  

---

## ⚙️ Features

- Agent-based simulation of market dynamics.  
- Visual interface for observing trades and price evolution.  
- Configurable parameters for different trading behaviors.  

---

## 🧩 Architecture / Design

```text
bse-simulator/
├── app.py
├── core/
│   ├── market.py
│   ├── agent.py
│   └── simulation.py
├── data/
└── README.md
