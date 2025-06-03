import matplotlib.pyplot as plt
import numpy as np
import csv
import random
import streamlit as st
from BSE import market_session

# --- Streamlit Title ---
st.title("Demo - BSE Simulator")
st.sidebar.info("Important Information")
st.sidebar.warning("I do not own the original BSE code. This project is an enhancement of the original work by Dave Cliff, and it is intended for educational purposes only. Please refer to the original BSE documentation for more information on its usage and limitations.")
st.sidebar.info("For more information, please visit the [GitHub Repository](https://github.com/pandeakshat/bse-simulation).")
st.sidebar.error("[Donate (PandeAkshat)](https://ko-fi.com/pandeakshat)")
mode = st.radio("Choose Demo Mode:",
         options=["Default - ZIP", "Default - Step-by-Step", "Default + Custom Trader"],
         index=0)

# --- Market Session Parameters ---
if mode == "Default - ZIP":
    st.subheader("Default - ZIP Traders")
    start_time = 0
    end_time = 60 * 10

    chart1_range = (80, 320)

    supply_schedule = [{'from': start_time, 'to': end_time, 'ranges': [chart1_range], 'stepmode': 'fixed'}]
    demand_schedule = [{'from': start_time, 'to': end_time, 'ranges': [chart1_range], 'stepmode': 'fixed'}]

    order_interval = 60
    order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                'interval': order_interval, 'timemode': 'periodic'}

    sellers_spec = [('ZIP', 11)]
    buyers_spec = sellers_spec
    prop_traders_spec = []
    traders_spec = {'sellers': sellers_spec, 'buyers': buyers_spec, 'proptraders': prop_traders_spec}

    verbose = False

    trial_id = 'smith_chart_1'
    dump_flags = {'dump_blotters': True, 'dump_lobs': True, 'dump_strats': True,
                'dump_avgbals': True, 'dump_tape': True}

    random.seed(100) # changing the seed value will give us different sequences of random numbers

    # --- Plot 1 ---
    st.subheader("Single Market Session (order_interval = 60, timemode = periodic)")
    market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

    prices_fname = 'data/' + trial_id + '_tape.csv'
    x = np.empty(0)
    y = np.empty(0)
    with open(prices_fname, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            time = float(row[1])
            price = float(row[2])
            x = np.append(x,time)
            y = np.append(y,price)

    fig1, ax1 = plt.subplots()
    ax1.plot(x, y, 'x', color='black')
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Price")
    ax1.set_title("Market Session Prices")
    st.pyplot(fig1)

    # --- Plot 2 ---
    st.subheader("Multiple Market Sessions (order_interval = 60, timemode = periodic)")
    n_sessions = 10

    x = np.empty(0)
    y = np.empty(0)

    for sess in range(n_sessions):
        trial_id = 'smith_chart_' + str(sess)

        market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

        prices_fname ='data/' +  trial_id + '_tape.csv'
        with open(prices_fname, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                time = float(row[1])
                price = float(row[2])
                x = np.append(x,time)
                y = np.append(y,price)

    fig2, ax2 = plt.subplots()
    ax2.plot(x, y, 'x', color='black')
    ax2.set_xlabel("Time")
    ax2.set_ylabel("Price")
    ax2.set_title(f"{n_sessions} Market Sessions Prices")
    st.pyplot(fig2)

    # --- Plot 3 (Duplicate of Plot 2, assuming it was intentional) ---
    st.subheader("Multiple Market Sessions (Duplicate Plot) (order_interval = 60, timemode = periodic)")
    n_sessions = 10

    x = np.empty(0)
    y = np.empty(0)

    for sess in range(n_sessions):
        trial_id = 'smith_chart_' + str(sess)

        market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

        prices_fname ='data/' +  trial_id + '_tape.csv'
        with open(prices_fname, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                time = float(row[1])
                price = float(row[2])
                x = np.append(x,time)
                y = np.append(y,price)

    fig3, ax3 = plt.subplots()
    ax3.plot(x, y, 'x', color='black')
    ax3.set_xlabel("Time")
    ax3.set_ylabel("Price")
    ax3.set_title(f"{n_sessions} Market Sessions Prices (Duplicate)")
    st.pyplot(fig3)

    # --- Plot 4 ---
    st.subheader("Multiple Market Sessions (order_interval = 10, timemode = drip-poisson)")
    order_interval = 10
    order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                'interval': order_interval, 'timemode': 'drip-poisson'}

    n_sessions = 10

    x = np.empty(0)
    y = np.empty(0)

    for sess in range(n_sessions):
        trial_id = 'smith_chart_' + str(sess)

        market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

        prices_fname ='data/' +  trial_id + '_tape.csv'
        with open(prices_fname, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                time = float(row[1])
                price = float(row[2])
                x = np.append(x,time)
                y = np.append(y,price)

    fig4, ax4 = plt.subplots()
    ax4.plot(x, y, 'x', color='black')
    ax4.set_xlabel("Time")
    ax4.set_ylabel("Price")
    ax4.set_title(f"{n_sessions} Market Sessions Prices (Drip-Poisson)")
    st.pyplot(fig4)

    # --- Plot 5 ---
    st.subheader("Multiple Market Sessions (40 ZIP traders, order_interval = 10, timemode = drip-poisson)")
    sellers_spec = [('ZIP', 40)]
    buyers_spec = sellers_spec
    traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}

    order_interval = 10
    order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                'interval': order_interval, 'timemode': 'drip-poisson'}

    n_sessions = 10

    x = np.empty(0)
    y = np.empty(0)

    for sess in range(n_sessions):
        trial_id = 'smith_chart_' + str(sess)

        market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

        prices_fname = 'data/' + trial_id + '_tape.csv'
        with open(prices_fname, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                time = float(row[1])
                price = float(row[2])
                x = np.append(x,time)
                y = np.append(y,price)

    fig5, ax5 = plt.subplots()
    ax5.plot(x, y, 'x', color='black')
    ax5.set_xlabel("Time")
    ax5.set_ylabel("Price")
    ax5.set_title(f"{n_sessions} Market Sessions Prices (40 ZIP traders)")
    st.pyplot(fig5)

    # --- Plot 6 ---
    st.subheader("Single Market Session (Mixed Traders, order_interval = 10, timemode = drip-poisson)")
    sellers_spec = [('ZIP', 10), ('ZIC', 10), ('SHVR', 10), ('GVWY', 10)]
    buyers_spec = sellers_spec
    traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}

    order_interval = 10
    order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                'interval': order_interval, 'timemode': 'drip-poisson'}

    n_sessions = 1

    x = np.empty(0)
    y = np.empty(0)

    for sess in range(n_sessions):
        trial_id = 'smith_chart_' + str(sess)

        market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

        prices_fname = 'data/' +  trial_id + '_tape.csv'
        with open(prices_fname, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                time = float(row[1])
                price = float(row[2])
                x = np.append(x,time)
                y = np.append(y,price)

    fig6, ax6 = plt.subplots()
    ax6.plot(x, y, 'x', color='black')
    ax6.set_xlabel("Time")
    ax6.set_ylabel("Price")
    ax6.set_title(f"{n_sessions} Market Session Prices (Mixed Traders)")
    st.pyplot(fig6)

    # --- Plot 7 ---
    st.subheader("Single Market Session (Shocked Demand/Supply, Mixed Traders)")
    shocked_range = (300, 400)
    shock_time = int(end_time / 2)

    supply_schedule = [ {'from':0, 'to':shock_time, 'ranges':[chart1_range], 'stepmode':'fixed'},
                        {'from':shock_time, 'to':end_time, 'ranges':[shocked_range], 'stepmode':'fixed'},
                    ]
    demand_schedule = supply_schedule

    sellers_spec = [('ZIP', 10), ('ZIC', 10), ('SHVR', 10), ('GVWY', 10)]
    buyers_spec = sellers_spec
    traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}

    order_interval = 10
    order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                'interval': order_interval, 'timemode': 'drip-poisson'}

    n_sessions = 1

    x = np.empty(0)
    y = np.empty(0)

    for sess in range(n_sessions):
        trial_id = 'smith_chart_' + str(sess)

        market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

        prices_fname = 'data/' + trial_id + '_tape.csv'
        with open(prices_fname, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                time = float(row[1])
                price = float(row[2])
                x = np.append(x,time)
                y = np.append(y,price)

    fig7, ax7 = plt.subplots()
    ax7.plot(x, y, 'x', color='black')
    ax7.set_xlabel("Time")
    ax7.set_ylabel("Price")
    ax7.set_title(f"{n_sessions} Market Session Prices (Shocked Demand/Supply)")
    st.pyplot(fig7)

elif mode == "Default - Step-by-Step":
    st.subheader("Default - Step-by-Step Mode")
    start_time = 0
    end_time = 60 * 10

    chart1_range = (80, 320)

    supply_schedule = [{'from': start_time, 'to': end_time, 'ranges': [chart1_range], 'stepmode': 'fixed'}]
    demand_schedule = [{'from': start_time, 'to': end_time, 'ranges': [chart1_range], 'stepmode': 'fixed'}]

    order_interval = 60
    order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                'interval': order_interval, 'timemode': 'periodic'}

    sellers_spec = [('ZIP', 11)]
    buyers_spec = sellers_spec
    prop_traders_spec = []
    traders_spec = {'sellers': sellers_spec, 'buyers': buyers_spec, 'proptraders': prop_traders_spec}

    verbose = False

    trial_id = 'smith_chart_1'
    dump_flags = {'dump_blotters': True, 'dump_lobs': True, 'dump_strats': True,
                'dump_avgbals': True, 'dump_tape': True}

    random.seed(100) # changing the seed value will give us different sequences of random numbers

    steps = ['Information', 'Single Market Session (Periodic)', 'Multi Market Session (Periodic)', 'Multi Market Session (Duplicate) (Periodic)', 'Multi Market Session (Drip-Poisson)', 'Multi Market Session (Drip-Poisson) (Multiple Trader)', 'Single Market Session (Drip-Poisson)(Mixed Trader)', 'Single Market Session (Shocked Demand/Supply, Mixed Traders)', 'Next Steps']
    step = st.select_slider(
    'Select your Step:',
    options=steps,
    value='Information' # Default selected value
    )
    if step == 'Information':
        st.subheader("Information")
        st.write("Demo of BSE Simulator with Step-by-Step Mode")
        st.subheader("Market Session Parameters")
        st.write("Start Time: 0")
        st.write("End Time: 600")
        st.write("Supply Schedule: [{'from': 0, 'to': 600, 'ranges': [(80, 320)], 'stepmode': 'fixed'}]")
        st.write("Demand Schedule: [{'from': 0, 'to': 600, 'ranges': [(80, 320)], 'stepmode': 'fixed'}]")
        st.write("Order Interval: 60")
        st.write("Order Schedule: {'sup': supply_schedule, 'dem': demand_schedule, 'interval': 60, 'timemode': 'periodic'}")
        st.write("Traders Specification: {'sellers': [('ZIP', 11)], 'buyers': [('ZIP', 11)], 'proptraders': []}")

    elif step == 'Single Market Session (Periodic)':
        st.subheader("Single Market Session (Periodic)")
        st.write("order_interval = 60, timemode = periodic")
        market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

        prices_fname = 'data/' + trial_id + '_tape.csv'
        x = np.empty(0)
        y = np.empty(0)
        with open(prices_fname, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                time = float(row[1])
                price = float(row[2])
                x = np.append(x,time)
                y = np.append(y,price)

        fig1, ax1 = plt.subplots()
        ax1.plot(x, y, 'x', color='black')
        ax1.set_xlabel("Time")
        ax1.set_ylabel("Price")
        ax1.set_title("Market Session Prices")
        st.pyplot(fig1)
    
    elif step == 'Multi Market Session (Periodic)':
        st.subheader("Multi Market Session (Periodic)")
        st.write("order_interval = 60, timemode = periodic")
        n_sessions = 10

        x = np.empty(0)
        y = np.empty(0)

        for sess in range(n_sessions):
            trial_id = 'smith_chart_' + str(sess)

            market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

            prices_fname ='data/' +  trial_id + '_tape.csv'
            with open(prices_fname, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time = float(row[1])
                    price = float(row[2])
                    x = np.append(x,time)
                    y = np.append(y,price)

        fig2, ax2 = plt.subplots()
        ax2.plot(x, y, 'x', color='black')
        ax2.set_xlabel("Time")
        ax2.set_ylabel("Price")
        ax2.set_title(f"{n_sessions} Market Sessions Prices")
        st.pyplot(fig2)

    elif step == 'Multi Market Session (Duplicate) (Periodic)':
        st.subheader("Multi Market Session (Duplicate) (Periodic)")
        st.write("order_interval = 60, timemode = periodic")
        n_sessions = 10

        x = np.empty(0)
        y = np.empty(0)

        for sess in range(n_sessions):
            trial_id = 'smith_chart_' + str(sess)

            market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

            prices_fname ='data/' +  trial_id + '_tape.csv'
            with open(prices_fname, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time = float(row[1])
                    price = float(row[2])
                    x = np.append(x,time)
                    y = np.append(y,price)

        fig3, ax3 = plt.subplots()
        ax3.plot(x, y, 'x', color='black')
        ax3.set_xlabel("Time")
        ax3.set_ylabel("Price")
        ax3.set_title(f"{n_sessions} Market Sessions Prices (Duplicate)")
        st.pyplot(fig3)

    elif step == 'Multi Market Session (Drip-Poisson)':
        st.subheader("Multi Market Session (Drip-Poisson)")
        st.write("order_interval = 10, timemode = drip-poisson")
        order_interval = 10
        order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                    'interval': order_interval, 'timemode': 'drip-poisson'}

        n_sessions = 10

        x = np.empty(0)
        y = np.empty(0)

        for sess in range(n_sessions):
            trial_id = 'smith_chart_' + str(sess)

            market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

            prices_fname ='data/' +  trial_id + '_tape.csv'
            with open(prices_fname, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time = float(row[1])
                    price = float(row[2])
                    x = np.append(x,time)
                    y = np.append(y,price)

        fig4, ax4 = plt.subplots()
        ax4.plot(x, y, 'x', color='black')
        ax4.set_xlabel("Time")
        ax4.set_ylabel("Price")
        ax4.set_title(f"{n_sessions} Market Sessions Prices (Drip-Poisson)")
        st.pyplot(fig4)

    elif step == 'Multi Market Session (Drip-Poisson) (Multiple Trader)':
        st.subheader("Multi Market Session (Drip-Poisson) (Multiple Trader)")
        st.write("40 ZIP traders, order_interval = 10, timemode = drip-poisson")
        sellers_spec = [('ZIP', 40)]
        buyers_spec = sellers_spec
        traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}

        order_interval = 10
        order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                    'interval': order_interval, 'timemode': 'drip-poisson'}

        n_sessions = 10

        x = np.empty(0)
        y = np.empty(0)

        for sess in range(n_sessions):
            trial_id = 'smith_chart_' + str(sess)

            market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

            prices_fname = 'data/' + trial_id + '_tape.csv'
            with open(prices_fname, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time = float(row[1])
                    price = float(row[2])
                    x = np.append(x,time)
                    y = np.append(y,price)

        fig5, ax5 = plt.subplots()
        ax5.plot(x, y, 'x', color='black')
        ax5.set_xlabel("Time")
        ax5.set_ylabel("Price")
        ax5.set_title(f"{n_sessions} Market Sessions Prices (40 ZIP traders)")
        st.pyplot(fig5)

    elif step == 'Single Market Session (Drip-Poisson)(Mixed Trader)':
        st.subheader("Single Market Session (Drip-Poisson)(Mixed Trader)")
        st.write("Mixed Traders, order_interval = 10, timemode = drip-poisson")
        sellers_spec = [('ZIP', 10), ('ZIC', 10), ('SHVR', 10), ('GVWY', 10)]
        buyers_spec = sellers_spec
        traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}

        order_interval = 10
        order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                    'interval': order_interval, 'timemode': 'drip-poisson'}

        n_sessions = 1

        x = np.empty(0)
        y = np.empty(0)

        for sess in range(n_sessions):
            trial_id = 'smith_chart_' + str(sess)

            market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

            prices_fname = 'data/' +  trial_id + '_tape.csv'
            with open(prices_fname, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time = float(row[1])
                    price = float(row[2])
                    x = np.append(x,time)
                    y = np.append(y,price)

        fig6, ax6 = plt.subplots()
        ax6.plot(x, y, 'x', color='black')
        ax6.set_xlabel("Time")
        ax6.set_ylabel("Price")
        ax6.set_title(f"{n_sessions} Market Session Prices (Mixed Traders)")
        st.pyplot(fig6)

    elif step == 'Single Market Session (Shocked Demand/Supply, Mixed Traders)':
        st.subheader("Single Market Session (Shocked Demand/Supply, Mixed Traders)")
        st.write("Shocked Demand/Supply, Mixed Traders")
        shocked_range = (300, 400)
        shock_time = int(end_time / 2)

        supply_schedule = [ {'from':0, 'to':shock_time, 'ranges':[chart1_range], 'stepmode':'fixed'},
                            {'from':shock_time, 'to':end_time, 'ranges':[shocked_range], 'stepmode':'fixed'},
                        ]
        demand_schedule = supply_schedule

        sellers_spec = [('ZIP', 10), ('ZIC', 10), ('SHVR', 10), ('GVWY', 10)]
        buyers_spec = sellers_spec
        traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}

        order_interval = 10
        order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                    'interval': order_interval, 'timemode': 'drip-poisson'}

        n_sessions = 1

        x = np.empty(0)
        y = np.empty(0)

        for sess in range(n_sessions):
            trial_id = 'smith_chart_' + str(sess)

            market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

            prices_fname = 'data/' + trial_id + '_tape.csv'
            with open(prices_fname, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time = float(row[1])
                    price = float(row[2])
                    x = np.append(x,time)
                    y = np.append(y,price)

        fig7, ax7 = plt.subplots()
        ax7.plot(x, y, 'x', color='black')
        ax7.set_xlabel("Time")
        ax7.set_ylabel("Price")
        ax7.set_title(f"{n_sessions} Market Session Prices (Shocked Demand/Supply)")
        st.pyplot(fig7)

    elif step == 'Next Steps':
        st.subheader("Next Steps")
        st.write("You can continue to explore the different market sessions and their effects on prices through Workshop & Simulator.")
        st.write("If you are able to contribute to the BSE Simulator, please consider contributing to the project on [Github](https://github.com/pandeakshat/bse-simulation).")
        st.write("More customer pages will be added in the future to enhance the simulator experience.")
        st.write("Thank you for using the BSE Simulator. We hope you find it useful for your market simulations and analysis.")

    else:
        st.write("Invalid step selected. Please choose a valid step from the options provided.")

elif mode == "Default + Custom Trader":
    traders_options = ['Info', 'ZIP', 'ZIC', 'SHVR', 'GVWY']

    selected_trader_type = st.radio(
        'Select your Trader Type for the simulation:',
        options=traders_options,
        index=0, 
        horizontal=True, 
        help="Choose a trader type to run the simulation with. 'Information' provides general details."
    )
    if selected_trader_type == 'Info':
        st.subheader("Information")
        st.write("Before choosing your trader, please read the description of each trader below:")
        st.write("1. **ZIP**: Zero Intelligence Proportional (ZIP) traders are designed to mimic the behavior of real-world traders who place orders based on a fixed price range.")
        st.write("2. **ZIC**: Zero Intelligence Cumulative (ZIC) traders are similar to ZIP traders but accumulate their orders over time, allowing for a more gradual market impact.")
        st.write("3. **SHVR**: Shaver traders are designed to shave off small profits from the market by placing orders that are slightly better than the current market price.")
        st.write("4. **GVWY**: Gateway traders are designed to act as a gateway for other traders, providing liquidity to the market by placing orders that are slightly worse than the current market price.")
        st.write("You can select a trader from the dropdown menu to see how it affects the market session prices.")
    
    elif selected_trader_type == 'ZIP':
        st.subheader("Trader -- ZIP")
        start_time = 0
        end_time = 60 * 10

        chart1_range = (80, 320)

        supply_schedule = [{'from': start_time, 'to': end_time, 'ranges': [chart1_range], 'stepmode': 'fixed'}]
        demand_schedule = [{'from': start_time, 'to': end_time, 'ranges': [chart1_range], 'stepmode': 'fixed'}]

        order_interval = 60
        order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                    'interval': order_interval, 'timemode': 'periodic'}

        sellers_spec = [('ZIP', 11)]
        buyers_spec = sellers_spec
        prop_traders_spec = []
        traders_spec = {'sellers': sellers_spec, 'buyers': buyers_spec, 'proptraders': prop_traders_spec}

        verbose = False

        trial_id = 'smith_chart_1'
        dump_flags = {'dump_blotters': True, 'dump_lobs': True, 'dump_strats': True,
                    'dump_avgbals': True, 'dump_tape': True}

        random.seed(100) # changing the seed value will give us different sequences of random numbers

        # --- Plot 1 ---
        st.subheader("Single Market Session (order_interval = 60, timemode = periodic)")
        market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

        prices_fname = 'data/' + trial_id + '_tape.csv'
        x = np.empty(0)
        y = np.empty(0)
        with open(prices_fname, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                time = float(row[1])
                price = float(row[2])
                x = np.append(x,time)
                y = np.append(y,price)

        fig1, ax1 = plt.subplots()
        ax1.plot(x, y, 'x', color='black')
        ax1.set_xlabel("Time")
        ax1.set_ylabel("Price")
        ax1.set_title("Market Session Prices")
        st.pyplot(fig1)

        # --- Plot 2 ---
        st.subheader("Multiple Market Sessions (order_interval = 60, timemode = periodic)")
        n_sessions = 10

        x = np.empty(0)
        y = np.empty(0)

        for sess in range(n_sessions):
            trial_id = 'smith_chart_' + str(sess)

            market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

            prices_fname ='data/' +  trial_id + '_tape.csv'
            with open(prices_fname, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time = float(row[1])
                    price = float(row[2])
                    x = np.append(x,time)
                    y = np.append(y,price)

        fig2, ax2 = plt.subplots()
        ax2.plot(x, y, 'x', color='black')
        ax2.set_xlabel("Time")
        ax2.set_ylabel("Price")
        ax2.set_title(f"{n_sessions} Market Sessions Prices")
        st.pyplot(fig2)

        # --- Plot 3 (Duplicate of Plot 2, assuming it was intentional) ---
        st.subheader("Multiple Market Sessions (Duplicate Plot) (order_interval = 60, timemode = periodic)")
        n_sessions = 10

        x = np.empty(0)
        y = np.empty(0)

        for sess in range(n_sessions):
            trial_id = 'smith_chart_' + str(sess)

            market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

            prices_fname ='data/' +  trial_id + '_tape.csv'
            with open(prices_fname, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time = float(row[1])
                    price = float(row[2])
                    x = np.append(x,time)
                    y = np.append(y,price)

        fig3, ax3 = plt.subplots()
        ax3.plot(x, y, 'x', color='black')
        ax3.set_xlabel("Time")
        ax3.set_ylabel("Price")
        ax3.set_title(f"{n_sessions} Market Sessions Prices (Duplicate)")
        st.pyplot(fig3)

        # --- Plot 4 ---
        st.subheader("Multiple Market Sessions (order_interval = 10, timemode = drip-poisson)")
        order_interval = 10
        order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                    'interval': order_interval, 'timemode': 'drip-poisson'}

        n_sessions = 10

        x = np.empty(0)
        y = np.empty(0)

        for sess in range(n_sessions):
            trial_id = 'smith_chart_' + str(sess)

            market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

            prices_fname ='data/' +  trial_id + '_tape.csv'
            with open(prices_fname, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time = float(row[1])
                    price = float(row[2])
                    x = np.append(x,time)
                    y = np.append(y,price)

        fig4, ax4 = plt.subplots()
        ax4.plot(x, y, 'x', color='black')
        ax4.set_xlabel("Time")
        ax4.set_ylabel("Price")
        ax4.set_title(f"{n_sessions} Market Sessions Prices (Drip-Poisson)")
        st.pyplot(fig4)

        # --- Plot 5 ---
        st.subheader("Multiple Market Sessions (40 ZIP traders, order_interval = 10, timemode = drip-poisson)")
        sellers_spec = [('ZIP', 40)]
        buyers_spec = sellers_spec
        traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}

        order_interval = 10
        order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                    'interval': order_interval, 'timemode': 'drip-poisson'}

        n_sessions = 10

        x = np.empty(0)
        y = np.empty(0)

        for sess in range(n_sessions):
            trial_id = 'smith_chart_' + str(sess)

            market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

            prices_fname = 'data/' + trial_id + '_tape.csv'
            with open(prices_fname, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time = float(row[1])
                    price = float(row[2])
                    x = np.append(x,time)
                    y = np.append(y,price)

        fig5, ax5 = plt.subplots()
        ax5.plot(x, y, 'x', color='black')
        ax5.set_xlabel("Time")
        ax5.set_ylabel("Price")
        ax5.set_title(f"{n_sessions} Market Sessions Prices (40 ZIP traders)")
        st.pyplot(fig5)

        # --- Plot 6 ---
        st.subheader("Single Market Session (Mixed Traders, order_interval = 10, timemode = drip-poisson)")
        sellers_spec = [('ZIP', 10), ('ZIC', 10), ('SHVR', 10), ('GVWY', 10)]
        buyers_spec = sellers_spec
        traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}

        order_interval = 10
        order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                    'interval': order_interval, 'timemode': 'drip-poisson'}

        n_sessions = 1

        x = np.empty(0)
        y = np.empty(0)

        for sess in range(n_sessions):
            trial_id = 'smith_chart_' + str(sess)

            market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

            prices_fname = 'data/' +  trial_id + '_tape.csv'
            with open(prices_fname, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time = float(row[1])
                    price = float(row[2])
                    x = np.append(x,time)
                    y = np.append(y,price)

        fig6, ax6 = plt.subplots()
        ax6.plot(x, y, 'x', color='black')
        ax6.set_xlabel("Time")
        ax6.set_ylabel("Price")
        ax6.set_title(f"{n_sessions} Market Session Prices (Mixed Traders)")
        st.pyplot(fig6)

        # --- Plot 7 ---
        st.subheader("Single Market Session (Shocked Demand/Supply, Mixed Traders)")
        shocked_range = (300, 400)
        shock_time = int(end_time / 2)

        supply_schedule = [ {'from':0, 'to':shock_time, 'ranges':[chart1_range], 'stepmode':'fixed'},
                            {'from':shock_time, 'to':end_time, 'ranges':[shocked_range], 'stepmode':'fixed'},
                        ]
        demand_schedule = supply_schedule

        sellers_spec = [('ZIP', 10), ('ZIC', 10), ('SHVR', 10), ('GVWY', 10)]
        buyers_spec = sellers_spec
        traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}

        order_interval = 10
        order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                    'interval': order_interval, 'timemode': 'drip-poisson'}

        n_sessions = 1

        x = np.empty(0)
        y = np.empty(0)

        for sess in range(n_sessions):
            trial_id = 'smith_chart_' + str(sess)

            market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

            prices_fname = 'data/' + trial_id + '_tape.csv'
            with open(prices_fname, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time = float(row[1])
                    price = float(row[2])
                    x = np.append(x,time)
                    y = np.append(y,price)

        fig7, ax7 = plt.subplots()
        ax7.plot(x, y, 'x', color='black')
        ax7.set_xlabel("Time")
        ax7.set_ylabel("Price")
        ax7.set_title(f"{n_sessions} Market Session Prices (Shocked Demand/Supply)")
        st.pyplot(fig7)
    
    elif selected_trader_type == 'ZIC':
        st.subheader("Trader -- ZIC")
        start_time = 0
        end_time = 60 * 10

        chart1_range = (80, 320)

        supply_schedule = [{'from': start_time, 'to': end_time, 'ranges': [chart1_range], 'stepmode': 'fixed'}]
        demand_schedule = [{'from': start_time, 'to': end_time, 'ranges': [chart1_range], 'stepmode': 'fixed'}]

        order_interval = 60
        order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                    'interval': order_interval, 'timemode': 'periodic'}

        sellers_spec = [('ZIC', 11)]
        buyers_spec = sellers_spec
        prop_traders_spec = []
        traders_spec = {'sellers': sellers_spec, 'buyers': buyers_spec, 'proptraders': prop_traders_spec}

        verbose = False

        trial_id = 'smith_chart_1'
        dump_flags = {'dump_blotters': True, 'dump_lobs': True, 'dump_strats': True,
                    'dump_avgbals': True, 'dump_tape': True}

        random.seed(100) # changing the seed value will give us different sequences of random numbers

        # --- Plot 1 ---
        st.subheader("Single Market Session (order_interval = 60, timemode = periodic)")
        market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

        prices_fname = 'data/' + trial_id + '_tape.csv'
        x = np.empty(0)
        y = np.empty(0)
        with open(prices_fname, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                time = float(row[1])
                price = float(row[2])
                x = np.append(x,time)
                y = np.append(y,price)

        fig1, ax1 = plt.subplots()
        ax1.plot(x, y, 'x', color='black')
        ax1.set_xlabel("Time")
        ax1.set_ylabel("Price")
        ax1.set_title("Market Session Prices")
        st.pyplot(fig1)

        # --- Plot 2 ---
        st.subheader("Multiple Market Sessions (order_interval = 60, timemode = periodic)")
        n_sessions = 10

        x = np.empty(0)
        y = np.empty(0)

        for sess in range(n_sessions):
            trial_id = 'smith_chart_' + str(sess)

            market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

            prices_fname ='data/' +  trial_id + '_tape.csv'
            with open(prices_fname, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time = float(row[1])
                    price = float(row[2])
                    x = np.append(x,time)
                    y = np.append(y,price)

        fig2, ax2 = plt.subplots()
        ax2.plot(x, y, 'x', color='black')
        ax2.set_xlabel("Time")
        ax2.set_ylabel("Price")
        ax2.set_title(f"{n_sessions} Market Sessions Prices")
        st.pyplot(fig2)

        # --- Plot 3 (Duplicate of Plot 2, assuming it was intentional) ---
        st.subheader("Multiple Market Sessions (Duplicate Plot) (order_interval = 60, timemode = periodic)")
        n_sessions = 10

        x = np.empty(0)
        y = np.empty(0)

        for sess in range(n_sessions):
            trial_id = 'smith_chart_' + str(sess)

            market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

            prices_fname ='data/' +  trial_id + '_tape.csv'
            with open(prices_fname, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time = float(row[1])
                    price = float(row[2])
                    x = np.append(x,time)
                    y = np.append(y,price)

        fig3, ax3 = plt.subplots()
        ax3.plot(x, y, 'x', color='black')
        ax3.set_xlabel("Time")
        ax3.set_ylabel("Price")
        ax3.set_title(f"{n_sessions} Market Sessions Prices (Duplicate)")
        st.pyplot(fig3)

        # --- Plot 4 ---
        st.subheader("Multiple Market Sessions (order_interval = 10, timemode = drip-poisson)")
        order_interval = 10
        order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                    'interval': order_interval, 'timemode': 'drip-poisson'}

        n_sessions = 10

        x = np.empty(0)
        y = np.empty(0)

        for sess in range(n_sessions):
            trial_id = 'smith_chart_' + str(sess)

            market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

            prices_fname ='data/' +  trial_id + '_tape.csv'
            with open(prices_fname, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time = float(row[1])
                    price = float(row[2])
                    x = np.append(x,time)
                    y = np.append(y,price)

        fig4, ax4 = plt.subplots()
        ax4.plot(x, y, 'x', color='black')
        ax4.set_xlabel("Time")
        ax4.set_ylabel("Price")
        ax4.set_title(f"{n_sessions} Market Sessions Prices (Drip-Poisson)")
        st.pyplot(fig4)

        # --- Plot 5 ---
        st.subheader("Multiple Market Sessions (40 ZIC traders, order_interval = 10, timemode = drip-poisson)")
        sellers_spec = [('ZIC', 40)]
        buyers_spec = sellers_spec
        traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}

        order_interval = 10
        order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                    'interval': order_interval, 'timemode': 'drip-poisson'}

        n_sessions = 10

        x = np.empty(0)
        y = np.empty(0)

        for sess in range(n_sessions):
            trial_id = 'smith_chart_' + str(sess)

            market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

            prices_fname = 'data/' + trial_id + '_tape.csv'
            with open(prices_fname, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time = float(row[1])
                    price = float(row[2])
                    x = np.append(x,time)
                    y = np.append(y,price)

        fig5, ax5 = plt.subplots()
        ax5.plot(x, y, 'x', color='black')
        ax5.set_xlabel("Time")
        ax5.set_ylabel("Price")
        ax5.set_title(f"{n_sessions} Market Sessions Prices (40 ZIC traders)")
        st.pyplot(fig5)

        # --- Plot 6 ---
        st.subheader("Single Market Session (Mixed Traders, order_interval = 10, timemode = drip-poisson)")
        sellers_spec = [('ZIP', 10), ('ZIC', 10), ('SHVR', 10), ('GVWY', 10)]
        buyers_spec = sellers_spec
        traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}

        order_interval = 10
        order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                    'interval': order_interval, 'timemode': 'drip-poisson'}

        n_sessions = 1

        x = np.empty(0)
        y = np.empty(0)

        for sess in range(n_sessions):
            trial_id = 'smith_chart_' + str(sess)

            market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

            prices_fname = 'data/' +  trial_id + '_tape.csv'
            with open(prices_fname, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time = float(row[1])
                    price = float(row[2])
                    x = np.append(x,time)
                    y = np.append(y,price)

        fig6, ax6 = plt.subplots()
        ax6.plot(x, y, 'x', color='black')
        ax6.set_xlabel("Time")
        ax6.set_ylabel("Price")
        ax6.set_title(f"{n_sessions} Market Session Prices (Mixed Traders)")
        st.pyplot(fig6)

        # --- Plot 7 ---
        st.subheader("Single Market Session (Shocked Demand/Supply, Mixed Traders)")
        shocked_range = (300, 400)
        shock_time = int(end_time / 2)

        supply_schedule = [ {'from':0, 'to':shock_time, 'ranges':[chart1_range], 'stepmode':'fixed'},
                            {'from':shock_time, 'to':end_time, 'ranges':[shocked_range], 'stepmode':'fixed'},
                        ]
        demand_schedule = supply_schedule

        sellers_spec = [('ZIP', 10), ('ZIC', 10), ('SHVR', 10), ('GVWY', 10)]
        buyers_spec = sellers_spec
        traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}

        order_interval = 10
        order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                    'interval': order_interval, 'timemode': 'drip-poisson'}

        n_sessions = 1

        x = np.empty(0)
        y = np.empty(0)

        for sess in range(n_sessions):
            trial_id = 'smith_chart_' + str(sess)

            market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

            prices_fname = 'data/' + trial_id + '_tape.csv'
            with open(prices_fname, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time = float(row[1])
                    price = float(row[2])
                    x = np.append(x,time)
                    y = np.append(y,price)

        fig7, ax7 = plt.subplots()
        ax7.plot(x, y, 'x', color='black')
        ax7.set_xlabel("Time")
        ax7.set_ylabel("Price")
        ax7.set_title(f"{n_sessions} Market Session Prices (Shocked Demand/Supply)")
        st.pyplot(fig7)
    
    elif selected_trader_type == 'SHVR':
        st.subheader("Trader -- SHVR")
        start_time = 0
        end_time = 60 * 10

        chart1_range = (80, 320)

        supply_schedule = [{'from': start_time, 'to': end_time, 'ranges': [chart1_range], 'stepmode': 'fixed'}]
        demand_schedule = [{'from': start_time, 'to': end_time, 'ranges': [chart1_range], 'stepmode': 'fixed'}]

        order_interval = 60
        order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                    'interval': order_interval, 'timemode': 'periodic'}

        sellers_spec = [('SHVR', 11)]
        buyers_spec = sellers_spec
        prop_traders_spec = []
        traders_spec = {'sellers': sellers_spec, 'buyers': buyers_spec, 'proptraders': prop_traders_spec}

        verbose = False

        trial_id = 'smith_chart_1'
        dump_flags = {'dump_blotters': True, 'dump_lobs': True, 'dump_strats': True,
                    'dump_avgbals': True, 'dump_tape': True}

        random.seed(100) # changing the seed value will give us different sequences of random numbers

        # --- Plot 1 ---
        st.subheader("Single Market Session (order_interval = 60, timemode = periodic)")
        market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

        prices_fname = 'data/' + trial_id + '_tape.csv'
        x = np.empty(0)
        y = np.empty(0)
        with open(prices_fname, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                time = float(row[1])
                price = float(row[2])
                x = np.append(x,time)
                y = np.append(y,price)

        fig1, ax1 = plt.subplots()
        ax1.plot(x, y, 'x', color='black')
        ax1.set_xlabel("Time")
        ax1.set_ylabel("Price")
        ax1.set_title("Market Session Prices")
        st.pyplot(fig1)

        # --- Plot 2 ---
        st.subheader("Multiple Market Sessions (order_interval = 60, timemode = periodic)")
        n_sessions = 10

        x = np.empty(0)
        y = np.empty(0)

        for sess in range(n_sessions):
            trial_id = 'smith_chart_' + str(sess)

            market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

            prices_fname ='data/' +  trial_id + '_tape.csv'
            with open(prices_fname, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time = float(row[1])
                    price = float(row[2])
                    x = np.append(x,time)
                    y = np.append(y,price)

        fig2, ax2 = plt.subplots()
        ax2.plot(x, y, 'x', color='black')
        ax2.set_xlabel("Time")
        ax2.set_ylabel("Price")
        ax2.set_title(f"{n_sessions} Market Sessions Prices")
        st.pyplot(fig2)

        # --- Plot 3 (Duplicate of Plot 2, assuming it was intentional) ---
        st.subheader("Multiple Market Sessions (Duplicate Plot) (order_interval = 60, timemode = periodic)")
        n_sessions = 10

        x = np.empty(0)
        y = np.empty(0)

        for sess in range(n_sessions):
            trial_id = 'smith_chart_' + str(sess)

            market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

            prices_fname ='data/' +  trial_id + '_tape.csv'
            with open(prices_fname, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time = float(row[1])
                    price = float(row[2])
                    x = np.append(x,time)
                    y = np.append(y,price)

        fig3, ax3 = plt.subplots()
        ax3.plot(x, y, 'x', color='black')
        ax3.set_xlabel("Time")
        ax3.set_ylabel("Price")
        ax3.set_title(f"{n_sessions} Market Sessions Prices (Duplicate)")
        st.pyplot(fig3)

        # --- Plot 4 ---
        st.subheader("Multiple Market Sessions (order_interval = 10, timemode = drip-poisson)")
        order_interval = 10
        order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                    'interval': order_interval, 'timemode': 'drip-poisson'}

        n_sessions = 10

        x = np.empty(0)
        y = np.empty(0)

        for sess in range(n_sessions):
            trial_id = 'smith_chart_' + str(sess)

            market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

            prices_fname ='data/' +  trial_id + '_tape.csv'
            with open(prices_fname, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time = float(row[1])
                    price = float(row[2])
                    x = np.append(x,time)
                    y = np.append(y,price)

        fig4, ax4 = plt.subplots()
        ax4.plot(x, y, 'x', color='black')
        ax4.set_xlabel("Time")
        ax4.set_ylabel("Price")
        ax4.set_title(f"{n_sessions} Market Sessions Prices (Drip-Poisson)")
        st.pyplot(fig4)

        # --- Plot 5 ---
        st.subheader("Multiple Market Sessions (40 SHVR traders, order_interval = 10, timemode = drip-poisson)")
        sellers_spec = [('SHVR', 40)]
        buyers_spec = sellers_spec
        traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}

        order_interval = 10
        order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                    'interval': order_interval, 'timemode': 'drip-poisson'}

        n_sessions = 10

        x = np.empty(0)
        y = np.empty(0)

        for sess in range(n_sessions):
            trial_id = 'smith_chart_' + str(sess)

            market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

            prices_fname = 'data/' + trial_id + '_tape.csv'
            with open(prices_fname, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time = float(row[1])
                    price = float(row[2])
                    x = np.append(x,time)
                    y = np.append(y,price)

        fig5, ax5 = plt.subplots()
        ax5.plot(x, y, 'x', color='black')
        ax5.set_xlabel("Time")
        ax5.set_ylabel("Price")
        ax5.set_title(f"{n_sessions} Market Sessions Prices (40 ZIP traders)")
        st.pyplot(fig5)

        # --- Plot 6 ---
        st.subheader("Single Market Session (Mixed Traders, order_interval = 10, timemode = drip-poisson)")
        sellers_spec = [('ZIP', 10), ('ZIC', 10), ('SHVR', 10), ('GVWY', 10)]
        buyers_spec = sellers_spec
        traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}

        order_interval = 10
        order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                    'interval': order_interval, 'timemode': 'drip-poisson'}

        n_sessions = 1

        x = np.empty(0)
        y = np.empty(0)

        for sess in range(n_sessions):
            trial_id = 'smith_chart_' + str(sess)

            market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

            prices_fname = 'data/' +  trial_id + '_tape.csv'
            with open(prices_fname, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time = float(row[1])
                    price = float(row[2])
                    x = np.append(x,time)
                    y = np.append(y,price)

        fig6, ax6 = plt.subplots()
        ax6.plot(x, y, 'x', color='black')
        ax6.set_xlabel("Time")
        ax6.set_ylabel("Price")
        ax6.set_title(f"{n_sessions} Market Session Prices (Mixed Traders)")
        st.pyplot(fig6)

        # --- Plot 7 ---
        st.subheader("Single Market Session (Shocked Demand/Supply, Mixed Traders)")
        shocked_range = (300, 400)
        shock_time = int(end_time / 2)

        supply_schedule = [ {'from':0, 'to':shock_time, 'ranges':[chart1_range], 'stepmode':'fixed'},
                            {'from':shock_time, 'to':end_time, 'ranges':[shocked_range], 'stepmode':'fixed'},
                        ]
        demand_schedule = supply_schedule

        sellers_spec = [('ZIP', 10), ('ZIC', 10), ('SHVR', 10), ('GVWY', 10)]
        buyers_spec = sellers_spec
        traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}

        order_interval = 10
        order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                    'interval': order_interval, 'timemode': 'drip-poisson'}

        n_sessions = 1

        x = np.empty(0)
        y = np.empty(0)

        for sess in range(n_sessions):
            trial_id = 'smith_chart_' + str(sess)

            market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

            prices_fname = 'data/' + trial_id + '_tape.csv'
            with open(prices_fname, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time = float(row[1])
                    price = float(row[2])
                    x = np.append(x,time)
                    y = np.append(y,price)

        fig7, ax7 = plt.subplots()
        ax7.plot(x, y, 'x', color='black')
        ax7.set_xlabel("Time")
        ax7.set_ylabel("Price")
        ax7.set_title(f"{n_sessions} Market Session Prices (Shocked Demand/Supply)")
        st.pyplot(fig7)
    
    elif selected_trader_type == 'GVWY':
        st.subheader("Trader -- GVWY")
        start_time = 0
        end_time = 60 * 10

        chart1_range = (80, 320)

        supply_schedule = [{'from': start_time, 'to': end_time, 'ranges': [chart1_range], 'stepmode': 'fixed'}]
        demand_schedule = [{'from': start_time, 'to': end_time, 'ranges': [chart1_range], 'stepmode': 'fixed'}]

        order_interval = 60
        order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                    'interval': order_interval, 'timemode': 'periodic'}

        sellers_spec = [('GVWY', 11)]
        buyers_spec = sellers_spec
        prop_traders_spec = []
        traders_spec = {'sellers': sellers_spec, 'buyers': buyers_spec, 'proptraders': prop_traders_spec}

        verbose = False

        trial_id = 'smith_chart_1'
        dump_flags = {'dump_blotters': True, 'dump_lobs': True, 'dump_strats': True,
                    'dump_avgbals': True, 'dump_tape': True}

        random.seed(100) # changing the seed value will give us different sequences of random numbers

        # --- Plot 1 ---
        st.subheader("Single Market Session (order_interval = 60, timemode = periodic)")
        market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

        prices_fname = 'data/' + trial_id + '_tape.csv'
        x = np.empty(0)
        y = np.empty(0)
        with open(prices_fname, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                time = float(row[1])
                price = float(row[2])
                x = np.append(x,time)
                y = np.append(y,price)

        fig1, ax1 = plt.subplots()
        ax1.plot(x, y, 'x', color='black')
        ax1.set_xlabel("Time")
        ax1.set_ylabel("Price")
        ax1.set_title("Market Session Prices")
        st.pyplot(fig1)

        # --- Plot 2 ---
        st.subheader("Multiple Market Sessions (order_interval = 60, timemode = periodic)")
        n_sessions = 10

        x = np.empty(0)
        y = np.empty(0)

        for sess in range(n_sessions):
            trial_id = 'smith_chart_' + str(sess)

            market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

            prices_fname ='data/' +  trial_id + '_tape.csv'
            with open(prices_fname, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time = float(row[1])
                    price = float(row[2])
                    x = np.append(x,time)
                    y = np.append(y,price)

        fig2, ax2 = plt.subplots()
        ax2.plot(x, y, 'x', color='black')
        ax2.set_xlabel("Time")
        ax2.set_ylabel("Price")
        ax2.set_title(f"{n_sessions} Market Sessions Prices")
        st.pyplot(fig2)

        # --- Plot 3 (Duplicate of Plot 2, assuming it was intentional) ---
        st.subheader("Multiple Market Sessions (Duplicate Plot) (order_interval = 60, timemode = periodic)")
        n_sessions = 10

        x = np.empty(0)
        y = np.empty(0)

        for sess in range(n_sessions):
            trial_id = 'smith_chart_' + str(sess)

            market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

            prices_fname ='data/' +  trial_id + '_tape.csv'
            with open(prices_fname, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time = float(row[1])
                    price = float(row[2])
                    x = np.append(x,time)
                    y = np.append(y,price)

        fig3, ax3 = plt.subplots()
        ax3.plot(x, y, 'x', color='black')
        ax3.set_xlabel("Time")
        ax3.set_ylabel("Price")
        ax3.set_title(f"{n_sessions} Market Sessions Prices (Duplicate)")
        st.pyplot(fig3)

        # --- Plot 4 ---
        st.subheader("Multiple Market Sessions (order_interval = 10, timemode = drip-poisson)")
        order_interval = 10
        order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                    'interval': order_interval, 'timemode': 'drip-poisson'}

        n_sessions = 10

        x = np.empty(0)
        y = np.empty(0)

        for sess in range(n_sessions):
            trial_id = 'smith_chart_' + str(sess)

            market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

            prices_fname ='data/' +  trial_id + '_tape.csv'
            with open(prices_fname, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time = float(row[1])
                    price = float(row[2])
                    x = np.append(x,time)
                    y = np.append(y,price)

        fig4, ax4 = plt.subplots()
        ax4.plot(x, y, 'x', color='black')
        ax4.set_xlabel("Time")
        ax4.set_ylabel("Price")
        ax4.set_title(f"{n_sessions} Market Sessions Prices (Drip-Poisson)")
        st.pyplot(fig4)

        # --- Plot 5 ---
        st.subheader("Multiple Market Sessions (40 GVWY traders, order_interval = 10, timemode = drip-poisson)")
        sellers_spec = [('GVWY', 40)]
        buyers_spec = sellers_spec
        traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}

        order_interval = 10
        order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                    'interval': order_interval, 'timemode': 'drip-poisson'}

        n_sessions = 10

        x = np.empty(0)
        y = np.empty(0)

        for sess in range(n_sessions):
            trial_id = 'smith_chart_' + str(sess)

            market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

            prices_fname = 'data/' + trial_id + '_tape.csv'
            with open(prices_fname, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time = float(row[1])
                    price = float(row[2])
                    x = np.append(x,time)
                    y = np.append(y,price)

        fig5, ax5 = plt.subplots()
        ax5.plot(x, y, 'x', color='black')
        ax5.set_xlabel("Time")
        ax5.set_ylabel("Price")
        ax5.set_title(f"{n_sessions} Market Sessions Prices (40 GVWY traders)")
        st.pyplot(fig5)

        # --- Plot 6 ---
        st.subheader("Single Market Session (Mixed Traders, order_interval = 10, timemode = drip-poisson)")
        sellers_spec = [('ZIP', 10), ('ZIC', 10), ('SHVR', 10), ('GVWY', 10)]
        buyers_spec = sellers_spec
        traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}

        order_interval = 10
        order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                    'interval': order_interval, 'timemode': 'drip-poisson'}

        n_sessions = 1

        x = np.empty(0)
        y = np.empty(0)

        for sess in range(n_sessions):
            trial_id = 'smith_chart_' + str(sess)

            market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

            prices_fname = 'data/' +  trial_id + '_tape.csv'
            with open(prices_fname, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time = float(row[1])
                    price = float(row[2])
                    x = np.append(x,time)
                    y = np.append(y,price)

        fig6, ax6 = plt.subplots()
        ax6.plot(x, y, 'x', color='black')
        ax6.set_xlabel("Time")
        ax6.set_ylabel("Price")
        ax6.set_title(f"{n_sessions} Market Session Prices (Mixed Traders)")
        st.pyplot(fig6)

        # --- Plot 7 ---
        st.subheader("Single Market Session (Shocked Demand/Supply, Mixed Traders)")
        shocked_range = (300, 400)
        shock_time = int(end_time / 2)

        supply_schedule = [ {'from':0, 'to':shock_time, 'ranges':[chart1_range], 'stepmode':'fixed'},
                            {'from':shock_time, 'to':end_time, 'ranges':[shocked_range], 'stepmode':'fixed'},
                        ]
        demand_schedule = supply_schedule

        sellers_spec = [('ZIP', 10), ('ZIC', 10), ('SHVR', 10), ('GVWY', 10)]
        buyers_spec = sellers_spec
        traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}

        order_interval = 10
        order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                    'interval': order_interval, 'timemode': 'drip-poisson'}

        n_sessions = 1

        x = np.empty(0)
        y = np.empty(0)

        for sess in range(n_sessions):
            trial_id = 'smith_chart_' + str(sess)

            market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

            prices_fname = 'data/' + trial_id + '_tape.csv'
            with open(prices_fname, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time = float(row[1])
                    price = float(row[2])
                    x = np.append(x,time)
                    y = np.append(y,price)

        fig7, ax7 = plt.subplots()
        ax7.plot(x, y, 'x', color='black')
        ax7.set_xlabel("Time")
        ax7.set_ylabel("Price")
        ax7.set_title(f"{n_sessions} Market Session Prices (Shocked Demand/Supply)")
        st.pyplot(fig7)
    
else:
    st.subheader("Invalid Mode Selected")
    st.write("Please select a valid demo mode from the options provided.")

