<img src=./images/beertaps.png alt='taps' width="800"/>

# Cheers! A Beer Recommendation System: A Content and Collaborative Approach

Author: Ashli Dougherty 

# Overview
This project's goal is to build a recommendation system for the beer enthusiast. I am interested in creating both a content based and collaborative filtering recommendation system. 
- A content based system will make recommendations based on a beer's features. The content based system will allow any user to enter the name of a beer and in return they will be given the names of other beers they will (hopefully) enjoy drinking.  
- The collaborative system will recommend items based on the ratings of other users. This system will compare beer reviewer profiles and then recommend beers based on predicted ratings from the similarity between these users. 

# Business Problem
As of December 2021, there are more than [9,000 breweries](https://vinepair.com/booze-news/us-record-number-breweries-2021/#:~:text=Even%20after%20the%20setbacks%20of,beer%20producers%20in%20the%20U.S.) in the US alone. Even though some taprooms were forced to shut their doors during the pandemic, the craft beer business is still going strong. The [Brewer’s Association](https://www.brewersassociation.org/statistics-and-data/national-beer-stats/) is expecting an increase in craft brewery volume share in the post-pandemic industry market, and reported that craft beer retail sales were over $26 billion dollars in 2021.    
  
Currently, there are mobile apps (like [Untapped](https://untappd.com/)) and websites (like [Beer Advocate](https://www.beeradvocate.com/)) that allow you to personally track and rate the beer you try, but consumers should know they can enjoy their next sip (or pint) with confidence. There are so many options on the market that choosing which beverage to buy next, what brewery to visit in person, or which booth to stand in line for at a festival can seem overwhelming. My goal is to provide a system for beer enthusiasts to try new beers that they are guaranteed to love. Cheers!

# Data
## Data Understanding
There are two datasets being utilized for this project.

### Tasting Profiles
The [first dataset](https://www.kaggle.com/datasets/stephenpolozoff/top-beer-information?select=beer_data_set.csv) contains data scraped from the website [BeerAdvocate.com](https://www.beeradvocate.com/). It is a CSV file that contains 5,558 beers in total across 112 styles. Other data represented in the table includes: the brewery the beer was produced, a description of the beer, and the overall rating of the beer. As there is no unique user review data, this dataset would be best for a content-based recommendation system. 

### Beer Reviews 
The [second dataset](https://www.kaggle.com/datasets/rdoume/beerreviews) is also scraped from [BeerAdvocate.com](https://www.beeradvocate.com/). It is a CSV file that contains approximately 1.6 million reviews of beers from their website. There are a total of 33,388 unique reviewers and 56,857 unique beers that have been reviewed. There are no descriptions of the beers, just names, brewery, style, and ratings on a scale of 1 - 5. Because this data set has both unique users and beer IDs it lends itself to be a user to user collaborative filtering system.   

Due to the large size of these datasets I downloaded them locally and saved to an external repository outside of github.

## Data Preparation 
All data cleaning can be found in the [DataPrep Notebook](./DataPrep.ipynb). For use in other notebooks the cleaned dataframes are saved to separate CSV files. Due to file size these files are saved and accessed locally and were not pushed to github.

### Content Based
For the tasting profiles dataset I cleaned using built in pandas methods and functions. Duplicates, entries that were missing descriptions, beers with ABVs above 15% were dropped from the dataset as part of the cleaning process. Styles were binned from 112 unique types to the main 17 from the BeerAdvocate website. Some beers initially had the same name, but are from different breweries. In order to preserve these entries I added the name of the brewry in front of the beers that had these generic names.

Below are the types of beers represented in the dataset and the range of ratings.
<img src=./images/contentgraphs.png alt='contentdata' width="800"/>
35% of all beers have a rating of 4.0 or higher. This was about the percent I expected for highly rated beers. 

In addition to the cleaned tasting profiles csv a separate csv was created with just the beer_ids and descriptions for text preprocessing. 

### Collaborative Filtering 
The reviews dataset was also cleaned using built in pandas methods. Duplicates, entries with missing values, beers with ABVs above 15% were dropped from the dataset as part of the cleaning process. Styles were binned from 104 unique types to the main 17 from the BeerAdvocate website. As this data set is being used to provide user to user recommendations only established reviewers (that have 5 or more reviews) were kept and all others were dropped. I also replaced each username with a unique userID number.  

Below are the types of beers represented in the dataset and the range of ratings.
<img src=./images/collabgraphs.png alt='collabdata' width="800"/>
More than 57% of all beers have a rating of 4.0 or higher. This was a higher number than expected, especially when compared to the other dataset. 

# Methods & Models
## Content Based
<img src=./images/content.png alt='content' width="350" align='center'/>
Content-based systems use item features to recommend other items similar to what the user likes, based on their previous actions or explicit feedback. Anyone can use this recommendation system without making any prior reviews, they only need to know the name of a beer they already like. Description text was cleaned using Texthero, vectorized with sklearn's TF-IDF vectorizer and combined with a dataframe containing dummied styles and scaled tasting profiles. Recommendations are determined based on distance metrics and the best recommendations returned were made using cosine similarity. As expected the returned beers are within the same general style. Displayed below are examples of returned recommendations. 
<img src=./images/shiner_recs.png alt='shiner' width="600"/>
<img src=./images/sierra_recs.png alt='shiner' width="600"/>

For a more indepth look at my code and other recommendations you can explore my [Content Based Notebook](./ContentBasedRecs.ipynb) or use the system for yourself as a [streamlit app](https://ashlidougherty-beer-recommender-app-ykyxz6.streamlitapp.com/).

## Collaborative Filtering 
<img src=./images/collab.png alt='collab' width="600" align='center'/>
Collaborative filtering uses similarities between users and items simultaneously to provide recommendations. For a user-based system (which is what this one is), an item’s recommendation score for a user is calculated depending on that items’ rating by other similar users. Using the Surprise library, I iterated through several models and retrieved recommendations for several different users before settling on a final model using NMF_GS. As seen below most models (even after being gridsearched) had roughly the same root mean squared error (RMSE) of 0.59.
<img src=./images/model_eval.png alt='model_eval' width="600"/>

To use this system, a user puts in their unique reviewerID, the number recommendations they want, and the top estimated rated beers are returned. Unlike the content-based system, the recommendations returned contained more diverse styles. Displayed below are examples of returned recommendations.  
<img src=./images/user1.png alt='user1' width="600"/>
<img src=./images/user1.png alt='user2' width="600"/>

For a more indepth look at my code and other recommendations you can explore my [Collaborative Filtering Notebook](./CollabFiltering.ipynb)

# Conclusions



# Next Steps


## Repository Structure 
```
├── [Data]
│    ├── df_dtm.parquet
│    ├── df_user.csv
│    ├── meta5.csv
│    ├── meta_all.csv
├── [Images]
├── [Model]
├── .gitignore
├── CollaborativeFiltering.ipynb
├── ContentBased.ipynb
├── DataPrepFinal.ipynb
├── LICENSE
├── Presentation.pdf
├── Procfile
├── README.md
├── app.py
├── environment.yml
├── requirements.txt
└── setup.sh
```