class Movie:
    """ This class is used to store information of movie like Title,\
Storyline, Poster and Trailer.
    This class is used by entertainment.py to store the data of\
 different Instances."""
    def __init__(self, titl, story, image, link):
        """ This method initiates a new movie

            :param titl: title
            :type titl : str

            :param story: sline
            :type story : str

            :param image: poster_image_url
            :type image : str

            :param link: trailer_youtube_url
            :type link :str
        """
        self.title = titl
        self.sline = story
        self.poster_image_url = image
        self.trailer_youtube_url = link
