//Загрузка модуля HTTP
const http = require("http");
const hostname = "localhost";
const port = 8080;

//Создание HTTP-сервера
const server = http.createServer((req, res) => {
  //Установка HTTP-заголовков ответа с HTTP-статусом и Content type
  res.statusCode = 200;
  res.setHeader("Content-Type", "text/plain");
  res.end("Hello World\n");
});

//Слушание запросов на порту 3000, и в качестве каллбака функция, которая пишет в лог
server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});