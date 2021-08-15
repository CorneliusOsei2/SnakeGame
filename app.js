
const canvas = document.getElementById('game')

// Get context from Canvas to draw on the screen
const ctx = canvas.getContext('2d')

let speed = 7;

let tileCount = 20;
let tileSize = canvas.width / tileCount - 2;

// Snake properties
let headX = 10;
let headY = 10;



const drawGame = () => {
    clearScreen();
    drawSnake();
    setTimeout(drawGame, 1000 / speed)
}

const clearScreen = () => {
    ctx.fillStyle = 'black'
    ctx.fillRect(0, 0, canvas.width, canvas.height)
}

drawGame()