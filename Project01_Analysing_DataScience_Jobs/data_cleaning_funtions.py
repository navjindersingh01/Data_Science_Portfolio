import ast
import pandas as pd


def col_list(dataframe):
    ''' (pandas.DataFrame) -> list of strings

    Return the list of columns of DataFrame.

    >>>col_list(df)
    ['name','id','roll']
    '''
    column_list = dataframe.columns.tolist()

    return column_list 


def max_len(list):
    ''' (list of str) -> int

    Retrun the maximum length of string in a list.

    >>>max_len(['Happy','no'])
    5
    '''
    len_list = []
    for i in range(len(list)):
       len_list.append(len(list[i]))
    
    col_len = max(len_list)

    return col_len


def null_info(dataframe,print_output = True): 
    ''' (pandas.DataFrame) -> int

    Return the total rows and null in dataframe df.

    >>>null_info(df)
    Rows with NaN: 34
    Total NaN's: 40
    '''

    cols = list(dataframe.isnull().sum().items())
    rows = max(dataframe.isnull().sum().tolist())
    count = len(dataframe)

    if print_output:
        print("\n")
        for i in range(len(cols)):
            print(f"{cols[i][0]}{' ' * (max_len(col_list(dataframe))-len(cols[i][0]))}: {cols[i][1]}")
        
        print(f"{'*' * (max_len(col_list(dataframe)) + 4)}")
        print(f"Number of Rows After removing cols are: {count}\n")
    return 


def null_remover(dataframe):
    ''' (pandas.DataFrame) -> NoneType

    Remove NaN's from DataFrame.

    defaults: dataframe = df
    
    >>>null_remover(df)
    '''

    dataframe = dataframe.dropna(axis = 0,how = 'any',ignore_index = True)

    return dataframe


def split_salary(lis):
    ''' (list of strings) -> three lists of ints

    Retrun the salary splits in 2 with converted to int.
    and list of average of both.

    precondition: list must have eliminated euro sign and comma.

    >>>split_salary(lis)
    min_list
    max_list
    '''

    min_list = []
    max_list = []
    avg_list = []

    for i in range(len(lis)):
        sum = 0

        if len(lis[i]) == 2: 
            min_list.append(int(lis[i][0]))
            max_list.append(int(lis[i][1]))

            sum += int(lis[i][0])
            sum += int(lis[i][1])
            avg_list.append(sum/2)
        else: 
            min_list.append(int(lis[i][0]))
            max_list.append(0)
            avg_list.append(int(lis[i][0]))
    


            
    return [min_list, max_list,avg_list]


def location_cleaner(lis):
    ''' (list of strings) -> list of strings

    Retrun the list in which after point part is trimmed.

    >>>location_cleaner(lis)
    lis
    '''
    location_list = []
    dot_list = []

    for i in range(len(lis)):
        try: 
            if int(lis[i].index('.')):
             dot_list.append(lis[i].index('.'))
        except:
            dot_list.append(0)

    for i in range(len(dot_list)):
        x = dot_list[i]
        if x != 0:
            location_list.append(lis[i][0:x])
        else:
            location_list.append(lis[i])

    return location_list


def skill_list(lis):
    ''' (lis) -> list of unique strings

    Return the list of stiring of a particular dataFrame.

    precondition: import ast and use ast.literal_eval method.

    >>>skill_list(lis)
    ['pandas','numpy']
    '''
    unique_skills = []

    skills_list = []
    for i in range(len(lis)):
        skills_list.append(ast.literal_eval(lis[i]))

    for i in range(len(skills_list)):
        for j in range(len(skills_list[i])):
            if skills_list[i][j] not in unique_skills:
                unique_skills.append(skills_list[i][j]) 

    return unique_skills


def skill_col_maker(dataframe,lis):
    ''' (list of skills) -> NoneType

    Make the columns of skills and fill value 1 if true or 0 otherwise.

    >>>skill_col_maker(lis)
    '''
    unique_skills = skill_list(lis)
    for i in range(len(unique_skills)):
        dataframe[unique_skills[i]] = dataframe['skills'].apply(lambda x: 1 if unique_skills[i] in x else 0)


def seperator(dataframe,lis,col_name):
    '''(pandas.DataFrame,list of string,Coloum_name) -> NoneType

    Make new coloumns of the categories of input list.

    >>>seperator(lis)
    '''
    for i in range(len(lis)):
        if pd.notna(lis[i]):
            dataframe[lis[i]] = dataframe[col_name].apply(lambda x: 1 if lis[i] == x else 0)