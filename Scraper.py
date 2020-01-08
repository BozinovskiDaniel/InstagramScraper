### Imports
import requests
from bs4 import BeautifulSoup

###


url = 'https://www.instagram.com/'  # Website we're scraping

response = requests.get(url, timeout = 5)   # Fetching the content

content = BeautifulSoup(response.content, 'html.parser') # Parse the data and store it in a var called content


textContent = []

# Loop over 20 iterations and add the paragraps of data to the var textContent
for i in range(20):
    para = content.find_all('p')[i].text
    textContent.append(para)

    










