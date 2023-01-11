import pandas as pd

df = pd.read_csv("output.csv",encoding_errors="ignore",low_memory=False)

df["channel_title"].fillna("None",inplace=True)
df["tags"].fillna("None",inplace=True)
x = df["video_error_or_removed"].mode()[0]
df["video_error_or_removed"].fillna(x,inplace=True)
df["description"].fillna("None",inplace=True)

df.to_csv(path_or_buf="clean_output.csv",index=False,mode ="w")
