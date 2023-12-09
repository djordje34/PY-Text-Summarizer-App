from flask import Flask, render_template, request, jsonify
from summarizer.sbert import SBertSummarizer


model = SBertSummarizer('paraphrase-miniLM-L6-v2')

app = Flask(__name__)

@app.route("/")
def msg():
    return render_template("index.html")

@app.route("/summarize", methods = ['POST','GET'])
def getSummary():
    body = request.form.get("query")
    num = request.form.get("num")
    result = model(body, num_sentences=int(num))
    sentences = result.split(".")
    formatted_result = "\n\n".join(["- " + sentence.strip() + "." for sentence in sentences if sentence.strip()])
    return jsonify({'result': formatted_result})


if __name__ == "__main__":
    app.run(debug = True, port = 8000)