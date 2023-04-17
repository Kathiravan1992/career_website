from flask import Flask
from flask import render_template,jsonify

app = Flask(__name__)

JOBS=[

    {
        'id':1,
        'title':'Data Analyst',
        'location':'Bangalore India',
        'salary': 'INR 10,00,000',
    },

    {
        'id':2,
        'title':'Data Scientist',
        'location':'Delhi India',
        'salary': 'INR 15,00,000',
    },

    {
        'id':3,
        'title':'Frontend engg',
        'location':'remote',
 
    },
    {
        'id':4,
        'title':'backend engg',
        'location':'SAN Franciso , USA',
        'salary': 'INR 12,00,000',
    },
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":

    app.run(debug=True)
