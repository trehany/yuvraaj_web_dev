from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>hello world<h1>"

if __name__ == "__main__":
    app.run(host = '0.0.0.0',debug = True)

print('i am tired of this')






    