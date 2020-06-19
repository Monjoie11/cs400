from flask import Flask, jsonify, request, send_from_directory
from wallet import Wallet
from flask_cors import CORS
from blockchain import Blockchain


app = Flask(__name__)
wallet = Wallet()
blockchain = Blockchain(wallet.public_key)
CORS(app) 


@app.route('/', methods=['GET'])
def get_ui():
    return send_from_directory('ui', 'node.html')


@app.route('/wallet', methods=['POST'])
def create_key():
    wallet.create_keys()
    if wallet.save_keys():
        global blockchain
        blockchain = Blockchain(wallet.public_key)
        response = {
            'public_key': wallet.public_key,
            'private_key': wallet.private_key,
            'funds': blockchain.get_balance()
        }
        return jsonify(response), 201
    else:
        response = {
            'message': 'perhaps you locked your keys in your car'
        }
        return jsonify(response), 500


@app.route('/wallet', methods=['GET'])
def load_keys():
    if wallet.load_keys():
        global blockchain
        blockchain = Blockchain(wallet.public_key)
        response = {
            'public_key': wallet.public_key,
            'private_key': wallet.private_key,
            'funds': blockchain.get_balance()
        }
        return jsonify(response), 201
    else:
        response = {
            'message': 'no hay llaves, senyor'
        }
        return jsonify(response), 500

@app.route('/balance', methods=['GET'])
def get_balance():
    balance = blockchain.get_balance()
    if balance != None:
        response = {
            'message': 'Fetched balance succesfully',
            'fund': balance
        }
        return jsonify(response), 201
    else:
        response = {
            'message': 'Loading balance no bueno',
            'wallet_set_up': wallet.public_key != None
        }
        return jsonify(response), 500


@app.route('/chain', methods=['GET'])
def get_chain():
    chain_snapshot = blockchain.chain
    dict_chain =[block.__dict__.copy() for block in chain_snapshot]
    for dict_block in dict_chain:
        dict_block['transactions'] = [tx.__dict__ for tx in dict_block['transactions']]
    return jsonify(dict_chain), 200


@app.route('/transaction', methods=['POST'])
def add_transaction():
    if wallet.public_key == None:
        response = {
            'message': "you're wallet ain't here"
        }
        return jsonify(response), 411
    values = request.get_json()
    if not values:
        response = {
            'message': 'Homie, you gotta get your game right'
        }
        return jsonify(response), 403
    required_fields =['recipient', 'amount']
    if not all(field in values for field in required_fields):
        response = {
            'message': 'not all fields fielded in the playing field' 
        }
        return jsonify(response), 418
    recipent = values['recipient']
    amount = values['amount']
    signature = wallet.sign_transaction(wallet.public_key, recipent, amount)
    success = blockchain.add_transaction(recipent, wallet.public_key, signature, amount)
    #I dont like this; it only underscores the fact that add tarnsaction shoulod take a transcation object that we should dictify below
    if success:
        response = {
            'message': 'successfully added transaction',
            'transaction': {
                'sender': wallet.public_key,
                'recipent': recipent,
                'amount': amount,
                'signature': signature
            },
            'funds': blockchain.get_balance()
        }
        return jsonify(response), 201
    else:
        response = {
            'message': 'adding transaction no bueno'
        }
        return jsonify(response), 201


@app.route('/transactions', methods=['GET'])
def get_open_transactions():
    transactions = blockchain.get_open_transactions()
    dict_transactions = [tx.__dict__ for tx in transactions]
    return jsonify(dict_transactions), 200


@app.route('/mine', methods=['POST'])
def mine():
    block = blockchain.mine_block()
    if block != None:
        dict_block = block.__dict__.copy()
        dict_block['transactions'] = [tx.__dict__ for tx in dict_block['transactions']]
        response = {
            
            'message': 'Block added succesfully',
            'block': dict_block,
            'funds': blockchain.get_balance()
        }
        return jsonify(response), 201
    else:
        response = {
            'message': 'Adding a block failed,',
            'wallet_set_up': wallet.public_key != None
        }
    return jsonify(response), 511


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)