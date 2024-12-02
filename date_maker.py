import datetime


def date_maker():
    date = []
    for counter in range(10):
        date.append(str(datetime.datetime.now() + datetime.timedelta(days=counter))[:10])
    return date


if __name__ == "__main__":
    print(date_maker())