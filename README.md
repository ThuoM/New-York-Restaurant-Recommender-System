# **Book-Recommendation-System**

<img src="Images\book3.png" alt="books" width="750" height="400">

#### **Authors**: 
[David Mwiti](david.mwiti@student.moringaschool.com),
[Keren Amanya](karen.amanya@student.moringaschool.com),
[Mercy Moraa](mercy.onduso@student.moringaschool.com),
[Nicholus Magak](nicholus.magak@student.moringaschool.com),
[Penina Wanyama](penina.wanyama@student.moringaschool.com) and
[Stephen Thuo](stephen.thuo@student.moringaschool.com).

## Overview
****
<p>A content recommender system is a type of artificial intelligence that uses algorithms to recommend content or items to users based on their interests, preferences, and behaviours. It is commonly used by businesses to personalize user experiences and increase engagement and revenue.</p>

<p>In the context of EatOut, a content recommender system could be used to recommend eateries and hotels to users based on specific keywords and explicit feedback from other users. The system could analyse a user's browsing behaviour and past interactions with the EatOut website to provide personalized recommendations that match their preferences and needs. The system could also consider the ratings and reviews of other users who have similar interests and preferences, providing a more accurate and relevant set of recommendations.</p>
<p>The key benefit of a content recommender system is that it provides users with a more personalized and efficient way of finding relevant content, leading to increased engagement and customer loyalty. It also enables businesses to target their marketing efforts more effectively, resulting in higher revenue and profitability.</p>

## Business Problem
***
<p>EatOut is a media and food tech company that operates mainly in Kenya and East Africa. Its establishment dates to 2010, and it provides customers with the ability to browse through numerous eateries, providing crucial data like menus, contacts, maps, events, reviews, and pictures. With the advent of social media, many people rely on influencer and user-generated recommendations on platforms like Instagram and TikTok because they offer a more personalized assessment of the restaurant's ambiance, service, and food, compared to a traditional rating system. Consequently, many restaurants and hotels are using these platforms as marketing tools, which is affecting the website visits and revenue of food tech businesses such as EatOut. However, they can enhance their competitive advantage by creating a more customized feel to their website. This would help users find eateries and hotels based on criteria beyond cuisine or ratings. A content recommender system, which considers explicit feedback from other users, rather than the standard similarity-based approach, could help. With this system, users can easily find relevant recommendations based on specific keywords, thus avoiding the need to browse through countless items.</p>

## Data
***
# **Data Understanding**

The data being used on this project was object after scraping on Yelp. It is meant to be used as a mockup for how Eat Out's data could look like on the probability our recommender is accepted.

The data contained two files: 

* **_restaurants.csv_**

Contained the restaurants we desired to recommend. A few notable features in the dataset are name(of restaurant), avg_rating, pricing_range, & cuisine. Regional data we have is from New York hence there is a location field with the restaurants' individual locs.

* **_final_revs.csv_**

Contained user info from the individual restaurants. Users have identification  based on their account links. Other features include (Username, date of review, individual rating). We were also able to acquire comments from users which can be used to give restaurants more context.

                    Visualizations:
***
                 i. Ratings
 <img src="images\rating_distribution.png"  width="750" height="400"> 

                 ii. Location density of restaurants
<img src="images\restaurant_locations.png"  width="750" height="400">

                 iii. Top 10 Restaurants
 <img src="images\top_ten_most_reviewed_restaurants.png"  width="750" height="400"> 
 
                 iv. Most common words in comments
 <img src="images\common_word_chart.png"  width="750" height="400"> 
 
                 v. Sentiment analysis of the comments
 <img src="images\word_sentiment_analysis.png"  width="750" height="400"> 
 
                 vi. Most popular cuisines available
 <img src="images\most_popular_cuisines.png"  width="750" height="400"> 
  
 
## Modelling
***
The modeling of this project consists of multiple recommender system implementations:

**Content Based Recommendation:**

This uses the information on the books together with information a user will input as a search word to pull the restaurants with the highest amount of similarity to the restaurant information based on cuisine, location, price class, and similarity to comments.

**Model-based Collaborative Filtering Recommendation system:**

We will be using the matrix factorization with SVD(Singular Value Decomposition) to ensure the latent features in the dataset of the user restaurant matrix are captured to further understand how users rate the restaurants they interact with.

**Nueral Collaborative Filtering Recommendation system:**

Utilizes neural networks to model user-restaurant interactions. Learns embeddings or representations for users and restaurants in a low-dimensional space and can capture non-linear relationships.


## Evaluation
***
<p>The surprise model achieved an M.A.E of 0.8420, which is a reasonably good score. The M.A.E measures the average absolute difference between the predicted ratings and the actual ratings, so a lower M.A.E value indicates better performance.

The manual collaborative filtering model achieved an M.A.E of 1. This indicates that this model is not as effective at predicting ratings as the surprise model and fast ai neural collaborative filtering models.

The manual neural collaborative filtering model also achieved an M.A.E of 1. This suggests that it is not as effective at predicting ratings as the surprise model and fast ai neural collaborative filtering models.

The fast ai neural collaborative filtering model achieved an M.A.E of 0.31 on the training set and 0.8391 on the validation set. The low M.A.E score on the training set indicates that the model was able to fit the training data very well. The higher M.A.E score on the validation set suggests that the model was able to generalize well to new data, as it was not overfitting to the training data.

Overall, based on the performance scores provided, it seems that the fast ai neural collaborative filtering model was the best-performing model among the models evaluated. It achieved the lowest M.A.E score and was able to fit the training data well while also generalizing well to new data</p>

<table>
<tr>
<th>Model Name</th>
<th>Mean Absolute Error</th>
</tr>
<tr>
<td>surprise</td>
<td>0.8420</td>
</tr>
<tr>
<td>Traditional collaborative filtering model </td>
<td>1.000</td>
</tr>
<tr>
<td>fast ai neural collaborative filtering</td>
<td>0.310</td>
</tr>
<tr>

</table>

## Conclusion
***
<p>Based on the performance scores provided, the fast ai neural collaborative filtering model appears to be the best-performing model among those evaluated for collaborative filtering. This model achieved the lowest M.A.E score (0.310) and was able to fit the training data well while also generalizing well to new data. For very active users, we recommend combining the fast ai neural collaborative filtering model with the content-based model to build a hybrid recommender system that leverages both collaborative filtering and content-based approaches. For less active or new users, we recommend using only the content-based model to provide recommendations.</p>

## Recommendations
***
<ul>
    <li>When combining the fast ai neural collaborative filtering model with the content-based model, consider using a weighted approach that takes into account the strengths and weaknesses of each model, as well as the preferences of your users. For example, you may want to give more weight to the collaborative filtering model for users who are highly engaged with your platform, while giving more weight to the content-based model for users who are less active or new to the platform.</li>
    <li>Consider conducting A/B testing to evaluate the performance of the hybrid recommender system compared to the individual models. This can help you determine the optimal approach for providing recommendations to your users.</li>
</ul>

## For More Information
***
See the full analysis in the [Jupyter Notebook](https://github.com/ThuoM/Restaurant-Recommender-System/blob/main/Restaurant_Recommender_System.ipynb) or review this [presentation](https://github.com/FridahKimathi/Book-Recommendation-System/blob/main/Book%20Recommendation%20System.pptx.pdf).

## Repository Structure
***

```
├── Data
├── Images
├── Book Recommendation System.pptx.pdf
├── Jumia Book Recommendation System Data Report.pdf
├── README.md
└── index.ipynb