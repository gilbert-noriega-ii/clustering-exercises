from env import host, user, password
import seaborn as sns
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
    sql_query = """
                SELECT *
                FROM predictions_2017 AS pred
                JOIN properties_2017 AS prop ON pred.parcelid = prop.parcelid
                LEFT JOIN airconditioningtype AS ac ON ac.airconditioningtypeid = prop.airconditioningtypeid
                LEFT JOIN architecturalstyletype AS arc ON arc.architecturalstyletypeid = prop.architecturalstyletypeid
                LEFT JOIN buildingclasstype AS bc ON bc.buildingclasstypeid = prop.buildingclasstypeid
                LEFT JOIN heatingorsystemtype AS heat ON heat.heatingorsystemtypeid = prop.heatingorsystemtypeid
                LEFT JOIN propertylandusetype AS plu ON plu.propertylandusetypeid = prop.propertylandusetypeid
                LEFT JOIN storytype AS st ON st.storytypeid = prop.storytypeid
                LEFT JOIN typeconstructiontype AS con ON con.typeconstructiontypeid = prop.typeconstructiontypeid
                WHERE transactiondate IN (SELECT MAX(transactiondate) FROM predictions_2017 GROUP BY parcelid)
                AND prop.latitude IS NOT NULL
                AND prop.longitude IS NOT NULL
                """

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
    