
console.log('start')
var Twit = require('twit')

var config = require('./config');
var T = new Twit(config);
var games = []



var makeRun = function(){
  var stream = T.stream('statuses/filter', { track: ['@ShariarKabir14'] });
  stream.on('tweet', tweetEvent);
  //stream.on('message', function (msg) {
  //  console.log('u got a message');

  //})
  function tweetEvent(tweet) {
    console.log("heyyy");
    // Who sent the tweet?
    var name = tweet.user.screen_name;
    var my_user_id = tweet.user.id;
    // What is the text?
    // var txt = tweet.text;
    // the status update or tweet ID in which we will reply
    var nameID  = tweet.id_str;

    T.post("direct_messages/new",{  screen_name	: name, text: 'YOUR_REPLY'}, function(err, data, response){
      console.log("sent")

    });

    var reply = "You mentioned me! @" + name + ' ' + 'You are super cool!';
    var params             = {
      status: reply,
      in_reply_to_status_id: nameID
    };
    /*
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
