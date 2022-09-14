# BitcoinPricing-Sentiment-DataPipeline

My goal for this project was to apply data engineering skills and a little bit of analytics to develop a simple ETL pipeline that extracts Bitcoin pricing and tweet data through an API and use AWS resources (EC2, S3, Redshift) to scrape the data and batch load it into a bucket then use Redshift to join data tables and finally visualize it in Tableau or any viz tool of your choice. Let me emphasize that everything is free using the AWS Free resources so anyone can get started on this.


## Requirements:

* [Binance API access](https://www.binance.com/en/binance-api)

* [Twitter API elevated access](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api)

* [An Amazon Web Services account.](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start/email) [(Please make sure to set budget alerts so you dont incur costs)](https://catalins.tech/how-to-setup-a-budget-on-aws)



## Contents:

* scraper_price.ipynb - This notebook contains the bitcoin price scraping code

* scraper_tweets.ipynb - This notebook contains the bitcoin tweets twitter scraping code

* requirements.txt - This text file contains the python packages required to successful the notebook. Make sure to have this downloaded in your local directory

* config.py - This python file contains all your secret codes, api keys and token keys

* datawrangling_code.ipynb - This notebook contains the data manipulation code



## How to run the jupyter notebooks:

* Download the files locally and run cells in saved order



## Key Project Takeaways:

* There is a clear correlation between the change in bitcoin price to daily sentiment, this is not enough to assert causation. Next steps, would be to get data from other social media sources aside from Twitter

* It may also be useful to think about each user's tweet metrics for example the amount of times the tweet was favorited, the number of followers the user has. You can use this to build an influence metric for each tweet

