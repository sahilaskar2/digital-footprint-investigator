import requests
import re
from flask import Flask, render_template, request
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)

# Social platforms
SOCIAL_PLATFORMS = {
    "GitHub": "https://github.com/{}",
    "Instagram": "https://www.instagram.com/{}/",
    "Reddit": "https://www.reddit.com/user/{}",
    "Twitter": "https://twitter.com/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}"
}

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def check_platform(platform, username):

    url = SOCIAL_PLATFORMS[platform].format(username)

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=6,
            allow_redirects=True
        )

        final_url = response.url.lower()
        content = response.text.lower()

        # GitHub detection
        if platform == "GitHub":
            if response.status_code == 200 and username.lower() in final_url:
                return (platform, True, url)

        # Instagram detection
        elif platform == "Instagram":
            if response.status_code == 200 and "profilepage" in content:
                return (platform, True, url)

        # Reddit detection
        elif platform == "Reddit":
            if "nobody on reddit goes by that name" not in content and response.status_code == 200:
                if username.lower() in final_url:
                    return (platform, True, url)

        # Twitter detection
        elif platform == "Twitter":
            if response.status_code == 200 and username.lower() in final_url:
                return (platform, True, url)

        # LinkedIn detection
        elif platform == "LinkedIn":
            if response.status_code == 200 and username.lower() in final_url:
                if "page not found" not in content:
                    return (platform, True, url)

    except:
        pass

    return (platform, False, None)


@app.route("/", methods=["GET", "POST"])
def index():

    results = {}
    score = 0
    risk = "Low"
    username = ""

    if request.method == "POST":

        username = request.form["username"]

        # clean username
        username = re.sub(r"[^a-zA-Z0-9_]", "", username)

        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = [
                executor.submit(check_platform, platform, username)
                for platform in SOCIAL_PLATFORMS
            ]

            for future in futures:
                platform, found, link = future.result()

                if found:
                    results[platform] = "✓ Found"
                    score += 20
                else:
                    results[platform] = "✗ Not Found"

        # Risk calculation
        if score >= 60:
            risk = "High"
        elif score >= 30:
            risk = "Medium"
        else:
            risk = "Low"

    return render_template(
        "index.html",
        results=results,
        score=score,
        risk=risk,
        username=username
    )


if __name__ == "__main__":
    app.run(debug=True)