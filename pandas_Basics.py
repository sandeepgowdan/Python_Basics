#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os


# In[2]:


# Set the desired working directory
change_directory = 'C:\\Users\\windows\\OneDrive\\Desktop'

# Change the working directory
os.chdir(change_directory)

# Load the data
data = pd.read_csv("morphological2.csv")     ### Read from Excel file        df = pd.read_excel('data.xlsx')
df =data


# In[3]:


# Display first few rows
df.head()


# In[4]:


# Display the first few rows of the DataFrame
print(df.head())


# In[5]:


# Select row with index label 5
print(df.loc[5])


# In[6]:


# Select row with index position 5
print(df.iloc[5])


# In[7]:


# Using iloc accessor
fifth_column_value = df.loc[5].iloc[4]
print(fifth_column_value)


# In[8]:


# Using iloc accessor
fifth_column_value = df.loc[5].iloc[4]
print(fifth_column_value)


# In[9]:


# Display last few rows
print(df.tail())


# In[10]:


# Get summary statistics
print(df.describe())


# In[11]:


# Get shape of DataFrame
print(df.shape)


# In[12]:


# Get data types of columns
print(df.dtypes)


# In[13]:


# Check for missing values in the DataFrame
print(df.isnull())


# In[14]:


# Check for missing values in the DataFrame
print(df.isnull().sum())


# In[15]:


# Assuming 'df' is your DataFrame
null_values_rowwise = df.isnull().sum(axis=1)
print(null_values_rowwise)


# In[16]:


# Select a single column
print(df['Genotypes'])


# In[17]:


# Select a specific column by label
selected_column = df['Genotypes']
print(selected_column)


# In[18]:


# Select multiple columns
print(df[['Genotypes', 'FP', 'FPP']])


# In[19]:


# Filter rows based on a condition
filtered_df = df[df['FP'] > 2]
print(filtered_df)


# In[20]:


# Sort DataFrame by a column
sorted_df = df.sort_values(by='FP', ascending=False)
print(sorted_df)


# In[21]:


# Group by a column and calculate mean for other columns
grouped_df = df.groupby('Genotypes').mean()
print(grouped_df)


# In[22]:


# Write the modified DataFrame to a new CSV file
df.to_csv('modified_dataset.csv', index=False)


# In[23]:


# Create a new column 'Fruit length=width' by adding values from columns 'FWI' and 'FL'
df['Fruit length=width'] = df['FWI'] + df['FL']

# Display the new DataFrame with the added column
print(df)


# In[24]:


# Remove the added column 'Fruit length=width'
df.drop(columns=['Fruit length=width'], inplace=True)

# Display the modified DataFrame without the added column
print(df)


# In[25]:


# Remove rows with null values
df.dropna(inplace=True)

# Display the modified DataFrame
print(df)


# In[26]:


# Replace null values with mean of each column
df.fillna(df.mean(), inplace=True)

# Display the modified DataFrame
print(df)


# iloc: It is used for integer-location based indexing, where you specify the positions of rows and columns by their integer index. 
# For example:
# df.iloc[0:3, 1:11] selects rows 0 to 2 and columns 1 to 10 (excluding 11) based on their integer positions.
# loc: It is used for label-based indexing, where you specify the names of rows and columns. 
# 
# For example:
# df.loc[0:3, 'FP':'NF'] selects rows 0 to 3 and columns 'FP' to 'NF' (inclusive) based on their labels.

# In[28]:


# Selecting columns by integer position
selected_columns = df.iloc[:, [0, 1, 2]]  # Selects first three columns (0-based indexing)
print(selected_columns)


# In[29]:


# Selecting columns by label
selected_columns = df.loc[:, ['FWI', 'FL']]  # Selects columns by their labels
print(selected_columns)


# In[31]:


# Selecting rows by integer position
selected_rows = df.iloc[0:5, :]  # Selects first five rows
print(selected_rows)


# In[33]:


# Selecting rows by label
selected_rows = df.loc[0:4, :]  # Selects rows by their labels
print(selected_rows)


# df.iloc[0:5, :] selects rows based on their integer position, where 0:5 means from position 0 up to but not including position 5. This selects the rows with integer positions 0, 1, 2, 3, and 4.
# 
# df.loc[0:4, :] selects rows based on their labels, where 0:4 means from label 0 up to label 4 (inclusive). This selects the rows with labels 0, 1, 2, 3, and 4.

# In[37]:


# Selecting columns by integer position range
selected_columns_iloc = df.iloc[:, 0:12]  # Selects columns from position 0 to 11 (excluding 12)
# selected_columns_iloc = df.iloc[:, 1:4]  # Selects columns from position 1 to 3 (excluding 4)

print(selected_columns_iloc)


# In[40]:


#split the dataset into dependent (X) and independent (y)
# Selecting independent variables (features)
X = df.iloc[:, :-1]  # Selects all rows and all columns except the last one

# Selecting dependent variable (target)
y = df.iloc[:, -1]  # Selects all rows and the last column

# Printing X and y
print("Independent variables (X):")
print(X)
print("Dependent variable (y):")
print(y)


# In[41]:


# Selecting independent variables (features)
X = df.loc[:, :'NSF']  # Selects all rows and columns up to 'NSF' (inclusive)

# Selecting dependent variable (target)
y = df['FYPP']  # Selects the 'FYPP' column as the dependent variable

# Printing X and y
print("Independent variables (X):")
print(X)
print("\nDependent variable (y):")
print(y)


# In[42]:


# Selecting independent variables (features)
X = df.iloc[:, 0:12]  # Selects all rows and columns from index position 0 to 11 (inclusive)

# Selecting dependent variable (target)
y = df.iloc[:, -1]  # Selects all rows and the last column

# Printing X and y
print("Independent variables (X):")
print(X)
print("Dependent variable (y):")
print(y)


# In[ ]:




