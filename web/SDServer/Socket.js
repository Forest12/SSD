var SocketIO = require('socket.io');
var moment = require('moment');

module.exports = (server) => {
    var io = SocketIO(server);
    console.log("소켓IO 서버 오픈");

    io.on('connection', function (socket) {
        console.log("유저가 접속하였습니다 :: ", moment().format("YYYY-MM-DD HH:mm:ss"));

        socket.on('chat', function (data) {
            var msg = {
                name: data.name,
                msg: data.msg,
                createdAt: moment().format("YYYY-MM-DD HH:mm:ss")
            };
            io.emit('broadcast', msg);
            console.log(data);
        });

        socket.on('Camera', function(img){
            io.emit('Mobile',img);
        });
    });
};