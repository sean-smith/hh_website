from flask import Flask, json, render_template, url_for
import generate2
app = Flask(__name__, static_url_path="")

@app.route("/")
def load():
    return app.send_static_file('index.html')

@app.route("/tiles")
def load_app():
    print("ran_get_tiles")
    x = generate2.generate("README.md")
    Json = x.get_json()
    return json.jsonify(Json)

if __name__ == "__main__":
    app.run(debug=True)
