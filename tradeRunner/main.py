
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../build/lib/backtrader')))

# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import backtrader as bt
from datetime import datetime

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    class SmaCross(bt.SignalStrategy):
        def __init__(self):
            sma1, sma2 = bt.ind.SMA(period=10), bt.ind.SMA(period=30)
            crossover = bt.ind.CrossOver(sma1, sma2)
            self.signal_add(bt.SIGNAL_LONG, crossover)

    cerebro = bt.Cerebro()
    cerebro.addstrategy(SmaCross)

    data0 = bt.feeds.YahooFinanceData(dataname='MSFT', fromdate=datetime(2011, 1, 1),
                                      todate=datetime(2012, 12, 31))
    cerebro.adddata(data0)

    cerebro.run()
    cerebro.plot()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
