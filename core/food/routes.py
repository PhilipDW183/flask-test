from core.food import food
from flask import render_template, request, redirect, url_for
from core.data.yelp import get_businesses, get_city_restaurants, error_message, get_city

base_path = "/food"

@food.route(base_path)
def food_index():
    restaurants = get_businesses()
    error = error_message()
    city = get_city()
    return render_template("food.html", 
        restaurants=restaurants,
        error = error,
        city = city)

@food.route(f'{base_path}/places', methods=["POST"])
def get_places():
    city = request.form.get("city")
    get_city_restaurants(city)
    return redirect(url_for("food.food_index"))