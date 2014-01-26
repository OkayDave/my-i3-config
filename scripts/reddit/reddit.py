#!/usr/bin/env python

from ReddiWrap import ReddiWrap

reddit = ReddiWrap(user_agent='ReddiWrap')

USERNAME = ''
PASSWORD = ''

reddit.load_cookies("cookies.txt")

if not reddit.logged_in or reddit.user.lower() != USERNAME.lower():
  login = reddit.login(user=USERNAME, password=PASSWORD)
  if login != 0:
    # 1 means invalid password, 2 means rate limited, -1 means unexpected error
    print('unable to log in: %d' % login)
    exit(1)
  # Save cookies so we won't have to log in again later
  reddit.save_cookies('cookies.txt')

info = reddit.user_info()

output = "L:%(link)d C:%(comment)d " % {"link": info.link_karma, "comment": info.comment_karma}

if info.has_mail: 
  output = output + u"\u2709" 
print(output)
