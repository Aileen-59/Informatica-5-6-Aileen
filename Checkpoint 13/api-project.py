import requests
import random

def get_movies():
    url = "https://api.watchmode.com/v1/"
    api_key = "qzZ"
    response = requests.get(url)
    return response.json()
def pick_random_movie(movies):
    return random.choice(movies)

def movie_info(movie):
    print(f"Title: ",{movie}["title"])