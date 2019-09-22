from flask import Flask, jsonify
app = Flask(__name__)

app_instance_name = 'myapp'

@app.route("/")
def hello():
    return '<h1>Hello from {}!</h1>'.format(app_instance_name)

@app.route("/health")
def health():
    return jsonify({'status': 'ok'})

if __name__ == "__main__":
    app.run(host='0.0.0.0')