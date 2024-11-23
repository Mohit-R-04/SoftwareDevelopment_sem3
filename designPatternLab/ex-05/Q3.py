class Movie:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    def __str__(self):
        return f"Movie(Name: {self.name}, Genre: {self.genre})"


class MovieList(list):
    """A list tailored to contain only movies of a specific genre."""
    
    def __init__(self, genre):
        self.genre = genre
        super().__init__()  # Inherit the initialization from list

    def append(self, movie):
        """Overrides the append method to ensure only movies of the same genre are added."""
        if not isinstance(movie, Movie):
            raise TypeError("Only Movie objects can be added to MovieList.")

        if movie.genre != self.genre:
            raise ValueError(f"Movie genre does not match. Expected genre: {self.genre}, but got: {movie.genre}.")

        # Append the movie to the list if it matches the genre
        super().append(movie)

    def __add__(self, other):
        """Overload the + operator to return the list with more movies."""
        if not isinstance(other, MovieList):
            raise TypeError("Can only add MovieList objects.")

        return self if len(self) >= len(other) else other

    def __str__(self):
        """Override string representation to show the movie list."""
        movie_names = [movie.name for movie in self]
        return f"MovieList(Genre: {self.genre}, Movies: {', '.join(movie_names)})"


# Example Usage:
# Create movies
movie1 = Movie("Inception", "thriller")
movie2 = Movie("The Dark Knight", "thriller")
movie3 = Movie("Interstellar", "sci-fi")
movie4 = Movie("Memento", "thriller")
movie5 = Movie("Blade Runner", "sci-fi")

# Create movie lists for specific genres
thriller_list = MovieList("thriller")
sci_fi_list = MovieList("sci-fi")

# Add movies to the lists
thriller_list.append(movie1)  # Added
thriller_list.append(movie2)  # Added
thriller_list.append(movie4)  # Added
sci_fi_list.append(movie3)    # Added
sci_fi_list.append(movie5)    # Added

# Print lists
print(thriller_list)
print(sci_fi_list)

# Operator overloading: compare movie lists
result_list = thriller_list + sci_fi_list
print("List with more movies:", result_list)
