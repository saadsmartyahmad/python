const express=require('express')
const app=express()

app.get('',(req,resp)=>{
    resp.send('courses')

})

app.get('/list',(res,rep)=>{
    rep.send('list of courses')
})
app.get('/java',(res,rep)=>{
    rep.send('java full stack with reat')
})
app.get('/python',(res,rep)=>{
    rep.send('python full stack with reat')
})
app.get('/java script',(res,rep)=>{
    rep.send('node js react js angular js express js mongo db')
})

app.get('/data base',(res,rep)=>{
    rep.send('mongo db oracle my sql')
})
app.listen(8000)