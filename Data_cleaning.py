#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import os


# In[2]:


# Set the desired working directory
change_directory = 'C:\\Users\\windows\\OneDrive\\Desktop'

# Change the working directory
os.chdir(change_directory)


# In[3]:


# Load the data
data = pd.read_csv("MaizeRILs_miss.csv")     ### Read from Excel file        df = pd.read_excel('data.xlsx')
# Create a DataFrame
df = pd.DataFrame(data)


# In[9]:


# Check if there are any missing values in the DataFrame
missing_values = df.isnull().any()

print("Are there missing values in the DataFrame?", missing_values)


# In[10]:


# Check for missing values and sum them up
missing_values = df.isnull().sum()
# Print the missing values
print("Missing Values:")
print(missing_values)


# In[12]:


# Remove rows with missing values
cleaned_df = df.dropna()
print(cleaned_df.head())


# In[13]:


# Create a new DataFrame to store the cleaned dataset
cleaned_df = df.copy()

# Impute missing values
for column in cleaned_df.columns:
    if cleaned_df[column].dtype == 'object':  # categorical columns
        cleaned_df[column].fillna(cleaned_df[column].mode()[0], inplace=True)
    else:  # numerical columns
        cleaned_df[column].fillna(cleaned_df[column].mean(), inplace=True)

# Print a message indicating the operation is complete
print("Missing values imputed and cleaned dataset saved to 'cleaned_dataset.csv'.")


# In[14]:


# View the head of the cleaned DataFrame
print(cleaned_df.head())


# In[ ]:




