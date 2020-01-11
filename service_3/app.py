from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/service_3', methods=['POST'])
def roll_dice():
    roll = random.randint(1, 6)
    return {'roll':'{}'.format(roll)}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
