import pandas as pd
import data_cleaning_functions as dc

df = pd.read_csv("data.csv")

# removing the nulls from data
dc.null_remover(df)

# remove other jobs beside data scientist

df = df[df['job_title'] == 'data scientist']

# SALARY PARSING 

## Reomoving € sign from salary
df['salary'] = df['salary'].apply(lambda x: x.replace("€","").replace(',',''))

## Spliting the Salary in Min and Max coloumns
lis = df['salary'].apply(lambda x: x.split("-")).tolist()
min_max_split = dc.split_salary(lis)

## making average salary coloumn
df['avg_salary'] = min_max_split[2]


# LOCATION FIELD
lis = df['location'].tolist()
location_list = dc.location_cleaner(lis)
df['location'] = location_list

# JOB DESCRIPTION
skill_lis = ['python','machine learning','sql','r','aws','deep learning']
dc.skill_col_maker(df,skill_lis)

# UNWANTED COLUMNS DROPED
col_to_drop = ["company","post_date","headquarter","company_size","revenue"]
df = df.drop(columns=col_to_drop)

# LAST DROP TO NaN ROWS: 
df = df.dropna()
df.loc[316,'avg_salary'] = float(df.loc[316,'avg_salary'] // 10)
dc.null_info(df)

df.to_csv("salary_data_cleaned.csv", index= False)


