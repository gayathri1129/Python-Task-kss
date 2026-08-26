import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#1. scenario convert data into csv
df=pd.read_csv(r"C:\Users\admin\OneDrive\Documents\Python Session\Python-Task-kss\Analysis\project 1\railway_gauges.csv")
print(df.head()) # print frst 5 lines
print(df.isnull().sum()) # missing value
df=df.fillna(0)
print(df.head())
# convert gauge to num
gauge_columns=["Broad Gauge","Metre Gauge","Narrow Gauge","Total"]
for column in gauge_columns:
    df[column]=pd.to_numeric(df[column])
df[gauge_columns]=df[gauge_columns].fillna(0)
print(df.head())



print("cleaned data")
print("-----------------------------------------------------------------------------------------------------------------------------")

# 2. scenario

#extract year and total
year=df["Year"]
total=df["Total"]
#plot a line graph
plt.plot(year,total)
#add title and lables
plt.title("Railway Track Growth ove years")
plt.xlabel("Year")
plt.ylabel("Total Tracks")
#save the graph
plt.savefig("railway_growth_scen2.png")
plt.show()
#identify the trend
if total.iloc[-1]>total.iloc[0]:
    print("Trend increasing")
else:
    print("Trend decreasing")   



#scenario 3

#convert the year
df["Year"]=df["Year"].str[:4].astype(int)    
#filter the year
recent=df[df["Year"]>2000]
print(recent)
#select columns
gauge_columns=["Broad Gauge","Metre Gauge","Narrow Gauge","Total"]
df_gauge=recent[["Year"] + gauge_columns]
#plot bar graph
df_gauge.set_index("Year").plot(kind="bar")
#add title and lables
plt.title("Railway Gauge Expansion After 2000")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.legend(title="Gauge Type")
#save the image
plt.savefig("Railway_gauge_exp_sce3.png")
plt.show()

#scenario 4
s_total=pd.Series({"BGT":df["Broad Gauge"].sum(),
                      "MGT":df["Metre Gauge"].sum(),
                      "NGT":df["Narrow Gauge"].sum()})
#print(s_total)
plt.pie(s_total,labels=["Broad Gauge","Metre Gauge","Narrow Gauge"],
        autopct="%1.1f%%",explode=(0.1,0,0),startangle=180)
plt.title("percentage contribution")
plt.savefig("Railway_gauge_eng_sce4.png")
plt.show()
print("Broad Gauge contributes the most to the total railway network among all gauge types.")


#scenario 5
#create the new columns
df["% Broad Gauge"]=(df["Broad Gauge"]/df["Total"])*100
df["% Metre Gauge"]=(df["Metre Gauge"]/df["Total"])*100
df["% Narrow Gauge"]=(df["Narrow Gauge"]/df["Total"])*100
df["Yearly_growth"]=np.insert(np.diff(df["Total"]),0,0)
print(df["Yearly_growth"]) # cal to year growth
#plo the graphs
plt.plot(df["Year"],df["Narrow Gauge"],label="Narrow Gauge",marker="o",color="grey")
plt.plot(df["Year"],df["Metre Gauge"],label="Metre Gauge",marker="o",color="green")
plt.plot(df["Year"],df["Broad Gauge"],label="Broad Gauge",marker="o",color="blue")
plt.ylabel("Gauges")
plt.xlabel("Year")
plt.legend()
plt.savefig("sce5(1).png")
plt.show()
#highter
plt.bar(df["Year"],df["Narrow Gauge"],label="Narrow Gauge",color="grey")
plt.bar(df["Year"],df["Metre Gauge"],label="Metre Gauge",color="green",bottom=df["Narrow Gauge"])
plt.bar(df["Year"],df["Broad Gauge"],label="Broad Gauge",color="blue",bottom=df["Metre Gauge"]+df["Narrow Gauge"])
plt.ylabel("Gauges")
plt.xlabel("Year")
plt.legend()
plt.savefig("sce5(2).png")
plt.show()
year_highest_growth=df.loc[df["Yearly_growth"].idxmax(),"Year"]
print(year_highest_growth)
print("Decline years:")
print(df.loc[df["Yearly_growth"] < 0, "Year"])
#conclusion
print("Yes, the railway system is clearly shifting toward a single dominant gauge that is Broad Gauge.")





















    
