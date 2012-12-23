from flask import request,Flask,render_template, url_for,redirect,request
import urllib2,json

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    people=json.loads(open("static/about/about.json").read())
    return render_template("about.html",people=people)

@app.route("/<template>")
def index(template="index"):
    template=template+".html"
    return render_template(template)


if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0")
