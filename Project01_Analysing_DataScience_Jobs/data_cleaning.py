import pandas as pd
import data_cleaning_funtions as dc

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

## making min salary and max salary coloumns
df['min_salary'] = min_max_split[0]     
df['max_salary'] = min_max_split[1]
df['avg_salary'] = min_max_split[2]


# LOCATION FIELD
lis = df['location'].tolist()
location_list = dc.location_cleaner(lis)
df['location'] = location_list

# JOB DESCRIPTION
skill_lis = df['skills'].unique().tolist()
dc.skill_col_maker(df,skill_lis)

# COMPANY OWNERSHIP
df['Public'] = df['ownership'].apply(lambda x: 1 if "Public" == x else 0)
df['Private'] = df['ownership'].apply(lambda x: 1 if "Private" == x else 0)

# STATUS COL_SEPERATION:
status_lis = df['status'].unique().tolist()
dc.seperator(df,status_lis,"status")

# INDUSTRY SEPERATOR
industry_lis = df['industry'].unique().tolist()
dc.seperator(df,industry_lis,"industry")

# SENEORITY_LEVEL SEPERATOR
seniority_level_lis = df['seniority_level'].unique().tolist()
dc.seperator(df,seniority_level_lis,"seniority_level")

# UNWANTED COLUMNS DROPED
col_to_drop = ["company","post_date","headquarter","company_size","revenue"]
df = df.drop(columns=col_to_drop)

# LAST DROP TO NaN ROWS: 
df = df.dropna()
dc.null_info(df)

df.to_csv("salary_data_cleaned.csv", index= False)


