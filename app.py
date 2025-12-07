from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'segredo'
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("message")
def handle_message(data):
    print(f"{data['username']}: {data['message']}")
    send(data, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, debug=True)
