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

function draw(){
  background("#00ffff");
  fill(0,0,0);
  text("Points: "+points, width/2, 50);

  image(avatarImg, avatarPos.x, avatarPos.y, IMG_WIDTH, IMG_HEIGHT);

  push();
  translate(otherPos.x, otherPos.y);
  scale(-1, 1);
  image(avatarImg, 0, 0, 75, 100);
  pop();

  otherPos.x += otherVel.x;
  otherPos.y += otherVel.y;

  // lets make the opponent move around randomly
  if (random() < 0.05){
    otherVel.x = random()*OPPONENT_MAX_SPEED/2;
    otherVel.y = random()*OPPONENT_MAX_SPEED/2;
  }
  if(otherPos.x < 0){
    otherVel.x = Math.abs(otherVel.x);
  }
  if(otherPos.x + IMG_WIDTH > width){
    otherVel.x = -Math.abs(otherVel.x);
  }
  if(otherPos.y < 0){
    otherVel.y = Math.abs(otherVel.y);
  }
  if(otherPos.y + IMG_HEIGHT > height){
    otherVel.y = -Math.abs(otherVel.y);
  }

  if(keyIsDown(KEY_CODES["a"])){
    avatarPos.x -= AVATAR_SPEED;
  }
  if(keyIsDown(KEY_CODES["d"])){
    avatarPos.x += AVATAR_SPEED;
  }
  if(keyIsDown(KEY_CODES["w"])){
    avatarPos.y -= AVATAR_SPEED;
  }
  if(keyIsDown(KEY_CODES["s"])){
    avatarPos.y += AVATAR_SPEED;
  }


  if(otherPos.x + IMG_WIDTH > avatarPos.x && avatarPos.x + IMG_WIDTH > otherPos.x && 
    otherPos.y + IMG_HEIGHT > avatarPos.y && avatarPos.y + IMG_HEIGHT > otherPos.y){
    points += 1;
  }

}


