import pickle
from flask import Flask, render_template, request


app = Flask(__name__)


tfidf = pickle.load(open('df.pkl','rb'))
model = pickle.load(open('Gradient_Boost.pkl','rb'))


@app.route("/", methods=['GET', 'POST'])
# @cross_origin()
def home ():

    return render_template("home.html")


@app.route('/predict', methods=['POST'])
# @cross_origin()
def predict():
    if request.method == "POST":
        Age = request.form.get('Age', type=int)

        Sex = request.form.get('Sex', type=int)
        if Sex == 'M':
            M = 1
            F = 0
        elif Sex == 'F':
            M = 0
            F = 1

        ChestPainType = request.form.get('ChestPainType', type=int)
        if ChestPainType == 'ASY':
            ASY = 1
            NAP = 0
            ATA = 0
            TA  = 0

        elif ChestPainType == 'NAP':
            ASY = 0
            NAP = 1
            ATA = 0
            TA  = 0

        elif ChestPainType == 'ATA':
            ASY = 0
            NAP = 0
            ATA = 1
            TA  = 0

        elif ChestPainType == 'TA':
            ASY = 0
            NAP = 0
            ATA = 0
            TA  = 1

        RestingBP   = request.form.get('RestingBP', type=int)

        Cholesterol = request.form.get('Cholesterol', type=int)

        FastingBS   = request.form.get('FastingBS', type=int)

        RestingECG  = request.form.get('RestingECG', type=int)
        if RestingECG == 'Normal':
            Normal = 1
            LVH    = 0
            ST     = 0
        elif RestingECG == 'LVH':
            Normal = 0
            LVH    = 1
            ST     = 0
        elif RestingECG == 'ST':
            Normal = 0
            LVH    = 0
            ST     = 1

        MaxHR = request.form.get('MaxHR', type=int)

        ExerciseAngina = request.form.get('ExerciseAngina', type=int)
        if ExerciseAngina == 'Y':
            Y = 1
            N = 0
        elif ExerciseAngina == 'N':
            Y = 0
            N = 1

        Oldpeak = request.form.get('Oldpeak', type=float)

        ST_Slope = request.form.get('ST_Slope', type=int)
        if ST_Slope == 'Flat':
            Flat = 1
            Up   = 0
            Down = 0
        if ST_Slope == 'Up':
            Flat = 0
            Up   = 1
            Down = 0
        if ST_Slope == 'Down':
            Flat = 0
            Up   = 0
            Down = 1

        result = model.predict([[Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG,MaxHR,
                                 ExerciseAngina, Oldpeak, ST_Slope]])

        if result == 0:
            label = 'Congrats! You have not any symptoms for Heart Disease.'
        else:
            label = 'Oops, You have to consult with Doctor.'

    return render_template('result.html', prediction_text=label)





if __name__ == '__main__':
    app.run(debug=True)