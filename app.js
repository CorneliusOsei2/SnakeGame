
const canvas = document.getElementById('game')

// Get context from Canvas to draw on the screen
const ctx = canvas.getContext('2d')

// Snake class
class Snake{
    constructor(x, y){
        this.x = x;
        this.y = y;
    }
}

let speed = 10;

let tileCount = 20;
let tileSize = canvas.width / tileCount - 2;

// Snake properties
let headX = 10;
let headY = 10;
const snakeParts= []
let tailLength= 2

// Fruit Properties
let fruitX = 5;
let fruitY = 5;

// Snake movement
// Controlled by Keyboard
let xVelocity = 0;
let yVelocity = 0;

// Score
let score = 0;

const drawGame = () => {
    
    changeSnakePosition();
    hitWall();

    let outcome = isGameOver()
    if (outcome) {
        return
    }

    clearScreen();

    checkFruitCollision();
    drawFruit();
    drawSnake();
    drawScore();
    setTimeout(drawGame, 1000 / speed)
}

const clearScreen = () => {
    ctx.fillStyle = 'rgb(14,14,14)'
    ctx.fillRect(0, 0, canvas.width, canvas.height)
}


const changeSnakePosition = () => {
    headX = headX + xVelocity;
    headY = headY + yVelocity;
}

const hitWall = () => {
    // Hitting left wall
    if (headX < 0){
        // isOver = true;
        headX += tileCount
    }

    // Hitting right wall
    if (headX >= tileCount){
        // isOver = true;
        headX -= tileCount
    }

    // Hitting top wall
    if (headY < 0){
        // isOver = true;
        headY += tileCount
    }

     // Hitting down wall
     if (headY >= tileCount){
        // isOver = true;
        headY -= tileCount
    }
}

const isGameOver = () => {

    if (xVelocity === 0 && yVelocity === 0){
        return false;
    }

    for (let i = 0; i < snakeParts.length; i++) {
        part = snakeParts[i];

        if (headX === part.x && headY === part.y){
            ctx.fillStyle = 'red'
            ctx.font = '28px Cambria'
            ctx.fillText('Game Over 💥', canvas.width/2 -40, canvas.width/2 -40)
            return true;
        }
    }

}

const checkFruitCollision = () => {
    if (fruitX == headX && fruitY == headY){
        fruitX = Math.floor(Math.random() * tileCount)
        fruitY = Math.floor(Math.random() * tileCount)
        tailLength++;
        score++;
    }

}


const drawSnake = () => {
    
    ctx.fillStyle = 'green';
    for (let i = 0; i < snakeParts.length; i++) {
        let part = snakeParts[i];
        ctx.fillRect(part.x * tileCount, part.y * tileCount, tileSize, tileSize)
    }

    snakeParts.push(new Snake(headX, headY))
    while (snakeParts.length > tailLength){
        snakeParts.shift();
    }

    ctx.fillStyle = 'orange'
    ctx.fillRect(headX * tileCount, headY * tileCount, tileSize, tileSize)


}

const drawFruit = () => {
    ctx.fillStyle = 'red';

    ctx.fillRect(fruitX * tileCount, fruitY * tileCount, tileSize, tileCount)
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

const drawScore = () => {
    ctx.fillStyle = 'white'
    ctx.font = '18px serif';
    ctx.fillText('Score: ' + score, canvas.width/2 -40, 15)
}

document.body.addEventListener('keydown', keyMovement)


drawGame();