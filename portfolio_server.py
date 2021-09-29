from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


# @app.route("/about.html")
# def about():
#     return render_template('about.html')


# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')

def write_to_file(user_data):
    with open('database.txt', mode='a+') as d:
        email = user_data["email"]
        userName = user_data["userName"]
        subject = user_data["subject"]
        message = user_data["message"]
        d.write(
            f"email = {email}, Name = {userName}, Subject = {subject}, Message = {message} \n")


def write_to_csv(user_data):
    with open('database.csv', newline='', mode='a') as d2:
        email = user_data["email"]
        userName = user_data["userName"]
        subject = user_data["subject"]
        message = user_data["message"]
        csv_writer = csv.writer(
            d2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, userName, subject, message])


@ app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            user_data = request.form.to_dict()
            write_to_csv(user_data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'Error, please try again'
