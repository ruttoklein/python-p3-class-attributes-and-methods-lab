class Song:
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class attributes
        Song.count += 1
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    
    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.add(self.genre)

   
    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.add(self.artist)

   
    def add_to_genre_count(self):
        Song.genre_count[self.genre] = Song.genre_count.get(self.genre, 0) + 1
   
    def add_to_artist_count(self):
        Song.artist_count[self.artist] = Song.artist_count.get(self.artist, 0) + 1

