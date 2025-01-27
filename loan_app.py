from flask import Flask, request
import pickle

app = Flask(__name__)

# model loading
model_file = open("classifier.pkl", "rb")
model = pickle.load(model_file)

# model.predict(inputs)

# let's create end point

@app.route("/", methods=["GET"])
def home():
    return "<h1>Loan Approval Application</h1>"

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        # use method and predict

        loan_req = request.get_json()
        print(loan_req)
        
        if loan_req['Gender'] == "Male":
            Gender =0
        else:
            Gender = 1

        if loan_req['Married'] == "No":
            Married = 0
        else:
            Married = 1

        if loan_req['Credit_History'] == "Unclear Debts":
            Credit_History = 0
        else:
            Credit_History = 1


        ApplicationIncome = loan_req['ApplicationIncome']
        LoanAmount = loan_req['LoanAmount'] / 1000
        #Credit_History = loan_req['Credit_History']
 
        result = model.predict([[Gender,Married,ApplicationIncome,LoanAmount,Credit_History]])


        if result == 0:
            pred = "Rejected"
        else:
            pred = "Approved"

        result = {
            'loan_approval_status': pred
        }

        return jsonify(result)


@app.route('/ping', methods=['GET'])
def ping():
    return "Pinging Model!!"
    #     return {"loan_approval_status":pred}  
    # else:
    #     return "I will make the predictions"      

     