from flask import Flask, request

app = Flask(__name__)


@app.route('/summa')
def summa():
    args = request.args
    x = int(args.get("x"))

    if x < 2:
        return f"luku {x} ei ole alkuluku"

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return f"luku {x} ei ole alkuluku"

    return f"luku {x} on alkuluku"


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
