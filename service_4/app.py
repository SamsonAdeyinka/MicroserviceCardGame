#from application import app


@app.route('/server_4', methods=['POST'])
def result():
    
    card = ''
    r = requests.post("http://service_2:5002/service_2")
    card = response.json()['random_card']

    die = ''
    req = request.post("http://service_3:5003/service_3")
    die = response.json()['roll_dice']


    points = int(card.Point) * int(die)
    prize = ''

    if points <= 78:
        prize_num = random.randint(1, 9)
        prize = prize_gen.query.filter_by(id=prize_num).first()

    elif points >= 79 and points <= 156:
        prize_num = random.randint(10, 19)
        prize = prize_gen.query.filter_by(id=prize_num).first()

    elif points >= 157 and points <= 234:
        prize_num = random.randint(20, 33)
        prize = prize_gen.query.filter_by(id=prize_num).first()

    elif points >= 235 and points <= 317:
        prize_num = random.randint(34, 39)
        prize = prize_gen.query.filter_by(id=prize_num).first()

    elif points == 318:
        prize = prize_gen.query.filter_by(id=40).first()

    return {'prize':f'{prize_gen.Prize}'}    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5004)
