#!/usr/bin/env python
# coding: utf-8

# # Call Center Cleanup
# 
# For this assignment, we will be working with call center data. You can start working on the assignment after the first lesson on Exploratory Data Analysis. Make sure to read the whole assignment before starting anything! As you code along in the Jupyter notebook, you are asked to make note of the results of your analysis. Do so by clicking on the results box and adding your notes beside each question.
# 
# ## Business Issue and Understanding
# 
# You are working for a company that has two call centers: the North Call Center and the South Call Center. The company is looking to possibly hire five additional reps to enhance customer experience. Your task is to explore how efficient the current reps are in each branch to determine which branch would benefit from additional assistance.
# 
# ### How the Call Center Works
# 
# Call center representatives are assigned queues. When calls are assigned to a queue, the call is assigned to the next person in line in the queue. After a call is assigned to a representative, the amount of time between assignment and the call starting is divided into busy minutes and not ready minutes. If the call is incoming and a customer is waiting on the phone for a rep, the time is split into three categories: busy minutes, not ready minutes, and incoming call wait time. Once the rep has the customer on the phone, there might be during call wait time, where the call is put on hold while the rep gets an answer for the customer.
# 
# ### Notes about the Dataset
# 
# If you haven't worked in a call center before, these notes might help you throughout your analysis.
# 
# * The call purpose is tagged for each call.
# * The time of the call is tagged in 1 hour blocks starting at 9:00 AM and ending at 5:00 PM.
# * Calls are tagged as incoming or outgoing.
# * Reps are assigned to queues. When the reps are working, they take calls in the order of their queue.
# * A call that is dropped due to technical error or missed by the center because they have reached maximum capacity is a lost call.
# * An abandoned call is when the customer hangs up because they have been waiting for too long.
# * Busy Minutes: the amount of time after a call comes in or needs to go out where the assigned rep is not available because they are busy with other customers.
# * Not Ready Minutes: the amount of time after a call comes in or needs to go out where the assigned rep is not available because they are not ready (for example, getting water).
# * Incoming Wait Time - amount of time after assigned rep is available to take the call customer waits for representative to pick up a call. This is tracked in seconds.
# * During Call Wait Time - amount of time during call that customer has to wait for representative
# 
# ## Getting Started
# 
# You have two CSVs at your disposal, `NorthCallCenter.csv` and `SouthCallCenter.csv`. Import the appropriate libraries and create two dataframes, one called `north_df` and one called `south_df`.

# In[2]:


# Import the appropriate libraries
import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib

plt.style.use('ggplot')
from matplotlib.pyplot import figure

get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.rcParams['figure.figsize']=(12,8)




# In[3]:


# Create two new dataframes
north_df = pd.read_csv("NorthCallCenter.csv")


# In[28]:


north_df.describe()


# In[29]:


list(north_df.columns)


# In[4]:


south_df = pd.read_csv("SouthCallCenter.csv")


# In[31]:


list(south_df.columns)


# In[32]:


south_df.describe()


# In[33]:


print(north_df.shape)


# In[34]:


print(north_df.dtypes)


# In[35]:


north_df.head(10)


# In[36]:


north_df.info()


# In[37]:


print(south_df.shape)


# In[38]:


print(south_df.dtypes)


# In[39]:


south_df.head(10)


# In[40]:


south_df.info()


# ## Exploratory Data Analysis
# 
# Time to do some EDA! In the process of learning more about the two datasets, make sure you answer the following questions:
# 
# 1. How many reps are in each branch?
# 2. What is the average busy minutes, not ready minutes, incoming wait time, and during call wait time for each branch?
# 3. What is the number of calls taken for each time block?

# In[41]:


# Put your EDA code here
north_df.describe()


# In[42]:


north_df.count()


# In[43]:


south_df.count()


# In[44]:


north_df['Rep ID'].value_counts()


# In[45]:


north_df['Rep ID'].describe()


# In[46]:


north_df['Busy Minutes'].mean()


# In[47]:


north_df['Not Ready Minutes'].mean()


# In[48]:


north_df['Incoming Wait Time'].mean()


# In[49]:


