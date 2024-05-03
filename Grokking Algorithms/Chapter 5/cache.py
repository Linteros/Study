cache = {}


def sett_page(url):
    if cache.get(url):
        return cache[url]
    # else:
        # data = get_data_from_server(url)
        # return data