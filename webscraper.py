# Using Python web scraper to get the minimum rent price on Avalon apartment website.
# Copyright (C) 2019  Shanglin Guo

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from bs4 import BeautifulSoup
import requests
import json
import time

url = 'https://www.avaloncommunities.com/massachusetts/framingham-apartments/avalon-framingham'
current_least_price = 2110

def get_least_price(url):
    response = requests.get(url, timeout=5)
    content = BeautifulSoup(response.content, "html.parser")
    containers = []
    for container in content.findAll('div', attrs={"class": "container"}):
        containers.append(container)
    
    least_price_text = containers[7].find('div', attrs={"class": "row"})\
                        .find('div', attrs={"class": "col-lg-12"})\
                        .find('div', attrs={"class": "content"})\
                        .find('div', attrs={"class": "pricing"}).text
    
    price = least_price_text[least_price_text.index("$")+1:]

    price_int = int("".join(price.split(",")))

    return price_int

print("running...")
while 1:
    current_price = get_least_price(url)
    time.sleep(5)

    if current_price != current_least_price:
        print("The least price has changed! Current least price: %s" % current_price)
        break