
console.log('start')
const request = require('request');

var Twit = require('twit')

var config = require('./config');
var T = new Twit(config);
var my_data = {
  "genres": [
    {
      "id": 28,
      "name": "Action"
    },
    {
      "id": 12,
      "name": "Adventure"
    },
    {
      "id": 16,
      "name": "Animation"
    },
    {
      "id": 35,
      "name": "Comedy"
    },
    {
      "id": 80,
      "name": "Crime"
    },
    {
      "id": 99,
      "name": "Documentary"
    },
    {
      "id": 18,
      "name": "Drama"
    },
    {
      "id": 10751,
      "name": "Family"
    },
    {
      "id": 14,
      "name": "Fantasy"
    },
    {
      "id": 36,
      "name": "History"
    },
    {
      "id": 27,
      "name": "Horror"
    },
    {
      "id": 10402,
      "name": "Music"
    },
    {
      "id": 9648,
      "name": "Mystery"
    },
    {
      "id": 10749,
      "name": "Romance"
    },
    {
      "id": 878,
      "name": "Science Fiction"
    },
    {
      "id": 10770,
      "name": "TV Movie"
    },
    {
      "id": 53,
      "name": "Thriller"
    },
    {
      "id": 10752,
      "name": "War"
    },
    {
      "id": 37,
      "name": "Western"
    }
  ]
}

var makeRun = function(){
  var stream = T.stream('statuses/filter', { track: ['@ShariarKabir14'] });
  stream.on('tweet', tweetEvent);
  function tweetEvent(tweet) {
    var name = tweet.user.screen_name;
    var my_user_id = tweet.user.id;
    var txt = tweet.text;
    var nameID  = tweet.id_str;
    var search_query = "https://api.themoviedb.org/3/";
    var reply = "";
    var data = {authors: [], titles: []}
    var response;
    var og = txt;
    if (txt.indexOf("genre") != -1){
      txt = txt.substring(txt.indexOf(" ") + 1,txt.length);
      txt = txt.substring(6, txt.length);
      var my_genre = txt.toLowerCase();
      var my_genre_num = 0;
      for (i = 0; i < my_data['genres'].length; i++){
        if ((my_data['genres'][i]['name']).toLowerCase() == my_genre){
          my_genre_num = my_data['genres'][i]['id'];
          i = my_data['genres'].length + 1;
        }
      }
      search_query += "discover/movie?api_key=65a3cdc61a25fc687d858ca991f83a4a&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_genres="+ my_genre_num;
    }
    else if (txt.indexOf("person") != -1){
      txt = txt.substring(txt.indexOf(" ") + 1,txt.length);
      txt = txt.substring(7, txt.length);
      search_query += "search/person?api_key=65a3cdc61a25fc687d858ca991f83a4a&query=" + txt;
    }
    else{
      txt = txt.substring(txt.indexOf(" ") + 1,txt.length);
      search_query += "search/movie?api_key=65a3cdc61a25fc687d858ca991f83a4a&query=" + txt;
    }
    if (og.toLowerCase().indexOf('person'.toLowerCase()) == -1){
      request(search_query, { json: true }, (err, res, body) => {
        response = res.body['results'];
        var my_movie = response[Math.floor(Math.random() * response.length)];;
        var my_movie_id = my_movie['id'];
        var reply = "https://www.themoviedb.org/movie/" + my_movie_id;
        T.post('statuses/update', { status: reply }, function(err, data, response) {
          console.log(data)
        })
      });
    }
    else{
      request(search_query, { json: true }, (err, res, body) => {
        response = res.body['results'][0]['known_for'];
        var my_movie = response[Math.floor(Math.random() * response.length)];;
        var my_movie_id = my_movie['id'];
        var reply = "https://www.themoviedb.org/movie/" + my_movie_id;
        T.post('statuses/update', { status: reply }, function(err, data, response) {
          console.log(data)
        })
      });

    }
  };
}

setInterval(makeRun, 4000);
