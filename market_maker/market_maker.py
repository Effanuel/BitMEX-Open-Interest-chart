from __future__ import absolute_import
from time import sleep
import sys
from datetime import datetime
from os.path import getmtime, join
import random
import requests
import atexit
import signal

from market_maker import bitmex
from market_maker.settings import settings
from market_maker.utils import log, constants, errors, math

# Used for reloading the bot - saves modified times of key files
import os

watched_files_mtimes = [
    (f, getmtime(f))
    for f in [
        join("market_maker", "market_maker.py"),
        join("market_maker", "bitmex.py"),
        "settings.py",
    ]
]


#
# Helpers
#
logger = log.setup_custom_logger("root")


class ExchangeInterface:
    def __init__(self, dry_run=False):
        self.dry_run = dry_run
        # if len(sys.argv) > 1:
        #     self.symbol = sys.argv[1]
        # else:
        self.symbol = "XBTUSD"
        self.bitmex = bitmex.BitMEX(
            base_url=settings.BASE_URL,
            symbol=self.symbol,
            # apiKey=settings.API_KEY,
            # apiSecret=settings.API_SECRET,
            orderIDPrefix="mm_bitmex_",
            postOnly=False,
            timeout=7,
        )

    def get_instrument(self, symbol=None):
        if symbol is None:
            symbol = self.symbol
        return self.bitmex.instrument(symbol)


    def is_open(self):
        """Check that websockets are still open."""
        return not self.bitmex.ws.exited

    def check_market_open(self):
        instrument = self.get_instrument()
        if instrument["state"] != "Open" and instrument["state"] != "Closed":
            raise errors.MarketClosedError(
                "The instrument %s is not open. State: %s"
                % (self.symbol, instrument["state"])
            )

    def check_if_orderbook_empty(self):
        """This function checks whether the order book is empty"""
        instrument = self.get_instrument()
        if instrument["midPrice"] is None:
            raise errors.MarketEmptyError("Orderbook is empty, cannot quote")

    def cancel_bulk_orders(self, orders):
        if self.dry_run:
            return orders
        return self.bitmex.cancel([order["orderID"] for order in orders])


class OrderManager:
    def __init__(self):
        self.exchange = ExchangeInterface(False)
        # Once exchange is created, register exit handler that will always cancel orders
        # on any error.
        atexit.register(self.exit)
        signal.signal(signal.SIGTERM, self.exit)

        logger.info("Using symbol %s." % self.exchange.symbol)

        logger.info(
            "Order Manager initializing, connecting to BitMEX. Fetching data..."
        )

        self.start_time = datetime.now()
        self.instrument = self.exchange.get_instrument()
        self.reset()

    def reset(self):
        # Create orders and converge.
        self.chart()

    ###
    # Orders
    ###

    def chart(self):
        """Create order items for use in convergence."""
        pass

    def check_file_change(self):
        """Restart if any files we're watching have changed."""
        for f, mtime in watched_files_mtimes:
            if getmtime(f) > mtime:
                self.restart()

    def check_connection(self):
        """Ensure the WS connections are still open."""
        return self.exchange.is_open()

    def exit(self):
        logger.info("Shutting down. All open orders will be cancelled.")
        try:
            self.exchange.bitmex.exit()
        except errors.AuthenticationError as e:
            logger.info("Was not authenticated; could not cancel orders.")
        except Exception as e:
            logger.info("Unable to cancel orders: %s" % e)

        sys.exit()

    def restart(self):
        logger.info("Restarting the market maker...")
        os.execv(sys.executable, [sys.executable] + sys.argv)


#
# Helpers
#


def XBt_to_XBT(XBt):
    return float(XBt) / constants.XBt_TO_XBT


def run():
    logger.info("BitMEX Market Maker Version: %s\n" % constants.VERSION)

    om = OrderManager()
    # Try/except just keeps ctrl-c from printing an ugly stacktrace
    try:
        om.run_loop()
    except (KeyboardInterrupt, SystemExit):
        sys.exit()
