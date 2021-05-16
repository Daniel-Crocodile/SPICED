import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import lag_plot
from pandas.plotting import autocorrelation_plot
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
from sklearn.model_selection import TimeSeriesSplit, cross_val_score
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.ar_model import ar_select_order
pd.options.mode.chained_assignment = None 
from sklearn.metrics import mean_squared_error, mean_squared_log_error, mean_absolute_error, r2_score
from math import *
import csv

plt.rcParams['figure.figsize'] = (14,6)


def clean(file,csv_name):
    '''
    Cleaning of the Mean-Temperature Dataset 
    Parameters
    ----------
    file: str
        The data to load
    csv_name: str
        The output name of the csv-file
    Returns
    ---------
    csv-file in the folder
    '''
    df = pd.read_csv('TG_STAID002759.txt',sep=",", skiprows=19,  index_col=1, header=0, parse_dates=True)
    df = df.rename(columns=lambda x: x.strip())                         # remove white spaces in the column names 
    df['meanT'] = df['TG']*0.1                                          # give back the comma to the temperature 
    df.drop(df.head(25567).index, inplace=True)                         # remove all the data up untill 1946
    df.drop(df[['SOUID', 'Q_TG', 'TG']], axis =1, inplace = True)       # drop the useless columns
    df.to_csv(csv_name)             


def plot(file):
    '''
    Vizualisation of the Temperature dataset(csv-file) 
    Parameters
    ----------
    csv_file: str
        The data to load
    Returns
    ---------
    plt.show() 
    '''
    df = pd.read_csv(file, index_col=0, parse_dates=True)
    plt.bar(x='Nan', height=df.isna().sum())
    plt.show()
    
    dates = df.index #assign x
    temp = df['meanT']#assign y

    plt.plot(dates,temp)
    plt.xlabel('dates')
    plt.ylabel('Mean Temp')
    plt.title('Temperature profile in Berlin')
    plt.show()
    
    year_2021 = df.index[-700:]
    temp_2021 = df['meanT'][-700:]
    plt.plot(year_2021,temp_2021)
    plt.xlabel('dates')
    plt.ylabel('Mean Temperature')
    plt.title('Temperature profile in Berlin 2021')
    plt.show()
    
    lag_plot(df)
    plt.show()
    
    autocorrelation_plot(df)
    plt.show()

    plot_acf(df, lags=30)
    plt.show()

def split_data(file):
    '''
    Load of the Temperature dataset(csv-file) and split into train and test data
    Parameters
    ----------
    csv_file: str
        The data to load
    Returns
    ---------
    train: pd.dataframe()
        The dataframe with the traindata
    test: pd.dataframe()
        The dataframe with the testdata 
    Xtrain: matrix
        The X values to train the model
    ytrain: vector
        The y values to train the model
    Xtest: matrix
        The X values to test the model
    ytest: vector
        The y values to test the model
    '''
    data = pd.read_csv(file, index_col=0, parse_dates=True)
    
    train = data[:-365]
    test = data[-365:]
    
    Xtrain = train.index
    ytrain = train['meanT']

    Xtest = test.index
    ytest = test['meanT']
    
    return train,test,Xtrain,ytrain,Xtest,ytest

def trend_seas(train):
    '''
    Analyzing the Trend of the Temperature dataset.
    Parameters
    ----------
    df: pd.dataframe()
        The dataframe with the traindata
    Xtrain: matrix
        The X values to train the model
    ytrain: vector
        The y values to train the model
    Returns
    ---------
    train: pd.dataframe()
        The new dataframe with the timestep, trend column
    '''
    train['timestep'] = range(len(train))      
    Xtrend = train[['timestep']]                    
    y = train['meanT']
    m = LinearRegression()
    m.fit(Xtrend, y)
    train['trend'] = m.predict(Xtrend)
    trend = m.coef_*12*74  
    print('Trend: '+str(trend)+' °C')            
    print('intercept: ' + str(m.intercept_))
    
    train['month'] = train.index.month                                      
    dummies = pd.get_dummies(train['month'],prefix='month', drop_first=True) 
    train = train.merge(dummies,left_index = True, right_index=True) 
    Xseason = train.drop(['meanT','trend','month'], axis=1) 
    m = LinearRegression()
    m.fit(Xseason, y)
    train['tre_sea'] = m.predict(Xseason)
    
    train[['meanT', 'trend']].plot()
    train[['meanT','tre_sea']].plot()
    return train


def rem_lags(csv_name):
    '''
    Analyzing the Remainder and save the df in a csv file.
    Parameters
    ----------
    train: pd.dataframe()
        The dataframe with the data
    Returns
    ---------
    train: pd.dataframe()
        The dataframe with all columns: .
    csv-file in the folder
    '''
    train_re = pd.read_csv(csv_name, index_col=0, parse_dates=True)
    plot_pacf(train_re['remainder'])
    mod = ar_select_order(endog=train_re['remainder'], maxlag=10, old_names=False) 
    lags = mod.ar_lags
    return train_re, lags