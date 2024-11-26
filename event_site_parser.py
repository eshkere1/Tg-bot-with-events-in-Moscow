import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def get_name_url_events(url, response):
    name_events = []
    url_events = []
    soup = BeautifulSoup(response.text, "lxml")
    tags_name_events = soup.find_all("a", class_="CjnHd y8A5E L_ilg Q8u7A R1IVp nFaMY")

    for tag in tags_name_events:
        if tag["href"] != "/selection/" and tag["href"] != "/msk/restaurants/?utm_campaign=headline&utm_medium=referral&utm_source=afisha":
            url_events.append(urljoin(url, tag["href"]))
            name_events.append(tag.text)

    return url_events[0:5], name_events[0:5]


def get_all_events(url_site, url):
    url_events = []
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")
    card_events = soup.find_all('div', class_='oP17O')

    for card in card_events:
        element_url = card.find('div', class_='QsWic rIUFv').find('a', class_='CjnHd y8A5E Vrui1')['href']
        url_event = urljoin(url_site, element_url)
        url_events.append(url_event)

    return url_events

def main():
    url_site = "https://www.afisha.ru/"
    response = requests.get(url_site)
    response.raise_for_status()

    url_events, name_events = get_name_url_events(url_site, response)
    url_event = get_all_events(url_site, url_events[0])
    print(url_event)


if "__main__" == __name__:
    main()
