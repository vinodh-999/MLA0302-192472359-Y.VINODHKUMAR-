import random

# Movie list
movies = ["Action", "Comedy", "Drama", "Sci-Fi"]

# Initial scores
scores = {
    "Action": 0,
    "Comedy": 0,
    "Drama": 0,
    "Sci-Fi": 0
}

print("Movie Recommendation System\n")

# Simulate 10 user feedbacks
for i in range(10):

    movie = random.choice(movies)

    # User rating (1 to 5)
    rating = random.randint(1, 5)

    # Update movie score
    scores[movie] += rating

    print("Movie:", movie)
    print("User Rating:", rating)
    print()

# Display final scores
print("Movie Scores\n")

for movie in movies:
    print(movie, ":", scores[movie])

# Best Recommendation
best_movie = max(scores, key=scores.get)

print("\nRecommended Movie:", best_movie)
