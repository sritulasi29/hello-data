import pandas as pd


def load_data(path):

    return pd.read_csv(path)


def generate_data(df):
    num_rows=df.shape[0]
    num_cols=df.shape[1]
    mean=df[["math","science","english"]].mean()
    columns=list(df.columns)

    return f"""
    STUDENT DATA INFO
    -----------------
    Number of rows: {num_rows}
    Number of columns: {num_cols}
    columns: {columns}
    Mean of subjects: 
    {mean}"""


def save_summary(text,path):
    with open(path,"w") as f:
        f.write(text)
    

def main():
    df=load_data("C:/Users/prasa/hello-data/data/students.csv")
    summary=generate_data(df)
    save_summary(summary,"C:/Users/prasa/hello-data/output/summary.txt")
    print(summary)


if __name__=="__main__":
    main()