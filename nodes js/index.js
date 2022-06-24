const  http=require('http')

http.createServer((res,rep)=>{
    rep.write('hello world');
    rep.end();

}).listen(7000)