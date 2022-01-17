import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"

def jobs_com(link):
  result = requests.get(link)
  soup = BeautifulSoup(result.text, "html.parser")
  job = soup.find("")
  print(job)

def get_brand():
  result = requests.get(alba_url)
  soup = BeautifulSoup(result.text, "html.parser")
  brand = soup.find_all("li", {"class":"impact"})
  
  for i in brand:

    link = i.find("a")["href"]
    title = i.find("a").find("span", {"class":"company"}).get_text(strip = True)
    specialChars = "/"
    title = title.replace(specialChars, "")
    file = open(f"{title}.csv", mode="w", encoding="utf8")
    
    writer = csv.writer(file)
    writer.writerow(["place", "title", "time", "pay", "date"])
    
    result = requests.get(link)
    soup = BeautifulSoup(result.text, "html.parser")
    job = soup.find_all("tr")
    for i in job:
      try:
        place = i.find("td", {"class":"local"}).get_text(strip = True)
      
        title = i.find("td", {"class":"title"}).find("a").find("span", {"class":"title"}).string
      
        time = i.find("td", {"class":"data"}).find("span").string
      
        pay = i.find("td", {"class":"pay"}).find("span", {"class":"payIcon"}).string
        number = i.find("td", {"class":"pay"}).find("span", {"class":"number"}).string
      
        date = i.find("td", {"class":"regDate last"}).get_text(strip = True)

        writer.writerow([place, title, time, pay + number, date])
      except:
        pass
   
get_brand()