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
let radius = 10 + 1 * 30;

const notes = [
  new Note("C", "red"),
  new Note("D", "orange"),
  new Note("E", "yellow"),
  new Note("F", "green"),
  new Note("G", "blue"),
  new Note("A", "indigo"),
  new Note("B", "violet"),
];

let waves = []; // Array to store waveforms

function setup() {
  createCanvas(window.innerWidth, window.innerHeight);
  //noLoop();
}

function draw() {
  background(0);
  stroke(255);

  for (let i = 1; i < 10; i++) {
    const octave = i * 25;
    noFill();
    circle(CENTER_X, CENTER_Y, octave);
  }

  // Draw all the stored waves
  for (let wave of waves) {
    drawWave(wave.color, wave.radius, wave.frequency);
  }
}

// Create a circular graph of the wave
function drawWave(color, radius, frequency) {
  noFill();
  stroke(color);
  const speed = frameCount * 0.1;

  beginShape();
  for (let i = 0; i < 360; i++) {
    let angle = radians(i); // Convert degrees to radians
    let amplitude = 5;
    let r = radius + sin(angle * frequency + speed) * amplitude;
    let x = r * cos(angle) + CENTER_X;
    let y = r * sin(angle) + CENTER_Y;
    curveVertex(x, y);
  }
  endShape(CLOSE);
}

function mousePressed() {
  const octave = int(random(1, 10));
  const note = int(random(0, 7));
  const radius = (octave * 25) / 2;

  // Modify the alpha value of the color
  const colorStroke = color(notes[note].color);
  let transparentColor = color(notes[note].color);
  transparentColor.setAlpha(100);

  let frequency = random(16, 8000);

  // Store the wave data in the array
  waves.push({
    color: colorStroke,
    radius: radius,
    frequency: frequency,
  });
}
