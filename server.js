const express = require('express')
const app= express()

app.set('view engine','ejs')

app.get('/',(req,res)=>{
    console.log("base route")
    res.render("index")
        })


app.get('/hello',(req,res)=>{
    console.log("api call logged")
    res.download("server.js")
})

app.get('/about',(req,res)=>{
    res.send("about page")
})
app.listen(3000)
