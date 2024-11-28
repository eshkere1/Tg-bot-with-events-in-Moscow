import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import datetime
import os


def get_name_url_events(url, response):
    name_events = []
    url_events = []
    soup = BeautifulSoup(response.text, "lxml")
    tags_name_events = soup.find_all("a", class_="CjnHd y8A5E L_ilg Q8u7A R1IVp nFaMY")

    for tag in tags_name_events:
        if (
            tag["href"] != "/selection/"
            and tag["href"]
            != "/msk/restaurants/?utm_campaign=headline&utm_medium=referral&utm_source=afisha"
        ):
            url_events.append(urljoin(url, tag["href"]))
            name_events.append(tag.text)

    return url_events[0:5], name_events[0:5]


def get_data_events(url, url_site):
    url_events = []
    price_events = []
    name_events = []
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")
    card_events = soup.find_all("div", class_="oP17O")

    for card in card_events:
        try:
            element_url = card.find("div", class_="QsWic rIUFv").find(
                "a", class_="CjnHd y8A5E Vrui1"
            )["href"]
            url_event = urljoin(url_site, element_url)
            url_events.append(url_event)

            element_name = (
                card.find("div", class_="QWR1k")
                .find("a", class_="CjnHd y8A5E nbCNS yknrM")
            )
            name_events.append(element_name.text)

            element_price = card.find("div", class_="MckHJ").find("a", class_="CjnHd y8A5E L_ilg tCbLK faVCW ScoTh")
            price_events.append(element_price.text)
        except AttributeError:
            price_events.append('Билетов нет')

    return url_events, price_events, name_events


def get_date_urls(urls, url_site):
    date_urls = []
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "lxml")

            card_all_events = soup.find(
                "a", class_="CjnHd y8A5E L_ilg k27zi faVCW ookR3 Qc4zI"
            )["href"]
            date_url = urljoin(url_site, card_all_events)
            date_urls.append(date_url)
        except TypeError:
            date_urls.append(url)
    return date_urls


def get_all_data_urls(data_url):
    all_data_urls = []
    months = [
        "yanvarya",
        "fevralya",
        "marta",
        "aprelya",
        "maya",
        "iyunya",
        "iyulya",
        "avgusta",
        "sentyabrya",
        "oktyabrya",
        "noyabrya",
        "dekabrya",
    ]
    today = datetime.date.today()
    tommorow = today + datetime.timedelta(days=1)
    for month in range(tommorow.month, 13):
        for day in range(1, 32):
            try:
                datetime.date(day=day, month=month, year=tommorow.year)
                if len(str(day)) == 1:
                    date = f"0{day}-{months[month-1]}"
                    url = urljoin(data_url, date)
                    all_data_urls.append(url)
                else:
                    date = f"{day}-{months[month-1]}"
                    url = urljoin(data_url, date)
                    all_data_urls.append(url)
            except ValueError:
                continue
        
    return all_data_urls


def main():
    try:
        name_folder = 'JSON'
        os.makedirs(name_folder, exist_ok=True)
        
        url_site = "https://www.afisha.ru/"
        response = requests.get(url_site)
        response.raise_for_status()

        url_events, name_events = get_name_url_events(url_site, response)
        date_urls = get_date_urls(url_events, url_site)
        for date_url in date_urls: # За категорию
            all_date_url = get_all_data_urls(date_url)
            for url in all_date_url:
                url_events, price_events, name_events = get_data_events(url, url_site) # За день
                print(url_events)
    except requests.exceptions.ConnectTimeout:
        print("Ошибка с соединения")
        time.sleep(3)


if "__main__" == __name__:
    main()
