import requests 
from bs4 import BeautifulSoup
url = "https://www.youtube.com/"
r = requests.get(url)
# print(r.text)


soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
for heading in soup.find_all("h2"):
  print(heading.text)
url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": 'Jaimin',
    "body": 'Prajapati',
    "userId": 4464684,
  }
headers =  {
    'Content-type': 'application/json; charset=UTF-8',
  }
response = requests.post(url, headers=headers, json=data)

print(response.text)