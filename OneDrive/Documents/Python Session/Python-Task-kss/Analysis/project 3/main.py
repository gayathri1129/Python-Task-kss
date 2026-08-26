import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#scenario 1
# load dataset
df = pd.read_csv(r"C:\Users\admin\OneDrive\Documents\Python Session\Python-Task-kss\Analysis\project 3\scottish_hills.csv")
print(df.head()) # frst 5 rows
df["Height"] = pd.to_numeric(df["Height"], errors='coerce')
#create region column
lat_mid = df["Latitude"].median()
lon_mid = df["Longitude"].median()
def assign_region(row):
    lat = row["Latitude"]
    lon = row["Longitude"]
    
    if lat >= lat_mid and lon >= lon_mid:
        return "North-East"
    elif lat >= lat_mid and lon < lon_mid:
        return "North-West"
    elif lat < lat_mid and lon >= lon_mid:
        return "South-East"
    else:
        return "South-West"

df["Region"] = df.apply(assign_region, axis=1)
print(df.head())
#handle missing values
df["Height"] = df["Height"].fillna(df["Height"].mean())

# Fill Region with mode
df["Region"] = df["Region"].fillna(df["Region"].mode()[0])
#output
print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())
print("--------------------------------------------------------------------")

#scenario 2
#select columns
data=df[["Hill Name","Height"]]
#frst 10 rows
data_10=data.head(10)
print(data_10)
#convert height to numpy array
height_array = np.array(data_10['Height'])
#plot line graph
plt.figure()
plt.plot(range(10), height_array, marker='o')
#add title and labels
plt.title("Height Variation of First 10 Hills")
plt.xlabel("Index (0–9)")
plt.ylabel("Height")
plt.tight_layout()
#save the graph
plt.savefig("sce1.png")
plt.show()
print("complete")

#scenario 3
# 1. Filter hills where Height > 900
tall_hills = df[df['Height'] > 900]

# 2. Count number of hills per Region
region_counts = tall_hills['Region'].value_counts()

# 3. Select top regions
top_regions = region_counts.head()

# 4. Convert results into NumPy arrays
regions_array = np.array(top_regions.index)
counts_array = np.array(top_regions.values)

# 5. Plot bar chart
plt.figure()
plt.bar(regions_array, counts_array)

# 6. Add labels and title
plt.title("Number of Tall Hills (>900m) per Region")
plt.xlabel("Region")
plt.ylabel("Count")

# Rotate x-axis labels
plt.xticks(rotation=0)
plt.tight_layout()

# Save the graph
plt.savefig("sce3.png")

# Show plot
plt.show()

#scenario 4
# 1. Count hills per Region
region_counts = df["Region"].value_counts()

# 2. Select top 5 regions
top_regions = region_counts.head(5)

# 3. Prepare labels and values
labels = top_regions.index
values = top_regions.values

# 4. Plot pie chart
plt.figure(figsize=(10, 6))
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)

# 5. Title
plt.title("Distribution of Hills by Region")
plt.tight_layout()

# Save graph
plt.savefig("region_distribution(sce4).png")

# Show plot
plt.show()

#scenario 5

#feature creation
def height_category(h):
    if h >= 1000:
        return "Very High"
    elif h >= 800:
        return "High"
    else:
        return "Moderate"

df["Height_Category"] = df["Height"].apply(height_category)

#numpy usage
height_array = np.array(df["Height"])

# Calculate differences
height_diff = np.diff(height_array)

print("\nFirst 10 Height Differences:")
print(height_diff[:10])

#visualization
#line graph
plt.figure()
plt.plot(range(len(height_array)), height_array)
plt.title("Height Trend of All Hills")
plt.xlabel("Index")
plt.ylabel("Height")
plt.tight_layout()
plt.savefig("height_trend(sce5(1)).png")
plt.show()

#bar chart
category_region = pd.crosstab(df["Region"], df["Height_Category"])

category_region.plot(kind="bar", stacked=True)
plt.title("Height Category Distribution per Region")
plt.xlabel("Region")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("height_category_stacked(sec5(2)).png")
plt.show()

#Histogram
plt.figure()
plt.hist(df["Height"], bins=10, edgecolor = 'black')
plt.title("Height Distribution")
plt.xlabel("Height")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("height_histogram(sce5(3)).png")
plt.show()

#insights
# Tallest region
tallest_region = df.groupby("Region")["Height"].mean().idxmax()

# Most common category
common_category = df["Height_Category"].value_counts().idxmax()

print("\nInsights We have Got are:")
print("Tallest Region (avg height):", tallest_region)
print("Most Common Height Category:", common_category)
'''
==============complete==============================
'''









