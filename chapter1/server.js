/**
 * TCP socket server
 */
var net = require('net');

net.createServer(function(conn) {
    console.log('listen port 3001');

    conn.write('\n');
    conn.pipe(conn);

    conn.on('close', function() {
        console.log('disconnect...');
    });
}).listen(3001);
