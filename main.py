import os
import json
import requests
from bs4 import BeautifulSoup
import random

url = "https://www.imdb.com/chart/top"

def main():
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    movie_tags = soup.select('td.titleColumn')
    inner_movie_tags = soup.select('td.titleColumn a')
    rating_tags = soup.select('td.posterColumn span[name=ir]')

    def get_year(movie_tag):
        return movie_tag.text.split()[-1]
    
    def get_actor(inner_movie_tag):
        return inner_movie_tag['title']
    
    def get_title(inner_movie_tag):
        return inner_movie_tag.text
    
    def get_rating(rating_tag):
        return float(rating_tag['data-value'])
    
    years = [get_year(tag) for tag in movie_tags]
    actors = [get_actor(tag) for tag in inner_movie_tags]
    titles = [get_title(tag) for tag in inner_movie_tags]
    ratings = [get_rating(tag) for tag in rating_tags]

    n_movies = len(titles)

    while True:
        idx = random.randrange(0, n_movies)

        print(f'\nTitle: {titles[idx]} {years[idx]}\nRating: ⭐ {ratings[idx]:.1f}\nStarring: {actors[idx]}\n')

        user_input = input("Do you want another option (y/[n])? ")

        if user_input != 'y':
            break

if __name__ == "__main__":
    main()