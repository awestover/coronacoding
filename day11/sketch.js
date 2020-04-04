
let avatarImg;

function setup(){
  createCanvas(500,500);
  avatarImg = loadImage("avatar.png");
}

function draw(){
  background("#00ffff");
  image(avatarImg, 10,10, 75, 100);
  if(keyIsDown(65)){// "a"
    alert("65");
  }
}


