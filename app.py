from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ PelagonChat е стартуван успешно!"

@app.route("/status")
def status():
    return "✅ Агенти се активни и работат!"

if __name__ == "__main__":
    app.run(debug=True)
