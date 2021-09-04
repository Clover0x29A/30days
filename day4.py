movie_tuple = ("Fear and Loathing in Las Vegas", 2001, "some director")

movie_input = []

temp = input("Movie Name? ")
movie_input.append(temp)

temp = input("Movie year? ")
movie_input.append(temp)

temp = input("Director? ")
movie_input.append(temp)

temp = input("Movie budjet? ")
movie_input.append(temp)
movie2_tuple = (movie_input[0], movie_input[1], movie_input[2], movie_input[2])
print(f"{movie2_tuple[0]} {movie2_tuple[1]}")

movies = [movie_tuple, movie2_tuple]
print(movies)

del movies[0]
print(movies)