
from flask import Flask, render_template, redirect, url_for
from flask import request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    '''
    You could put a homepage here, maybe with some navigation to registration/login pages
    :return:
    '''

    error = None
    if request.method == 'POST':

        if request.values.keys() == {'Navigation'}:
            return redirect(url_for("secondpage"))
    return render_template('home.html', error=error)

@app.route('/secondpage', methods=['GET','POST'])
def secondpage():
    """
    This could be a login page, or maybe a user page, you can take textbox input and pass it to an input, you could also
    preform some sort of hashing on the text here before passing it to a webapi. IF YOUR WEBSITE IS HTTPS ENABLED: you
    could potentially use this to pass passwords, and this would mean that the plaintext password is passed over an
    encrypted ssl connection, and is stored in the memory of the machine running this website for a very short period of
    time before being hashed and stored.

    By contacting apis and making clever use of the redirect(url_for()) and render_template() methods you can make some
    suprisingly impressive systems.
    :return:
    """
    error = None
    if request.method == 'POST':
        if "Back" in request.values.keys():
            if request.values["Back"] == "Back":
                return redirect(url_for("home"))
                pass
        if "PassText" in request.values.keys():
            if request.values["PassText"]:
                if "passToCode" in request.values.keys():
                    passed_text = request.values["passToCode"]
                    if passed_text.isalnum(): # Use this if you want to sanitize input
                        return render_template('secondpage.html', passText=passed_text, error=error)
                    else:
                        error = "Text must be alphanumeric"
                else:
                    error = "Must enter text to pass it to code!"


    return render_template('secondpage.html', error=error)

if __name__ == '__main__':
    app.run(host="0.0.0.0")