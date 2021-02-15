from flask import Flask, request,jsonify
from sklearn.externals import joblib
import json
app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def fun1():
    model = joblib.load("spam_model.pkl")
    cvec = joblib.load("cvec.pkl")
    data = request.get_json(force=True)
    data3 = [data["msg"]]
    data3 = cvec.transform(data3)
    output = model.predict(data3)   
    return jsonify(output[0])

@app.route("/hi")
def fun2():
    return "oh! you just said hi!, thanks"

if __name__=="__main__":
    app.run(debug=True)