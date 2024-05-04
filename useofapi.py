import requests
import json

news = input("Enter type of news : ")

url = f"https://newsapi.org/v2/everything?q={news}&from=2024-04-27&to=2024-04-27&sortBy=popularity&apiKey=0efb32bae75448cd94ff17c173dbb386"
response = requests.get(url)
print(response.status_code)

# print(response.text)
# print(response.json())
shuff = json.loads(response.text)
# shuff.sort(key = lambda x: x['publishedAt'], reverse = True) 
# print(shuff) 
# print("-----------------------")
# for article in response.json()['articles']:
for article in shuff['articles']:
    print(article['title'])
    # print(article['url']) 
    print()
    # print(article['urlToImage'] if article['urlToImage'] else "No Image" if article['urlToImage'] is not None else "No Image")
    print()
    print(article['description']) 
    print() 
    print(article['publishedAt']) 
    print("-----------------------")
