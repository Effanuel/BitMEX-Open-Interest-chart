import urllib.request, urllib.error, urllib.parse
import time
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc
import matplotlib
import pylab
import json

import matplotlib.animation as animation

matplotlib.rcParams.update({'font.size': 9})

def rsiFunc(prices, n=14):
    deltas = np.diff(prices)
    seed = deltas[:n+1]
    up = seed[seed>=0].sum()/n
    down = -seed[seed<0].sum()/n
    rs = up/down
    rsi = np.zeros_like(prices)
    rsi[:n] = 100. - 100./(1.+rs)

    for i in range(n, len(prices)):
        delta = deltas[i-1] # cause the diff is 1 shorter

        if delta>0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta

        up = (up*(n-1) + upval)/n
        down = (down*(n-1) + downval)/n

        rs = up/down
        rsi[i] = 100. - 100./(1.+rs)

    return rsi

def movingaverage(values,window):
    weigths = np.repeat(1.0, window)/window
    smas = np.convolve(values, weigths, 'valid')
    return smas # as a numpy array


def ExpMovingAverage(values, window):
    weights = np.exp(np.linspace(-1., 0., window))
    weights /= weights.sum()
    a =  np.convolve(values, weights, mode='full')[:len(values)]
    a[:window] = a[window]
    return a


def computeMACD(x, slow=26, fast=12):
    """
    compute the MACD (Moving Average Convergence/Divergence) using a fast and slow exponential moving avg'
    return value is emaslow, emafast, macd which are len(x) arrays
    """
    emaslow = ExpMovingAverage(x, slow)
    emafast = ExpMovingAverage(x, fast)
    return emaslow, emafast, emafast - emaslow


def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter
i = 1
def graphData(stock, MA1,MA2):
    fig.clf()
    global i

    '''
        Use this to dynamically pull a stock:

    '''
    stock = 'TSLA'
    try:
        
        #print('Currently Pulling')
        urlToVisit = 'https://www.bitmex.com/api/v1/instrument?symbol=XBTUSD'
        stockFile =[]
        data = 1
        with urllib.request.urlopen(urlToVisit) as sourceCode:#.read().decode()
            data = json.loads(sourceCode.read().decode())
            
            print(data[0]['openInterest'])
            
            
        ax1.plot([1,2,3,4,5], [2,4,6,1,2])
        i = i + 1
            # splitSource = sourceCode.split('\n')
            # for eachLine in splitSource:
            #     splitLine = eachLine.split(',')
            #     if len(splitLine)==6:
            #         if 'values' not in eachLine:
            #             stockFile.append(eachLine)
                            
            # y = len(date)
            # newAr = []
            # while x < y:
            #     appendLine = date[x],openp[x],highp[x],lowp[x],closep[x],volume[x]
            #     newAr.append(appendLine)
            #     x+=1
                
            # Av1 = movingaverage(closep, MA1)
            # Av2 = movingaverage(closep, MA2)

            # SP = len(date[MA2-1:])
                

                        # ax1 = plt.subplot2grid((6,4), (1,0), rowspan=4, colspan=4)
                        # # candlestick_ohlc(ax1, newAr[-SP:], width=.6, colorup='#53c156', colordown='#ff1717')

                        # Label1 = str(MA1)+' SMA'
                        # Label2 = str(MA2)+' SMA'

                        # # ax1.plot(date[-SP:],Av1[-SP:],'#e1edf9',label=Label1, linewidth=1.5)
                        # # ax1.plot(date[-SP:],Av2[-SP:],'#4ee6fd',label=Label2, linewidth=1.5)
                        
                        # ax1.grid(True, color='w')
                        # # ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
                        # # ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
                        # ax1.yaxis.label.set_color("w")
                        # ax1.spines['bottom'].set_color("#5998ff")
                        # ax1.spines['top'].set_color("#5998ff")
                        # ax1.spines['left'].set_color("#5998ff")
                        # ax1.spines['right'].set_color("#5998ff")
                        # ax1.tick_params(axis='y', colors='w')
                        # plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(prune='upper'))
                        # ax1.tick_params(axis='x', colors='w')
                        # plt.ylabel('Stock price and Volume')
                      

                        # # maLeg = plt.legend(loc=9, ncol=2, prop={'size':7},
                        # #            fancybox=True, borderaxespad=0.)
                        # # maLeg.get_frame().set_alpha(0.4)
                        # # textEd = pylab.gca().get_legend().get_texts()
                        # # pylab.setp(textEd[0:5], color = 'w')

                        # volumeMin = 0
                        
                    
                        # # rsi = rsiFunc(closep)
                        # rsiCol = '#c1f9f7'
                        # posCol = '#386d13'
                        # negCol = '#8f2020'
                        

                        # ax1v = ax1.twinx()
                        # # ax1v.fill_between(date[-SP:],volumeMin, volume[-SP:], facecolor='#00ffe8', alpha=.4)
                        # # ax1v.axes.yaxis.set_ticklabels([])
                        # ax1v.grid(False)
                        # ###Edit this to 3, so it's a bit larger
                        # # ax1v.set_ylim(0, 3*volume.max())
                        # ax1v.spines['bottom'].set_color("#5998ff")
                        # ax1v.spines['top'].set_color("#5998ff")
                        # ax1v.spines['left'].set_color("#5998ff")
                        # ax1v.spines['right'].set_color("#5998ff")
                        # ax1v.tick_params(axis='x', colors='w')
                        # ax1v.tick_params(axis='y', colors='w')
                    
                        # fillcolor = '#00ffe8'
                        # nslow = 26
                        # nfast = 12
                        # nema = 9
                        # # emaslow, emafast, macd = computeMACD(closep)
                        # # ema9 = ExpMovingAverage(macd, nema)
                        # # ax2.plot(date[-SP:], macd[-SP:], color='#4ee6fd', lw=2)
                        # # ax2.plot(date[-SP:], ema9[-SP:], color='#e1edf9', lw=1)
                        # # ax2.fill_between(date[-SP:], macd[-SP:]-ema9[-SP:], 0, alpha=0.5, facecolor=fillcolor, edgecolor=fillcolor)

                        # plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(prune='upper'))



                        # plt.suptitle(stock.upper(),color='w')
                        # # plt.setp(ax0.get_xticklabels(), visible=False)
                        # # plt.setp(ax1.get_xticklabels(), visible=False)
                        

                        # plt.subplots_adjust(left=.09, bottom=.14, right=.94, top=.95, wspace=.20, hspace=0)

    except Exception as e:
        print(str(e), 'failed to organize pulled data.')