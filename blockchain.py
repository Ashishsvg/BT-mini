import hashlib, json, time
from uuid import uuid4
from flask import Flask, jsonify, request

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.create_block(previous_hash='1', nonce=100)

    def create_block(self, nonce, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
            'transactions': self.current_transactions,
            'nonce': nonce,
            'previous_hash': previous_hash,
            'hash': ''
        }
        block['hash'] = self.hash(block)
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        encoded = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_nonce):
        nonce = 0
        while self.valid_proof(last_nonce, nonce) is False:
            nonce += 1
        return nonce

    @staticmethod
    def valid_proof(last_nonce, nonce):
        guess = f'{last_nonce}{nonce}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            prev_block = self.chain[i - 1]
            curr_block = self.chain[i]
            if curr_block['previous_hash'] != prev_block['hash']:
                return False
            if curr_block['hash'] != self.hash(curr_block):
                return False
        return True
