# BitMEX-Open-Interest-chart

<p align="center"> 
  <img src='https://github.com/Effanuel/BitMEX-Open-Interest-chart/blob/master/assets/chart.png'>
</p>

## Table of Contents

- [Current Features](#current-features)
- [Built With](#built-with)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [License](#license)
- [Useful material](#useful-material)

## BitMEX-Open-Interest-chart

This project is a program which displays BitMEX XBTUSD **current price** with **Open-Interest**

### Current Features

- Display XBTUSD price and Open Interest of XBTUSD every 5 seconds _(Open Interest is updated every 5 seconds so it makes sense to also update the price at the same interval)_;
- Saves price and interest data to a file;
- Read price/interest data to display on a chart;
- **No authentication required**;
- Customise chart colors and saved chart time in `settings.py` file:

```python
SAVE_CHART_IN_SECONDS = 1800 # Default saves 30 minutes of chart time
PRICE_LINE_COLOR = "green"
INTEREST_LINE_COLOR = "orange"

# To export data to new file, to read later
EXPORT_DATA_TO_FILE_AFTER_CHART_CLOSE = False
EXPORT_TO_FILE_NAME = 'data.csv'

# True or False // Currently doesnt work with live data
ENABLE_VERTICAL_LINES_ON_HOVER = True
ENABLE_HORIZONTAL_LINES_ON_HOVER = False
```

### Built With

The majority of the code is taken from [Sample-market-maker](https://github.com/BitMEX/sample-market-maker). In addition to that, the program uses matplotlib to chart the data from a websocket.

- [Sample-market-maker](https://github.com/BitMEX/sample-market-maker) + [Matplotlib](https://matplotlib.org/)

### Prerequisites

- [Python](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads) _(for cloning the repository)_
- [Virtualenv](https://www.pythoncentral.io/how-to-install-virtualenv-python/): `pip install virtualenv`

### Installation

1. **Clone the repo** or [download zip](https://github.com/Effanuel/BitMEX-Open-Interest-chart/archive/master.zip):

```sh
git clone https://github.com/Effanuel/BitMEX-Open-Interest-chart.git
cd Bitmex-Open-Interest-chart
```

2. **Init a virtual environment** _(highly recommended)_

```sh
virtualenv open-interest
.\open-interest\Scripts\activate
```

   2.1 **Activate virtual environment**:

```sh
.\open-interest\Scripts\activate
```

3. **Install dependencies** for the virtual environment:

```sh
pip install -r requirements.txt
```

4. **Run live charting of Price and Open-Interest**:

```sh
python main.py
```

5. **Read data from a csv file**:

```
python main.py data.csv
```

<!-- USAGE EXAMPLES -->

#### TLDR setup:

```sh
git clone https://github.com/Effanuel/BitMEX-Open-Interest-chart.git
cd Bitmex-Open-Interest-chart
virtualenv open-interest
.open-interest\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Usage

##### Run application:

```sh
cd Bitmex-Open-Interest-chart
python main.py
```

## Roadmap

- Specify current price and Open Interest more clearly;

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- USEFUL METERIAL -->

## Useful Material

- [BitMEX Survival Guide](https://www.crypto-simplified.com/wp-content/uploads/2018/09/BitMEX-Survival-Guide-v1.5.pdf)
- [Crypto news](https://cointelegraph.com/)
- [BitMEX position calculator](https://blockchainwhispers.com/bitmex-position-calculator/)
- [Crypto sentiment/statistics tool](https://thetie.io/)
