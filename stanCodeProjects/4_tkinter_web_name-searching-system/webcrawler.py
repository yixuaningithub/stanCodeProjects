"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)
        tags = soup.tbody
        # ----- Write your code below this line ----- #
        male_num = female_num = 0                           # to count the total number of the male and female number
        trs = tags.find_all("tr")                        # get the source in the tr
        for tr in trs:
            tds = tr.find_all("td")                     # get the source in the td
            count = 0                                   # for determine whether is the male num or the female num
            for td in tds:
                num_split = td.text.split(",")          # separate the text into str
                if len(num_split) > 1:
                    num_int = int(num_split[0]) * 1000 + int(num_split[1])  # ex: 12,345 to 12*1000+345
                    if count == 0:                      # first number is the male number
                        male_num += num_int
                    elif count == 1:                    # second number is the female number
                        female_num += num_int
                    count += 1
        print("Male Number:", male_num)
        print("Female Number:", female_num)


if __name__ == '__main__':
    main()
