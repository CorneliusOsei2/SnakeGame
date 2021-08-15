
const canvas = document.getElementById('game')

// Get context from Canvas to draw on the screen
const ctx = canvas.getContext('2d')

let speed = 7;

let tileCount = 20;
let tileSize = canvas.width / tileCount - 2;

// Snake properties
let headX = 10;
let headY = 10;

// Snake movement
// Controlled by Keyboard
let xVelocity = 0;
let yVelocity = 0;

const drawGame = () => {
    clearScreen();
    changeSnakePosition();
    drawSnake();
    setTimeout(drawGame, 1000 / speed)
}

const clearScreen = () => {
    ctx.fillStyle = 'black'
    ctx.fillRect(0, 0, canvas.width, canvas.height)
}


const drawSnake = () => {
    ctx.fillStyle = 'orange'
    ctx.fillRect(headX * tileCount, headY * tileCount, tileCount, tileCount)
}

const changeSnakePosition = () => {
    headX = headX + xVelocity;
    headY = headY + yVelocity;
}


const keyMovement = (event) => {
    // Go up
    if (event.keyCode == 38) {
        if (yVelocity == 1) {
            return
        }
        yVelocity = -1;
        xVelocity = 0;
    }

    // Go down
    if (event.keyCode == 40) {
        if (yVelocity == -1) {
            return
        }
        yVelocity = 1
        xVelocity = 0
    }

    // Go left
    if (event.keyCode == 37) {
        if (xVelocity == 1) {
            return
        }
        yVelocity = 0
        xVelocity = -1
    }

    // Go right
    if (event.keyCode == 39) {
        if (xVelocity == -1) {
            return
        }
        yVelocity = 0
        xVelocity = 1
    }
}

document.body.addEventListener('keydown', keyMovement)


drawGame();