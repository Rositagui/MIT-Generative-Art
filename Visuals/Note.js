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

export default Note;
