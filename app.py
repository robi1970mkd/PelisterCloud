from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ PelagonChat е стартуван успешно!"

if __name__ == "__main__":
    app.run(debug=True)
