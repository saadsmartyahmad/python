const {MongoClient}=require('mongodb')

const url='mongodb://localhost:27017'

const client=new MongoClient(url)

async function dbconnects(){
    let result=await client.connect();
    let db=result.db('mys')
    return db.collection('you')
}

dbconnects().then((ses)=>{
    ses.find().toArray().then((date)=>{
        console.warn(date)
    })
})