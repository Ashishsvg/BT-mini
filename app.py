from flask import Flask, render_template, request, redirect, url_for, flash
from blockchain import Blockchain
import uuid

app = Flask(__name__)
app.secret_key = "blockchain-demo"
blockchain = Blockchain()

# Unique node id (simulates a wallet)
node_identifier = str(uuid.uuid4()).replace('-', '')[:8]

@app.route('/')
def index():
    balance = calc_balance(node_identifier)
    return render_template('index.html', address=node_identifier, balance=balance)

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        sender = node_identifier
        recipient = request.form['recipient']
        amount = int(request.form['amount'])
        blockchain.new_transaction(sender, recipient, amount)
        flash('Transaction added to mempool!', 'success')
        return redirect(url_for('send'))
    return render_template('send.html')

@app.route('/mine')
def mine():
    last_block = blockchain.last_block
    last_nonce = last_block['nonce']
    nonce = blockchain.proof_of_work(last_nonce)
    blockchain.new_transaction(sender="0", recipient=node_identifier, amount=10)
    previous_hash = last_block['hash']
    block = blockchain.create_block(nonce, previous_hash)
    flash(f'Block {block["index"]} mined successfully!', 'success')
    return redirect(url_for('view_chain'))

@app.route('/chain')
def view_chain():
    valid = blockchain.is_chain_valid()
    return render_template('chain.html', chain=blockchain.chain, valid=valid)

def calc_balance(address):
    bal = 0
    for block in blockchain.chain:
        for tx in block['transactions']:
            if tx['recipient'] == address:
                bal += tx['amount']
            if tx['sender'] == address:
                bal -= tx['amount']
    return bal

if __name__ == "__main__":
    app.run(debug=True)
