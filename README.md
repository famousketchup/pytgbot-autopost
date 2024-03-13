<!-- markdownlint-configure-file {
  "no-inline-html": false,
  "MD041": false
} -->

<div align="center">

# 📅 AutoPost: The Telegram Bot 🤖

_Every day at a time you choose, post to my (or yours) Telegram channel,_ \
_with memes or other picture topics (with a caption!),_ \
_let me introduce: `pytgbot-autopost`_

<img src="logo.jpg" title="Logo" width="40%"
  alt="Look at our cute little Python-based helper!"
/>

</div>

![Build Status](https://img.shields.io/travis/com/yourusername/autopost-telegram-bot/main?style=flat-square)
![Code Quality](https://img.shields.io/codacy/grade/a1234567890fe0987654321f?style=flat-square)
![License](https://img.shields.io/github/license/yourusername/autopost-telegram-bot?style=flat-square)
![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg?style=flat-square)

## Introduction ❤️

Welcome to the **AutoPost Telegram Bot**. It is a simple yet clever Python-based bot which automatically posts messages or media to Telegram groups or channels daily. It's perfect for sharing memes, wallpapers, stories, news, or any other picture with a comment. You've found the right open-source bot for keeping your channel active with daily content without all the manual scheduling b^shit.

## 🔥 Features 🔥

- **Automated Posting:** Schedule up to 100 images with captions to be posted at chosen time daily. 📆
- _And... And... Let me think - something else?_

## Planned features

- **More Media Support:** Whether it's photos, videos, or documents, AutoPost handles it all. 🖼️🎥📄
- **Interactive Scheduler:** Set up your posting schedule with ease through our intuitive command-line interface. ⏲️
- **Customizable Templates:** Tailor your messages with dynamic content for that personal touch. ✍️
- **Logging and Analytics:** Keep track of what's posted and engage your audience more effectively. 📊

<<<<<<< HEAD

## 🚀 Getting Started 🚀

=======

## 🚀 Usage guide 🚀

> > > > > > > 68732c3 (Finish polishing README.md)

### Prerequisites

- Python 3.6 or later
- `pip` / `pipx`

### Installation and simple usage

1. # From `git clone` to running a script:

### 1. Installation and simple usage

_(From `git clone` to running a script):_

1.1. **Installation**

```bash
git clone https://github.com/dmitriy-korotayev/pytgbot-autopost.git
cd pytgbot-autopost
```

1.2. **Preamble and dependencies**

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

1.3 **Daemon run**:

```bash
python3 main.py
```

---

### 2. You can use a `šystend-service.service` to automate script launch

===

```bash
# Copy service from repo
sudo cp systend-service.service /etc/systemd/system/autopost-telegram-bot.service
# Reload
sudo systemctl daemon-reload
# Enable autorun and start
sudo systemctl enable autopost-telegram-bot
sudo systemctl start autopost-telegram-bot
```

---

### 3. You can just use shell scripts

===

```bash
./1-prep.sh
./2-run.sh
```

### Configure the bot for yourself

#### Current configuration method

```bash
# TOKEN
sed -i s/6703451102:AAHFrv3Fjln_o41_TwaRDyFSnIsY13GTTqQ/[YOUR_TOKEN]
sed -i s/@memetimes/[YOUR_CHANNEL_ID]
sed -i s/18, 20/[YOUR_POSTING_TIME]/
sed -i
```

#### Future configuration method

```bash
$EDITOR .env
```
