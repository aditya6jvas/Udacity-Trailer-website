import mvie
import fresh_tomatoes
# mvie.Movie(Title,Plot,Poster Link,youtube link)

# First Movie
usual_suspects = mvie.Movie("The Usual Suspects",
                            "Five criminals meet during a routine police line-\
up.Upon their release, they plan to pull off a dangerous\
heist involving precious emeralds worth three million dollars.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BYTViNjMyNmUtNDFkNC00ZDRlLThmMDUtZDU2YWE4NGI2ZjVmXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
                            "https://www.youtube.com/watch?v=oiXdPolca5w")

# Second Movie
sixth_sense = mvie.Movie("Sixth Sense",
                    "Child psychologist, starts treating a young boy who acts\
as a medium of communication between Crowe and a slew of unhappy spirits.",
                        "http://www.impawards.com/1999/posters/sixth_sense_ver1.jpg",  # noqa
                        "https://www.youtube.com/watch?v=VG9AGf66tXM")

#  Third Movie
perks_ob_wallflower = mvie.Movie("The Perks of being wallflower",
                                "Charlie, a 15-year-old introverted\
bright Pittsburgh boy, enters high school\
and is nervous about his new life.\
He is befriended by his seniors who\
show him the way to the real world.",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BMzIxOTQyODU1OV5BMl5BanBnXkFtZTcwMDQ4Mjg4Nw@@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
                                "https://www.youtube.com/watch?v=XO3-PumyjoI")

# Fourth Movie
fight_club = mvie.Movie("Fight Club",
                    "Discontented with his capitalistic lifestyle, a\
white-collared insomniac forms an underground fight club with Tyler, a \
careless soap salesman.\
 The project soon spirals down into something sinister.",
                        "http://www.gstatic.com/tv/thumb/movieposters/23069/p23069_p_v8_ad.jpg",  # noqa
                        "https://www.youtube.com/watch?v=BdJKm16Co6M")

# Fifth Movie
pursuit_of_happiness = mvie.Movie("The Pursuit of Happiness",
                                "Chris Gardner takes up an unpaid internship in\
 a brokerage firm after he loses his life's earnings selling a product he\
 invested in. His wife leaves him and he is left with the custody of his son.",
                                "http://www.gstatic.com/tv/thumb/movieposters/162523/p162523_p_v8_ad.jpg",  # noqa
                                "https://www.youtube.com/watch?v=89Kq8SDyvfg")

# Sixth Movie
wolf_of_wallstreet = mvie.Movie("The wolf og wall street",
                            "Introduced to life in the fast lane through\
 stockbroking, Jordan Belfort takes a hit after a Wall Street crash.\
 He teams up with Donnie Azoff, cheating his way to the\
 top as his relationships slide.",
                                "http://sociologylegacy.pbworks.com/f/1426548534/6738.jpg",  # noqa
                                "https://www.youtube.com/watch?v=idAVRvQeYAE")

movies = [usual_suspects,
          sixth_sense,
          perks_ob_wallflower,
          fight_club,
          pursuit_of_happiness,
          wolf_of_wallstreet]  # List of all movies

fresh_tomatoes.open_movies_page(movies)   # Link to fresh_tomatoes file
