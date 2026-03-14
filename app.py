import requests
import re
from flask import Flask, render_template, request
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)

PLATFORMS = {
    "GitHub": "https://github.com/{}",
    "Instagram": "https://www.instagram.com/{}/",
    "Reddit User": "https://www.reddit.com/user/{}",
    "Reddit Subreddit": "https://www.reddit.com/r/{}",
    "Twitter": "https://twitter.com/{}",
    "LinkedIn Profile": "https://www.linkedin.com/in/{}",
    "LinkedIn Company": "https://www.linkedin.com/company/{}",
    "Pinterest": "https://www.pinterest.com/{}/",
    "Facebook": "https://www.facebook.com/{}",
    "YouTube": "https://www.youtube.com/@{}",
    "Telegram": "https://t.me/{}"
}

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def check_platform(platform, username):

    url = PLATFORMS[platform].format(username)

    try:

        r = requests.get(url, headers=HEADERS, timeout=6, allow_redirects=True)
        text = r.text.lower()
        final_url = r.url.lower()

        # ---------- GitHub ----------
        if platform == "GitHub":
            if r.status_code == 200 and "not found" not in text:
                return platform, True, url

        # ---------- Instagram ----------
        elif platform == "Instagram":
            if r.status_code == 200 and "profilepage" in text:
                return platform, True, url

        # ---------- Reddit user ----------
        elif platform == "Reddit User":
            if r.status_code == 200 and "nobody on reddit goes by that name" not in text:
                return platform, True, url

        # ---------- Reddit subreddit ----------
        elif platform == "Reddit Subreddit":
            if r.status_code == 200 and "community not found" not in text:
                return platform, True, url

        # ---------- Twitter ----------
        elif platform == "Twitter":
            if r.status_code == 200 and "this account doesn’t exist" not in text:
                return platform, True, url

        # ---------- LinkedIn profile ----------
        elif platform == "LinkedIn Profile":
            if r.status_code == 200 and "profile not found" not in text:
                return platform, True, url

        # ---------- LinkedIn company ----------
        elif platform == "LinkedIn Company":
            if r.status_code == 200 and "page not found" not in text:
                return platform, True, url

        # ---------- Pinterest ----------
        elif platform == "Pinterest":
            if r.status_code == 200 and "profile" in final_url:
                return platform, True, url

        # ---------- Facebook ----------
        elif platform == "Facebook":
            if r.status_code == 200 and "content not found" not in text:
                return platform, True, url

        # ---------- YouTube ----------
        elif platform == "YouTube":
            if r.status_code == 200 and ("subscribers" in text or "videos" in text):
                return platform, True, url

        # ---------- Telegram ----------
        elif platform == "Telegram":
            if r.status_code == 200 and ("send message" in text or username.lower() in text):
                return platform, True, url

    except:
        pass

    return platform, False, None


@app.route("/", methods=["GET", "POST"])
def index():

    results = {}
    links = {}
    score = 0
    risk = "Low"
    username = ""

    if request.method == "POST":

        username = request.form["username"]
        username = re.sub(r"[^a-zA-Z0-9_]", "", username)

        with ThreadPoolExecutor(max_workers=10) as executor:

            futures = [
                executor.submit(check_platform, platform, username)
                for platform in PLATFORMS
            ]

            for future in futures:

                platform, found, link = future.result()

                if found:
                    results[platform] = "✓ Found"
                    links[platform] = link
                    score += 9
                else:
                    results[platform] = "✗ Not Found"

        if score >= 60:
            risk = "High"
        elif score >= 30:
            risk = "Medium"
        else:
            risk = "Low"

    return render_template(
        "index.html",
        username=username,
        results=results,
        links=links,
        score=score,
        risk=risk
    )


if __name__ == "__main__":
    app.run(debug=True)