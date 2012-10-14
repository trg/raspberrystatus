Installation Instructions
=========================

    $ pip install -r requirements.txt

    $ chmod +x raspberrystatus.py pizzaclub.py

To run the status app:

    $ ./raspberrystatus.py

TO run the Pizza Club app:

    $ ./pizzaclub.py

Environment Variables
=====================

Required:
 - WUNDERGROUND_API_KEY - sign up for one at wunderground.com
 - RS_DEBUG - if set to anything, is in DEBUG mode.  use `unset RS_DEBUG` to disable DEBUG mode
 
Set the following from https://dev.twitter.com/apps/
 - TWITTER_CONSUMER_KEY
 - TWITTER_CONSUMER_SECRET
 - TWITTER_ACCESS_TOKEN
 - TWITTER_ACCESS_TOKEN_SECRET=

Notes
=====

    $ export $(cat .env)

To enable DEBUG mode:
export RS_DEBUG=anything

To disable DEBUG mode:
unset RS_DEBUG


