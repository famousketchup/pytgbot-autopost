<!-- markdownlint-configure-file {
  "no-inline-html": false,
  "MD041": false
} -->

<div align="center">

# 📅 \\\ AutoPost: The Telegram Bot // 🤖

_Every day at a time you choose, post to my (or yours) Telegram channel,_ \
_with memes or other picture topics (with a caption!),_ \
_let me introduce: `pytgbot-autopost`_

![GitHub Release](https://img.shields.io/github/v/release/dmitriy-korotayev/pytgbot-autopost)
![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg?style=flat-square)
<a target="_blank" href="https://www.linkedin.com/in/foreverdev/">
<img height="20" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)](https://github.com/dmitriy-korotayev/pytgbot-autopost/fork)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

<img src="logo.jpg" title="Logo" width="40%"
  alt="Look at our cute little Python-based helper!"
/>

</div>

<!-- ![Build Status](https://img.shields.io/travis/com/yourusername/autopost-telegram-bot/main?style=flat-square) -->
<!-- ![Code Quality](https://img.shields.io/codacy/grade/a1234567890fe0987654321f?style=flat-square) -->
<!-- ![License](https://img.shields.io/github/license/yourusername/autopost-telegram-bot?style=flat-square) -->

## ❤️ Introduction ❤️

Welcome to the **AutoPost Telegram Bot**. It is a simple yet clever Python-based bot which automatically posts messages or media to Telegram groups or channels daily. It's perfect for sharing memes, wallpapers, stories, news, or any other picture with a comment. You've found the right open-source bot for keeping your channel active with daily content without all the manual scheduling b^shit.

## 🔥 Features 🔥

- [x] **Automated Posting:** Schedule up to 100 images with captions to be posted at chosen time daily. 📆
- [x] _And... And... Let me think - you need more? Read along_

## 📥 Planned features 📥

- [ ] **More Media Support:** Whether it's photos, videos, or documents, AutoPost handles it all. 🖼️🎥📄
- [ ] **Interactive Scheduler:** Set up your posting schedule with ease through our intuitive command-line interface. ⏲️
- [ ] **Customizable Templates:** Tailor your messages with dynamic content for that personal touch. ✍️
- [ ] **Logging and Analytics:** Keep track of what's posted and engage your audience more effectively. 📊

## 🚀 Usage Guide 🚀

### Prerequisites

- Python 3.6 or later
- `pip` / `pipx`

### Installation and usage
_(From `git clone` to running a bot daemon script):_

#### 1. 🔧 Fetch and configure the bot 🔧

```bash
git clone https://github.com/dmitriy-korotayev/pytgbot-autopost.git
cd pytgbot-autopost
cp .env.sample .env
$EDITOR .env
```

#### 2. 📥 Preamble and dependencies installation 📥

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### 3. 🤖 Run the bot 🤖:

```bash
python3 main.py
```

---

### ⏲️ You can use a `šystend-service.service` to automate script launch ⏲️

```bash
# Copy service from repo
sudo cp systend-service.service /etc/systemd/system/autopost-telegram-bot.service
# Reload
sudo systemctl daemon-reload
# Enable autorun and start
sudo systemctl enable autopost-telegram-bot
sudo systemctl start autopost-telegram-bot
```

<div align="center">

## 🚦 Support 🚦

Contributions, issues, and feature requests are welcome! \
Give a ⭐️ if you like this project!

## 📝 License 📝

MIT License - Free, open-source license with minimal restrictions.

-----------

Copyright (c) 2024 **Dmitriy Korotayev** \
[Profile ⚛️](https://github.com/dmitriy-korotayev "My GitHub profile") \
[Email me 🤝](mailto:korotayev.dmitriy+github "Email any questions you might have!") \
**[LinkedIn (Hire me 😊)](https://www.linkedin.com/in/foreverdev/ "My professional profile: skills, experience and much more...")**

</div>
