#scenario 1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


#access the data csv
data = pd.read_csv(r"C:\Users\admin\OneDrive\Documents\Python Session\Python-Task-kss\Analysis\Project 2\ign.csv")
#frist 5 rows
print(data.head())
print("---------------------------------------------------------------------")
#last 5 row
print(data.tail())
print("---------------------------------------------------------------------")
#shape of data
print(data.shape)
print("---------------------------------------------------------------------")
#removing unncessary colums
data.drop(columns=['Unnamed: 0'], inplace=True, errors='ignore')
print("Removed the column Unnamed!!")
print("------------------------------------------------------------------------------")
#check missing values befor handle
missing_values = data[['score_phrase', 'genre', 'platform']].isnull().sum()
print("Total missing values before handling:\n", missing_values)
print("------------------------------------------------------------------------------")
#convert score to num
data['score_phrase'] = pd.to_numeric(data['score_phrase'], errors='coerce')
#fill num colums with means
average_score = data['score_phrase'].mean()
data['score_phrase'] = data['score_phrase'].fillna(average_score)
#fill categorical colums with mode
if not data['genre'].mode().empty:
    mode_val_genre = data['genre'].mode()[0]
    data['genre'] = data['genre'].fillna(mode_val_genre)

if not data['platform'].mode().empty:
    mode_val_platform = data['platform'].mode()[0]
    data['platform'] = data['platform'].fillna(mode_val_platform)

print("Replaced missing values correctly!!")
print("------------------------------------------------------------------------------")
#checking missing value after handle
missing_values_after = data[['score_phrase', 'genre', 'platform']].isnull().sum()
print("Total missing values AFTER handling:\n", missing_values_after)
print("------------------------------------------------------------------------------")
#Changing data types
data = data.astype({
    'score_phrase': 'float64',
    'release_year': 'int32',
    'release_month': 'int32',
    'release_day': 'int32'
})
print("Changed the type of columns into its respective types")
print("------------------------------------------------------------------------------")


#scenario 2
grouped_year = data.groupby('release_year')['score'].mean()
print("------------------------------------------------------------------------------")
#Calculating average score per year using pandas
print("The average score for respective years is: ")
print(grouped_year)
print("------------------------------------------------------------------------------")
#converting into numpy arrays
years = grouped_year.index.to_numpy()
avg_scores = grouped_year.values
print("------------------------------------------------------------------------------")
#Plotting line graph
plt.figure()
plt.plot(years,avg_scores, marker = 'o')
plt.title("Average Game Score Over Years")
plt.xlabel("release_year")
plt.ylabel("average_score")
plt.tight_layout()
plt.savefig("sce2.png")
plt.show()
print("------------------------------------------------------------------------------")

#scenario 3

# Filtering dataset where score > 7
filtered_data = data[data['score'] > 7]
print("------------------------------------------------------------------------------")
# Count number of high-rated games per platform
top_rated_games = filtered_data.groupby('platform')['title'].count()
print(top_rated_games)
print("------------------------------------------------------------------------------")
# Select top 10 platforms based on count
top_10 = top_rated_games.sort_values(ascending=False).head(10)
print(top_10)
print("------------------------------------------------------------------------------")
# Convert to NumPy arrays
platforms = top_10.index.to_numpy()
counts = top_10.values
print(platforms)
print(counts)
# Plotting bar chart
plt.figure()
plt.bar(platforms, counts)
plt.title("Top 10 Platforms by High-Rated Games")
plt.xlabel("Platform")
plt.ylabel("Number of Games")
# Rotate x-axis labels
plt.xticks(rotation=45)
plt.tight_layout()
# Save before show
plt.savefig("sce3.png")
plt.show()


#scenario 4
# Counting number of games per genre
genre_counts = data['genre'].value_counts()
print("The number of games per genre are:")
print(genre_counts)
print("------------------------------------------------------------------------------")
# Select top 5 genres
top_5 = genre_counts.head(5)
print("Top 5 genres are:")
print(top_5)
print("------------------------------------------------------------------------------")
# Prepare labels and values
genres = top_5.index.to_numpy()
counts = top_5.values
# Plot pie chart
plt.figure()
plt.pie(counts, labels=genres, autopct='%1.1f%%')
plt.title("Genre Distribution")
plt.tight_layout()
# Save before show
plt.savefig("sce4.png")
plt.show()

#scenario 5
#create a new columns for score
data['score_category'] = np.where(
    data['score'] >= 9, "Excellent",
    np.where(data['score'] >= 7, "Good", "Average")
)
print("Score category column created!")
print("------------------------------------------------------------------------------")
#convert edit choice colums
data['editors_choice'] = data['editors_choice'].map({'Y': 1, 'N': 0})
print("Converted editors_choice to numeric!")
print("------------------------------------------------------------------------------")

#Part 2: NumPy Analysis

# Average score per year (reuse or recompute safely)
yearly_avg = data.groupby('release_year')['score'].mean()
years = yearly_avg.index.to_numpy()
avg_scores = yearly_avg.values
# Calculate yearly growth using np.diff()
score_growth = np.diff(avg_scores)
print("Yearly score growth:")
print(score_growth)
print("------------------------------------------------------------------------------")

#Part 3: Visualizations

#1. Line Graph (Score Trend)
plt.figure()
plt.plot(years, avg_scores, marker='o')
plt.title("Average Score Trend Over Years")
plt.xlabel("Release Year")
plt.ylabel("Average Score")
plt.tight_layout()
plt.savefig("scroe_trend.png")
plt.show()
#bar chart
# Create pivot table
category_counts = data.pivot_table(
    index='release_year',
    columns='score_category',
    aggfunc='size',
    fill_value=0
)

category_counts.plot(kind='bar', stacked=True)

plt.title("Score Category Distribution per Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Games")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("score_category.png")
plt.show()
#histogram
plt.figure()
plt.hist(data['score'], bins=20)
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("score_distribution.png")
plt.show()

# Year with highest average score
max_year = yearly_avg.idxmax()
max_score = yearly_avg.max()

print(f"Year with highest average score: {max_year} ({max_score:.2f})")

# Check trend direction
if score_growth.mean() > 0:
    print("Overall trend: Scores are increasing over time ")
else:
    print("Overall trend: Scores are decreasing or fluctuating ")

# Editors choice vs score
editors_avg = data.groupby('editors_choice')['score'].mean()

print("\nAverage score based on editors_choice:")
print(editors_avg)

if editors_avg[1] > editors_avg[0]:
    print("Editors' Choice games generally have higher scores ")
else:
    print("Editors' Choice does not strongly correlate with higher scores ")



