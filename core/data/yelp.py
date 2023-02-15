from flask_config import Config
import requests
import json
from flask import session

_RESTAURANTS = [

]

def get_businesses():
    """
    Fetches all businesses saved from the session

    returns:
        list: The list of all the businesses
    """
    return session.get("restaurants", _RESTAURANTS.copy())

def clear_buinsses():
    """
    Clears all buinsses saved from the session
    """
    existing_restaurants = get_businesses()

    updated_restaurants = existing_restaurants.clear

    session["restaurants"] = updated_restaurants

    return


def get_city_restaurants( city ):
    """
    gets restaurants from the given city

    Args:
        city: The location of the city

    returns:
        city: the location of the city
    """

    headers = {"Authorization": "Bearer " + Config().YELP_AUTH_TOKEN}
    params = {"location": city, "limit": 5, "term": "restaurants" }

    request = requests.get(
        "https://api.yelp.com/v3/businesses/search",
        params=params,
        headers=headers
    )

    businesses = json.loads(request.text)["businesses"]

    session["restaurants"] = businesses

    return city