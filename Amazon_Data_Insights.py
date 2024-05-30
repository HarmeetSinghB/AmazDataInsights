import numpy as np
import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt

# READING THE CSV FILE AND CLEANING IT

df = pd.read_csv('C:/Users/rajya/OneDrive/Desktop/1024_Final Assignment/DATA/data.csv')


df = df.drop_duplicates()
df = df.dropna()

Index_def = df[df['Personalized_Recommendation_Frequency']=='Sometimes'].index
df = df.drop(Index_def)

Index_def_2 = df[df['Add_to_Cart_Browsing']=='Maybe'].index
df = df.drop(Index_def_2)

Index_def_3 = df[df['Cart_Completion_Frequency']=='Sometimes'].index
df = df.drop(Index_def_3)

Index_def_4 = df[df['Saveforlater_Frequency']=='Sometimes'].index
df = df.drop(Index_def_4)

Index_def_5 = df[df['Review_Helpfulness']=='Sometimes'].index
df = df.drop(Index_def_5)

Index_def_6 = df[df['Recommendation_Helpfulness']=='Sometimes'].index
df = df.drop(Index_def_6)

Index_def_7 = df[df['Service_Appreciation']=='.'].index
df = df.drop(Index_def_7)

Index_def_8 = df[df['Improvement_Areas']=='.'].index
df = df.drop(Index_def_8)

Index_def_9 = df[df['Improvement_Areas']=='Nil'].index
df = df.drop(Index_def_9)

# df.to_csv('C:/Users/rajya/OneDrive/Desktop/1024_Final Assignment/DATA/df_cleaned.csv') ---- To download the cleaned dataset



# CODE TO CREATE THE PIE CHART WHICH SHOWS THE FACTORS OF CART ABANDONMENT WITH THEIR PERCENTAGES

df2 = pd.DataFrame(df.query("Add_to_Cart_Browsing=='Yes'")["Cart_Completion_Frequency"])
#print(df2.head())
a = df2['Cart_Completion_Frequency'].value_counts()
#print(a)
col_to_list = df2.Cart_Completion_Frequency.unique().tolist()
#print(col_to_list)
labels = ["Often", "Always", "Rarely"]
fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(a, labels= labels, autopct='%.1f%%')
ax.set_title('Cart Completion frequency after Add_To_Cart Browsing')
plt.tight_layout()
plt.show()

df3 = pd.DataFrame(df.query("Cart_Completion_Frequency=='Often'" or "Cart_Completion_Frequency=='Rarely'")["Cart_Abandonment_Factors"])
b = df3['Cart_Abandonment_Factors'].value_counts()
#print(b)
col_to_list_2 = df3.Cart_Abandonment_Factors.unique().tolist()
#print(col_to_list)
labels_2 = ["Found a better price elsewhere", "Changed my mind or no longer need the item ", "High shipping costs "]
fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(b, labels= labels_2, autopct='%.1f%%')
ax.set_title('Cart Abandonment Factors of customers whose Cart Completion Frequency is "Often" or "Rarely" ')
plt.tight_layout()
plt.show()


# CODE TO CREATE THE PIE CHART FOR KNOWING THE IMPROVEMENT AREAS SUGGESTED BY HEAVILY OR MODERATLY RELIABLE CUSTOMERS

df4 = pd.DataFrame(df.query("Review_Reliability=='Heavily'" or "Review_Reliability=='Moderately'")["Improvement_Areas"])
#print(df4)
c = df4['Improvement_Areas'].value_counts()
#print(c)
col_to_list_3 = df4.Improvement_Areas.unique().tolist()
#print(col_to_list)
labels_3 = ['Product quality and accuracy', 'Reducing packaging waste', 'Customer service responsiveness', 'Shipping speed and reliability']
fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(c, labels= labels_3, autopct='%.1f%%')
ax.set_title('Improvement Areas provided by the customers on whom "Heavily" or "Moderately" reliable')
plt.tight_layout()
plt.show()


# CODE TO CREATE A SCATTER PLOT - PURCHASE FREQUENCY VS AGE

plt.figure(figsize=(10, 6))
plt.scatter(df['age'], df['Purchase_Frequency'], alpha=0.5)
plt.title('Purchase Frequency vs Age')
plt.xlabel('Age')
plt.ylabel('Purchase Frequency')
plt.grid(True)
plt.show()


# CODE TO CREATE BAR GRAPH OF PURCHASE CATEGORIES DISTRIBUTION

purchase_counts = df['Purchase_Categories'].value_counts()
plt.figure(figsize=(10, 6))
plt.bar(purchase_counts.index, purchase_counts.values)
plt.title('Purchase Categories Distribution')
plt.xlabel('Purchase Categories')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.show()


# CODE TO CREATE BAR PLOT OF AVERAGE SHOPPING SATISFACTION VS GENDER

gender_satisfaction = df.groupby('Gender')['Shopping_Satisfaction'].mean()
print("\nAverage Shopping Satisfaction by Gender:\n", gender_satisfaction)
plt.figure(figsize=(8, 6))
sns.barplot(x=gender_satisfaction.index, y=gender_satisfaction.values)
plt.title('Average Shopping Satisfaction by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Shopping Satisfaction')
plt.show()
