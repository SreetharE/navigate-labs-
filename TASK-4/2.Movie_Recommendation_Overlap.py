user1 = set(user1_movies)
user2 = set(user2_movies)
common_movies = user1 & user2
unique_movies = user1 ^ user2
print("Common movies:", common_movies)
print("Unique movies:", unique_movies)
