// 다른 모듈을 포함하는 것과 동일한 방식으로 "대문자"패키지를 포함합니다.
var http = require('http');
var uc = require('upper-case');
http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.write(uc.upperCase("Hello World!"));
  res.end();
}).listen(8080);