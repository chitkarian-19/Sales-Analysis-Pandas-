import pandas as pd
data=pd.read_csv("Superstore_Sales.csv",engine="python")


data.sort_values("Sales",axis=0,ascending=False,inplace=True,na_position="last")
n_data=data[["Sales","Customer Segment"]]

f_data=n_data.drop_duplicates("Customer Segment",keep="first",inplace=False)
print(f_data)
print()
print()
p_data=data.loc[data['Customer Name'] == "Carlos Soltero"]
p_data
p_data=p_data.drop_duplicates("Customer Segment",keep="first",inplace=False)
m_data=p_data[["Sales","Customer Segment"]]
print(m_data)
