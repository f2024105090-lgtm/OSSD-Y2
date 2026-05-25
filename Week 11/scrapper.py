import requests
from bs4 import BeautifulSoup
import csv

def scrapper(car):
    url = f'https://www.pakwheels.com/new-cars/pricelist/{car}'
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    data = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.find_all('table')

        for table in tables:
            rows = table.find_all('tr')

            for row in rows:
                cols = row.find_all('td')

                if len(cols) >= 2:
                    name = cols[0].get_text(strip=True)
                    price = cols[1].get_text(strip=True)
                    print(f"Name: {name}, Price: {price}")
                    data.append([name, price])

    return data

def save_to_file(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Car Name", "Price"])
        writer.writerows(data)

car = input("Enter name: ")
data = scrapper(car)
save_to_file(data, "cars.csv")