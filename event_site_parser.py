import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def get_name_url_events(url, response):
    name_events = []
    url_events = []
    soup = BeautifulSoup(response.text, "lxml")
    tags_name_events = soup.find_all("a", class_="CjnHd y8A5E L_ilg Q8u7A R1IVp nFaMY")

    for tag in tags_name_events:
        if tag["href"] != "/selection/":
            url_events.append(urljoin(url, tag["href"]))
            name_events.append(tag.text)

    return url_events, name_events

def get_all_events(urls):
    pass


def main():
    url_site = "https://www.afisha.ru/"
    response = requests.get(url_site)
    response.raise_for_status()

    url_events, name_events = get_name_url_events(url_site, response)
    get_all_events(url_events)


if "__main__" == __name__:
    main()
