const mongoose = require('mongoose');
var moment = require('moment');

module.exports = () => {
  function connect() {
    mongoose.connect('mongodb://localhost:27017/SmartDoor',
      function (error) {
        if (error) {
          console.error('mongodb connection error', error);
        }
        else {
          var time = moment().format("YYYY-MM-DD HH:mm:ss");
          console.log(time + " MongoDB Connected !!");
        }
      });
  }
  connect();
  mongoose.connection.on('disconnected', connect);
};