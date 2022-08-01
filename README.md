# Twitpy
Ultimate Automation tool for Twittter.

Getting started
git clone https://github.com/CodeDroid/TwitPy.git
cd TwitPy
pip install .
# or depending on your system
python setup.py install
Make sure to get the right chromedrive for your system from here. Just put it in /assets.

Now edit the quickstart.py file to your needs.

API
from twitpy import TwitPy

# if you want to run it on a server simply set nogui=True

TwitPy(username="****", password="****",nogui=False) \
  .login() \
  # follows up to 250 accounts from your recommendations
  .follow_from_recom(amount=250) \ 
  # unfollows 100 accounts from your following list
  .unfollow_users(amount=100) \ 
  .end()
