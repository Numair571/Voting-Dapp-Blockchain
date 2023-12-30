from flask import Flask,request
from ledger import assign,prin

app=Flask(__name__)

@app.route('/assign',methods=['get'])
def assign1():
    wallet=request.args.get('wallet')
    b=request.args.get('b')
    id=int(request.args.get('id'))
    print(wallet,b)
    response=assign(wallet,b)
    return {'response':response}

@app.route('/print',methods=['get'])
def print1():
    wallet=request.args.get('wallet')
    print(wallet)
    response=prin(wallet)
    return {'response':response}

if __name__=="__main__":
    app.run(
        host='0.0.0.0',
        port=3000,
        debug=True
    )