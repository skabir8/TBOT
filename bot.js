
console.log('start')
var Twit = require('twit')

var config = require('./config');
var T = new Twit(config);


var makePost = function(){

  T.post('statuses/update', { status: "I'm still not a robot boi" }, function(err, data, response) {
    console.log(data)
  })

}

setInterval(makePost, 4000);
