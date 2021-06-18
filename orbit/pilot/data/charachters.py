from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://rickandmortyapi.com/api/character').text

character = BeautifulSoup(source, 'lxml')

print(character.prettify())