north_df['During Call Wait Time'].mean()


# In[50]:


south_df['Rep ID'].value_counts()


# In[51]:


south_df['Rep ID'].describe()


# In[52]:


south_df['Busy Minutes'].mean()


# In[53]:


south_df['Not Ready Minutes'].mean()


# In[54]:


south_df['Incoming Wait Time'].mean()


# In[55]:


south_df['During Call Wait Time'].mean()


# In[56]:


north_df['Time Block'].value_counts()


# In[57]:


south_df['Time Block'].value_counts()


# In[58]:


# % of missing.
for col in north_df.columns:
    pct_missing = np.mean(north_df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))


# In[59]:


# % of missing.
for col in south_df.columns:
    pct_missing = np.mean(south_df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))


# ### EDA Results
# 
# Make note of your results here!
# 
# 1. How many reps are in each branch?
# 2. What is the average busy minutes, not ready minutes, incoming wait time, and during call wait time for each branch?
# 3. What is the number of calls taken for each time block?

# In[60]:


#1.
# North: 9 Representatives
# South: 11 Representatives

#2
# North: Busy Minutes: 9.99, Not ready minutes: 1.91, Incoming wait time: 3.05, During call wait time: 2.97
# South: Busy Minutes:10.05, Not ready minutes: 1.91 , Incoming wait time: 3 , During call wait time: 3.08

# #3 North: 
# 12:00 PM    45
# 10:00 AM    43
# 2:00 PM     35
# 3:00 PM     30
# 4:00 PM     28
# 11:00 AM    25
# 1:00 PM     17
# 5:00 PM     17
# 9:00 AM      5
    
# South: 
# 12:00 PM    75
# 10:00 AM    56
# 3:00 PM     43
# 11:00 AM    31
# 2:00 PM     30
# 5:00 PM     26
# 4:00 PM     25
# 1:00 PM     23
# 9:00 AM      5


# ## Cleaning Data
# 
# Now you need to clean up the datasets. When cleaning the datasets, you may find that there isn't dirty data to clean. That is okay! Some questions you need to answer about the data sets:
# 
# 1. Incoming wait time is null in many places. Do all of those places correspond to outgoing calls?
# 2. In the North data set, there are two separate "YES" values for a sale. Why and how did you rectify the issue?
# 3. Are there duplicates in the two data sets? If there are, how did you handle them?
# 4. Is any of the data in the two data sets unnecessary? If yes, how did you handle it?

# In[61]:


# Clean your data here

print(south_df.isnull().sum(), 'Incoming or Outgoing'  == True)


# In[62]:


print(north_df.isnull().sum(), 'Incoming or Outgoing'  == True)


# In[63]:


north_df['Incoming Wait Time'].isnull().sum()


# In[64]:


south_df['Incoming Wait Time'].value_counts()


# In[65]:


south_df['Incoming Wait Time'].isnull().sum()


# In[66]:


print(south_df.isnull().sum(), 'Incoming or Outgoing'  == True)


# In[67]:


# 2. In the North data set, there are two separate "YES" values for a sale. Why and how did you rectify the issue?
# used excel. cannot get code to properly run in jupyter


# In[68]:


# 3. Are there duplicates in the two data sets? If there are, how did you handle them?
north_df.duplicated()


# In[69]:


south_df.duplicated()


# ### Cleaning Data Results
# 
# Make note of your results!
# 
# 1. Incoming wait time is null in many places. Do all of those places correspond to outgoing calls?
# 2. In the North data set, there are two separate "YES" values for a sale. Why and how did you rectify the issue?
# 3. Are there duplicates in the two data sets? If there are, how did you handle them?
# 4. Is any of the data in the two data sets unnecessary? If yes, how did you handle it?

# In[70]:


# 1. Incoming wait time is null in many places. Do all of those places correspond to outgoing calls? Yes. Ran an excel spreadsheet
#     to see that all "incoming wait time" that is null corrlates with a setting of outgoing calls. 
# 2. In the North data set, there are two separate "YES" values for a sale. Why and how did you rectify the issue? Yes appears for sale
#  with product support and sales support. I determined this with an expel spreadsheet. 
# 3. Are there duplicates in the two data sets? If there are, how did you handle them? There are no duplicates
# 4. Is any of the data in the two data sets unnecessary? If yes, how did you handle it? I do not think any data is unnecessary 
# at this time, but if so, I would possibly use the .drop() fcn to remove the column from the data. 


