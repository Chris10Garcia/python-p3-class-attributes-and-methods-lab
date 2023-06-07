class Song:
    artists = []
    genres = set()
    genres_list = []
    genre_count = {}
    artist_count = {}
    count = 0

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.soung_count()
        self.keep_track(self)
        self.build_count()

    
    @classmethod
    def soung_count(cls, increase = 1):
        cls.count += increase

    @classmethod
    def keep_track(cls, self):
        cls.artists.append(self.artist)
        cls.genres_list.append(self.genre)
        cls.genres.add(self.genre)

    
    @classmethod
    def build_count(cls):
        cls.genre_count = {key : cls.genres_list.count(key) for key in cls.genres_list }
        cls.artist_count = {key : cls.artists.count(key) for key in cls.artists }
        