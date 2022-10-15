from crypt import methods
import sys
import requests
from flask import Flask, request, render_template, redirect, jsonify

app = Flask('__name__')


def get_weather(states):

    url = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={states}&units=metric&appid=b21a2633ddaac750a77524f91fe104e7')
    val = url.json()

    return val


def re_formated(s):
    '''
    Replace all spaces by '+'
    '''

    return s.replace(' ', '+')


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/locate')
def locate():

    states = request.args.get('states')
    if states:
        w = get_weather(re_formated(states))
        return jsonify(w)

    return jsonify()
