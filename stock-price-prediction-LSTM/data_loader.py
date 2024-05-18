import numpy as np
from torch.utils.data import Dataset
from torch.utils.data import DataLoader

class TimeSeriesData(Dataset):
    def __init__(self,x, y):
        x = np.expand_dims(x,2)
        self.x = x.astype(np.float32)
        self.y = y.astype(np.float32)
    
    def __len__(self):
        return len(self.x)

    def __getitem__(self, idx):
        return (self.x[idx], self.y[idx])


