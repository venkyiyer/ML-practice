from config import config
from alpha_vantage.timeseries import TimeSeries

class DownloadData:
    def download(self,config):
        ts = TimeSeries(key= config['alpha-vantage']['key'])
        data = ts.get_daily(symbol= config['alpha-vantage']['symbol'], outputsize=config['alpha-vantage']['outputsize'])       

        date_data = [date for date in data.keys()]
        date_data.reverse()

        data_close_price = [float(data[date]['4. close']) for date in data.keys()]
        data_close_price.reverse()

        num_data_points = len(date_data)
        display_date_range = "from" + date_data[0] + " to " + date_data[num_data_points-1]

        print("Number of data points", num_data_points, display_date_range)

        return date_data, data_close_price, num_data_points, display_date_range
 
