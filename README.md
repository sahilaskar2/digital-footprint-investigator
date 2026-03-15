# 🔎 Digital Footprint Investigation and Profiling Tool

## 📘 Course Information

**Course Name:** Cyber Forensic and Investigation
**Course Code:** PECCS604T
**Year/Semester:** 3 / VI
**Session:** 2025–26

---

# 🌐 Project Overview

The **Digital Footprint Investigation and Profiling Tool** is a web-based **cyber forensic application** designed to investigate a person's online presence across multiple social media platforms using their username.

The tool collects **publicly accessible information (Open Source Intelligence – OSINT)** and generates a **digital footprint profile** that shows where a user may have accounts on the internet.

This project demonstrates the process of **digital footprint investigation**, which is an important technique used in **cyber forensics 🔐, cybersecurity 🛡️ investigations, and digital intelligence gathering 📊**.

---

# 🎯 Objectives

The main objectives of this project are:

* 🔍 To investigate digital footprints using publicly available information.
* 🌐 To detect possible social media accounts associated with a username.
* 📊 To generate a digital presence score based on detected accounts.
* ⚠️ To classify the risk level of a digital footprint.
* 🧠 To demonstrate the application of OSINT techniques in cyber forensics.

---

# ⚙️ Key Features

### 🔎 Username Investigation

The system allows the user to enter a username and investigate its presence across multiple platforms.

### 🌍 Multi-Platform Detection

The tool checks several major platforms including:

* 🐙 GitHub
* 📸 Instagram
* 👤 Reddit (User Profiles)
* 💬 Reddit (Subreddits)
* 🐦 Twitter / X
* 💼 LinkedIn Profiles
* 🏢 LinkedIn Company Pages
* 📌 Pinterest
* 👍 Facebook
* ▶️ YouTube Channels
* ✉️ Telegram Accounts

### 📈 Digital Presence Score

The system calculates a **digital footprint score** based on the number of platforms where the username is found.

### 🚦 Risk Level Classification

Based on the digital presence score, the system categorizes the profile into:

* 🟢 **Low Risk** – minimal online presence
* 🟡 **Medium Risk** – moderate online presence
* 🔴 **High Risk** – strong digital footprint

### 🔗 Investigation Links

If a profile is detected, the tool provides **clickable links** that allow investigators to directly open the profile.

### 🖥️ Cyber Security Dashboard UI

The application uses a **dark cybersecurity-style interface** with result cards, status indicators, and a responsive layout to simulate a real investigation dashboard.

---

# 🛠️ Technologies Used

### ⚙️ Backend

* 🐍 Python
* 🌶️ Flask

### 🎨 Frontend

* 🌐 HTML5
* 🎨 CSS3

### 📦 Libraries

* requests
* concurrent.futures

### 🧰 Tools

* Git
* GitHub

---

# 📁 Project Structure

```
digital-footprint-investigator
│
├── app.py
│
├── templates
│   └── index.html
│
├── static
│   └── css
│       └── style.css
│
└── README.md
```

---

# ⚡ How the System Works

1. 👤 The user enters a **username** into the search field.
2. 🔗 The application generates profile URLs for multiple platforms.
3. 🌐 The system sends HTTP requests to each platform.
4. 🧠 Each platform is analyzed using platform-specific detection rules.
5. ✅ The system identifies whether the profile exists.
6. 📊 Results are displayed on the investigation dashboard.
7. 📈 A **digital presence score and risk level** are calculated.

---

# 📊 Example Output

Example search:

```
Username: nasa
```

Example result:

```
GitHub: Found
Instagram: Found
Reddit User: Not Found
Reddit Subreddit: Found
Twitter: Found
LinkedIn Company: Found
Pinterest: Found
Facebook: Found
YouTube: Found
Telegram: Not Found
```

📈 **Digital Presence Score:** 70%
🚦 **Risk Level:** High

---

# ⚖️ Ethical Considerations

This tool only analyzes **publicly available information** and does not access private or restricted data.

The project is developed **strictly for educational 🎓 and cyber forensic learning purposes**.

---

# 🚀 Future Improvements

Possible future enhancements include:

* 📧 Email breach detection
* 🔎 Reverse username search
* 🧰 Integration with OSINT investigation tools
* 📊 Data visualization dashboards
* 📄 Automatic investigation report generation
* 🤖 Machine learning based profiling

---

# 👨‍💻 Author

**Sahil Askar**
Computer Science Engineering
6th Semester

---

# 📌 Conclusion

The **Digital Footprint Investigation and Profiling Tool** demonstrates how publicly available information can be used in **cyber forensic investigations 🔐** to analyze a person's online presence.

The project highlights the importance of **digital footprint awareness 🌐** and showcases how **OSINT techniques 🧠** can assist investigators in cybersecurity and digital intelligence analysis.
