from os.path import join
import logging


# True or False
EXPORT_DATA_TO_FILE_AFTER_CHART_CLOSE = False

# True or False // Currently doesnt work with live data
ENABLE_VERTICAL_LINES_ON_HOVER = True
ENABLE_HORIZONTAL_LINES_ON_HOVER = False


# API URL.
BASE_URL = "https://www.bitmex.com/api/v1/"

########################################################################################################################
# Connection/Auth
########################################################################################################################

# The BitMEX API requires permanent API keys. Go to https://www.bitmex.com/app/apiKeys to fill these out.
API_KEY = ""
API_SECRET = ""

# What is the maximum duration of price/interest you can see on the chart
# Default saves 1 hour of time on the chart
SAVE_CHART_IN_SECONDS = 3600

# Charting color of price and interest
# Available colors :
# "blue"
# "orange"
# "green"
# "red"
# "purple"
# "brown"
# "pink"
# "gray"
# "olive"
# "cyan"
PRICE_LINE_COLOR = "green"
INTEREST_LINE_COLOR = "red"
HOVER_LINE_COLOR = "cyan"

# ---
# LOG_LEVEL = logging.INFO
CONTRACTS = ["XBTUSD"]
