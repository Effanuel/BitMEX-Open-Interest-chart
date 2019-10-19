# BitMEX-Open-Interest-chart

## Table of Contents

- [Current Features](#current-features)
- [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [License](#license)
- [Useful material](#useful-material)

<p align="center"> 
<img src="assets/interface_range_tool.png">
</p>

# BitMEX scaled orders tool

This project is a program which displays BitMEX XBTUSD current price with Open-Interest

### Current Features

- Display XBTUSD price and Open Interest of XBTUSD using Websocket with matplotlib.

### Built With

The majority of the code is taken from [Sample-market-maker](https://github.com/BitMEX/sample-market-maker). In addition to that, the program uses matplotlib to chart the data from a websocket.

- [Sample-market-maker](https://github.com/BitMEX/sample-market-maker) + [Matplotlib](https://matplotlib.org/)


<!-- GETTING STARTED -->

## Getting Started

- Go to https://www.bitmex.com
* Get API keys:
  - Account > API keys > Create API key;
    - **Key Permissions** : -;
    - **Withdraw**: Unchecked;

*(Freshly created account with API keys also works)*

### Prerequisites

- [Python](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads) _(for cloning the repository)_

### Installation

1. Clone the repo or [download zip]():

```sh
git clone ...
cd Bitmex-Open-Interest-chart-master/api
```

2. Init a virtual environment _(highly recommended)_
```sh
virtualenv open-interest
.open/Scripts/activate
```

2.1 Activate virtual environment:
```sh
.open/Scripts/activate
```

2. Install dependencies for the virtual environment:
```sh
pip install -r requirements.txt
```


3. Enter your API keys in `settings.py`:

```
API_KEY = "qqSqebwbwymenrPxL3BjFsJHJv"
API_SECRET = "hgcjYUk37frty2Vaaa-fNKYk0yla26a33ro34U53wVOFA333ab-"
```

4. Run the application:

```sh
python main.py
```

<!-- USAGE EXAMPLES -->

#### TLDR setup:

```sh
git clone https://github.com/Effanuel/Bitmex-scaled-orders.git
cd Bitmex-Open-Interest-chart
virtualenv open-interest
.open/Scripts/activate
```

- Put API keys in `settings.py`;

```sh
pip install -r requirements.txt
python main.py
```

## Usage

##### Run application:

```sh
cd Bitmex-scaled-orders/api
python main.py
```


## Roadmap

- Save price and interest data to a file;
- Read price/interest data to display on a chart;

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- USEFUL METERIAL -->

## Useful Material

- [BitMEX Survival Guide](https://www.crypto-simplified.com/wp-content/uploads/2018/09/BitMEX-Survival-Guide-v1.5.pdf)
- [Crypto news](https://cointelegraph.com/)
- [BitMEX position calculator](https://blockchainwhispers.com/bitmex-position-calculator/)
- [Crypto sentiment/statistics tool](https://thetie.io/)


