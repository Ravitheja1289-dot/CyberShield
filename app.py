from flask import Flask, render_template
import mail  # Import the file where the variable is stored

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", value=mail.result)

if __name__ == "__main__":
    app.run(debug=True)
