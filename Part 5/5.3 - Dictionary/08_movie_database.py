def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    # Create a new movie dictionary with the given details
    movie = {
        "name": name,
        "director": director,
        "year": year,
        "runtime": runtime
    }
    # Add the new movie to the database
    database.append(movie)

