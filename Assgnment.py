# Sample movie data
movies = [
    ["Casablanca", "Michael Curtiz", 1942, "Drama"],
    ["The Godfather", "Francis Ford Coppola", 1972, "Crime"],
    ["The Shawshank Redemption", "Frank Darabont", 1994, "Drama"],
    ["The Dark Knight", "Christopher Nolan", 2008, "Action, Thriller"],
    ["Living in Bondage", "Ola Balogun", 1992, "Drama"],
    ["Nneka the Pretty Serpent", "Christian Chukwu", 1994, "Drama, Thriller"],
    ["Rattlesnake", "Amaka Igwe", 1995, "Crime, Thriller"],
    ["Aki na Ukwa", "Chico Ejiro", 2002, "Comedy"],
    ["Saworo IDE", "unknown", 1997, "Drama"]
]

print(f"Total number of movies: {len(movies)}")

#function to get movie count by genre
def count_movies_by_genre(movies):
    drama_count, crime_count, action_count, thriller_count, comedy_count = 0, 0, 0, 0, 0,  
    for movie in movies:
        genres = movie[3].split(", ")  # Split genres by comma and space if there's more than one genre in the list
        for genre in genres:
            if genre == "Drama":
                drama_count += 1
            elif genre == "Crime":
                crime_count += 1
            elif genre == "Action":
                action_count += 1
            elif genre == "Thriller":
                thriller_count += 1
            elif genre == "Comedy":
                comedy_count +=1
    return {
    "Drama": drama_count,
    "Crime": crime_count,
    "Action": action_count,
    "Thriller": thriller_count,
    "Comedy": comedy_count
    }

def print_result(movies):
    genre_count = count_movies_by_genre(movies)
     
    print("Movie counts by genre: ")
    for genre, count in genre_count.items():
        print(f"  {genre}: {count}")

print_result(movies)


#Movies released after specified year
def find_movies_after_year(movies, year):
    collection_of_movies = []
 
    for movie in movies:
        if movie[2] > year:
            collection_of_movies.append(movie)

    print(f"Movies released after {year}:")

    for movie in collection_of_movies:
        print(f"  {movie[0]} ({movie[2]})")

    return collection_of_movies

find_movies_after_year(movies, 1994)

# def print_movies_after_year(movies, year):
#     collection_of_movies = find_movies_after_year(movies, year)
#     print(f"Movies released after {year}:")
#     for movie in collection_of_movies:
#         print(f"  {movie[0]} ({movie[2]})")

# # print_movies_after_year(movies, 1994)
# print(find_movies_after_year(movies, 2002))



#simple interest assignment,
#Ensuring the principal is an integer,
#also rate is an integer and not more than 100,
#&Convert time from months to years if time is >= 12 months

def calculate_simple_interest(principal:int, rate:int, time_months):
    if type(principal) != int:
        print(f"Principal amount must be an integer.")
        return
    if type(rate) != int or rate > 100:
        print("Rate must be an integer and not more than 100.")
        return
    if time_months >= 12:
        time_years = time_months / 12
    else:
        time_years = time_months / 12  # Still convert months to fraction of a year

    simple_interest = (principal * rate * time_years) / 100
    print(f"Interest equals to",simple_interest)

# calculate_simple_interest(100,40,9)











    