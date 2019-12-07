import pandas as pd
df=pd.read_csv("DOHMH_New_York_City_Restaurant_Inspection_Results.csv")
df = df[["CAMIS", "DBA", "BORO", "ZIPCODE", "CUISINE DESCRIPTION", "VIOLATION CODE", "VIOLATION DESCRIPTION","CRITICAL FLAG","SCORE","GRADE","INSPECTION TYPE"]]
df.columns = ["id", "name", "boro", "zipcode", "foodtype", "viocode", "viodetail","critical","score","grade","inspectype"]

def categ(x):
    if x=="Manhattan":
        return 1
    elif x=="Bronx":
        return 2
    elif x=="Brooklyn":
        return 3
    elif x=="Queens":
        return 4
    elif x=="Staten Island":
        return 5
    else:
        return 0
#def per(x):
    #return x/len(df["boro"]=")
    
df["boroindex"]=df.boro.apply(categ) #add a column of dummy variables by boro
#print(df.iloc[0][11])# df 1st row, 11th column 's value
#print(df.iloc[:,11])#df 11th column
#print(df.ix[:,11])#same as above
counts=[0,0,0,0,0]
for i in range(5):
    for n in range(len(df)-1):
        if i+1==df["boroindex"].iloc[n]:#select the 11th column
            counts[i]+=1
        else:
            continue
print(counts)#number of violation by boro
#Rat Problem
rate=[0,0,0,0,0]
ratdf=df[(df["viocode"]=="04K") | (df["viocode"]=="04L")]
#print(ratdf)
bororat=ratdf.groupby("boroindex").count()
#print(bororat)
print(bororat["viocode"])# number of rat related volation by boro


    #bororat=ratdf[ratdf["boroindex"]==i+1]
#print(rate)

    
        
        
