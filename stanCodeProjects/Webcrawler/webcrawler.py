"""
File: webcrawler.py
Name: Yi Syuan Chung
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10905209
Female Number: 7949058
---------------------------
2000s
Male Number: 12979118
Female Number: 9210073
---------------------------
1990s
Male Number: 14146775
Female Number: 10644698
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
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #
        # tags = soup.tbody
        # male_num = female_num = 0
        # trs = tags.find_all("tr")
        # for tr in trs:
        #     tr_text = tr.text
        #     # print(tr_text)
        #     tds = tr.find_all("td")
        #     count = 0
        #     for td in tds:
        #         num_split = td.text.split(",")
        #         # print(num_split)
        #         if len(num_split) > 1:
        #             num_int = int(''.join(num_split))
        #             if count == 0:          # first num is the male num
        #                 male_num += num_int
        #             elif count == 1:        # second num is the female num
        #                 female_num += num_int
        #             count += 1
        # print("Male Number:", male_num)
        # print("Female Number:", female_num)

        # sol2
        male_amount = 0
        female_amount = 0
        tags = soup.find('table', {'class': 't-stripe'})
        # # if writing find_all(), need to loop tags despite len(tags) == 1
        year_data_list = tags.tbody.text.split()
        n = 0  # n for stop the loop
        male_index = 2  # index for get the number
        female_index = 4
        while n < 200:
            male_amount += get_num(year_data_list[male_index])
            female_amount += get_num(year_data_list[female_index])
            male_index += 5
            female_index += 5
            n += 1
        print(f'Male Number: {male_amount}')
        print(f'Female Number: {female_amount}')

        # sol3
        # male_amount = 0
        # female_amount = 0
        # # tags = soup.table
        # # if writing find_all(), need to loop tags despite len(tags) == 1
        # tags = soup.find('table', {'class': 't-stripe'}).tbody
        # print(tags.text)
        # for tag in tags:
        #     print("hehehheheheheh")
        #     print(tag.text)
        # n = 0  # n for stop the loop
        # male_index = 2  # index for get the number
        # female_index = 4
        # while n < 200:
        #     male_amount += get_num(year_data_list[male_index])
        #     female_amount += get_num(year_data_list[female_index])
        #     male_index += 5
        #     female_index += 5
        #     n += 1
        # print(f'Male Number: {male_amount}')
        # print(f'Female Number: {female_amount}')
