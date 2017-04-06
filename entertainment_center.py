import media
import fresh_tomatoes

# create all movie objects
three_ten_to_yuma = media.Movie(
    "310 to Yuma",
    "In Arizona in the late 1800's, infamous outlaw Ben Wade "
    "and his vicious gang of thieves and murderers have plagued "
    "the Southern Railroad. When Wade is captured, Civil War "
    "veteran Dan Evans, struggling to survive on his drought-plagued "
    "ranch, volunteers to deliver him alive to the 3:10 to Yuma, "
    "a train that will take the killer to trial.",
    "https://images-na.ssl-images-amazon.com/images"
    "/M/MV5BODE0NTcxNTQzNF5BMl5BanBnXkFtZTcwMzczOTIzMw"
    "@@._V1_SY1000_CR0,0,663,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=jX1m45CwvJ8",
    "2007")

avatar = media.Movie(
    "Avatar",
    "In the 22nd century, a paraplegic Marine is dispatched to "
    "the moon Pandora on a unique mission, but becomes torn between "
    "following orders and protecting an alien civilization.",
    "https://images-na.ssl-images-amazon.com/images/M/"
    "MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY",
    "2009")

mad_max = media.Movie(
    "Mad Max: Fury Road",
    "A woman rebels against a tyrannical ruler in postapocalyptic "
    "Australia in search for her home-land with the help of a group "
    "of female prisoners, a psychotic worshipper, and a drifter named Max.",
    "https://images-na.ssl-images-amazon.com/images/M/"
    "MV5BMTUyMTE0ODcxNF5BMl5BanBnXkFtZTgwODE4NDQzNTE"
    "@._V1_SY1000_CR0,0,687,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=jUHrve5oUQk",
    "2015")

star_wars = media.Movie(
    "Star Wars Espisode: Episode IV - A New Hope ",
    "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, "
    "a wookiee and two droids to save the galaxy from the Empire's "
    "world-destroying battle-station, while also attempting to rescue "
    "Princess Leia from the evil Darth Vader.",
    "https://images-na.ssl-images-amazon.com/images/M/"
    "MV5BYzQ2OTk4N2QtOGQwNy00MmI3LWEwNmEtOTk0OTY3NDk2MGJkL2ltYWdlL2ltYW"
    "dlXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_SY1000_CR0,0,664,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=1g3_CFmnU7k",
    "1977")

fifth_element = media.Movie(
    "The Fifth Element",
    "In 2257, a taxi driver is unintentionally given the task of saving a "
    "young girl who is part of the key that will ensure the survival of "
    "humanity.",
    "https://images-na.ssl-images-amazon.com/images/M/"
    "MV5BZWFjYmZmZGQtYzg4YS00ZGE5LTgwYzAtZmQwZjQ2NDliMGVmXkEyXkFqcGde"
    "QXVyNTUyMzE4Mzg@._V1_SY1000_CR0,0,696,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=fQ9RqgcR24g",
    "1997")


# store all my movies in an array list
movies = [three_ten_to_yuma, avatar, mad_max, star_wars, fifth_element]

# call the fresh_tomatoes code that will create,
# and open the website with the movie information
fresh_tomatoes.open_movies_page(movies)
