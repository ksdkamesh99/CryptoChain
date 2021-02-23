from flask import Flask, render_template, request, send_file, \
    send_from_directory
import numpy as np
from blockchain import CryptoChain
import time
import uuid

app = Flask(__name__, static_folder='static',
            template_folder='templates')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/transaction', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        data = request.form
        sender = str(data['from'])
        receiver = str(data['to'])
        amount = str(data['amount'])
        timestamp = str(time.time())
        transaction_id = str(uuid.uuid4())
        transaction = {}
        transaction['transaction_id'] = transaction_id
        transaction['timestamp'] = timestamp
        transaction['sender'] = sender
        transaction['receiver'] = receiver
        transaction['amount'] = amount
        crypto.pending_transactions.append(transaction)
        return 'Transaction is done successfully with id ' \
            + transaction_id

    if request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
    crypto = CryptoChain()
    app.run(debug=False, threaded=False)
