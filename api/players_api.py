import requests
from toolz import curry

@curry
def make_request(method, url, **kwargs):
    response = requests.request(method, url, **kwargs)
    return response.json()

get = make_request('GET')

def get_trivia_from_api(season: int):
    url = f"http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/season/{season}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data:
            return data
        else:
            return "trivia not found"
    else:
        return f"Error {response.status_code}: {response.text}"




import requests
from toolz import curry

@curry
def make_request(method, url, **kwargs):
    response = requests.request(method, url, **kwargs)
    return response.json()

get = make_request('GET')

def get_players_from_api(season):
    url = f"http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/season/{season}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data:
            return data
        else:
            return "player not found"
    else:
        return f"Error {response.status_code}: {response.text}"