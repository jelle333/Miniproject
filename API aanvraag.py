import requests
import xmltodict
import datetime

date = datetime.datetime.now().strftime ("%d-%m-%Y")

api_url = 'http://api.filmtotaal.nl/filmsoptv.xml?apikey=etr76i16piyqy73oqbybd9l6hfe8laxb&dag='+date+'&sorteer=0'
response = requests.get(api_url) #auth=auth_details)
filmXML = xmltodict.parse(response.text)
info = []
filmInfo = filmXML['filmsoptv']['film']
for film in filmInfo:
    lst = []
    lst.append(film['cover'])
    lst.append(film['titel'])
    lst.append(film['jaar'])
    lst.append(film['synopsis'])
    lst.append(film['zender'])
    lst.append(film['starttijd'])
    lst.append(film['eindtijd'])
    lst.append(film['duur'])
    lst.append(film['imdb_rating'])
    info.append(lst)
    print(lst)

