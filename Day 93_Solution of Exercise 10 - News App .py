# Use the NewsAPI and the requests module to fetch the daily news related to different topics. Go to: https://newsapi.org/ and explore the various options to build you application

import requests

# Replace 'YOUR_API_KEY' with your actual News API key
API_KEY = "c3d163a93a1f48139aaa0750bf70bc08"

# Replace 'YOUR_KEYWORD' with the keyword you want to filter news for
a = """For Everything Enter 1
For Business Enter 2
For Tesla Enter 3
For TechCrunch Enter 4
Enter your intrest : """
KEYWORD = int(input(a))

if KEYWORD == 1:
    BASE_URL = 'https://newsapi.org/v2/everything?'

elif KEYWORD == 2:
    BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=c3d163a93a1f48139aaa0750bf70bc08'

elif KEYWORD == 3:
    BASE_URL = "https://newsapi.org/v2/everything?q=tesla&from=2023-09-14&sortBy=publishedAt&apiKey=c3d163a93a1f48139aaa0750bf70bc08"

elif KEYWORD == 4:
    BASE_URL = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=c3d163a93a1f48139aaa0750bf70bc08"

else :
    BASE_URL = None
# Set the parameters for the API request
params = {
    'q': KEYWORD,
    'apiKey': API_KEY
}

# Make the GET request to the News API
response = requests.get(BASE_URL, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Check if there are articles in the response
    if 'articles' in data:
        articles = data['articles']

        # Iterate through the articles and print the title and description
        for article in articles:
            print(f"Title: {article['title']}")
            print(f"Description: {article['description']}")
            print("\n")

    else:
        print("No articles found for the keyword.")
else:
    print(f"Error: {response.status_code}")
