from flask import Flask, render_template, request
import requests

app = Flask(__name__)

sites = {
    "GitHub": "https://github.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Instagram": "https://www.instagram.com/{}",
    "Twitter": "https://twitter.com/{}"
}

@app.route("/", methods=["GET","POST"])
def home():

    results = {}

    if request.method == "POST":

        username = request.form["username"]

        for site, url in sites.items():

            profile_url = url.format(username)

            r = requests.get(profile_url)

            if r.status_code == 200:
                results[site] = "✓ Found"
            else:
                results[site] = "✗ Not Found"

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)