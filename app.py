
from flask import Flask, request, render_template_string
import subprocess

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Pelister Chat</title>
</head>
<body>
    <h2>🧠 Pelister AI Chat (Admin Only)</h2>
    <form method="post">
        <textarea name="command" rows="4" cols="50" placeholder="Внеси команда до Пелистер или Стибера..."></textarea><br>
        <input type="submit" value="Испрати">
    </form>
    {% if response %}
        <h3>✅ Одговор:</h3>
        <pre>{{ response }}</pre>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def chat():
    response = None
    if request.method == "POST":
        command = request.form.get("command")
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, timeout=10)
            response = output.decode("utf-8")
        except subprocess.CalledProcessError as e:
            response = f"Грешка: {e.output.decode('utf-8')}"
        except Exception as e:
            response = f"Непозната грешка: {str(e)}"
    return render_template_string(HTML_TEMPLATE, response=response)

if __name__ == "__main__":
    app.run(debug=True)
