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
    
#rating vs. grade
gdf=df.groupby("grade").mean()
print(gdf['rating'])
from matplotlib import pyplot as plt
plt.style.use('seaborn')

plt.bar(["A","B","C"],gdf['rating'])
plt.show()


#rating vs. Score
df["boroindex"]=df.boro.apply(categ)



colors=df["boroindex"]#size of point
boros=("MANHATTAN","BRONX","BROOKLYN","QUEENS","STATEN ISLAND")
color=("red","green","blue","yellow","purple")
plt.scatter(df['rating'],df['score'],s=5, c=colors,cmap='summer',label=boros)#s is the point size, c is color of point
#marker is the data label as"x",edgecolor=outline color of the cicle,or marker; alpha soften the color, linewidth is the outline width
#cbar=plt.colorbar()
#cbar.set_label('Rating')
#plt.xscale('log')#log scale of x axis
#plt.yscale('log')
plt.title('Inspection score vs. Rating',fontsize=30)
#plt.figtext(0.5,1,'Inspection score vs. Rating',fontsize=40,ha='center')
plt.xlabel("Rating",fontsize=20)
plt.ylabel("Inspection score",fontsize=20)
#plt.legend()
plt.show()

#Grade by boro

pd.crosstab(df.boro, df.grade).plot(kind="bar", stacked=True)
plt.title('Grade Distribution by Borough (yelp data)', fontsize = 15)
borodf=df.groupby("boro")

pd.crosstab(df.cuisine, df.grade).plot(kind="bar", stacked=True)
plt.title('Grade Distribution by cuisine type (yelp data)', fontsize = 15)

pd.crosstab(df.cuisine, df.boro).plot(kind="bar", stacked=True,)
plt.title('Cuisine types in different boroughs (yelp data)', fontsize = 15)