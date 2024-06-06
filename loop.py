#  #number guessing game

# import random

# number = random.randrange(1, 10)
# print(number)
# attempt = 5

# while attempt > 0:
#     users_guess =int(input("kindly make your guess"))
#     if number > users_guess:
#         print("Your guess is too low")
#     elif number < users_guess:
#         print(" Your guess is too high")
#     else:
#         print("You made the right guess: ")
#         break
#     attempt -= 1
#     if attempt > 0:
#         print(f"You have {attempt} {'attempts' if attempt > 1 else 'attempt'} left")
#     else:
#         print(f" Sorry,You've used all your attempts. The number was {number}")





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

def count_movies_by_genre(movies):
    genre_counts = {}
    for movie in movies:
        genres = movie[3].split(", ")  # Split genres by comma and space
        for genre in genres:
            if genre in genre_counts:
                genre_counts[genre] += 1
            else:
                genre_counts[genre] = 1
    return genre_counts

def find_movies_after_year(movies, year):
    movies_after_year = [movie for movie in movies if movie[2] >= year]
    return movies_after_year

# Call the functions and process the movie data
def process_movie_data(movies, year):
    total_movies = len(movies)
    genre_counts = count_movies_by_genre(movies)
    movies_after_year = find_movies_after_year(movies, year)
    
    print(f"Total number of movies: {total_movies}")
    print("Movie counts by genre:")
    for genre, count in genre_counts.items():
        print(f"  {genre}: {count}")
    print(f"Movies released after {year}:")
    for movie in movies_after_year:
        print(f"  {movie[0]} ({movie[2]})")

# Example usage
process_movie_data(movies, 1994)



def calculate_simple_interest(principal, rate, time_months):
    # Ensure the principal is an integer
    if type(principal) != int:
        return "Principal amount must be an integer."
    
    # Ensure the rate is an integer and not more than 100
    if type(rate) != int or rate > 100:
        return "Rate must be an integer and not more than 100."
    
    # Convert time from months to years if time is >= 12 months
    if time_months >= 12:
        time_years = time_months / 12
    else:
        time_years = time_months / 12  # Still convert months to fraction of a year
    
    # Calculate simple interest
    simple_interest = (principal * rate * time_years) / 100
    return simple_interest

# Example usage
principal = 1000  # Principal amount in integers
rate = 5          # Rate of interest in integers, not more than 100
time_months = 18  # Time in months

simple_interest = calculate_simple_interest(principal, rate, time_months)
if isinstance(simple_interest, str):
    print(simple_interest)
else:
    print(f"The simple interest is: {simple_interest}")
