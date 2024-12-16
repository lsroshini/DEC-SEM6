// server.js
const express = require('express');
const http = require('http');
const socketIo = require('socket.io');

// Initialize express and create a server
const app = express();
const server = http.createServer(app);
const io = socketIo(server);

// Serve static files from the public directory
app.use(express.static('public'));

// Listen for incoming socket connections
io.on('connection', (socket) => {
    console.log('A user connected');

    // Listen for drawing data from the client
    socket.on('drawing', (data) => {
        // Broadcast the drawing data to all other clients
        socket.broadcast.emit('drawing', data);
    });

    // Handle user disconnect
    socket.on('disconnect', () => {
        console.log('A user disconnected');
    });
});

// Start the server
const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
