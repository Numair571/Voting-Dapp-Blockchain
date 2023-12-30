const {Web3,HttpProvider} = require('web3');
const fs=require('fs');
const { resolve } = require('path');

blockchain="http://127.0.0.1:7545"

const httpprovider=new HttpProvider(blockchain);
const web3=new Web3(httpprovider);

artifact_demo="../build/contracts/demo.json";

function assign(wallet,b) {
    var data=fs.readFileSync(artifact_demo,"utf-8");
    data=JSON.parse(data);
    contract_abi=data['abi'];
    contract_address=data['networks']['5777']['address'];

    contract=new web3.eth.Contract(contract_abi,contract_address);
    console.log('Contract Selected');
    try {
        
        contract.methods.assign(b).send({
            from: wallet,
            gas: 1000000,
            gasPrice: 1000000000000
        }).then((data)=>{
            console.log(data);
        })   
    } catch (error) {
        console.log(error);
        return 'Transaction Failed'
    }

    return 'Transaction Done    '

}

async function print(wallet) {
    
    var data=fs.readFileSync(artifact_demo,"utf-8");
    data=JSON.parse(data);
    contract_abi=data['abi'];
    contract_address=data['networks']['5777']['address'];

    contract=new web3.eth.Contract(contract_abi,contract_address);
    console.log('Contract Selected');

    try {
        response=await contract.methods.print().call();
        console.log(response);
        return response;
    } catch (error) {
        console.log(error);
        return 'something went wrong'
    }
}

module.exports={
    assign,
    print
}