from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://medium.com/').text

soup = BeautifulSoup(source, "lxml")

with open("medium_scrape.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["headline", "summary", "url"])

    for story in soup.find_all("div", class_="extremeHero-postContent"):
        headline = story.find("div", class_="extremeHero-titleClamp").a.h3.text
        print(headline)

        summary = story.find("div", class_="ui-summary").text
        print(summary)

        long_url = story.find("a")["href"]
        url = long_url.split("?")[0]
        print(url)

        print()

        csv_writer.writerow([headline, summary, url])

