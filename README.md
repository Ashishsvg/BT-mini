💸 Blockchain-Based Decentralized Money Transfer System
🧠 Overview

This project is a mini blockchain simulation that demonstrates how decentralized money transfer works using the core principles of blockchain technology.

It is built using Python (Flask) for the backend and HTML + Bootstrap for the user interface.
The system allows users to send money, mine new blocks, and view the blockchain ledger — all within a simple and interactive web app.

🚀 Features

✅ Transaction System – Users can send coins to others (simulated wallets).
✅ Blockchain Ledger – Each transaction is recorded inside blocks.
✅ Mining & Proof of Work – Blocks are mined using a simple Proof-of-Work algorithm.
✅ Chain Validation – Detects any tampering with the blockchain.
✅ Flask Web Interface – Easy-to-use UI for sending coins, viewing chain, and mining.
✅ Mining Reward – The miner gets a reward (10 coins) for mining a new block.

🧩 Tech Stack
Component	Description
Language	Python 3
Framework	Flask
Frontend	HTML, CSS, Bootstrap 5
Library	hashlib (for SHA-256 hashing)
Storage	In-memory Python list (no database needed)
⚙️ How It Works
1. Transaction

A user enters:

Sender Address

Receiver Address

Amount

This transaction is added to a pending transactions list.

2. Mining a Block

When you click “Mine Block”:

The system performs a Proof of Work (finds a hash starting with ‘0000’).

All pending transactions are packed into a new block.

The miner (your address) automatically receives 10 coins as a reward.

The new block is linked to the previous one using its hash.

3. Blockchain Ledger

Every block contains:

Block Index

Timestamp

Transactions List

Nonce (Proof of Work number)

Previous Block Hash

Current Block Hash

All blocks are linked using their hashes — this makes the data immutable (if one block changes, the entire chain becomes invalid).

4. Chain Verification

You can verify if the chain is valid using:

Each block’s previous_hash must match the actual hash of the previous block.

Every hash must start with "0000" (as per Proof of Work).
If either condition fails, the system detects tampering.

🧱 Example Block Structure
{
  'index': 3,
  'timestamp': '2025-10-15 22:40:10',
  'transactions': [
    {'sender': 'Alice', 'recipient': 'Bob', 'amount': 50},
    {'sender': '0', 'recipient': 'Miner123', 'amount': 10}
  ],
  'nonce': 20384,
  'previous_hash': '0000a9c3f...',
  'hash': '00009b21e...'
}

🧠 Key Blockchain Concepts Demonstrated
Concept	Explanation
Block	Unit of data that stores transactions.
Chain	Blocks linked together via hashes.
Hashing	SHA-256 ensures each block’s integrity.
Proof of Work	Finding a hash with specific conditions (e.g., starting with “0000”).
Mining	The process of adding a new block.
Decentralization (Simulated)	No central server; each node can maintain its copy.
💻 Folder Structure
blockchain-project/
│
├── app.py               # Main Flask app
├── blockchain.py         # Blockchain logic (class)
│
├── templates/            # HTML pages
│   ├── index.html        # Home / Send Money page
│   ├── blockchain.html   # Blockchain ledger view
│   └── mine.html         # Mining success page
│
├── static/
│   └── style.css         # Optional styling
│
└── README.md             # Project documentation

🧪 How to Run the Project
Step 1: Install Dependencies
pip install flask

Step 2: Run the Flask App
python app.py

Step 3: Open in Browser

Go to:
👉 http://localhost:5000

🎨 User Interface Flow
Page	Description
/	Home page – shows wallet balance and form to send coins.
/transactions/new	Submits a new transaction.
/mine_block	Mines a new block (creates and adds it to chain).
/blockchain	Displays full blockchain ledger in table format.
🧩 Example Use Case

Alice sends 50 coins to Bob.

Transaction added to pending list.

Miner mines a new block → includes this transaction + mining reward.

Blockchain updates with new block.

Ledger shows updated blocks and transactions.

🧠 Learning Outcome

By completing this project, we understood:

How blockchain links blocks using cryptographic hashes.

How transactions are validated and recorded.

How Proof of Work ensures data integrity.

How mining and rewards simulate real-world cryptocurrency logic.

How Flask can be used to build a blockchain-based web app.

🏁 Conclusion

This project successfully simulates a decentralized money transfer system using blockchain technology.
It demonstrates secure, immutable data handling, transparent ledger management, and the fundamentals of consensus and Proof of Work — all implemented in a single-night mini project using Flask.
