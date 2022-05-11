import random

import credentials
import tweepy
from PyDictionary import PyDictionary
from random_words import RandomWords


def load_random_word():
    """Generate a random word and definition and return these values"""
    # Generate random word and its definition
    dictionary = PyDictionary()
    rw = RandomWords()
    word = rw.random_word()
    definitions = dictionary.meaning(word)

    # If the word doesn't have a definition, return an error
    try:
        part_of_speech = random.choice(list(definitions.keys()))
        definition = random.choice(definitions[part_of_speech])
    except:
        return "NULL_DEFINITION"
    return {"word": word, "definition": definition, "part_of_speech": part_of_speech}


def post_wotd_twitter(word_def):
    """Post WOTD on Twitter with a gif"""
    # Credentials
    api_key = credentials.API_KEY
    api_secret_key = credentials.API_SECRET_KEY
    access_token = credentials.ACCESS_TOKEN
    access_token_secret = credentials.ACCESS_TOKEN_SECRET

    # Authentication Twitter
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Random GIF
    gifs = (
        "images/dictionary.gif",
        "images/mean.gif",
        "images/mouth.gif",
        "images/simpson.gif",
        "images/words.gif",
    )
    gif = random.choice(gifs)

    # Post a tweet
    api.update_status_with_media(
        f'#WOTD {word_def["word"].upper()} : '
        f'({word_def["part_of_speech"]}) '
        f'{word_def["definition"].capitalize()}',
        gif,
    )


if __name__ == "__main__":
    wotd = load_random_word()
    while wotd == "NULL_DEFINITION":
        wotd = load_random_word()
    post_wotd_twitter(wotd)
