
##requirements

- python 3.7 or above
- all packages as specify in `requirements.txt`

##user prompt mode

run `session.py` (input will be prompt from stdin)

##server mode
run `server.py`

the server will bind to port 8888 at localhost
to init a session make a GET request to `/api/init`

to submit an answer make a GET request to `/api/submit?data=[answer]`

example run