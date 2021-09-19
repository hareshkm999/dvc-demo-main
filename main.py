from wsgiref import simple_server
from flask import Flask, render_template, request, jsonify
import joblib
import os
import numpy as np
from prediction_service import prediction
#import json
#import numpy as np
"""
*****************************************************************************
*
* filename:       main.py
* version:        1.0
* author:         HARISH
* creation date:  2-feb-2021
*
* change history:
*
* who             when           version  change (include bug# if apply)
* ----------      -----------    -------  ------------------------------
* HARISH          23-JAN-2021    1.0      initial creation
*
*
* description:    flask main file to run application
*
****************************************************************************
"""

app = Flask(__name__)



@app.route('/')
def index_page():
    """
    * method: index_page
    * description: method to call index html page
    * return: index.html
    *
    * who             when           version  change (include bug# if apply)
    * ----------      -----------    -------  ------------------------------
    * HARISH          23-JAN-2021    1.0      initial creation
    *
    * Parameters
    *   None
    """
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    try:
        if request.method == 'POST':
            air_temperature = float(request.form['air_temperature'])
            rotational_speed = float(request.form['rotational_speed'])
            torque = float(request.form['torque'])
            wear = float(request.form['wear'])
            failure = float(request.form['failure'])
            twf = float(request.form['twf'])
            hdf = float(request.form['hdf'])
            pwf = float(request.form['pwf'])
            osf = float(request.form['osf'])
            rnf = float(request.form['rnf'])
            filename = 'saved_models/model.joblib'

            loaded_model = joblib.load(filename)

            prediction = str(list(loaded_model.predict([[air_temperature, rotational_speed, torque, wear, failure, twf, hdf, pwf, osf, rnf]])))
            print(prediction)


            #return render_template('result.html', prediction=prediction)
            return "prediction results captured, prediction is   : " + str(prediction)
        else:
            return render_template('index.html')
    except Exception as e:
        print(e)





if __name__ == "__main__":
    #app.run(debug=True)
    host = '0.0.0.0'
    port = 5026
    httpd = simple_server.make_server(host, port, app)
    httpd.serve_forever()
