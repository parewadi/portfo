from flask import Flask,render_template,request,redirect,redirect
import csv

app =  Flask(__name__)

@app.route('/')
def about():
    return render_template('index.html')

@app.route('/<page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return "Something went wrong!!"

def write_to_file(data):
    with open('database.txt', 'a') as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        db.write(f"\n{email}, {subject}, {message}")

def write_to_csv(data):
    with open('database_csv.csv', 'a',newline='') as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_write = csv.writer(db,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([email,subject,message])

