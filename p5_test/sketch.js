
var serial;          // variable to hold an instance of the serialport library
var portName = '/dev/cu.usbmodem143101'; // fill in your serial port name here
var inData;                            // for incoming serial data
var outByte = 10;                       // for outgoing data
 
function setup() {
  createCanvas(displayWidth, displayHeight);          // make the canvas
  serial = new p5.SerialPort();    // make a new instance of the serialport library
  serial.on('data', serialEvent);  // callback for when new data arrives
  serial.on('error', serialError); // callback for errors
  serial.on('list', printList);       // set a callback function for the serialport list event
  serial.list();                   // list the serial ports
  
  serial.open(portName);           // open a serial port
}

function serialEvent() {
  // read a byte from the serial port:
  var inByte = serial.read();
  // store it in a global variable:
  inData = inByte;
  serial.write(outByte);
}
 
function serialError(err) {
  println('Something went wrong with the serial port. ' + err);
}

function draw() {
  background(220);
  
}