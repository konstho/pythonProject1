import requests
kaupunki = input("syötä kaupunki: ")
url = f'http://api.openweathermap.org/data/2.5/weather?q={kaupunki}&APPID=e1f95a3c85091b21381da9a3a8e34c2f&units=metric'

pyyntö = requests.get(url).json()

sää = pyyntö['main']['temp']
tilanne = pyyntö['weather'][0]['description']

print(sää)
print(tilanne)