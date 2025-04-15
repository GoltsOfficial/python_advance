from flask import Flask, request, jsonify

app = Flask(__name__)
storage: dict[str, list[int]] = {}


@app.route('/add/', methods=['POST'])
def add():
    data = request.get_json()

    date = data.get('date')
    amount = data.get('amount')

    if not isinstance(date, str) or len(date) != 8 or not date.isdigit():
        raise TypeError("Date must be in format YYYYMMDD (string of 8 digits)")

    if date not in storage:
        storage[date] = []

    storage[date].append(amount)
    return jsonify({'message': 'Added successfully'})


@app.route('/calculate/', methods=['GET'])
def calculate():
    date = request.args.get('date')

    if date:
        total = sum(storage.get(date, []))
        return jsonify({'total': total})
    else:
        total = sum(sum(amounts) for amounts in storage.values())
        return jsonify({'total': total})


if __name__ == '__main__':
    app.run()