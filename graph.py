import pandas as pd
import plotly.express as px

df= pd.read_csv("storage.csv")
fig=px.scatter(df,x="date",y="cases",color="country")

fig.show()

