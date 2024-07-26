def find_movies(database: list, search_term: str):
    found_ones = [] #which movies have we found 
    for movie in database:
        # The function lower() converts a string to lowercase
        # when this is done for both strings search is case insensitive
        if search_term.lower() in movie["name"].lower():
            found_ones.append(movie)

 
