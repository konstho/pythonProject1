import requests

def hae():
    try:
        pyyntö = "https://api.chucknorris.io/jokes/random"
        vastaus = requests.get(pyyntö)
        vastaus.raise_for_status()

        data = vastaus.json()
        vitsi = data['value']
        print("vitsi on: ", vitsi)

    except requests.exceptions.RequestException as e:
        print("virheellinen tunnus: ", e)
hae()