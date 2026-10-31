const socket = new WebSocket(`ws://${window.location.host}/systemws`);
const chat = new WebSocket(`ws://${window.location.host}/chatws`);

socket.onmessage = function (event) {
    const data = JSON.parse(event.data);
    document.getElementById('CPU').innerText = data.cpu + '% CPU';
    document.getElementById('RAM').innerText = data.ram + '% RAM';
    document.getElementById('online').innerText = data.online;
};


chat.onmessage = function(event) {
    const messages = document.getElementById('messages');
    const message = document.createElement('div');
    message.textContent = event.data;
    messages.appendChild(message);
    messages.scrollTop = messages.scrollHeight;
};

function sendMessage() {
    const input = document.getElementById('messageText');
    if (input.value) {
        chat.send(input.value);
        input.value = '';
    }
}