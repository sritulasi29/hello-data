import pandas as pd 
df=pd.read_csv("C:/Users/prasa/hello-data/data/students.csv")
num_rows=df.shape[0]
num_cols=df.shape[1]
columns=list(df.columns)
summary=f"""
STUDENT DATA INFO
-----------------
Number of rows: {num_rows}
Number of columns: {num_cols}
columns: {columns}
"""
with open("C:/Users/prasa/hello-data/output/summary.txt","w") as f:
    f.write(summary)
print(summary)