"""Telegram bot which queues photos and posts them at specified time.

Posts are added to the json database and posted to the channel specified.
"""

import os
import time as time_sleep
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, time, timedelta

import schedule
import simplejson as json
import telebot
from tinydb import TinyDB, where

# >> Preamble

# Telegram bot token
TOKEN = "6703451102:AAHFrv3Fjln_o41_TwaRDyFSnIsY13GTTqQ"
# Channel to auto-post images to
channel_id = '@memetimes'
# When to post images from queue
target_time = time(18, 20)
# Debugger set to ipdb
os.environ['PYTHONBREAKPOINT'] = 'ipdb.set_trace'

bot = telebot.TeleBot(TOKEN, parse_mode=None)
db = TinyDB('schedule.json')


# Queue posts handler
@bot.message_handler(content_types=['photo'])
def queue_image(message):
    """Handle posts received by a bot and add them to a database."""
    # Get the file ID of the largest photo (assuming it's the original)
    # For reference when it will be posted as per schedule
    photo_id = message.photo[-1].file_id

    # Posts count in queue which are already scheduled
    queue_length = db.count(where('posted') == 0)

    now = datetime.now()

    # Calculate date to post a queue item
    today = now.date()
    date_to_post = today + timedelta(days=queue_length)
    # except if time has already passed, then tomorrow, with empty queue
    if queue_length == 0 and now.time() > time(18, 20):
        date_to_post += timedelta(days=1)

    # Save all the necessary data for a queued post
    data = {
        'photo_id': photo_id,
        'channel_id': channel_id,
        'caption': message.caption,
        'scheduled_for': date_to_post.isoformat(),
        'added': now,
        'posted': 0
    }
    json_data = json.dumps(data, default=lambda obj: obj.isoformat()
                           if isinstance(obj, datetime) else None)
    db.insert(json.loads(json_data))

    # Reply about scheduled post
    scheduled_for = f'This post is scheduled for {date_to_post.isoformat()}'
    bot.reply_to(message, scheduled_for)


def do_a_post(not_todays_post=False):
    """Post image with caption from queue stored in a database."""
    # Check if there are any posts in queue db
    if len(db.all()) == 0:
        print('No posts are scheduled')
        return False

    # Get scheduled post (today or otherwise first)
    if not_todays_post:
        chosen_post = db.all()[0]
    else:
        is_not_posted = where('posted') == 0
        is_for_today = where('scheduled_for') == date.today().isoformat()
        chosen_post = db.search((is_not_posted) & (is_for_today))
        if (len(chosen_post) == 0):
            print('No posts for today')
            return False
        else:
            chosen_post = chosen_post[0]

    # Send out the image post with a caption
    photo_id = chosen_post['photo_id']
    caption = chosen_post['caption']
    bot.send_photo(channel_id, photo_id, caption=caption)

    # Change status to posted
    post_query = where('photo_id') == photo_id
    update_value = {'posted': 1}
    db.update(update_value, post_query)
    print(f'Post with caption {caption} posted')


# >>> Scheduler and bot init

# Schedule to post at a specific time
scheduled_time = f'{target_time.hour}:{target_time.minute}'
schedule.every().day.at(scheduled_time).do(do_a_post)


# # Post on 'p' key press
# def p_key_handler(key):
#     """Do a post when 'p' is pressed."""
#     if key.char == 'p':
#         do_a_post(True)
#
#
# # Listener for key press
# with Listener(on_release=p_key_handler) as listener:
#     listener.join()

# Keep scheduled jobs running
def parallel_scheduler_function():
    print('Starting post scheduler')
    while True:
        schedule.run_pending()
        time_sleep.sleep(1)

# Start bot to work without stop
with ThreadPoolExecutor() as executor:
    # Submit the parallel function to the thread pool
    future = executor.submit(parallel_scheduler_function)

    # Start the bot's long polling loop
    print('Starting bot')
    bot.infinity_polling()
