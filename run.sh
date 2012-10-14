#!env sh

. ~/.virtualenv/curses/bin/activate
export $(cat .env)
python raspberrystatus.py
