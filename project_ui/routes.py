from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

from make_prediction import ModelPrediction

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict_price():
    if request.method == "POST":
        # collect form data

        form_house_data = {
            "total_sqft" : request.form.get("total_area"),
            "livable_sqft" : request.form.get("livable_area"),
            "num_bedrooms" : request.form.get("num_bedrooms"),
            "num_bathrooms" : request.form.get("num_bathrooms"),
            "flat_condition" : request.form.get("flat_condition"),
            "flooring_type" : request.form.get("flooring_type"),
            "parking" : request.form.get("parking_available"),
            "furnishing_state" : request.form.get("furnishing_state"),
            "year_built" : request.form.get("year_built"),
            "location": request.form.get("location"),
            "property_on_num" : request.form.get("property_on"),
        }

        # return jsonify(form_house_data)
        # exit()

        predict_obj = ModelPrediction()
        output = predict_obj.make_prediction(form_house_data)


        return render_template("result.html", output = output)

# app.add_url_rule('/','/',index())


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)