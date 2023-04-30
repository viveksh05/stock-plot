import yfinance as yf
import pendulum
import matplotlib.pyplot as plt

def stock_info(stock_name):
    stock_n = yf.Ticker(stock_name)
    stock_i = stock_n.info
    #print stock info
    print(stock_i['longName'])
    print(stock_i['website']) 
    return stock_data(stock_n)

def stock_data(stock_code):
    #stock_period=input("Please enter the period in format like 5d,1mo..:  ")
    hist = stock_code.history(period="3mo")
    return plot_graph(hist)

def plot_graph(stock_history):
    time_series = list(stock_history['Open'])
    dt_list = [pendulum.parse(str(dt)).float_timestamp for dt in list(stock_history.index)]
    plt.style.use('dark_background')
    plt.plot(dt_list, time_series, linewidth=2)
   

if __name__ == "__main__":
    print("This utility helps you visualize stock prices for NYSE over a specific period.")
    stock=input("Please enter the stock you would like to visualize:  ")
    stock_info(stock)