# ## Data Manipulation
# 
# Before you begin answering any questions, combine the two datasets together to create a third dataframe called `df`. You can use this third dataframe to compare the two call centers to company-wide trends.
# 
# 1. Group by Rep ID and sum the resulting structure. Sort by calls to determine which rep in each branch has the highest number of calls.
# 2. The average call abandonment rate is a KPI when it comes to determining call center efficiency. As you may recall, abandoned calls are calls where the customer hangs up due to long call times. What is the average call abandonment rate for each branch and the whole company? Do any of these fall out of the optimal range of 2-5%?
# 3. Service level is another KPI when it comes to measuring call center efficiency. Service level is the percentage of calls answered within a specific number of seconds. In the case of your employer, their ideal time frame is 2 seconds. What is the percentage of calls answered within 2 seconds for each branch and the entire company?
# 4. For each branch and the entire company, what is the average speed of answer?

# In[71]:


# Manipulate data here
#  1. Group by Rep ID and sum the resulting structure. 
# Sort by calls to determine which rep in each branch has the highest number of calls.
south_df['Rep ID'].value_counts().sum()


# In[72]:


south_df.groupby(['Rep ID']).count().sort_values(by='Rep ID', ascending=False)


# In[73]:


north_df['Rep ID'].value_counts().sum()


# In[74]:


north_df.groupby(['Rep ID']).count().sort_values(by='Rep ID', ascending=False)


# In[75]:


south_df['Abandoned'].mean()


# In[76]:


north_df['Abandoned'].mean()


# In[77]:


(north_df['Abandoned'].mean()) + (south_df['Abandoned'].mean())


# In[78]:


north_df['Incoming Wait Time'].mean()


# In[79]:


north_df.groupby(['Incoming Wait Time']).count().sort_values(by='Rep ID', ascending=False)


# In[80]:


cluster_count_north=north_df.groupby(['Incoming Wait Time']).count().sort_values(by='Rep ID', ascending=False)


# In[81]:


print(cluster_count_north)


# In[82]:


south_df['Incoming Wait Time'].mean()


# In[83]:


south_df.groupby(['Incoming Wait Time']).count().sort_values(by='Rep ID', ascending=False)


# In[84]:


cluster_count_south=south_df.groupby(['Incoming Wait Time']).count().sort_values(by='Rep ID', ascending=False)


# In[85]:


print(cluster_count_north)


# In[86]:


((south_df['Incoming Wait Time'].mean()) + (north_df['Incoming Wait Time'].mean())) / 2


# In[87]:


# Data Manipulation Results
# Group by Rep ID and sum the resulting structure. Sort by calls to determine which rep in each branch has the highest number of calls.
# south: Helga, North: Brent

# The average call abandonment rate is a KPI when it comes to determining call center efficiency. As you may recall, abandoned calls are calls where the customer hangs up due to long call times. What is the average call abandonment rate for each branch and the whole company? Do any of these fall out of the optimal range of 2-5%?
# north: .02, South: .01. Both are within range.

# Service level is another KPI when it comes to measuring call center efficiency. Service level is the percentage of calls answered within a specific number of seconds. In the case of your employer, their ideal time frame is 2 seconds. What is the percentage of calls answered within 2 seconds for each company and the entire company?
##help
# For each branch and the entire company, what is the average speed of answer?
# north: 3.04, south: 3.0, collective: 3.02


# ## Visualization
# 
# Create a visualization for each of the following questions. Some of the code to handle aggregating and storing data may be written for you. For each visualization, you choose the chart style that you feel suits the situation best. Make note of the chart style you chose and why.
# 
# 1. What is the average abandonment rate per queue?
# 2. What is the service level and average speed of answer per each rep?
# 3. For each type of call purpose, how many calls are outgoing vs. incoming?

