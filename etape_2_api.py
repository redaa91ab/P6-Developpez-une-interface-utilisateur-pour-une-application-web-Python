import requests
from bs4 import BeautifulSoup


def print_movies(max_pages):
    session = requests.Session()
    url = "http://localhost:8000/api/v1/titles/"
    
    page = 0
    while url and page <= max_pages:
        response = session.get(url)
        data = response.json()
        for movie in data["results"] :
            print("Title :", movie["title"])
        url = data["next"]
        page += 1

def get_movie_infos(id_imdb) :
    session = requests.Session()
    url = "http://localhost:8000/api/v1/titles/"

    while True :
        response = session.get(url)
        data = response.json()
        for movie in data['results'] : 
            if movie['id'] == id_imdb :
                for info in movie.items() :
                    print(info[0], ":", info[1])
                return
        if data['next'] :
            url = data['next']
        else : 
            print("No result found")

def get_all_genres() :
    session = requests.Session()
    url = "http://localhost:8000/api/v1/genres/"

    while True : 
        response = session.get(url)
        data = response.json()
        for element in data["results"] :
            print(element["name"])
        if data["next"] :
            url = data["next"]
        else :
            return


get_all_genres()