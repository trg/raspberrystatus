#!env sh

# Assumes a virtenv exists in this dir:
. ~/.virtualenv/curses/bin/activate
# put your env vars in a ".env" file
export $(cat .env)
# lets go!
python raspberrystatus.py
