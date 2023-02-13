# Watch Next suggestion generator
'''
This program helps decide on what to 'watch later' with help from natural language generation
'''
#---Import section---
import spacy
nlp = spacy.load('en_core_web_md')

# movie suggesting function
def suggested_movie(a_movie_desc):
    '''
    Takes in movie name and description as one string, separates into name and description,
    compares input movie description to each movie description from data base.
    Outputs movie with highest similarity to input movie as suggested movie
    '''
    a_movie_desc = nlp(a_movie_desc)
    highest_similarity_coefficient = 0

    for movie in movie_data:
        movie_split = movie.split(" :")
        movie_desc = movie_split[1]
        movie_desc = nlp(movie_desc)
        this_similarity_coefficient = a_movie_desc.similarity(movie_desc)

        if this_similarity_coefficient > highest_similarity_coefficient:
            highest_similarity_coefficient = this_similarity_coefficient
            suggested_movie_output = movie
    
    return suggested_movie_output


# reads data about movies from .txt file
f = open('movies.txt', 'r')
movie_data = f.readlines()
f.close()

# data about previously watched movie
watched_movie = "Planet Hulk :Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
watched_movie_name = watched_movie.split(" :")[0]
watched_movie_description = watched_movie.split(" :")[1]

# final output
print(f"\nSince you've watched {watched_movie_name}, why not try this:\n")
print(suggested_movie(watched_movie))
