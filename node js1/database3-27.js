const express=require('express')
const { appendFileSync } = require('fs')
const {MongoClient}=require('mongodb')
const app=express()

const url='mongodb://localhost:27017'
const client=new MongoClient(url)

async function data(){
    let result=await client.connect()
    let db=result.db('mys')
    return db.collection('you')
}

app.get('/datbase',async(re,rep)=>{
    let id=await data();
    let ids=await id.find().toArray()

    rep.send(ids)
})
app.listen(5500)