# In[12]:


# Create visualization 1 here
# The dictionary abandonment_rates has the data you need.

# sns.barplot(x =[north_df('Abandoned'), y = [north_df('Calls'))
# plt.show()
# i cannot get the graphs to run!!!
abandonment_rates = {[north_df('Abandoned')]}
queues = ["A", "B", "C", "D"]
queue_dict = north_df.groupby("Queue").agg("sum")
for i in range(1):
    abandonment_rates[queues[i]] = queue_dict["Abandoned"][i] / queue_dict["Calls"][i] 
plt.title('Abandonment Rates')
plt.xpoints = abandoment_rates
plt.ypoints = calls
plt.plot (xpoints, ypoints)
plt.show()


# In[13]:


# Create visualization 2 here
# north_plt contains the data you need for the average speed of answer of each rep
# i cannot get the graphs to run!!!

north_plt = north_df.groupby("Rep ID")["Incoming Wait Time"].mean().to_frame().reset_index()

# Finding each Rep's Personal Service Level Percentage.  Basically, Calls within 2 secs / total calls

# Table 1: Total Incoming calls less than 2 seconds grouped by Rep
quick_calls = north_df[north_df["Incoming Wait Time"] <= 2.0]
quick_reps = quick_calls[["Rep ID", "Calls"]]
quick_stats = quick_reps.groupby(["Rep ID"]).sum()  # Final Table


# Table 2: Total Incoming Calls Only grouped by Rep
total_calls_in = north_df[north_df["Incoming or Outgoing"] == "Incoming"]
rep_calls = total_calls_in[["Rep ID", "Calls"]]     
total_stats = rep_calls.groupby(["Rep ID"]).sum() # Final Table  

#  Table 3: Service Level Percentage created via merge
service_level = pd.merge(quick_stats, total_stats, on="Rep ID")

# Create Percentage Column in Table 3
service_level["Service Level %"] = service_level["Calls_x"]/service_level["Calls_y"] * 100


# In[89]:


# Create visualization 3 here
# The three dictionaries, complaints, sales_support, and product_support, have the information you need
# i cannot get the graphs to run!!!
purpose_counts = purpose_group["Incoming or Outgoing"].value_counts()
complaints = purpose_counts["Complaint"].to_dict()
sales_support = purpose_counts["Sales Support"].to_dict()
product_support = purpose_counts["Product Support"].to_dict()
x= complaints
y= sales_support
z =  product_support
plt.bar(complaints, sales_support, product_support)
plt.show


# ### Visualization Results
# 
# For each chart you created, explain why you chose the chart style you chose.

# ## Summarize Your Work
# 
# With what you know now about the two call centers and the entire company, answer the following questions. Note that while this is subjective, you should include relevant data to back up your opinion.
# 
# 1. Using KPIs such as average abandonment rate, service level and average speed of answer, in your opinion, which one of the two branches is operating more efficiently? Why?
# 2. Based on the number of reps in each branch and how quickly the reps are working, in your opinion, which branch would benefit from the extra help?
# 3. Now that you have explored the datasets, is there any data or information that you wish you had in this analysis?

# In[ ]:


# North has 9 employees, South has  11. Avg abandonment rate for South is 0.012, busy is 10.05 and in call wait is 3. 
# Avg abandoment rate for North is .02, busy is 9.98 
# in call wait 2.96. 
# North is much more effecient than south with better numbers and less employees to handle the work load.


# ## Submit Your Work
# 
# After you have completed your work on the assignment, push your work to your Github repo. Navigate to the repo, copy the link to your assignment and paste the URL in the Canvas assignment's submission box. 

# ## Bonus Mission
# 
# Create a visualization that answers this question:
# 
# 1. For each call purpose, how many calls (incoming and outgoing) take place in each time block?

# In[14]:


# Create your visualization here!
# call_times = north_df[["Time Block", "Call Purpose", "Incoming or Outgoing", "Calls"]]

# Use groupby to plot based on time blocks:
call_times.groupby('Call Purpose').get_group('Complaint').plot.bar()
# Use groupby and get_group to select which call purpose to plot:

