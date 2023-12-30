from web3 import Web3,HTTPProvider
import json

blockchain="http://127.0.0.1:7545"
web3=Web3(HTTPProvider(blockchain))
web3.eth.defaultAccount=web3.eth.accounts[0]
print('Connected with Ganache')

artifact="../build/contracts/demo.json"

with open(artifact) as f:
    artifact_json=json.load(f)
    contract_abi=artifact_json['abi']
    contract_address=artifact_json['networks']['5777']['address']

contract=web3.eth.contract(
    abi=contract_abi,
    address=contract_address
)
print('Smart Contract Selected')

# assign function
tx_hash=contract.functions.assign("Hi CSE IV Years").transact()
web3.eth.waitForTransactionReceipt(tx_hash)

# print function
m=contract.functions.print().call()
print(m)