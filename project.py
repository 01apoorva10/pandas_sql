from sqlalchemy import create_engine
from pandas.io import sql
import pandas as pd
data = pd.read_csv("D:\PROJECTS\data_engineering\data_literacy_raw.csv")
print(data.head(5))
data.columns = data.columns.str.replace(' ','_')
print(data.columns)



literacy_table_one = data[['Respondent_ID', 'Wealth_Planning', 'Wealth_Action_Text',
                           'Health_Planning_Text', 'Health_Action_Text']]

literacy_table_two = data[['Respondent_ID', 'Gender',
                           'Age', 'Race', 'Education', 'Education_Group', 'Income', 'Employment',
                           'Job_Role', 'Region']]

literacy_table_three = data[['Respondent_ID', 'Wealth', 'Health', 'Civic', 'Total_Score', 'Planning',
                             'Action', 'Status']]


engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}".format(
    user="root", pw="123mysqladmin", db="datamodel"))


# literacy_table_one.to_sql(con=engine, name='literacy_table_one',
#                           if_exists='replace', chunksize=1000, index=False)


literacy_table_two.to_sql(con=engine, name='literacy_table_two',
                          if_exists='replace', chunksize=1000, index=False)

literacy_table_three.to_sql(con=engine, name='literacy_table_three',
                          if_exists='replace', chunksize=1000, index=False)
