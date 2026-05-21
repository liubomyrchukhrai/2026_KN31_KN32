const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");
const scoreElement = document.getElementById("score");

const cell = 20;
const w = canvas.width;
const h = canvas.height;

class SnakeLogic {
    constructor(width, height, cellSize) {
        this.width = width;
        this.height = height;
        this.cellSize = cellSize;
        this.reset();
    }

    reset() {
        this.snake = [{x: 100, y: 100}, {x: 80, y: 100}, {x: 60, y: 100}];
        this.direction = "RIGHT";
        this.score = 0;
        this.food = this._generateFood();
        this.gameOver = false;
    }

    _generateFood() {
        const x = Math.floor(Math.random() * (this.width / this.cellSize)) * this.cellSize;
        const y = Math.floor(Math.random() * (this.height / this.cellSize)) * this.cellSize;
        return {x, y};
    }

    move() {
        let headX = this.snake[0].x;
        let headY = this.snake[0].y;

        if (this.direction === "UP") headY -= this.cellSize;
        else if (this.direction === "DOWN") headY += this.cellSize;
        else if (this.direction === "LEFT") headX -= this.cellSize;
        else if (this.direction === "RIGHT") headX += this.cellSize;

        const newHead = {x: headX, y: headY};


        const hitSelf = this.snake.some(segment => segment.x === newHead.x && segment.y === newHead.y);
        if (headX < 0 || headX >= this.width || headY < 0 || headY >= this.height || hitSelf) {
            this.gameOver = true;
            return;
        }

        this.snake.unshift(newHead);


        if (newHead.x === this.food.x && newHead.y === this.food.y) {
            this.score += 1;
            scoreElement.innerText = "Рахунок: " + this.score;
            this.food = this._generateFood();
        } else {
            this.snake.pop();
        }
    }

    changeDirection(newDir) {
        const opposites = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"};
        if (newDir !== opposites[this.direction]) {
            this.direction = newDir;
        }
    }
}


const game = new SnakeLogic(w, h, cell);


document.addEventListener("keydown", (event) => {
    if (event.key === "ArrowUp") game.changeDirection("UP");
    if (event.key === "ArrowDown") game.changeDirection("DOWN");
    if (event.key === "ArrowLeft") game.changeDirection("LEFT");
    if (event.key === "ArrowRight") game.changeDirection("RIGHT");
});


function gameLoop() {
    if (game.gameOver) {
        alert("Гра закінчена! Ваш рахунок: " + game.score);
        game.reset();
        scoreElement.innerText = "Рахунок: 0";
    }

    game.move();

  
    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, w, h);


    ctx.fillStyle = "lime";
    game.snake.forEach(segment => {
        ctx.fillRect(segment.x, segment.y, cell, cell);
    });

    ctx.fillStyle = "red";
    ctx.fillRect(game.food.x, game.food.y, cell, cell);
}


setInterval(gameLoop, 100);
