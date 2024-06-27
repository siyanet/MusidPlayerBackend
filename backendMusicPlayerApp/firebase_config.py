import pyrebase

config = {
    "apiKey": "AIzaSyCCLDOmi0zh99ALrEdauToijOzNks0Hmzo",
    "authDomain": "my-music-b4f74.firebaseapp.com",
    "projectId": "my-music-b4f74",
    "storageBucket": "my-music-b4f74.appspot.com",
    "messagingSenderId": "473491962611",
    "databaseURL": "",
    "appId": "1:473491962611:web:5b69474de565b7ca515586",
}
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
