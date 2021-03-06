import sys
import csv
from time import sleep

import settings
import random

from market_maker.market_maker import OrderManager
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.animation as animation
from matplotlib import style

import matplotlib.ticker as ticker

# For exporting
from pandas import DataFrame

# Style adjustments for matplotlib
style.use("dark_background")
mpl.rcParams["toolbar"] = "None"

# Figures
fig, ax1 = plt.subplots(2)
# Window title
fig = plt.gcf()
fig.canvas.set_window_title('BitMEX price and open-interest chart')
# Arrays to display data using matplotlib
ticks_array = []
price_data = []
open_interest_data = []
time_data = []

# Colors for the chart
color_arr = [
    "blue",
    "orange",
    "green",
    "red",
    "purple",
    "brown",
    "pink",
    "gray",
    "olive",
    "cyan",
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
    interest_color = "orange"
# Get line save time from settings
if settings.SAVE_CHART_IN_SECONDS >= 300:  # 5 minutes
    save_time = settings.SAVE_CHART_IN_SECONDS / 5
else:
    save_time = 300 / 5

if settings.HOVER_LINE_COLOR in color_arr:
    hover_color = settings.HOVER_LINE_COLOR
else:
    hover_color = "purple"


x = []  # Ticks from data file
y = []  # Price from data file
z = []  # Open-Interest from data file
v_lines = bool(settings.ENABLE_VERTICAL_LINES_ON_HOVER)
h_lines = bool(settings.ENABLE_HORIZONTAL_LINES_ON_HOVER)


def readData(file_name) -> None:
    with open(file_name, "r") as csv_file:
        plots = csv.DictReader(csv_file, delimiter=",")
        for row in plots:
            y.append(float(row["Price"]))
            z.append(float(row["Open-Interest"]))
        x.extend(list(range(0, len(y)))) # Ticks


def onMouseEvent(event):
    if not event.inaxes:
        try:
            ax1[0].lines.pop(1)
            ax1[1].lines.pop(1)
            plt.draw()
        except:
            return
        return
    ax1[0].lines = [ax1[0].lines[0]]
    ax1[1].lines = [ax1[1].lines[0]]

    # INIT VERTICAL LINES
    if v_lines:
        ax1[0].axvline(x=event.xdata, color=hover_color, linestyle="--", linewidth=0.5)
        ax1[1].axvline(x=event.xdata, color=hover_color, linestyle="--", linewidth=0.5)

    # INIT HORIZONTAL LINES
    if h_lines:
        ax1[0].axhline(
            y=y[int(event.xdata)], color=hover_color, linestyle="--", linewidth=0.5
        )

        ax1[1].axhline(
            y=z[int(event.xdata)], color=hover_color, linestyle="--", linewidth=0.5
        )

    # ax1[1].axvline(x=event.xdata, color="k")
    plt.draw()


# Inheritance from sample-market-maker class OrderManager
class Chart(OrderManager):
    """A class to initialize charting. Inheritance from sample-market-maker class OrderManager"""

    def animate(self, i) -> None:
        # Gets websocket XBTUSD data
        exchange_data = self.exchange.get_instrument("XBTUSD")
        # Gets current price of XBTUSD
        price_tick = exchange_data["lastPrice"]
        # Gets Open Interest of XBTUSD
        open_interest_tick = exchange_data["openInterest"] / 1000000
        # Gets timestamp of last price of XBTUSD
        time_tick = exchange_data["timestamp"]

        # On each iteration appends values to an array to display later

        ticks_array.append(i)
        price_data.append(price_tick)
        open_interest_data.append(open_interest_tick)
        time_data.append(time_tick)


        # INIT PRICE CHART
        ax1[0].ticklabel_format(useOffset=False)
        ax1[0].set_ylabel("Price", color=price_color)
        ax1[0].grid(color="w", linestyle="-", linewidth=0.1)
        ax1[0].plot(ticks_array, price_data, color=price_color, linewidth=1)
        ax1[0].tick_params(axis="y", labelcolor=price_color)
        ax1[0].set_xlim(left=max(0, i - save_time), right=i + 5)

        # INIT OPEN-INTEREST CHART
        ax1[1].ticklabel_format(useOffset=False)
        ax1[1].set_xlabel("ticks (1 tick = 5s)", color=interest_color)
        ax1[1].set_ylabel("Open Interest", color=interest_color)
        ax1[1].plot(
            ticks_array, open_interest_data, color=interest_color, linewidth=0.5
        )
        ax1[1].tick_params(axis="y", labelcolor=interest_color)
        ax1[1].set_xlim(left=max(0, i - save_time), right=i + 5)
        ax1[1].grid(color="w", linestyle="-", linewidth=0.1)

        plt.tight_layout()
        # Clear arrays to save from a memory leak
        # if len(price_data)-save_time % 3 == 0:
        #     print('cleared array')
        #     self.export_data_to_csv()
        #     del price_data[:]
        #     del open_interest_data[:]
        #     del time_data[:]

    def chart(self) -> None:

        ani = animation.FuncAnimation(fig, self.animate, interval=5000)

        plt.show()

    def start(self) -> None:
        pass

    # Exports collected data of price and OI to a file
    def export_data_to_csv(self, file_name=settings.EXPORT_TO_FILE_NAME, mode='a', header=False) -> None:
        print(f"---EXPORTING data to {file_name}---")
        # CSV headers
        data = {
            "Time": time_data,
            "Price": price_data,
            "Open-Interest": open_interest_data,
        }
        # Creates dataframe to export
        df = DataFrame(data, columns=["Time", "Price", "Open-Interest"])
        # Exports to file data.csv (not currently appending)
        # For appending set header=False, and mode='a'
        df.to_csv(f"./{file_name}", mode=mode, index=None, header=header)


# MAIN FUNCTION
def run_program() -> None:
    """
    This class initialization calls inherited constructor OrderManager
    which calls chart function
    """
    try:
        if len(sys.argv) == 2:
            try:
                # Read data into x,y,z arrays
                readData(sys.argv[1])
                if (
                    settings.ENABLE_HORIZONTAL_LINES_ON_HOVER
                    or settings.ENABLE_VERTICAL_LINES_ON_HOVER
                ):
                    print("hello")
                    # Enable onHoverEffect
                    plt.connect("motion_notify_event", onMouseEvent)

                # INIT PRICE CHART
                ax1[0].plot(x, y, color=price_color, linewidth=1)
                ax1[0].set_ylabel("Price", color=price_color)
                ax1[0].set_xlim(xmin=-5, xmax=x[-1] + 25)  # no empty space on left side
                # INIT OPEN-INTEREST CHART
                ax1[1].plot(x, z, color=interest_color, linewidth=1)
                ax1[1].set_xlabel("Ticks (1 tick = 5s)", color=interest_color)
                ax1[1].set_ylabel("Open Interest", color=interest_color)
                ax1[1].set_xlim(
                    xmin=-5, xmax=x[-1] + 25
                )  # no empty space on left/right side

                plt.tight_layout()
                plt.show()
            except (OSError, IOError) as e:
                print("Wrong file name.")
            except KeyError as e:
                print("Wrong file format.")

        else:
            chart = Chart()  # Is alive while the chart window is opened
            if settings.EXPORT_DATA_TO_FILE_AFTER_CHART_CLOSE is True:
                chart.export_data_to_csv()  # Export data to csv file
            else:
                sys.exit()  # Closes the program if chart window is closed
    except (KeyboardInterrupt, SystemExit):
        sys.exit()


if __name__ == "__main__":
    run_program()
