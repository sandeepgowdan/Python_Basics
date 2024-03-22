#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Set matplotlib to display plots inline
get_ipython().run_line_magic('matplotlib', 'inline')
# Set seaborn style
sns.set(style="whitegrid")
import os


# In[6]:


# Set the desired working directory
change_directory = 'C:\\Users\\windows\\OneDrive\\Desktop'

# Change the working directory
os.chdir(change_directory)


# In[7]:


# Load the data
data = pd.read_csv("morphological.csv")


# In[8]:


data.head()


# In[9]:


data.corr()


# In[10]:


sns.heatmap(data.corr())


# In[ ]:


# Box plot with colors based on "Genotypes"
sns.boxplot(data=data, x="PH", y="Genotypes", palette="Set2")
plt.title("Box Plot of PH Distribution with Colors by Genotypes")
plt.show()


# In[11]:


# box plot 
sns.boxplot(data=data.drop(columns="Genotypes"), orient="h")
plt.title("Box Plot of Numeric Variables")
plt.show()


# In[15]:


# Compute the correlation matrix
correlation_matrix = data.corr()

# Heatmap with colors indicating correlation strength
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", annot_kws={"size": 6})
plt.title("Correlation Heatmap")
plt.show()


# In[19]:


# Bar plot for a categorical variable
sns.barplot(data=data, y='Genotypes', x='FYPP')
plt.title("Bar Plot of FYPP across Genotypes")
plt.xlabel("FYPP")
plt.ylabel("Genotypes")
plt.show()


# In[17]:


# Histogram for a numerical variable
sns.histplot(data=data, x='FYPP', bins=10, kde=True)
plt.title("Histogram of FYPP")
plt.show()


# In[31]:


sns.swarmplot(data=data, y='Genotypes', x='FYPP', palette='viridis')
plt.title("Swarm Plot of FYPP across Genotypes")
plt.show()


# In[24]:


sns.jointplot(data=data, x='FWI', y='FEW', kind='scatter')
plt.title("Joint Plot of FWI vs. FEW")
plt.show()


# In[28]:


sns.stripplot(data=data, y='Genotypes', x='FYPP', jitter=True, palette='rainbow')
plt.title("Strip Plot of FYPP across Genotypes")
plt.show()


# In[34]:


sns.pointplot(data=data, x='FYPP',  y='Genotypes',ci='sd', palette='magma')
plt.title("Point Plot of FYPP across Genotypes")
plt.show()


# In[35]:


sns.lmplot(data=data, x='FWI', y='FEW', hue='Genotypes', palette='Set1')
plt.title("LM Plot of FWI vs. FEW with Genotypes")
plt.show()


# In[41]:


# Using sns.regplot()
sns.regplot(data=data, x='FWI', y='FEW')
plt.title("Regression Plot of FWI vs. FEW")
plt.xlabel("FWI")
plt.ylabel("FEW")
plt.show()


# In[42]:


# Using sns.lmplot() (if you want to include hue for different genotypes)
sns.lmplot(data=data, x='FWI', y='FEW', hue='Genotypes')
plt.title("Regression Plot of FWI vs. FEW with Genotypes")
plt.xlabel("FWI")
plt.ylabel("FEW")
plt.show()


# In[45]:


sns.pointplot(data=data, y='Genotypes', x='FYPP')
plt.title("Point Plot of FYPP across Genotypes")
plt.xlabel("Genotypes")
plt.ylabel("FYPP")
plt.show()


# In[48]:


# Drop 'Genotypes' column
data_no_genotypes = data.drop(columns=['Genotypes'])

# Plot histograms for each column
plt.figure(figsize=(15, 10))
for i, column in enumerate(data_no_genotypes.columns):
    plt.subplot(4, 4, i + 1)
    sns.histplot(data_no_genotypes[column], kde=True, color='skyblue')
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()


# In[54]:


# Drop 'Genotypes' column
data_no_genotypes = data.drop(columns=['Genotypes'])

# Define a color palette with different colors
colors = sns.color_palette("husl", len(data_no_genotypes.columns))

# Plot box plots for each column with different colors
plt.figure(figsize=(15, 10))
for i, column in enumerate(data_no_genotypes.columns):
    plt.subplot(4, 4, i + 1)
    sns.boxplot(y=data_no_genotypes[column], color=colors[i])
    plt.title(f'Box Plot of {column}')
    plt.ylabel(column)

plt.tight_layout()
plt.show()


# In[68]:


# Define a color palette with different colors
colors = sns.color_palette("husl", len(data_no_genotypes.columns))

# Plot box plots for each column with different colors and fancy box styles
plt.figure(figsize=(15, 10))
for i, column in enumerate(data_no_genotypes.columns):
    plt.subplot(4, 4, i + 1)
    sns.boxplot(y=data_no_genotypes[column], color=colors[i], 
                boxprops=dict(facecolor='lightblue', edgecolor='black', linewidth=2),  # Change box fill color and edge properties
                whiskerprops=dict(color='black', linewidth=2),  # Change whisker properties
                medianprops=dict(color='red', linewidth=2),  # Change median line properties
                capprops=dict(color='black', linewidth=2),  # Change caps (whisker ends) properties
                flierprops=dict(marker='o', markersize=8, markerfacecolor='yellow', markeredgecolor='black'))  # Change outlier properties
    plt.title(f'Box Plot of {column}', fontsize=12, fontweight='bold')  # Add title with custom fontsize and fontweight
    plt.ylabel(column, fontsize=10)  # Customize y-axis label fontsize

plt.tight_layout()
plt.show()


# In[60]:


# Define a color palette with different colors
colors = sns.color_palette("husl", len(data['Genotypes'].unique()))

# Regression plots for each pair of variables with colors
sns.set(style="ticks")
sns.pairplot(data, hue='Genotypes', palette=colors)
plt.show()


# In[29]:



# Drop the 'Genotypes' column
data_without_genotypes = data.drop(columns=['Genotypes'])

# Colorful pair plot without 'Genotypes' column
sns.pairplot(data=data_without_genotypes, palette='husl')
plt.title("Pair Plot without Genotypes")
plt.show()


# In[ ]:




