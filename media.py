import webbrowser

class Movie():
    """ This class is used to display movies poster, storyline and to"""
    """play the movie triler."""

    #initialization of the class
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube

    #This function plays thr movie trailer.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
