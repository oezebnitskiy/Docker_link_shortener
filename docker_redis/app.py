# compose_flask/app.py
from flask import Flask, request, redirect
from redis import Redis
import random
import string

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

# Get redirection via existing link code
@app.route('/<link>')
def get_link(link):
    redir = redis.get(link),
    if not link:
        return 'Pass a link code as a part of url'
    if not redis.get(link):
        return 'Sorry, there is no such link in a base'
    return redirect(redis.get(link).decode(), code=302)


# Create new link code
@app.route('/create')
def create_link():
    # TODO: wrap if there is no string
    link = request.args.get('link')
    if not link:
        return "Create a link parameter with an url"
    letters = string.ascii_lowercase
    link_alias = ''.join(random.choice(letters) for i in range(10))
    redis.mset({link_alias:link})
    return f"Your link code is {link_alias}"

# Root with small instruction
@app.route('/')
def hello():
    return "Hi there. This is a small link shortener. Pass link code as an url to get redirection (/<link_code>). Or create one via /create?link=https:ya.ru"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

