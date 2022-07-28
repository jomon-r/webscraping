from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
def get_url_flipkart(search_term):    
    template = 'https://www.flipkart.com/search?q={}&as-show=on&as=off'
    search_term = search_term.replace(' ','+')
    url = template.format(search_term)
    return url
def main(search):
  url= get_url_flipkart(search)
  record=[]
  rest=requests.get(url)
  soup=BeautifulSoup(rest.text,'html',features="html.parser")
  results = soup.find_all('div', {'class': '_13oc-S'})
  for item in results:
    description= item.find('a',{'class':'s1Q9rs'}).text
    price = item.find('div',{'class':'_30jeq3'}).text
    price = price.replace('₹','Rs ')
    rating1 =  item.find('div',{'class':'_3LWZlK'}).text
    rating = rating1 + ' out of 5 stars'
    atag = item.find('a')['href']
    url = 'http://www.flipkart.com' + atag
    result = (description,price,rating,url)
    record.append(result)
    with open('demo.csv','w',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Description','Price','Rating','URL'])
        for item in record:
          writer.writerow(item)
  data = pd.read_csv("demo.csv")
  return data

main('Extention cable')