const express=require('express')
const app=express()

app.get('',(req,resp)=>{
    resp.send('hello world')

})

app.get('/hello',(res,rep)=>{
    rep.send('contact.js file')
})
app.listen(7600)