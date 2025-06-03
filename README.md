# BSE Interactive Simulation Platform

---

## Overview

This project presents the **BSE Interactive Simulation Platform**, an enhanced and interactive version of the classic Bristol Stock Exchange (BSE) simulation. Developed by Dave Cliff, the original BSE simulation is a simple, single-threaded Python tool designed to help students understand Level 2 market data and develop automated trading strategies.

Our platform amplifies BSE's educational impact by providing a **user-friendly, interactive experience** built with Streamlit. It aims to make complex market dynamics accessible, engaging, and extensible for learning and experimentation.

---

## Features

Our interactive platform offers multiple modes to explore market behavior:

* **Interactive Demo:** Jump straight into pre-configured simulations to see different market scenarios in action. This includes:
    * **Default - ZIP:** Observe market behavior with standard Zero Intelligence Proportional (ZIP) traders.
    * **Default - Step-by-Step:** Walk through various market conditions and trader configurations incrementally, with detailed explanations at each stage.
    * **Default + Custom Trader:** Experiment with different individual trader types (ZIP, ZIC, SHVR, GVWY) to understand their unique impact on market sessions.
* **General Workshop Tool:** (Planned for future development / Workshop use) A more in-depth environment for guided learning and hands-on exercises.
* **Advanced Simulator:** (Planned for future development) For users who want to dive deeper into custom configurations and advanced analysis.
* **Community-Driven Platform:** We aim to foster a collaborative environment where users can contribute and expand the simulator's capabilities.

---

## Background on BSE

The original Bristol Stock Exchange (`BSE.py`) is lauded for its simplicity, transparency, and foundational assumptions (like zero latency), making it an excellent educational tool. This project builds upon that robust foundation, aiming to extend its reach and utility.

For more information on the original BSE, please refer to its official documentation.

---

## How to Run Locally

To get this interactive simulation up and running on your machine, follow these simple steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/pandeakshat/bse-simulation.git](https://github.com/pandeakshat/bse-simulation.git)
    cd bse-simulation
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    # (You'll need a requirements.txt file with: streamlit, matplotlib, numpy, bse)
    ```
    * **Note:** The `BSE` library might need to be installed directly if it's not on PyPI: `pip install bse`.

4.  **Create a `data` directory:**
    The simulation outputs CSV files into a `data/` subdirectory. Make sure this directory exists:
    ```bash
    mkdir data
    ```

5.  **Run the Streamlit application:**
    Assuming your main Streamlit app file is named `app.py` (or similar, adjust if different):
    ```bash
    streamlit run app.py
    ```
    This command will open the application in your web browser.

---

## Project Structure (Example)

.
├── app.py           # Main Streamlit application file (combining Home and Demo)

├── BSE.py           # Original BSE simulation engine (or its equivalent)

├── data/            # Directory for simulation output CSV files

├── requirements.txt # Python dependencies

└── README.md        # This file


---

## 🙏 Important Note

I do not own the original BSE code. This project is an enhancement of the original work by Dave Cliff, and it is intended for educational purposes only. Please refer to the original BSE documentation for more information on its usage and limitations.

### Modifications to BSE.PY
While this project largely builds upon the original Bristol Stock Exchange (BSE.py) simulation, a minor functional enhancement has been applied to the BSE.py file included in this repository.

Specifically, the file dump paths within BSE.py have been modified to automatically save all generated output files (such as blotters, LOB frames, average balances, and transaction tapes) into a dedicated data/ subdirectory. This change helps keep the project directory organized and ensures that all simulation outputs are consistently stored in a single, easily accessible location.

Example of the modification:
Python

# Original (example)
bdump = open(session_id+'_blotters.csv', 'w')

# Modified
bdump = open('data/' + session_id+'_blotters.csv', 'w')


This ensures that all simulation output files are neatly organized in the data/ folder, which you're instructed to create when running the application locally. If you encounter any issues related to file output during the simulation, please ensure you are using the BSE.py file provided within this repository.

---

## 🤝 Contributing

We welcome contributions to make this platform even better! If you have ideas for new features, improvements, or bug fixes, please feel free to:

* Open an issue to discuss your ideas.
* Fork the repository and submit a pull request.

---

## 💖 Support the Project

If you find this project useful and would like to support its development, consider buying me a coffee!

[Donate (PandeAkshat)](https://ko-fi.com/pandeakshat)

---