from env import host, user, password
import pandas as pd
import numpy as np
import os



def get_connection(db, user = user, host = host, password = password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def new_zillow_data():
    '''
    This function reads the zillow data from CodeUp database into a df,
    write it to a csv file, and returns the df.
    '''
    sql_query = '''
    SELECT *
    FROM properties_2017
    JOIN(
        SELECT parcelid, logerror, max(transactiondate) AS lasttransactiondate
        FROM predictions_2017
        GROUP BY parcelid, logerror
        ) AS pred USING(parcelid)
    LEFT JOIN airconditioningtype USING(airconditioningtypeid)
    LEFT JOIN architecturalstyletype USING(architecturalstyletypeid)
    LEFT JOIN buildingclasstype USING(buildingclasstypeid)
    LEFT JOIN heatingorsystemtype USING(heatingorsystemtypeid)
    LEFT JOIN propertylandusetype USING(propertylandusetypeid)
    LEFT JOIN storytype USING(storytypeid)
    LEFT JOIN typeconstructiontype USING(typeconstructiontypeid)
    WHERE latitude IS NOT NULL
    AND longitude IS NOT NULL;
                '''

    df = pd.read_sql(sql_query, get_connection('zillow'))
    df.to_csv('zillow_df.csv')
    return df

def get_zillow_data(cached=False):
    '''
    This function reads in zillow data from CodeUp database if cached == False 
    or if cached == True reads in mall customers df from a csv file, returns df.
    '''
    if cached or os.path.isfile('zillow_df.csv') == False:
        df = new_zillow_data()
    else:
        df = pd.read_csv('zillow_df.csv', index_col=0)
    return df
    