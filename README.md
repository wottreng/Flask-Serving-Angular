# Flask-Serving-Angular
Serve angular production application from python flask backend
* Flask will serve production app in dist folder
* NO Static folder needed!
* This is done by requesting javascript and css files as args to root url
* This makes developement and deployment simple with the Angular frontend UI and Flask backend together in one folder
* JS and CSS files can be secured behind password protection if needed
* less bots bogging down your server with static content requests

## build angular app
`ng build` within app folder like normal

## run flask server
when `flaskBackend.py` is run it will edit `index.html` to add static links as url args and serve them as required

Open up `http://localhost:8080/` and production app is served

## update flask server
* `ng build` angular app
* restart `flaskBackend.py` to resync documents

Cheers 🍺 
