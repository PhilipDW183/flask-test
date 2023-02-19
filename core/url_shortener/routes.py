from core.url_shortener import url_shortener
from flask import render_template, url_for, redirect, request
import pyshorteners

s = pyshorteners.Shortener()

base_path = "/url"

@url_shortener.route(base_path)
def todo_index():
    return render_template("url.html")

@url_shortener.route(f'{base_path}/shorten_url', methods=["POST"])
def shorten_url():
    long_url = request.form.get('long_url')
    short_url = s.tinyurl.short(long_url)
    return render_template("url.html", short_url=short_url)

@url_shortener.route(f'{base_path}/<shortened_url>')
def redirect_to_url(shortened_url):
    long_url = s.tinurl.expand(shortened_url)
    print(long_url)
    return redirect(long_url)