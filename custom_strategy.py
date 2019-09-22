import sys
from time import sleep
import settings
import random
from market_maker.market_maker import OrderManager
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.animation as animation
from matplotlib import style
import numpy as np

import matplotlib.ticker as ticker

style.use('dark_background')
mpl.rcParams['toolbar'] = 'None'



class CustomOrderManager(OrderManager):
    """A sample order manager for implementing your own custom strategy"""
    def animate(self, i) -> None:
        xs.append(i)
        y1 = self.exchange.get_instrument()['lastPrice']
        y2 = self.exchange.get_instrument()['openInterest']/1000000
        ys1.append(y1)
        ys2.append(y2)
        
        # ax1.plot(xs, ys1, color='g')
        # ax1.plot(xs, ys2, color='g')


        color = 'tab:green'
        ax1[0].ticklabel_format(useOffset=False)
        ax1[0].set_ylabel('Price', color=color)
        ax1[0].grid(color='w', linestyle='-', linewidth=0.1)
        ax1[0].plot(xs, ys1, color=color, linewidth=1)
        ax1[0].tick_params(axis='y', labelcolor=color)
        
         # instantiate a second axes that shares the same x-axis
       
        # color = 'tab:blue'
        # ax2.ticklabel_format(useOffset=False)
        # ax2.set_ylabel('sin', color=color)
        #   # we already handled the x-label with ax1
        # ax2.plot(xs, ys2, color=color)
        # ax2.tick_params(axis='y', labelcolor=color)

        #save last 50 ticks
        ax1[0].set_xlim(left=max(0, i-720), right=i+5)

        color = 'tab:red'
        ax1[1].ticklabel_format(useOffset=False)
        ax1[1].set_xlabel('time (s)')
        
        ax1[1].set_ylabel('Open Interest', color=color)
        ax1[1].plot(xs, ys2, color=color, linewidth=0.5)
        ax1[1].tick_params(axis='y', labelcolor=color)
        # start, end = ax1[1].get_xlim()
        # ax1[1].yaxis.set_ticks(np.arange(start, end, 1e9))
       # ax1[1].yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
        ax1[1].set_xlim(left=max(0, i-120), right=i+5)
        # ax2.set_xlim(left=max(0, i-50), right=i+5)
        # ax2.set_xlim(left=max(0, i-50), right=i+5)
        # ax1.get_xaxis().get_major_formatter().set_scientific(False)
        # ax2.get_xaxis().get_major_formatter().set_scientific(False)
        ax1[1].grid(color='w', linestyle='-', linewidth=0.1)
        plt.tight_layout()
        # plt.xlabel('Time(s)')
        # plt.ylabel('Open Interest')
        # plt.title('OI chart')

    def place_orders(self) -> None:
         ani = animation.FuncAnimation(fig, self.animate, interval = 5000)
         plt.show()
       


      
    def run_loop11(self) -> None:
        while True:
            sys.stdout.write("-----\n")
            sys.stdout.flush()

            self.check_file_change()
            sleep(settings.LOOP_INTERVAL)

            # This will restart on very short downtime, but if it's longer,
            # the MM will crash entirely as it is unable to connect to the WS on boot.
            if not self.check_connection():
                logger.error("Realtime data connection unexpectedly closed, restarting.")
                self.restart()

            self.sanity_check()  # Ensures health of mm - several cut-out points here
            self.print_status()
           
             # Print skew, delta, etc


            
            
  # Creates desired orders and converges to existing orders


# fig = plt.figure()

fig, ax1 = plt.subplots(2)
# ax2 = ax1.twinx()
# ax2 = ax1.twinx() 
xs = []
ys1 = []
ys2 = []
def run_program() -> None:
    order_manager = CustomOrderManager()    
    # Try/except just keeps ctrl-c from printing an ugly stacktrace
    try:
        order_manager.run_loop11()
    except (KeyboardInterrupt, SystemExit):
        sys.exit()

if __name__ == "__main__":
    run_program()