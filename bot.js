
console.log('start')
const request = require('request');
var unirest = require('unirest');

var Twit = require('twit')

var config = require('./config');
var T = new Twit(config);
var games = []



var makeRun = function(){
  var stream = T.stream('statuses/filter', { track: ['@ShariarKabir14'] });
  stream.on('tweet', tweetEvent);
  function tweetEvent(tweet) {
    console.log("lets start");
    var name = tweet.user.screen_name;
    var my_user_id = tweet.user.id;
    var txt = tweet.text;
    var nameID  = tweet.id_str;
    var search_query = "http://poetrydb.org/lines/" + "shall%20i%20compare";
    var reply = "";
    var data = {authors: [], titles: []}
    var response;
    request(search_query, { json: true }, (err, res, body) => {
      response = res.body;
      if (response != null){
        for (i = 0; i < 3; i++){
          console.log('adasdasd')
          var poem_selection_index = Math.floor(Math.random() * (response.length - 0 + 1)) + 0;
          if (response[poem_selection_index] != null){
            var poem_selection = response[poem_selection_index]['lines'];
            for (j = 0; j < poem_selection.length; j++){
              var my_sentence = poem_selection[j].toLowerCase();
              if (my_sentence.indexOf("Shall I compare".toLowerCase()) != -1){
                data['authors'].push(response[poem_selection_index]['author']);
                data['titles'].push(response[poem_selection_index]['title']);
                reply += my_sentence + '\n';
              }
              j = poem_selection.length + 1;
            }
          }
          else{
            i--;
          }
        }
        console.log(reply, data['authors'], data['titles']);
      }
    });
    /*
    T.post("direct_messages/new",{  screen_name	: name, text: 'YOUR_REPLY'}, function(err, data, response){
      console.log("sent")

    });



    var reply = "You mentioned me! @" + name + ' ' + 'You are super cool!';
    var params             = {
      status: reply,
      in_reply_to_status_id: nameID
    };

    T.post('statuses/update', params, function(err, data, response) {
      if (err !== undefined) {
        console.log(err);
      } else {
        console.log('Tweeted: ' + params.status);
      }
    })*/


  };
  /*
  T.post('statuses/update', { status: "I'm still not a robot boi" }, function(err, data, response) {
    console.log(data)

  })*/

}
//my_id('ShariarKabir14')
//get_userID('shkabir8');
setInterval(makeRun, 4000);
