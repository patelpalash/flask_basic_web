from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Hello world'

@app.route('/sucess/<int:score>')
def success(score):
    return "the person has passed and the marks is "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "the person has failed and the marks is "+str(score)
#result checker

@app.route('/result/<int:marks>')
def results(score):
    result=""
    marks=""
    if marks<50:
        result="fail"
    else:
        result="success"
    return redirect(url_for(result,score=marks))



if __name__ == "__main__":
    app.run(debug=True)
