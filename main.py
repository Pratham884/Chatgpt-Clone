from flask import Flask,render_template , jsonify , request 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route ( "/api ", methods=["GET","POST"])
def qa():
    
    if request.method=="POST":
            print(request.json)
            question=request.json.get("question")
            data = {"result": question }

            return jsonify(data)
    data = {"result": "Thank you! I'm just a machine learning model designed to respond to questions and generate text based on my training data. Is there anything specific you'd like to ask or discuss? "}

    return jsonify(data)

app.run(debug=True)