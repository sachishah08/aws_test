import pandas as pd
if __name__ == "__main__":
    #read your dataframe (locally)
    df = pd.read_csv('dataframe.csv')
    #compute the process you want
    shuffled_df = df.sample(frac=1)
    #print df's head in console to check it works
    print(shuffled_df.head())