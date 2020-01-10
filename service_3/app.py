#from service_3 import app
from random import random

def dice():
    roll = random.randint(1, 6)
    return roll

@app.route('/service_3', methods=['POST'])
def roll_dice():
    roll = dice()
    return {'die':f'{roll}'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
