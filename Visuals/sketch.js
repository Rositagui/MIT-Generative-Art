class Note {
  constructor(name, color, frequencies) {
    this._name = name;
    this._color = color;
    this._frequency = frequencies;
  }
}

const notes = [
  new Note("C", "red",    [16.35, 32.70, 65.41, 130.81, 261.63, 523.25,	1046.50, 2093.00, 4186.01]),
  new Note("D", "orange", [18.35, 36.71, 73.42, 146.83, 293.66, 587.33, 1174.66, 2349.32, 4698.63]),
  new Note("E", "yellow", [20.60, 41.20, 82.41, 164.81, 329.63, 659.25, 1318.51, 2637.02, 5274.04]),
  new Note("F", "green",  [21.83, 43.65, 87.31, 174.61, 349.23, 698.46, 1396.91, 2793.83, 5587.65]),
  new Note("G", "blue",   [24.50, 49.00, 98.00, 196.00, 392.00, 783.99, 1567.98, 3135.96, 6271.93]),
  new Note("A", "indigo", [27.50, 55.00, 110.00, 220.00, 440.00, 880.00, 1760.00, 3520.00, 7040.00]),
  new Note("B", "violet", [30.87, 61.74, 123.47, 246.94, 493.88, 987.77, 1975.53, 3951.07, 7902.13]),
];

const CENTER_X = window.innerWidth / 2;
const CENTER_Y = window.innerHeight / 2;


let waves = []; // Array to store waveforms

function setup() {
  createCanvas(window.innerWidth, window.innerHeight);
}

function draw() {
  background(0);
  stroke(255);

  // Draw main circles/octaves
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

// Detect note sound
function mousePressed() {
  const octave = int(random(0, 9));
  const noteId = int(random(0, 7));
  
  const actualNote = notes[noteId];
  
  const radius = ((octave + 1) * 25) / 2;
  const colorStroke = color(actualNote._color);
  const frequency = actualNote._frequency[octave];
  
  console.log(actualNote._name);
  console.log(frequency);

  // Store the wave data in the array
  waves.push({
    color: colorStroke,
    radius: radius,
    frequency: frequency,
  });
}
