import sys, subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'flask'])
from flask import Flask,render_template
import os,json

app = Flask(__name__)

@app.route("/")
def index(): # also called view
    return render_template('index.html', page_title="Home",)


@app.route("/about")
def about():
    data=[]
    with open('data/company.json','r') as json_data:
        data = json.load(json_data)

    return render_template('about.html', page_title="About",company = data)



@app.route("/about/<member_name>")
def about_member(member_name):
    member = []
    with open('data/company.json', 'r') as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj['url'] == member_name:
                member = obj

    return render_template('member.html', member=member)



@app.route("/contact")
def contact():
    return render_template('contact.html', page_title="Contact")


@app.route("/careers")
def careers():
    return render_template('careers.html',page_title="Careers")


if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP","0.0.0.0"),
        port = int(os.environ.get("PORT","5000")),
        debug = True
    )
    
