from os.path import join
import logging


# True or False
EXPORT_DATA_TO_FILE_AFTER_CHART_CLOSE = False
# File for exporting data
EXPORT_TO_FILE_NAME = 'data.csv'

# True or False // Currently doesnt work with live data
ENABLE_VERTICAL_LINES_ON_HOVER = True
ENABLE_HORIZONTAL_LINES_ON_HOVER = False

# API URL.
BASE_URL = "https://www.bitmex.com/api/v1/"

# What is the maximum duration of price/interest you can see on the chart
# Default saves 30 minutes of time on the chart
SAVE_CHART_IN_SECONDS = 1800

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
INTEREST_LINE_COLOR = "orange"
HOVER_LINE_COLOR = "cyan"

# ---
# LOG_LEVEL = logging.INFO
CONTRACTS = ["XBTUSD"]
