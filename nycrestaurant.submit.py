import pandas as pd
df=pd.read_csv("DOHMH_New_York_City_Restaurant_Inspection_Results.csv")
df = df[["CAMIS", "DBA", "BORO", "ZIPCODE", "CUISINE DESCRIPTION", "VIOLATION CODE", "VIOLATION DESCRIPTION","CRITICAL FLAG","SCORE","GRADE","INSPECTION TYPE"]]
df.columns = ["id", "name", "boro", "zipcode", "foodtype", "viocode", "viodetail","critical","score","grade","inspectype"]

#graph for common violation code by cuisine type, eg bakery
inputtype=input("Enter Cuisine Type(Capitalize first letter): ")
foodtypedf=df[df["foodtype"]==inputtype]
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns1
sns1.set(font_scale=1.4)
ax=foodtypedf['viocode'].value_counts().plot(kind='bar', figsize=(20, 6), rot=0)
plt.xlabel("Violation code", labelpad=14)
plt.ylabel("Count", labelpad=14)
plt.title(str(inputtype)+" violation code count", y=1.02,fontsize=30);
ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha="right")
plt.tight_layout()
plt.show()

#number of restaurants in a boro
restnum=df.groupby(["id"]).count()#26969 different restaurants in dataset
typebyboro=df.groupby(["boro","id"]).count()#group by boro first then group by id
#print(len(typebyboro.loc["Bronx"]))# number of restaurant in Bronx
typebyboro2=typebyboro.reset_index()# reset index from 0 to  
#print(len(typebyboro2[typebyboro2["boro"]=="Bronx"]))#number of restaurants in a boro

restbyboro=typebyboro2.groupby("boro").count()# restaurants by boro
print("Number of restaurants in a boro: "+"\n"+str(restbyboro["id"]))

#04K or 04L(rat sighting violation code) analysis and plot
ratdf=df[(df["viocode"]=="04K") | (df["viocode"]=="04L")]
bororat=ratdf.groupby("boro").count()
print("Number of 04K&04L violation in a boro: "+"\n"+str(bororat["viocode"]))# number of 04K and 04L violation by boro
viorate=bororat["viocode"]/restbyboro["id"]
vioratedf=viorate.to_frame()
import pandas as pd 
plot1=vioratedf.plot.bar(title='04K/04L violation rate',legend=False)
plot1.set_ylabel("rate")
plt.show()

# Rat Sighting analysis and plot
import pandas as pd
ratsdf=pd.read_csv("Rat_Sightings.csv")
ratsdf = ratsdf[[ "Borough"]]
ratsdf.columns = ["Boro"]
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font_scale=1.4)
axr=ratsdf['Boro'].value_counts().plot(kind='bar', figsize=(20, 6), rot=0)#figsize(width,height)
plt.xlabel("Boro", labelpad=14)
plt.ylabel("Count", labelpad=14)
plt.figtext(0.5,1,"Rat sighting count", fontsize=50, ha='center')#first number(small number=left,bigger number to the right),second number vertical postition, bigger number higher
axr.set_xticklabels(axr.get_xticklabels(), rotation=0, ha="center")#rotation is xlabel rotation degree
plt.tight_layout()
plt.show()