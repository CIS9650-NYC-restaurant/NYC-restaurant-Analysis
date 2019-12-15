import pandas as pd
df=pd.read_csv("yelp_rating_grade.csv")

def categ(x):
    if x=="MANHATTAN":
        return "red"
    elif x=="BRONX":
        return "green"
    elif x=="BROOKLYN":
        return "yellow"
    elif x=="QUEENS":
        return "blue"
    elif x=="STATEN ISLAND":
        return "purple"
    else:
        return 0

#Number of restaurants in yelp data
count1=df["camis"].unique()
print(len(count1))

#Average rating vs. grade
gdf=df.groupby("grade").mean()
print(gdf['rating'])#average rating for corresponding grade
from matplotlib import pyplot as plt
plt.style.use('seaborn')
plt.bar(["A","B","C"],gdf['rating'])
plt.show()

#rating vs. Score plot
df["boroindex"]=df.boro.apply(categ)
colors=df["boroindex"]
boros=("MANHATTAN","BRONX","BROOKLYN","QUEENS","STATEN ISLAND")
plt.scatter(df['rating'],df['score'],s=5, c=colors,cmap='summer',label=boros)#s is the point size, c is color of point
#marker is the data label as"x",edgecolor=outline color of the cicle,or marker; alpha soften the color, linewidth is the outline width
plt.title('Inspection score vs. Rating',fontsize=30)
plt.xlabel("Rating",fontsize=20)
plt.ylabel("Inspection score",fontsize=20)
plt.show()

#Grade distribution in boros
pd.crosstab(df.boro, df.grade).plot(kind="bar", stacked=True)
plt.title('Grade Distribution by Borough (yelp data)', fontsize = 15)
borodf=df.groupby("boro")

#Grade for different cuisine types
pd.crosstab(df.cuisine, df.grade).plot(kind="bar", stacked=True)
plt.title('Grade Distribution by cuisine type (yelp data)', fontsize = 15)

#Cuisin type count in different boros
pd.crosstab(df.cuisine, df.boro).plot(kind="bar", stacked=True,)
plt.title('Cuisine types in different boroughs (yelp data)', fontsize = 15)