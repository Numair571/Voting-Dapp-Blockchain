from web3 import Web3,HTTPProvider
import json

blockchain="http://127.0.0.1:7545"

def connect_with_demo(wallet):
    # Step - 1: Connect with Blockchain Server
    web3=Web3(HTTPProvider(blockchain))
    print('Connected with Ganache')

    # Step - 2: ABI, Contract Address
    with open('../build/contracts/demo.json') as f:
        artifact_json=json.load(f)
        contract_abi=artifact_json['abi']
        contract_address=artifact_json['networks']['5777']['address']
    
    # Step - 3: Connect with Contract
    web3.eth.defaultAccount=wallet
    contract=web3.eth.contract(
        abi=contract_abi,
        address=contract_address
    )
    return (web3,contract)

# Sub - Functions
def assign(wallet,b):
    try:
        web3,contract=connect_with_demo(wallet)
        tx_hash=contract.functions.assign(b).transact()
        web3.eth.waitForTransactionReceipt(tx_hash)
        return 'transaction done'
    except:
        return 'transaction failed'

def prin(wallet):
    try:
        web3,contract=connect_with_demo(wallet)
        data=contract.functions.print().call()
        return data
    except:
        return 'transaction failed'