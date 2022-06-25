const {MongoClient}=require('mongodb')
const url='mongodb://localhost:27017'
const client=new MongoClient(url)

async function dbconnect(){
    let result=await client.connect()
    let db=result.db('mys')
    return db.collection('you')   
}
// dbconnect().then((resp)=>{
//     resp.find().toArray().then((data)=>{
//         console.warn(data)
//     })
// })
module.exports=dbconnect