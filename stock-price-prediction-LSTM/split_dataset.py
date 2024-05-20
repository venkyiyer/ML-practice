import numpy as np 
from config import config

class SplitDataset:

    def normalize_data(self, x):
        self.mu = None
        self.sd = None
        self.mu = np.mean(x, axis = (0), keepdims= True)
        self.sd = np.mean(x, axis = (0), keepdims = True)
        normalized_x = (x - self.mu)/ self.sd

        return normalized_x
    
    def inverse_transform(self,x):
        return (x*self.sd) + self.mu
        

    def prepare_data_x(self, x, window_size):
        n_row = x.shape[0] - window_size + 1 
        output = np.lib.stride_tricks.as_strided(x, shape=(n_row, window_size),strides= (x.strides[0], x.strides[0]))
        return output[-1], output[-1]
    
    def prepare_data_y(self, x, window_size):
        output = x[window_size:]
        return output

    data_x, data_x_unseen = prepare_data_x(normalize_data(data_close_price), window_size= config['dataset']['window_size'])
    data_y = prepare_data_y(normalize_data(data_close_price), window_size=config['dataset'['window_size']])

    split_index = int(data_y.shape[0]*config['dataset']['train_test_split'])
    x_train_data = data_x[:split_index]
    x_val_data = data_x[split_index:]
    y_train_data = data_y[:split_index]
    y_val_data = data_y[split_index:]

