var fs = require('fs');

// fs.appendFile()메서드는 지정된 콘텐츠를 파일에 추가. 파일이 없으면 파일을 생성.
// fs.appendFile('mynewfile1.txt', 'Hello content!', function (err) {
//   if (err) throw err;
//   console.log('Saved!');
// }); 

// fs.open()메서드는 "플래그"를 두 번째 인수로 사용하며 플래그가 "쓰기"에 대해 "w"이면 지정된 파일이 쓰기를 위해 열림. 파일이 없으면 빈 파일이 생성.
// fs.open('mynewfile2.txt', 'w', function (err, file) {
//   if (err) throw err;
//   console.log('Saved!');
// }); 

// fs.writeFile()메서드는 지정된 파일과 콘텐츠가있는 경우, 이를 대체. 파일이 없으면 지정된 내용을 포함하는 새 파일이 생성.
// fs.writeFile('mynewfile3.txt', 'Hello content!', function (err) {
//   if (err) throw err;
//   console.log('Saved2!');
// }); //Open or Save

// fs.appendFile()메서드는 지정된 파일의 끝에 지정된 콘텐츠를 추가.
// fs.appendFile('mynewfile1.txt', ' This is my text.', function (err) {
//     if (err) throw err;
//     console.log('Updated!');
//   });

// fs.writeFile()메서드는 지정된 파일과 콘텐츠를 바꿈.
// fs.writeFile('mynewfile3.txt', 'This is my text', function (err) {
//   if (err) throw err;
//   console.log('Replaced!');
// });

// fs.unlink()메서드는 지정된 파일을 삭제
// fs.unlink('mynewfile2.txt', function (err) {
//     if (err) throw err;
//     console.log('File deleted!');
//   });

// fs.rename()메서드는 지정된 파일의 이름을 바꿈.
// fs.rename('mynewfile1.txt', 'myrenamedfile.txt', function (err) {
//   if (err) throw err;
//   console.log('File Renamed!');
// });