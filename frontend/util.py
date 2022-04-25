
import json
import os
from textwrap import indent
import pandas as pd
import datetime
import numpy as np
import math
from django.conf import settings
from backend.settings import BASE_DIR

def getDictData(expiry, formatedString):
    """
    creating the data as json format.
    """

    dict = {
        'Token':[],
        'Date':[],
        'Time':[],
        'Open':[],
        'High':[],
        'Low':[],
        'Close':[],
        'Volume':[],
        'Open_Interest':[],
        }
    
    df_log3 = pd.DataFrame(dict)
    




    # wholedata = pd.read_csv (os.path.join(BASE_DIR, 'media', f'{expiry}.csv')) #enter expiry here
    wholedata = pd.read_csv (f"{settings.MEDIA_ROOT}13aprilexpiry.csv") #enter expiry here


    # In[4]:


    data = wholedata.loc[wholedata['Ticker'] == 'BANKNIFTYWK37600CE'] #enter string here


    timeinterval = pd.read_csv (f"{settings.MEDIA_ROOT}timeinterval5min.csv",  names=["Time"])
    threemindata = pd.read_csv (f"{settings.MEDIA_ROOT}mintimeframe.csv",  names=["Time"])


    # In[6]:


    uniquedate = data.Date.unique()
    print(uniquedate)


    # In[7]:


    len(uniquedate)


    # In[8]:


    for p in range(len(uniquedate)):
        datefilterdata = data.loc[data['Date'] == uniquedate[p]]
        x=0
        y=0
        i=0
        for i in range(76):
            try:
                particulartime = datefilterdata.loc[datefilterdata['Time'] == threemindata.iloc[x]['Time']]
            except:
                print('error')
            try:
                if particulartime.iloc[0]['Time'] == threemindata.iloc[x]['Time'] :
                    df = particulartime
            except:
                print('1')
            x = x + 1

            try:
                particulartime = datefilterdata.loc[datefilterdata['Time'] == threemindata.iloc[x]['Time']]
            except:
                print('error')
            try:
                if particulartime.iloc[0]['Time'] == threemindata.iloc[x]['Time'] :
                    df =  pd.concat([df,particulartime])
            except:
                print('2')
            x = x + 1

            try:
                particulartime = datefilterdata.loc[datefilterdata['Time'] == threemindata.iloc[x]['Time']]
            except:
                print('error')
            try:
                if particulartime.iloc[0]['Time'] == threemindata.iloc[x]['Time'] :
                    df =  pd.concat([df,particulartime])
            except:
                print('3')
            x = x + 1
            
            try:
                particulartime = datefilterdata.loc[datefilterdata['Time'] == threemindata.iloc[x]['Time']]
            except:
                print('error')
            try:
                if particulartime.iloc[0]['Time'] == threemindata.iloc[x]['Time'] :
                    df =  pd.concat([df,particulartime])
            except:
                print('4')
            x = x + 1
            
            try:
                particulartime = datefilterdata.loc[datefilterdata['Time'] == threemindata.iloc[x]['Time']]
            except:
                print('error')
            try:
                if particulartime.iloc[0]['Time'] == threemindata.iloc[x]['Time'] :
                    df =  pd.concat([df,particulartime])
            except:
                print('5')
            x = x + 1

            try:
                open = df.head(1).Open.to_string(index=False)
            except:
                print('open')
            try:
                close = df.tail(1).Close.to_string(index=False)
            except:
                print('close')
            try:
                high = df['High'].max()
                low = df['Low'].min()
            except:
                print('hl')
            try:
                opentime = timeinterval.iloc[y]['Time']
            except:
                print('opentime')
            try:
                token = df.head(1).Ticker.to_string(index=False)
                date = df.head(1).Date.to_string(index=False)
                y = y + 1
            except:
                print('tokendate')
            
            try:
                volume = df['Volume'].sum()
            except:
                print('Vol error')
                
            try:
                oi = df['Open Interest'].sum()
            except:
                print('oi error')



            try:
                df_log3.loc[len(df_log3.index)] = [token,date,opentime,open,high,low,close,volume,oi]
            except:
                print('Cant Load')




    # df_log3.to_csv(f"{settings.MEDIA_ROOT}5mindata.csv", index=False, header=False)
    dataFrame = df_log3.to_dict("records")
    # print(dataFrame)    
    # print(dataFrame)
    return dataFrame 

