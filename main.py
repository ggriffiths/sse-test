from flask import Flask, Response, render_template
import time
import json

app = Flask(__name__)

def generate_events():
    """
    Generator function to yield events.
    """
    count = 0
    data = []
    to_stream = ['So you want to know how many users...',
                "Try this: SELECT COUNT(*) FROM users;",
                "Why: This will give you the number of users in the database.",
                "What do you want to do next?"
                ]
    for m in to_stream:
        time.sleep(1)  #
        data.append(m)
        yield f"data: {data}\n\n"

@app.route('/events')
def events():
    """
    Route to serve Server-Sent Events.
    """
    return Response(generate_events(), content_type='text/event-stream')

@app.route('/')
def index():
    """
    Route to serve a simple HTML page that consumes the SSE.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, threaded=True)