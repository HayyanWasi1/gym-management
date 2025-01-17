from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/service")
def service():
    return render_template('service.html')

@app.route("/membership")
def membership():
    return render_template('membership.html')

@app.route("/gallery")
def gallery():
    return render_template('gallery.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')


if __name__ =="__main__":
    app.run(debug = True, port=8000)










# from flask import Flask, render_template, send_from_directory

# app = Flask(__name__)

# # Home route
# @app.route("/")
# def home():
#     return render_template("index.html")  # Renders the index.html file in /templates

# # About route
# @app.route("/about")
# def about():
#     return render_template("about.html")  # Renders the about.html file in /templates
# @app.route("/contact")
# def contact():
#     return render_template("contact.html")  # Renders the about.html file in /templates
# @app.route("/gallery")
# def gallery():
#     return render_template("gallery.html")  # Renders the about.html file in /templates
# @app.route("/login")
# def login():
#     return render_template("login.html")  # Renders the about.html file in /templates
# @app.route("/membership")
# def membership():
#     return render_template("membership.html")  # Renders the about.html file in /templates
# @app.route("/register")
# def register():
#     return render_template("register.html")  # Renders the about.html file in /templates
# @app.route("/service")
# def service():
#     return render_template("service.html")  # Renders the about.html file in /templates


# if __name__ == "__main__":
#     app.run(debug=True)
