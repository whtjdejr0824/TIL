// 파일을 열고 닫을 때 readStream 객체가 이벤트를 발생시키는 것처럼 Node.js의 객체는 이벤트를 발생시킬 수 있다.
// 내장 이벤트 모듈을 포함하려면 require() 메소드를 사용
var events = require('events');
var eventEmitter = new events.EventEmitter();

//Create an event handler:
var myEventHandler = function () {
  console.log('I hear a scream!');
}

//Assign the event handler to an event:
eventEmitter.on('scream', myEventHandler);

//Fire the 'scream' event:
eventEmitter.emit('scream');
// emit()메소드를 사용하면, EventEmitter 개체를 사용하여 이벤트 처리기를 자신의 이벤트에 할당 할 수 있다.