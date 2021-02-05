from flask import Flask,request,jsonify
import utils

app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():

    response = jsonify({
        'locations': utils.get_location_names()
    })

    response.headers.add('Access-Control-Allow-Origin','*')

    return response


@app.route('/predict',methods=['POST'])
def predict():
    sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price':utils.estimated_price(location,sqft,bhk,bath)
    })

    response.headers.add('Access-Control-Allow-Origin','*')

    return response


if __name__ == '__main__':

    print('app started')

    utils.load_saved_artifacts()
    app.run()