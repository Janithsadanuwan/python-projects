import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    def hash(self, block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

blockchain = Blockchain()
t1 = blockchain.new_transaction('Lucas', 'José', 100)
t2 = blockchain.new_transaction('José', 'Lucas', 50)
t3 = blockchain.new_transaction('Lucas', 'José', 25)
blockchain.new_block(proof=23334)

t4 = blockchain.new_transaction('José', 'Lucas', 35)
t5 = blockchain.new_transaction('Lucas', 'José', 40)
t6 = blockchain.new_transaction('José', 'Lucas', 15)
blockchain.new_block(proof=22321)

print(blockchain.chain)
