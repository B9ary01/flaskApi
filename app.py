from flask import Flask

app=Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to home page."


if __name__ == '__main__':
   app.run(debug=True)
