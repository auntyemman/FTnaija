console.log('welcome mole');

// creating new channels websocket for this app
const socket = new WebSocket('ws://' + window.location.host + '/ws/mole/'); // making it static for now.
console.log(socket);

socket.onmessage = function(e) {
    console.log('Server: ' + e.data);
};

socket.onopen = function(e) {
    socket.send(JSON.stringify({
        'message': 'hello from the client',
        'sender': 'mole',
    }));
};