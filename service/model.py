import requests
import pickle
import pandas as pd
import os
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("AUTH_API_TOKEN")

distance_similarity = pickle.load(open("./pickle_data/similarity.pkl", "rb"))
new_movies = pd.DataFrame(pickle.load(open("./pickle_data/data.pkl", "rb")))


headers = {
    "accept": "application/json",
    "Authorization": api_key,
}


# url = f"""https://api.themoviedb.org/3/movie/{id}/external_ids"""
# response = requests.get(url, headers=headers)
# temp = response.json()

# url = f"https://api.themoviedb.org/3/find/{temp['imdb_id']}?external_source=imdb_id"
# response = requests.get(url, headers=headers)
# final = response.json()

# title = final["movie_results"][0]["title"]
# poster_path = (
#     "https://image.tmdb.org/t/p/original/"
#     + final["movie_results"][0]["poster_path"]
# )


def tmbd_data(id):
    url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"
    response = requests.get(url, headers=headers)
    data = response.json()
    poster_path = "https://image.tmdb.org/t/p/original/" + data["poster_path"]
    title = data["title"]

    return {"title": title, "poster": poster_path}


def recommend(name):
    movies_index = new_movies.loc[(new_movies["title"] == name)].index[0]
    dist_simi = list(enumerate(distance_similarity[movies_index]))
    dist_simi.sort(reverse=True, key=lambda x: x[1])

    return [tmbd_data(int(new_movies.iloc[i[0]]["movie_id"])) for i in dist_simi[1:6]]
