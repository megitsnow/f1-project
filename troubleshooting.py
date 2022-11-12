import requests 
import os

API_KEY = os.environ["NEWS_API_KEY"]

url =f'https://newsapi.org/v2/everything?q=F1 Racing&from=2022-10-30&sortBy=popularity&apiKey={API_KEY}'

response = requests.get(url)
data = response.json()
news_list = data['articles']

news_articles = []

for i in range(len(news_list)):
    article= {
    "title": data['articles'][i]['title'],
    "description": data['articles'][i]['description'],
    "url": data['articles'][i]['url'],
    "url_to_img": data['articles'][i]['urlToImage']
    }
    news_articles.append(article)

