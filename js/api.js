const {assign,print} = require('./ledger');
const express=require('express');
const url=require('url');

var api=express();

api.get('/assign',async function(req,res){
    var urldata=url.parse(req.url,true);
    var wallet=urldata.query.wallet;
    var b=urldata.query.b;

    const response=await assign(wallet,b);
    res.send({'response':response});
});

api.get('/print',async function(req,res){
    var urldata=url.parse(req.url,true);
    var wallet=urldata.query.wallet;

    const response=await print(wallet);
    console.log(response);
    res.send({'response':response});
});

api.listen(2000,function(){
    console.log('API Server Started');
});