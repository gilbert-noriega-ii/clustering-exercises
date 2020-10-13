import pandas as pd
import matplotlib.pyplot as plt
from acquire import get_connection

from sklearn.model_selection import train_test_split
import sklearn.preprocessing



#################################### Get Mall Data Function ####################################


def new_mall_data():
    '''
    This function reads the mall customer data from CodeUp database into a df,
    write it to a csv file, and returns the df.
    '''
    sql_query = '''
                select * 
                from customers
                '''
    df = pd.read_sql(sql_query, get_connection('mall_customers'))
    df.to_csv('mall_df.csv')
    return df



#################################### Detect Outliers Function ####################################


def detect_outliers(df):
    '''
    This function finds the outliers to a column
    in a dataframe and displays their location
    '''
    for col in df.select_dtypes('int64'):
        #find lower quartile
        q1 = df[col].quantile(0.25)
        #find upper quartile
        q3 = df[col].quantile(0.75)
        #find inner quartile range
        iqr = q3 - q1
        #establish a k value
        k = 1.5
        #find the lower bound
        lower_bound = q1 - (k * iqr)
        #find the upper bound
        upper_bound = q3 + (k * iqr)
        #find the lower outliers
        lower_outliers = df[col][df[col] < lower_bound]
        #find the upper outliers
        upper_outliers = df[col][df[col] > upper_bound]
        #if the column has no outliers
        if lower_outliers.empty == True & upper_outliers.empty == True:
            print(f'There are no outliers in {col}. \n') 
        #if the column has only lower outliers
        elif (lower_outliers.empty == False) & (upper_outliers.empty == True):
            print(f'The lower outliers in {col} are \n{lower_outliers}\n')
        #if the column has only upper outliers
        elif (upper_outliers.empty == False) & (lower_outliers.empty == True):
            print(f'The upper outliers in {col} are \n{upper_outliers}\n')
        #if the column has both upper and lower outliers
        elif (upper_outliers.empty == False) & (lower_outliers.empty == False):
            print(f'The upper outliers in {col} are \n{upper_outliers}\n')
            print(f'The lower outliers in {col} are \n{lower_outliers}\n')



#################################### Mall Split Function ####################################

def mall_split(df):
    '''
    This functions takes a dataframe and splits it 
    into train, validate and test data sets
    '''
    train_and_validate, test = train_test_split(df, test_size=.2, random_state=123)
    train, validate = train_test_split(train_and_validate, test_size=.25, random_state=123)
    return train, validate, test



#################################### Scale and Wrangle Mall Data Function ####################################


def wrangle_mall(cached=True):
    '''
    This function acquires new_mall_data, 
    splits into train, validate, and test,
    scales the numeric columns using min-max scaling,
    and adds the scaled columns to the respective split data sets
    '''
    #acquires mall data and saves it as df
    df = new_mall_data()
    #set 'customer_id' as index
    df = df.set_index('customer_id')
    #dropping the two upper outliers for annual_income
    df = df.drop([199, 200])
    #creates a dummy variable for gender
    gender_dummies = pd.get_dummies(df.gender, drop_first=True)
    #adds dummy gender column to original dataframe
    df = pd.concat([df, gender_dummies], axis=1)
    #drops original gender column
    df = df.drop(columns=['gender'])
    #uses the function above to split the into train, validate and test
    train, validate, test = mall_split(df)
    #assigns the scaling method as min-max scaler
    scaler = sklearn.preprocessing.MinMaxScaler()
    #identifies the columns to scale
    columns_to_scale = ['age', 'annual_income', 'spending_score']
    #adds '_scaled' to the end of the newly scaled columns to identify differences
    new_column_names = [c + '_scaled' for c in columns_to_scale]
    #fts the columns to the scaler
    scaler.fit(train[columns_to_scale])
    #concatonates the newly created scaled columns to their respective data sets,
    #adds 'new_column_names' as the label to the added columns
    #uses the original index since the new columns no longer have an index
    train = pd.concat([
        train,
        pd.DataFrame(scaler.transform(train[columns_to_scale]), columns=new_column_names, index=train.index),
    ], axis=1)
    validate = pd.concat([
        validate,
        pd.DataFrame(scaler.transform(validate[columns_to_scale]), columns=new_column_names, index=validate.index),
    ], axis=1)
    test = pd.concat([
        test,
        pd.DataFrame(scaler.transform(test[columns_to_scale]), columns=new_column_names, index=test.index),
    ], axis=1)
    #returns the data sets with the new respective scaled data
    return train, validate, test
