from flask import Flask

app = Flask(__name__)  # creating the Flask class object


@app.route('/')  # decorator drfines the
def home():
    return "hello, Mr.GON96 How are You? ";


if __name__ == '__main__':
    app.run(debug=False)