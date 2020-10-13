import pandas as pd




def handle_missing_values(df, prop_required_column, prop_required_row):
    thresh_col = int(round(prop_required_column*df.shape[0],0))
    df.dropna(axis=1, thresh=thresh_col, inplace=True)
    thresh_row = int(round(prop_required_row*df.shape[1],0))
    df.dropna(axis=0, thresh=thresh_row, inplace=True)
    return df 