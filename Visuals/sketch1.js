class Note {
  constructor(name, color) {
    this._name = name;
    this._color = color;
  }

  get name() {
    return this._name;
  }

  get color() {
    return this._color;
  }
}

const CENTER_X = window.innerWidth / 2;
const CENTER_Y = window.innerHeight / 2;
let radius = 100;

const notes = [
  new Note("C", "red"),
  new Note("D", "orange"),
  new Note("E", "yellow"),
  new Note("F", "green"),
  new Note("G", "blue"),
  new Note("A", "indigo"),
  new Note("B", "violet")
];

function setup() {
  createCanvas(window.innerWidth, window.innerHeight);
  //noLoop();
}

function draw() {
  background(0);
  stroke(255);
  //strokeWeight(2);

  // for (let i = 0; i < 8; i++) {
  //   const radius = 10 + i * 30;
  //   noFill();
  //   circle(CENTER_X, CENTER_Y, radius);
  // }

  
  translate(CENTER_X, CENTER_Y);
  noFill();
  beginShape();
  for (var i = 0; i < 360; i++) {
    var angle = radians(i); // Convert degrees to radians
    var r = sin(angle) * radius;
    var x = r * cos(i);
    var y = r * sin(i);
    vertex(x, y);
  }
  endShape();

}

function mousePressed() {
  const octave = int(random(0, 8));
  const note = int(random(0, 7));
  const radius = 10 + octave * 30;

  // Modify the alpha value of the color
  const colorStroke = color(notes[note].color);
  var transparentColor = color(notes[note].color);
  transparentColor.setAlpha(100); // Set the alpha value (0-255)

  newTone(radius, radius, colorStroke, transparentColor)
}

function newTone(radius, growRadius, color, transparentColor) {  
  stroke(color);
  strokeWeight(2);

  fill(transparentColor);
  //circle(CENTER_X, CENTER_Y, growRadius);
  
  noFill();
  circle(CENTER_X, CENTER_Y, radius);
}
