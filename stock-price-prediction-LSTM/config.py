config = {
    'alpha-vantage':{
        'key': '1VSH24OETDFS678F',
        'function': 'TIME_SERIES_DAILY_ADJUSTED',
        'symbol': 'IBM',
        'outputsize': 'full'
    },
    'dataset':{
        'window_size':20,
        'train_test_split': 0.80
    },
    'training':{
        'device':'cpu',
        'batch_size': 64,
        'num_epoch': 100,
        'learning_rate': 0.01,
        'scheduler_step_size': 40
    },
    'model':{
        'input_size':1,
        'number_lstm_layers':2,
        'lstm_size':32,
        'dropout':0.2
    }
}