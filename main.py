import sys
from time import sleep
import settings
import random
from market_maker.market_maker import OrderManager
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.animation as animation
from matplotlib import style

import matplotlib.ticker as ticker


# Style adjustments for matplotlib
style.use("dark_background")
mpl.rcParams["toolbar"] = "None"

# Figures
fig, ax1 = plt.subplots(2)
# Arrays to display data using matplotlib
xs = []
ys1 = []
ys2 = []


# Inheritance from sample-market-maker class OrderManager
class Chart(OrderManager):
    """A class to initialize charting. Inheritance from sample-market-maker class OrderManager"""

    def animate(self, i) -> None:

        # On each iteration appends values to an array to display later
        xs.append(i)
        # Gets current price of XBTUSD
        y1 = self.exchange.get_instrument()["lastPrice"]
        # Gets Open Interest of XBTUSD
        y2 = self.exchange.get_instrument()["openInterest"] / 1000000
        ys1.append(y1)
        ys2.append(y2)

        # Colors for the chart
        color_arr = [
            "tab:blue",
            "tab:orange",
            "tab:green",
            "tab:red",
            "tab:purple",
            "tab:brown",
            "tab:pink",
            "tab:gray",
            "tab:olive",
            "tab:cyan",
        ]
        # Get price line color from settings
        if settings.PRICE_LINE_COLOR in color_arr:
            price_color = settings.PRICE_LINE_COLOR
        else:
            price_color = "green"
        # Get interest line color from settings
        if settings.INTEREST_LINE_COLOR in color_arr:
            interest_color = settings.INTEREST_LINE_COLOR
        else:
            interest_color = "red"
        # Get line save time from settings
        if settings.SAVE_CHART_IN_SECONDS >= 300:  # 5 minutes
            save_time = settings.SAVE_CHART_IN_SECONDS / 5
        else:
            save_time = 300 / 5

        # INIT PRICE CHART
        ax1[0].ticklabel_format(useOffset=False)
        ax1[0].set_ylabel("Price", color=price_color)
        ax1[0].grid(color="w", linestyle="-", linewidth=0.1)
        ax1[0].plot(xs, ys1, color=price_color, linewidth=1)
        ax1[0].tick_params(axis="y", labelcolor=price_color)
        ax1[0].set_xlim(left=max(0, i - save_time), right=i + 5)

        # INIT OPEN-INTEREST CHART
        ax1[1].ticklabel_format(useOffset=False)
        ax1[1].set_xlabel("ticks (1 tick = 5s)", color=interest_color)
        ax1[1].set_ylabel("Open Interest", color=interest_color)
        ax1[1].plot(xs, ys2, color=interest_color, linewidth=0.5)
        ax1[1].tick_params(axis="y", labelcolor=interest_color)
        ax1[1].set_xlim(left=max(0, i - save_time), right=i + 5)
        ax1[1].grid(color="w", linestyle="-", linewidth=0.1)

        plt.tight_layout()

    def chart(self) -> None:
        ani = animation.FuncAnimation(fig, self.animate, interval=5000)
        plt.show()

    def start(self) -> None:
        pass


# MAIN FUNCTION
def run_program() -> None:
    """
    This class initialization calls constructor inherited OrderManager
    which calls chart function
    """
    try:
        chart = Chart()  # Is alive while the chart window is opened
        sys.exit()  # Closes the program if chart window is closed
    except (KeyboardInterrupt, SystemExit):
        sys.exit()


if __name__ == "__main__":
    run_program()
