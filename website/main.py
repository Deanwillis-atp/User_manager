from flask import Flask, render_template, request 
from website import create_app
import json
import os 




app = create_app()


if __name__ 


@app.route('/',methods =['GET','POST'])
def home():

    if os.path.exists("users_info.json"):
        with open('users_info.json',"r") as f:
            try:
                users = json.load(f)
            except json.JSONDecodeError:
                users = []
    else:
        users = []        

    if request.method == "POST":
        name = request.form['name']
        users.append({'name':name})

        with open ('users_info.json','w')as f:
            json.dump(users, f, indent=4)

    return render_template("form.html", users =users)
    

if __name__ == '__main__':
    app.run(debug=True)
