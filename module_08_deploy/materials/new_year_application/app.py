import os
from flask import Flask, render_template, send_from_directory

root_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__,
            template_folder=os.path.join(root_dir, "templates"))

# Самореализованный endpoint для статики
@app.route("/static/<path:filename>")
def send_static(filename):
    static_folder = os.path.join(root_dir, "static")
    return send_from_directory(static_folder, filename)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)