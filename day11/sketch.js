let avatarImg;
let avatarPos = {"x": 0, "y": 0};
const AVATAR_SPEED = 10;
const OPPONENT_MAX_SPEED = 10;

const IMG_WIDTH = 75;
const IMG_HEIGHT = 100;

let otherPos = {"x": 0, "y": 0};
let otherVel = {"x": 0, "y": 1};

function setup(){
  createCanvas(500,500);
  avatarImg = loadImage("avatar.png");
  textSize(50);
}

let KEY_CODES = {
  "a": 65,
  "d": 68,
  "w": 87,
  "s": 83
}

let points = 0;
let ct = 0;

function draw(){
  background("#00ffff");
  fill(0,0,0);
  text("Points: "+points, width/2, 50); 
  ct += 1;

  image(avatarImg, avatarPos.x, avatarPos.y, IMG_WIDTH, IMG_HEIGHT);

  push();
  translate(otherPos.x+IMG_WIDTH/2, otherPos.y+IMG_HEIGHT/2);
  scale(-1, 1);
  image(avatarImg, -IMG_WIDTH/2, -IMG_HEIGHT/2, IMG_WIDTH, IMG_HEIGHT);
  pop();

  otherPos.x += otherVel.x;
  otherPos.y += otherVel.y;

  // lets make the opponent move around randomly
  if (ct % 100 == 0){
    otherVel.x = (random()-0.5)*OPPONENT_MAX_SPEED;
    otherVel.y = (random()-0.5)*OPPONENT_MAX_SPEED;
  }
  if(otherPos.x < 0){
    otherVel.x = Math.abs(otherVel.x);
    console.log("x < 0");
  }
  if(otherPos.x + IMG_WIDTH > width){
    otherVel.x = -Math.abs(otherVel.x);
    console.log("x > w");
  }
  if(otherPos.y < 0){
    otherVel.y = Math.abs(otherVel.y);
    console.log("y < 0");
  }
  if(otherPos.y + IMG_HEIGHT > height){
    otherVel.y = -Math.abs(otherVel.y);
    console.log("y > h");
  }

  if(keyIsDown(KEY_CODES["a"]) && avatarPos.x > 0){
    avatarPos.x -= AVATAR_SPEED;
  }
  if(keyIsDown(KEY_CODES["d"]) && avatarPos.x + IMG_WIDTH < width){
    avatarPos.x += AVATAR_SPEED;
  }
  if(keyIsDown(KEY_CODES["w"]) && avatarPos.y > 0){
    avatarPos.y -= AVATAR_SPEED;
  }
  if(keyIsDown(KEY_CODES["s"]) && avatarPos.y + IMG_HEIGHT < height){
    avatarPos.y += AVATAR_SPEED;
  }


  if(otherPos.x + IMG_WIDTH > avatarPos.x && avatarPos.x + IMG_WIDTH > otherPos.x && 
    otherPos.y + IMG_HEIGHT > avatarPos.y && avatarPos.y + IMG_HEIGHT > otherPos.y){
    points += 1;
  }

}


