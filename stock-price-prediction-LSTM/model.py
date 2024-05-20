import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

class LSTM(nn.Module):
    def __init__(self, input_size =1, hidden_layer =32, num_layers=2, output_size =1, dropout = 0.2):
        super().__init__()
        self.hidden_layer = hidden_layer
        self.linear_1 = nn.Linear(input_size, hidden_layer)
        self.relu = nn.ReLU()
        self.lstm = nn.LSTM(hidden_layer, hidden_size = self.hidden_layer, num_layers = num_layers,
                            batch_first = True)
        self.dropout = nn.Dropout(dropout)
        self.linear_2 = nn.Linear(num_layers * hidden_layer, output_size)

        self.init_weights()
    
    