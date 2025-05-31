import streamlit as st

def home():
    st.title("BSE Simulation - Home Page")
    st.write(" This project aims to develop the BSE Interactive Simulation Platform, an enhanced, interactive version of the existing Bristol Stock Exchange (BSE) simulation.")

    st.subheader("Background")
    st.write("""
      The Bristol Stock Exchange (BSE) was developed by Dave Cliff as a simple, single-threaded Python simulation to help students understand "Level 2" market data and develop automated trading strategies. Its core strengths lie in its simplicity, transparency (all in one file), and its foundation on simplifying assumptions like zero latency, making it an excellent educational tool. The existing `BSE.py` file contains the simulation engine, and `BSE_VernonSmith1962_demo.ipynb` provides a practical demonstration. This project seeks to amplify BSE's educational impact by making it more accessible, interactive, and extensible.
    """)
    st.markdown("""
        ## Features
        - Interactive Demo
        - General Workshop Tool
        - Advanced Simulator
        - Community-Driven Platform
    """)

if __name__ == "__main__":
    home()  