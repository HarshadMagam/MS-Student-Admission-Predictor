from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

@app.route('/')
def my_form():
	return render_template('home1.html')

@app.route('/front')
def my_form_return():
	return render_template('home1.html')

@app.route('/',methods = ['POST'])
def my_form_post():
    gre = int(request.form['GRE'])
    toefl=int(request.form['TOEFL'])
    ur=int(request.form['UR'])
    cgpa=float(request.form['CGPA'])

    print(request.form)
    loaded_model = pickle.load(open('admission_model.pkl', 'rb'))
    result=loaded_model.predict([[gre,toefl,ur,cgpa]])
    expected_per=round((result[0]*100),2)
    answer="The chance of getting admission after graduation is "+str(expected_per)+"%"
    return render_template('result.html',answer=answer)

if __name__ == "__main__":
    app.run()
