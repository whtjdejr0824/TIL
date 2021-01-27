var http = require('http');
var formidable = require('formidable');
var fs = require('fs');

http.createServer(function (req, res) {
  if (req.url == '/fileupload') { // '/fileupload'(제출클릭시 해당 페이지로 이동하여'File uploaded'표시)
    var form = new formidable.IncomingForm();
    form.parse(req, function (err, fields, files) {
      var oldpath = files.filetoupload.path; //파일이 서버에 성공적으로 업로드되면 임시 폴더에 저장. 
      var newpath = 'C:/Users/name/' + files.filetoupload.name; // 이 디렉토리의 경로는 "files"객체에서 찾을 수 있으며 parse()메서드의 콜백 함수 에서 세 번째 인수로 전달됨.
      // 선택한 폴더로 파일을 이동하려면 파일 시스템 모듈을 사용하고 파일 이름을 바꿈.
      fs.rename(oldpath, newpath, function (err) {
        if (err) throw err;
        res.write('File uploaded and moved!');
        res.end();
      });
 });
  } else { // 이 코드는 HTML '파일업로드', '제출'버튼기능을 생성.
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write('<form action="fileupload" method="post" enctype="multipart/form-data">');
    res.write('<input type="file" name="filetoupload"><br>');
    res.write('<input type="submit">');
    res.write('</form>');
    return res.end();
  }
}).listen(8080);





