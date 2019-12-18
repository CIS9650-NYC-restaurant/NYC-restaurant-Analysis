**NYC restaurants Analysis**

By Group 4(Menghui Huang, Min Ah Park, Qifeng Sun, Rui Wang, Yining Yao)

*Problem Statement:*

New York City is a big metropolis which is not only known for its prosperous streets but also diversified restaurants.  There are millions of restaurants in NYC and they are regulated by Department of Health and Mental Hygiene (DOHMH). Our problem rises as how can we help our restaurant owners or future restaurant owners to achieve better grades for their restaurants. We would like to find an insight on restaurant grading based on its cuisine type and other variables such as borough, and violation code.  

*Datasets description:*

DOHMH New York City Restaurant Inspection Results 

https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/43nn-pn8j 

The above data set is obtained from NYC open data. It contains inspection results of restaurants in five boroughs in NYC from Aug 1st 2014 to present. Some major entries in this data set are Borough name, cuisine type, violation code, and grade.

NYC Rat Sightings 

https://www.kaggle.com/new-york-city/nyc-rat-sightings/download 

The above dataset is obtained from Kaggle but originally from NYC open data. It is based on 311 calls complaining about rodent sighting. The data was recorded from 2010 to Sep 16th, 2017. Some basic entries in this data set are borough name, zip code and status.

yelp_rating_grade

https://akshayvaghani.shinyapps.io/NYC_Restaurants/

The above dataset is copied from the above weblink and saved as a csv file, which can be find on this repository. The original dataset has 14,418 entries but only 5500 of them are used for this project. The dataset contains inspection scores, grade and rating for 5500 restaurants in NYC. The original data was collected and cleaned from Yelp's API and NYC open data website.

*Analysis Summary*

Restaurants selling different cuisines do have difference in their top 10 common violations. Future restaurant owners can focus on those violations based on their cusine types.

Restaurants in Bronx have highest frequency in receiving 04K/04L violations(rat sighting). However, there are much more rat sighting reports in Brooklyn.

Restaurants in Staten Island have highest percent of Grade A.

Restaurants receiving grade A have slightly higher yelp rating. 

Manhattan has most restaurants compared to other 4 boroughes. The two most restaurants are American and Chinese.

*File Directory*

Python files used to generate graphs used in presentation ppt can be find in code folder.

To understand meaning of each violation code use ri-violation-penalty.pdf file.

Datasets can be found in data folder or downloaded using given links.

Presentation slides is named as "slides final project".




