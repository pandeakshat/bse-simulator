# BSE Simulator

> Interactive academic simulator reproducing Bristol Stock Exchange dynamics.

---

## 📘 Overview

The BSE Simulator recreates the agent-based market model designed by Dave Cliff for the Bristol Stock Exchange. It simulates trader interactions, price fluctuations, and equilibrium formation to provide insight into market microstructure. The project is built for academic exploration, algorithmic trading research, and demonstration of complex adaptive systems in action.

- Type: Streamlit App  
- Tech Stack: Python, Streamlit  
- Status: Completed  

---

## ⚙️ Features

- Agent-based trading simulation in real time.  
- Interactive visualization of trades, prices, and liquidity.  
- Configurable parameters for market behavior experimentation.  

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
```

Explain briefly how your components fit together:
- `agent.py` defines trading agents with strategy logic.  
- `market.py` manages order matching and transaction flow.  
- `app.py` renders the simulation and graphs through Streamlit.  

---

## 🚀 Quick Start

### 1. Clone and setup environment
```bash
git clone https://github.com/pandeakshat/bse-simulator.git
cd bse-simulator
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run
```bash
streamlit run app.py
```

> The app will open locally at http://localhost:8501

---

## 🧠 Example Output / Demo

Displays live graphs of simulated trades, showing how agent interactions form market prices and liquidity trends.

> Example: “Visualizes the emergent dynamics of a market where autonomous agents trade under supply and demand rules.”

---

## 🔍 Core Concepts

| Area | Tools | Purpose |
|------|--------|----------|
| Simulation | Python | Agent and market modeling |
| Visualization | Streamlit | Live trading visualization |
| Research | Matplotlib | Data exploration and export |

---

## 📈 Roadmap

- [x] Base simulation and visualization layer  
- [x] Agent diversity module  
- [ ] AI/ML-driven trading agents  
- [ ] Extended data export and replay feature  

---

## 🧮 Tech Highlights

**Languages:** Python  
**Frameworks:** Streamlit  
**Integrations:** ProjectFlow (tracking), Data Intelligence (data checks)  

---

## 🧰 Dependencies

- streamlit  
- pandas  
- numpy  
- matplotlib  

---

## 🧾 License

MIT License © [Akshat Pande](https://github.com/pandeakshat)

---

## 🧩 Related Projects

- [Sales Dashboard](https://github.com/pandeakshat/sales-dashboard) — Interactive BI dashboard for performance analysis.  
- [Customer Intelligence Hub](https://github.com/pandeakshat/customer-intelligence) — Unified analytics platform for customer behavior.  

---

## 💬 Contact

**Akshat Pande**  
📧 [mail@pandeakshat.com](mailto:mail@pandeakshat.com)  
🌐 [Portfolio](https://pandeakshat.com) | [LinkedIn](https://linkedin.com/in/pandeakshat)
