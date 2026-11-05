import pandas as pd
import numpy as np


#construct tables for individual GRBs
def build_individual_grb_table(full_df,GRB_name):
    GRB=full_df[full_df['GRB']==GRB_name]
    return(GRB)

#separate flare data from non-flare data and append a binary flare flag to the full data
def separate_flare_data(df):

    #number of flares for this grb
    n_flares=int(df['N_flares'].iloc[0])

    #if no flares, return no flare data (after appending binary flare flag)
    if n_flares==0:
        df['Flare_flag']=0
        return(None, df.copy(),df.copy())

    #else, get all flare data
    else:

        #new df to hold flare data
        flare_df=pd.DataFrame(columns=df.columns)

        #loop through all flares 
        for i in range(1,n_flares+1):

            #get flare start and end times for each flare 
            local_flare_start=df['Flare_{}_start'.format(i)].iloc[0]
            local_flare_end=df['Flare_{}_end'.format(i)].iloc[0]

            #isolate flare data, add the binary flag, and merge to new df
            local_df=df[(df['Time'] >= local_flare_start) & (df['Time'] <= local_flare_end)]
            local_df['Flare_flag']=1
            flare_df=pd.concat([flare_df,local_df])

        #get the non flare data too, add binary flag
        non_flare_df=df[~df.index.isin(flare_df.index)].copy()
        non_flare_df['Flare_flag']=0

        #append flare flags to get the full df with flare flags
        full_df=pd.concat([flare_df,non_flare_df]).sort_index()
        return(flare_df, non_flare_df, full_df)
