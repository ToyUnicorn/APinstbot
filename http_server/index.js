import express, { response } from 'express';
import {requestTime} from './middleware.js';

const app = express();
const hostname = "localhost";
const port = 3000;

// Обработчик middleWare - перед запросом
app.use(requestTime);

app.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

app.route('/')
  .get((req, res) => {
    res.send('123otvet');
  })
  .post((req, res) => {
    console.log('Add a record', req.test);
    res.send('ok');
  })
  .put((req, res) => {
    res.send('Update the record');
  });