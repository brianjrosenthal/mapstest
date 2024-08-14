import requests

url = 'https://docs.google.com/spreadsheets/d/jHHcQf17lQUyoTTCuFFZyBGig9hkQnG90JaCoct4/gviz/tq?tqx=out:csv&sheet=Access_to_electricity'

response = requests.get(url)
content = response.content.decode('utf-8')
import csv
from pprint import pprint
from io import StringIO
f = StringIO(content)
reader = csv.reader(f, delimiter = ',')
for row in reader:
  pprint(row)
