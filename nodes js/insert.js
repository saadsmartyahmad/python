const dbconnect=require('./mongo1')

const insert=async()=>{
    let data= await dbconnect();
    let result=data.insertOne({name:"solution"})
    if((await result).acknowledged){
        console.log('data inserted')
    }
}

insert()