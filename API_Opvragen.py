import requests
import xmltodict
def coversOpvragen():
    api_url = 'http://api.filmtotaal.nl/filmsoptv.xml?apikey=uw7tbns0awlo3ovvngkv55j4ofjq9u8m&dag=01-11-2016&sorteer=0'
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

    return info

