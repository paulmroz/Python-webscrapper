from time import sleep
from random import randint
import mysql.connector
from bs4 import BeautifulSoup
import requests
import csv
import numpy

mydb = mysql.connector.connect(
    host="localhost",
    user="paul",
    passwd="space",
    database="movies_webscraping"
)

mycursor = mydb.cursor()
sqlFormula = "TRUNCATE TABLE movies_movie"
mycursor.execute(sqlFormula)

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)

csv_writer.writerow(['Title', 'Year', 'IMDB rating', 'Metascore', 'Votes', 'Description', 'Type'])

pages = numpy.arange(0, 250, 50)

titles = []
years = []
imdb_ratings = []
metascores = []
votes = []
description = []
type = []

for page in pages:

    source = requests.get(
        f'https://www.imdb.com/search/title/?release_date=2010-01-01,2019-12-31&start={page}&ref_=adv_nxt').text

    sleep(randint(3, 7))

    soup = BeautifulSoup(source, 'lxml')

    for movie_card in soup.find_all('div', class_='lister-item mode-advanced'):

        if movie_card.find('div', class_='ratings-metascore') is not None:

            movie_poster = movie_card.find('div', class_='lister-item-image')
            movie_poster = movie_poster.a.img
            movie_poster = movie_poster['loadlate']

            movie_title = movie_card.h3.a.text
            titles.append(movie_title)

            movie_year = movie_card.h3.find('span', class_='lister-item-year text-muted unbold').text
            movie_year = movie_year[-5:-1]
            years.append(movie_year)

            movie_rating_imdb = float(movie_card.strong.text)
            imdb_ratings.append(movie_rating_imdb)

            movie_metascore = movie_card.find('span', class_='metascore').text
            metascores.append(int(movie_metascore))

            movie_votes = movie_card.find('span', attrs={'name': 'nv'})
            movie_votes = int(movie_votes['data-value'])
            votes.append(movie_votes)

            movie_description = movie_card.find_all("p", class_='text-muted')[1].text
            description.append(description)

            movie_genre = movie_card.find('span', class_='genre').text
            type.append(movie_genre)

            csv_writer.writerow([
                movie_title,
                movie_year,
                movie_rating_imdb,
                movie_metascore,
                movie_votes,
                movie_description,
                movie_genre
            ])

            sqlFormula = "INSERT INTO movies_movie(name, year, description, imdb_rating, metascore, votes, " \
                         "type, url) VALUES(%s, %s, %s, %s, %s, %s, %s, %s) "

            mycursor.execute(sqlFormula, (movie_title,
                             movie_year,
                             movie_description,
                             movie_rating_imdb,
                             movie_metascore,
                             movie_votes,
                             movie_genre,
                             movie_poster))
            mydb.commit()

mydb.close()
mycursor.close()
