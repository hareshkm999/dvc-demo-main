from flask import Flask, render_template, request, jsonify
import os
import numpy as np
from prediction_service import prediction


webapp_root = "webapp"

static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")

app = Flask(__name__, static_folder=static_dir,template_folder=template_dir)


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

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




        try:
            if request.form:
                dict_req = dict(request.form)
                response = prediction.form_response(dict_req)
                print(dict_req)
                return render_template("index.html", response=response)

        except Exception as e:
            print(e)
            error = {"error": "Something went wrong!! Try again later!"}
            error = {"error": e}

            return render_template("404.html", error=error)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)