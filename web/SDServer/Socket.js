var SocketIO = require('socket.io');
var moment = require('moment');

module.exports = (server) => {
    var io = SocketIO(server);
    
    console.log("소켓IO 서버 오픈");

    io.on('connection', function (socket) {
        console.log("유저가 접속하였습니다 :: ", moment().format("YYYY-MM-DD HH:mm:ss"));

        socket.on('Token', function (data) {
            console.log(data);
        });
        
        socket.on('Camera', function(img){
            console.log(img);
            io.emit('Image',img);
        });

        socket.on('MobileMsg', function (data) {
            console.log(data);
            io.emit('MobileMsg', data);
        });

        socket.on('DoorMsg', function (data) {
            console.log(data);
            io.emit('DoorMsg', data);
        });
    });
};