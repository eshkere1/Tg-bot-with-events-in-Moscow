import requests
from bs4 import BeautifulSoup


def get_name_events(response):
    name_events = []
    url_events = []
    soup = BeautifulSoup(response.text, "lxml")
    tags_name_events = soup.find_all("a", class_="CjnHd y8A5E L_ilg Q8u7A R1IVp nFaMY")

    for tag in tags_name_events:
        if tag["href"] != "/selection/":
            url_events.append(tag["href"])
            name_events.append(tag.text)

    return url_events, name_events


def main():
    url_site = "https://www.afisha.ru/"
    response = requests.get(url_site)
    response.raise_for_status()

    url_events, name_events = get_name_events(response)

    print(url_events)
    print(name_events)


if "__main__" == __name__:
    main()
