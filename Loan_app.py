from flask import Flask, request, jsonify
import pickle
import sklearn

app = Flask(__name__)

@app.route("/", methods=['GET']) # base url
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ping", methods=['GET'])
def pinger():
    return "<p>Hello i am under water!</p>"

@app.route("/json", methods=['GET'])
def json_check():
    return {"message": "Hi i am json!"}

with open("classifier.pkl", "rb") as f:
    clf = pickle.load(f)

@app.route("/predict", methods=['POST'])
def prediction():
    loan_req = request.get_json()

    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1

    if loan_req['Married'] == "Yes":
        Married = 1
    else:
        Married = 0

    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount']
    Credit_History = loan_req['Credit_History']

    result = clf.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

    if result == 0:
        pred = "Rejected"
    else:
        pred = "Approved"

    return jsonify({"loan_approval_status": pred})

if __name__ == "__main__":
    #app.run(debug=True, port=5000)
    app.run(host="0.0.0.0", port=5000)