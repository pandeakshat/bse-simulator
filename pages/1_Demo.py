import matplotlib.pyplot as plt
import numpy as np
import csv
import random
import streamlit as st
from BSE import market_session


start_time = 0
end_time = 60 * 10

chart1_range=(80, 320)

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

trial_id = './data/demo/smith_chart_1'
dump_flags = {'dump_blotters': True, 'dump_lobs': True, 'dump_strats': True,
              'dump_avgbals': True, 'dump_tape': True}


random.seed(100) # changing the seed value will give us different seqences of random numbers

market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

prices_fname = trial_id + '_tape.csv'
x = np.empty(0)
y = np.empty(0)
with open(prices_fname, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        time = float(row[1])
        price = float(row[2])
        x = np.append(x,time)
        y = np.append(y,price)

plt.plot(x, y, 'x', color='black');


# n_sessions = 10

# x = np.empty(0)
# y = np.empty(0)

# for sess in range(n_sessions):
#     trial_id = './data/demo/smith_chart_' + str(sess)

#     market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

#     prices_fname = trial_id + '_tape.csv'
#     with open(prices_fname, newline='') as csvfile:
#         reader = csv.reader(csvfile)
#         for row in reader:
#             time = float(row[1])
#             price = float(row[2])
#             x = np.append(x,time)
#             y = np.append(y,price)

# plt.plot(x, y, 'x', color='black');