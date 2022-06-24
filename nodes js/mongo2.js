const dbconnect=require('./mongo1')
const main=async()=>{
    let data= await dbconnect()
    data=await data.find().toArray()
    console.warn(data)
}
main();