#Function to save HTML locally.
def save_html(html, path):
    with open(path, 'wb') as f: #wb stands for "write bytes. Avoids encoding issues when saving"
        f.write(html)

#Function to open HTML from a local file.
def open_html(path):
    with open(path, 'rb') as f: #rb stands for "read bytes".
        return f.read()

#Make request to server.
import requests

url = 'https://www.allsides.com/media-bias/media-bias-ratings'

r = requests.get(url)
#Confirm that we have source of the page.
print(r.content[:100])

#Parse HTML
from bs4 import BeautifulSoup

soup = BeautifulSoup(r.content, 'html.parser')

rows = soup.select('tbody tr')

row = rows[0]

name = row.select_one('.source-title').text.strip()

print(name)