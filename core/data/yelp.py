from flask_config import Config
import requests
import json
from flask import session
import logging

_RESTAURANTS = [

]
_ERROR = []
_CTIY = ""

def get_businesses():
    """
    Fetches all businesses saved from the session

    returns:
        list: The list of all the businesses
    """
    return session.get("restaurants", _RESTAURANTS.copy())

def get_errors():
    """
    Fetches all errors saved from the session

    returns:
        list: the list of errors
    """
    return session.get("error", _ERROR.copy())

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

    
    session["error"] = []

    try:
        request = requests.get(
            "https://api.yelp.com/v3/businesses/search",
            params=params,
            headers=headers
        )
        request.raise_for_status()
        businesses = json.loads(request.text)["businesses"]
        session["restaurants"] = businesses
    except requests.exceptions.RequestException as e:
        #log the error and return an empty list
        logging.error(f"Error in get_city_resuatrants: {e}")
        session["restaurants"] = []
        session["error"] = json.loads(request.text)["error"]

    return city

def error_message():
    """
    Transform API error into a readable messages
    
    output:
        string: readable error messgae
    """

    error = get_errors()

    print(error)
    
    if not error:
        return ""
    elif error.get("code") == "LOCATION_NOT_FOUND":
        return "Location not found. Please try again."
    else:
        return "Search failed. Please try again."
