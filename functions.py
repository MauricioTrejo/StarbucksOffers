import numpy as np
from datetime import datetime

def df_to_channel_df(portfolio):
    
    """
    This functions returns all the unique channels in the portfolio dataframe.
    
    Input:
        portfolio - Dataframe with the offers and channels
    Output:
        channels - List with unique channels in portfolio dataframe.
    """
    
    channels = []
    
    for channel in portfolio.channels:
        channels = np.union1d(channel, channels)
    return channels

def integers_to_dates(integers):
    """
    Convert a list of integers with the format YYYYMMDD into a date
    Input:
        integers - List of intergers with the following format YYYYMMDD
    Output:
        dates - List of datetime objects
    """
    
    dates = []
    
    for i in range(len(integers)):
        string = str(integers[i])
        date = datetime(year=int(string[0:4]), month=int(string[4:6]), day=int(string[6:8]))
        dates.append(date)
    
    return dates

def users_offer_path(data, user, offer):
    """
    Function that defines the path followed by a client after receiving an offer
    
    Input:
        data - Dataframe with data from portfolio, transcript and profile tables
        user - String with the user id
        offer - String with the offer id
        
    Output:
        path - Dictionary with the following information:
            user, offer, offer_received, offer_viewed, offer_completed, offer_type, 
            transaction_amt, reward and duration, completed_time
    """
    
    path = {}
    
    # User and offer
    path['user'] = user
    path['offer'] = offer
    
    # Filter data by user and offer
    user_offer_data = data.loc[data.person == user, :].loc[data.offer_id == offer, :]
    
    # Find the beginning of the promotion
    try:
        start_data = user_offer_data[user_offer_data.event == 'offer received']
        offer_start = start_data.time.iloc[0]
        path['offer_type'] = start_data.offer_type.iloc[0]
        path['reward'] = start_data.reward_y.iloc[0]
        path['duration'] = start_data.duration.iloc[0]
        
        path['offer_received'] = 1
    except:
        path['offer_received'] = 0
    
    # Find when the user saw the offer
    try:
        offer_viewed = int(user_offer_data.time[user_offer_data.event == 'offer viewed'])
        path['offer_viewed'] = 1
    except:
        path['offer_viewed'] = 0
        
    # Find when the user completed the offer
    try:
        completed_data = user_offer_data[user_offer_data.event == 'offer completed']
        offer_end = completed_data.time.iloc[0]
        path['offer_completed'] = 1
    except:
        path['offer_completed'] = 0
        
    # Completed time
    try:
        path['completed_time'] = (offer_end - offer_start) / 24 #We want data in days
        amount = data.loc[data.person == user, :].loc[data.time >= offer_start].loc[data.time <= offer_end].amount
        path['transaction_amt'] = np.sum(amount)
    except:
        path['completed_time'] = np.nan
        path['transaction_amt'] = np.nan
    
    return path

