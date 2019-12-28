"""BitMEX API Connector."""
from __future__ import absolute_import
import requests
import time
import datetime
import json
import base64
import uuid
import logging
from market_maker.auth import APIKeyAuthWithExpires
from market_maker.utils import constants, errors
from market_maker.ws.ws_thread import BitMEXWebsocket


# https://www.bitmex.com/api/explorer/
class BitMEX(object):

    """BitMEX API Connector."""

    def __init__(
        self,
        base_url=None,
        symbol=None,
        # apiKey=None,
        # apiSecret=None,
        orderIDPrefix="mm_bitmex_",
        shouldWSAuth=False,
        postOnly=False,
        timeout=7,
    ):
        """Init connector."""
        self.logger = logging.getLogger("root")
        self.base_url = base_url
        self.symbol = symbol
        self.postOnly = postOnly
        # if apiKey is None:
        #     raise Exception(
        #         "Please set an API key and Secret to get started. See "
        #         + "https://github.com/BitMEX/sample-market-maker/#getting-started for more information."
        #     )
        # self.apiKey = apiKey
        # self.apiSecret = apiSecret
        if len(orderIDPrefix) > 13:
            raise ValueError(
                "settings.ORDERID_PREFIX must be at most 13 characters long!"
            )
        self.orderIDPrefix = orderIDPrefix
        self.retries = 0  # initialize counter

        # Prepare HTTPS session
        self.session = requests.Session()
        # These headers are always sent
        self.session.headers.update({"user-agent": "liquidbot-" + constants.VERSION})
        self.session.headers.update({"content-type": "application/json"})
        self.session.headers.update({"accept": "application/json"})

        # Create websocket for streaming data
        self.ws = BitMEXWebsocket()
        self.ws.connect(base_url, symbol, shouldAuth=shouldWSAuth)

        self.timeout = timeout

    def __del__(self):
        self.exit()

    def exit(self):
        self.ws.exit()

    #
    # Public methods
    #

    def instrument(self, symbol):
        """Get an instrument's details."""
        return self.ws.get_instrument(symbol)

    def instruments(self, filter=None):
        query = {}
        if filter is not None:
            query["filter"] = json.dumps(filter)
        return self._curl_bitmex(path="instrument", query=query, verb="GET")