import pandas as pd
import os
from sqlalchemy import create_engine

def percentToFloat(df, x):
    # Returning floats from percentage strings (format of xx%)
    df[x] = df[x].str.rstrip('%').astype('float') / 100.0
    return df

# Reading in the JSON file
basePath = os.path.dirname(os.path.abspath(__file__))
df = pd.read_json(basePath + '/fighter.json', 
                  orient = 'records')

# Naming columns to be converted to floats
percent_cols = ['StrAcc', 'StrDef', 'TDAcc', 'TDDef']

# Listing all column names
columns = ['name', 'wins', 'losses', 'draws', 'height', 'weight', 'reach',
          'stance', 'dob', 'SLpM', 'StrAcc', 'SApM', 'StrDef', 'TDAvg',
          'TDAcc', 'TDDef', 'SubAvg']

def main(df):
    # Returning floats from percentage strings (format of xx%)
    for col in percent_cols:
        percentToFloat(df, col)

    # Dropping any row that has blank data (blanks here are --)
    for col in columns:  
        df = df.drop(df[df[col] == '--'].index)

    # Removing lbs. from weight
    df['weight'] = df['weight'].str.rstrip('lbs.').astype('float')

    # Removing " from reach
    df['reach'] = df['reach'].str.rstrip('"').astype('float')

    # Converting height to inches
    df['height'] = df['height'].apply(lambda x: int(x.split('\'')[0])*12 + int(x.split()[1].rstrip('\"')))

    # Renaming columns
    df = df.rename(columns={"height":"height (in)", "weight":"weight (lbs)", "reach":"reach (in)", "StrAcc":"StrAcc (%)", "StrDef":"StrDef (%)", "TDAcc":"TDAcc (%)", "TDDef":"TDDef (%)"})

    # Calculating and classifying each fighter
    df["ratio"] = df["SLpM"] / (df["TDAvg"] + df["SubAvg"])
    quartiles = pd.qcut(df["ratio"], 5, labels = ["Heavy Grappling", "Light Grappling", "Balanced", "Light Striking", "Heavy Striking"])
    df = df.assign(Classification = quartiles.values)
    df = df.drop(columns=["ratio"])

    df = df.reset_index(drop=True)
    
    # Uploading the dataframe to a sqlite database
    engine = create_engine('sqlite:///fighter.sqlite', echo=True)
    sqlite_connection = engine.connect()
    sqlite_table = "fighter"
    df.to_sql(sqlite_table, sqlite_connection, if_exists='replace')
    sqlite_connection.close()

if __name__ == '__main__':
    main(df)
