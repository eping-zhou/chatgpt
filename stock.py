import requests
import pandas as pd

url = 'https://www.realestate.com.au/buy/in-new+south+wales/list-1'
response = requests.get(url)
html_content = response.content



