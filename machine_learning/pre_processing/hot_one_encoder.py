# URL : https://gist.github.com/ImUnlikely/3d7798d381f1df3b771277e8b49e0fa9

# 1. My solution
# Method 4 (integers (1 and 0))
# Method 4 from Leon
df = load_csv_to_dataframe(file_path) # Load data

ocean_proxy = pd.get_dummies(df['ocean_proximity'],drop_first=False)
df = df.drop('ocean_proximity', axis=1)
df = pd.concat([df, ocean_proxy], axis=1)

df.head()


# 2. Extreme mess but uses no libraries
# Also a mess that works (even later in the evening now, been at school for 13 hours)
column_ = []
for i in range(0,210):
    column_.append(df_org[i][7])
new_columns = []
for i in range(0,210):
    new_columns.append([])
    if column_[i] == 1:
        new_columns[i].append(1)
        new_columns[i].append(0)
        new_columns[i].append(0)
    elif column_[i] == 2:
        new_columns[i].append(0)
        new_columns[i].append(1)
        new_columns[i].append(0)
    elif column_[i] == 3:
        new_columns[i].append(0)
        new_columns[i].append(0)
        new_columns[i].append(1)
#print(new_columns)
for i in range(0,210):
    df[i].append(new_columns[i][0])
    df[i].append(new_columns[i][1])
    df[i].append(new_columns[i][2])