import media
import fresh_tomatoes

#This file is has the 6 objects of the class Movie from the file media.py


toy_story = media.Movie("Toy Story","A story of a boy and his toys",
                        "http://img.lum.dolimg.com/v1/images/"
                        "open-uri20150422-20810-m8zzyx_5670999f.jpeg?"
                        "region=0,0,300,450",
                        "https://www.youtube.com/watch?v=Bj4gS1JQzjk");

avatar = media.Movie("Avatar","A marine on an alien planet",
                     "http://static02.mediaite.com/themarysue/uploads/"
                     "2015/12/avatar.jpeg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY");

dhoni = media.Movie("MS Dhoni","A story of a indian cricketer",
                    "http://wikiprofile.in/wp-content/uploads/2015/"
                    "05/MS-Dhoni-The-Untold-Story-Movie-movie-wiki-"
                    "starcast-poster.jpg",
                    "https://www.youtube.com/watch?v=6L6XqWoS8tw");


midnight_in_paris = media.Movie("Midnight in Paris","todo!!!",
                                "https://upload.wikimedia.org/wikipedia/en/9/"
                                "9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY");

hunger_games = media.Movie("Hunger Games","todo!!!",
                         "http://www.thehungergames.co.uk/wp-content/uploads/"
                           "2014/08/HUNGER-GAMES-jacket.jpg",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY");

captain_america = media.Movie("Captain America","todo!!!",
                              "http://i.annihil.us/u/prod/marvel/movies/civilwar"
                              "/images/captainamerica_hero.png",
                              "https://www.youtube.com/watch?v=zAqCbTKbmYI");

#List of movies.
movies=[toy_story,avatar,dhoni,midnight_in_paris,hunger_games,captain_america]

fresh_tomatoes.open_movies_page(movies)
