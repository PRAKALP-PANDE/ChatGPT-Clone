from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route("/api", methods=["GET", "POST"])
def qa():
    if request.method == "POST":
        data = {"result": "As an AI language model, I don't have direct experiences or the ability to take courses. However, I can provide you with some general information on important things that people commonly learn from courses. The specific learnings may vary depending on the course topic, but here are two important things that many courses aim to impart:"}
        return jsonify(data)
    return render_template("index.html")

app.run(debug=True)