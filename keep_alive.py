from flask import Flask
import random
import threading

app = Flask(__name__)

number = 0

@app.route("/")
def hello_world():
    """ URL returns random number """
    return str(number)


def gen_rand():
    """ generating random numbers """
    global number
    while True:
        number = random.randint(0, 5)
        time.sleep(2)

if __name__ == '__main__':
    # starting thread to generate the number
    x = threading.Thread(target=gen_rand, daemon=True)
    x.start()

    # starting web server
    app.run()


# from flask import Flask, render_template
# from threading import Thread

# app = Flask(__name__)
# @app.route('/')
# def index():
#     return "Alive"

# def run():
#     app.run(host='0.0.0.0',port=8080)

# def keep_alive():
#     t = Thread(target=run)
#     t.start()    