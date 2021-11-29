import dask

df = dask.datasets.timeseries(start='2020-01-01', end='2020-01-30', freq="3600s").compute()
# EX1
def ex1(df):
    df['X_mean'] = df.groupby('name')['x'].transform('mean')
    return df


# EX2
def sub_table(df,name):
    sub = df.loc[df['name'] == name]
    sub = sub.sort_values('x')[:10]
    return sub