import pandas as pd
df=pd.read_csv("DOHMH_New_York_City_Restaurant_Inspection_Results.csv")
df = df[["CAMIS", "DBA", "BORO", "ZIPCODE", "CUISINE DESCRIPTION", "VIOLATION CODE", "VIOLATION DESCRIPTION","CRITICAL FLAG","SCORE","GRADE","INSPECTION TYPE"]]
df.columns = ["id", "name", "boro", "zipcode", "foodtype", "viocode", "viodetail","critical","score","grade","inspectype"]



#Violation code bar plot by cuisinetype
#df = df.dropna() # drop null values
#print(df)
#print(df.info())#print data type and nulls
#print(df["VIOLATION CODE"])
#107 different violation code, 63 after taking null out
#code=df['viocode'].unique()
#print(code)
#print(len(code))
#84 different cuisine type
#cuisinetype=df['foodtype'].unique()
#print(cuisinetype)
#print(len(cuisinetype))
#bar plot
foodtypedf=df[df["foodtype"]=="Fruits/Vegetables"]
#foodtypedf2=df[df["foodtype"]=="Chinese"]
#bakecode=bakedf["viocode"]
#bakecode.plot(kind='bar')

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns1
#% matplotlib inline
sns1.set(font_scale=1.4)
ax=foodtypedf['viocode'].value_counts().plot(kind='bar', figsize=(20, 6), rot=0)#figsize(width,height)
#ax=foodtypedf2['viocode'].value_counts().plot(kind='bar', figsize=(20, 6), rot=0)#figsize(width,height)
plt.xlabel("Violation code", labelpad=14)
plt.ylabel("Count", labelpad=14)
plt.title("Fruits/Vegetables shops violation code count", y=1.02,fontsize=30);
#plt.figtext(0.5,1,"Fruits/Vegetables shops violation code count", fontsize=50, ha='center')#first number(small number=left,bigger number to the right),second number vertical postition, bigger number higher
#change the xlabel so it is crowded
ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha="right")#rotation is xlabel rotation degree
plt.tight_layout()
plt.show()

#pre-permit inspection
predf=df[(df["inspectype"]=="Pre-permit (Operational) / Initial Inspection") | (df["inspectype"]=="Pre-permit (Non-operational) / Initial Inspection")  ]
foodtypepre=predf[predf["foodtype"]=="Japanese"]#food type filter
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set(font_scale=1.4)
ax=foodtypepre['viocode'].value_counts().plot(kind='bar', figsize=(20, 6), rot=0)#figsize(width,height)
plt.xlabel("Violation code", labelpad=14)
plt.ylabel("Count", labelpad=14)
#plt.title("Bakery violation code and count", y=1.02);
plt.figtext(0.5,1,"Pre-permit(initial) violation code count for Japanese Restaurants", fontsize=40, ha='center')#first number(small number=left,bigger number to the right),second number vertical postition, bigger number higher
#plt.figtext cause problem of overlap
#change the xlabel so it is crowded
ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha="right")#rotation is xlabel rotation degree
plt.tight_layout()
plt.show()
#Boroughwise violation code
mandf=df[df["boro"]=="Manhattan"]#filter by location
print("Number of inspections in Manhattan is "+ str(len(mandf)))
manidf = mandf.groupby("id")#group by CAMIS
print("The number of restaurants in Manhattan is "+str(len(manidf)))

broodf=df[df["boro"]=="Brooklyn"]#filter by location
print("Number of inspections in Brooklyn is "+ str(len(broodf)))
brooidf = broodf.groupby("id")#group by CAMIS
print("The number of restaurants in Brooklyn is "+str(len(brooidf)))

qdf=df[df["boro"]=="Queens"]#filter by location
print("Number of inspections in Queens is "+ str(len(qdf)))
qidf = qdf.groupby("id")#group by CAMIS
print("The number of restaurants in Queens is "+str(len(qidf)))

brondf=df[df["boro"]=="Bronx"]#filter by location
print("Number of inspections in Bronx is "+ str(len(brondf)))
bronidf = brondf.groupby("id")#group by CAMIS
print("The number of restaurants in Bronx is "+str(len(bronidf)))

stdf=df[df["boro"]=="Staten Island"]#filter by location
print("Number of inspections in Staten Island is "+ str(len(stdf)))
stidf = stdf.groupby("id")#group by CAMIS
print("The number of restaurants in Staten Island is "+str(len(stidf)))

#Rat problem
#04K or #04L
ratdf=df[(df["viocode"]=="04K") | (df["viocode"]=="04L")]
#print(ratdf)
#print(len(ratdf))#31584

bronxrat=ratdf[ratdf["boro"]=="Bronx"]#filter by location
print("Number of 04K/04L violations in Bronx is "+ str(len(bronxrat)))#3429
bronxratv=len(bronxrat)/len(bronidf)
print("The rate in Bronx is "+str(bronxratv))

Manrat=ratdf[ratdf["boro"]=="Manhattan"]#filter by location
print("Number of 04K/04L violations in Manhattan is "+ str(len(Manrat)))#11647
Manratv=len(Manrat)/len(manidf)
print("The rate in Manhattan is "+str(Manratv))

qrat=ratdf[ratdf["boro"]=="Queens"]#filter by location
print("Number of 04K/04L violations in Queens is "+ str(len(qrat)))#7073
qratv=len(qrat)/len(qidf)
print("The rate in Manhattan is "+str(qratv))

broorat=ratdf[ratdf["boro"]=="Brooklyn"]#filter by location
print("Number of 04K/04L violations in Brooklyn is "+ str(len(broorat)))#8582
brooratv=len(broorat)/len(brooidf)
print("The rate in Brooklyn is "+str(brooratv))

strat=ratdf[ratdf["boro"]=="Staten Island"]#filter by location
print("Number of 04K/04L violations in Staten Island is "+ str(len(strat)))#11647
stratv=len(strat)/len(stidf)
print("The rate in Staten Island is "+str(stratv))

import pandas as pd 
# intialise data of lists. 
data = {'Boro':['Bronx','Brooklyn', 'Queens', 'Manhattan','Staten Island'], 'rate':[bronxratv,brooratv,qratv,Manratv,stratv]} 
# Create DataFrame 
ratvdf = pd.DataFrame(data) 
# Print the output. 
print(ratvdf)
ratvdf.plot.bar(x='Boro',title='04K/04L violation rate')
plt.show()

import pandas as pd
ratsdf=pd.read_csv("Rat_Sightings.csv")
ratsdf = ratsdf[[ "Borough"]]
ratsdf.columns = ["Boro"]
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#% matplotlib inline
sns.set(font_scale=1.4)
axr=ratsdf['Boro'].value_counts().plot(kind='bar', figsize=(20, 6), rot=0)#figsize(width,height)
plt.xlabel("Boro", labelpad=14)
plt.ylabel("Count", labelpad=14)
#plt.title("Rat sighting count ", y=1.02);
plt.figtext(0.5,1,"Rat sighting count", fontsize=50, ha='center')#first number(small number=left,bigger number to the right),second number vertical postition, bigger number higher
#change the xlabel so it is crowded
axr.set_xticklabels(axr.get_xticklabels(), rotation=0, ha="center")#rotation is xlabel rotation degree
plt.tight_layout()
plt.show()
#where are the most pizza shop    
qdf=df[df["boro"]=="Queens"]
cqdf=qdf[qdf["foodtype"]=="Pizza"]
print(len(cqdf))





