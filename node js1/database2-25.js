const express=require('express')
const {MongoClient}=require('mongodb')
const app=express();


const url='mongodb://localhost:27017'

const client=new MongoClient(url)

async function dbconnects(){
    let result=await client.connect();
    let db=result.db('mys')
    return db.collection('you')
}

// dbconnects().then((ses)=>{
//     ses.find().toArray().then((date)=>{
//         console.warn(date)
//     })
// })

app.get('/1',async(nep,seps)=>{
    let check=await dbconnects()
    // let chext=await check.insertOne({name:"hp laptop"})
    let checks=await check.find().toArray();
    seps.send(checks)

})
app.listen(3500)