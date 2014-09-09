/**
 * TCP socket server
 */
var net = require('net');

net.createServer(function(conn) {
    conn.write('220 FreeFloat Ftp Server (Version 1.00)\n');
    conn.pipe(conn);
    conn.on('close', function() {
        console.log('disconnect...');
    });
}).listen(3001);

console.log('listen port 3001');
