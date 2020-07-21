# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask_pymongo import PyMongo


# -- Initialization section --
app = Flask(__name__)

# name of database
app.config['MONGO_DBNAME'] = 'music'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://bernard_2:charmander@cluster0.jxvpj.mongodb.net/music?retryWrites=true&w=majority'

mongo = PyMongo(app)

# -- Routes section --
# INDEX

@app.route('/')
@app.route('/index')

def index():
    collection = mongo.db.my_music
    songs = collection.find({})
    # return message to user
    return render_template('template.html', songs = songs)


# ADD SONGS

@app.route('/add')
def add():
    # define a variable for the collection you want to connect to
    collection = mongo.db.my_music
    # use some method on that variable to add/find/delete data
    #collection.insert_one({'song': 'Heartless', 'artist': 'Kanye', 'description': 'sounds good'})
    #collection.insert_one({'song': 'Location', 'artist': 'Khalid', 'description': 'sounds mad good'})
    collection.insert_one({'song': 'AAAA', 'artist': 'Taylor Swift', 'description': 'for testing purposes'})
    # return a message to the user (or pass data to a template)
    print("song added")
    return 'ADDED SONG!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'

# SHOW A LIST OF ALL SONG TITLES
@app.route('/all_music')
def all_music():
    collection = mongo.db.my_music
    #songs = collection.find().sort('song',1)
    songs = collection.find().sort('artist',1)
    return render_template('template.html', songs = songs)


# ADVANCED: A FORM TO COLLECT USER-SUBMITTED SONGS
@app.route('/add_song', methods = ["GET", "POST"])
def add_song():
    if request.method == "POST":
        song_name = request.form['song_name']
        song_artist = request.form['song_artist']
        song_description = request.form['song_description']
        collection = mongo.db.my_music
        collection.insert({'song': song_name, 'artist': song_artist, 'description': song_description})
        songs = collection.find().sort('song', 1)
        return render_template('template.html', songs = songs)
    else:
        return("you dum goof look what you done")

# DOUBLE-ADVANCED: SHOW ARTIST PAGE
@app.route('/artist/<name>')
def find_artist(name):
    collection = mongo.db.my_music
    songs = collection.find({'artist': name})
    return render_template('template.html', songs = songs)

# TRIPLE-ADVANCED: SHOW SONG PAGE
# @app.route('/song/<_id>')
# def find_song(_id):
#     collection = mongo.db.my_music
#     songs = collection.find({'ObjectID': _id})
#     return render_template('template.html', songs = songs)