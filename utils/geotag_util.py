import requests

def call_geocode_api(query):
    url = 'https://api.mapy.cz/v1/geocode'
    params = {
        'query': query,
        'lang': 'cs',
        'limit': 1,
        'type': ['poi'],}
    headers = {
        'accept': 'application/json',
        'X-Mapy-Api-Key': '3K68wIf8T7iwOfvaxPGoeneVzZZ2IFnvWN1MXqKMM_Q'
    }

    response = requests.get(url, params=params, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error {response.status_code}: {response.text}')
        return None

