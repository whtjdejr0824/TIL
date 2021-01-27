var http = require('http');

//create a server objects:
http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  //write a response to the client
  res.end('Hello World!<br>John Homepage<br>Welcome to my home<br><table><tr><td>THIS IS TABLE</td></tr></table><br><br><img src=\'https://www.cleverfiles.com/howto/wp-content/uploads/2018/03/minion.jpg\'>'); 
  // end the response
}).listen(8080); // the server object listen on port 8080

console.log('This example is different!');
console.log('The result is displayed in the Command Line Interface');

