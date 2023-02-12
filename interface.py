from flask import Flask , render_template, jsonify , request
from utilities import predict_species
import config

app=Flask(__name__)

# Route to home page
@app.route("/")
def app_home():
    return render_template("index.html")

# Route to prediction page
@app.route("/prediction" , methods=["post"])

# function to get the result
def get_species_name():
    data=request.form
    species=predict_species(data)

    #return jsonify({"result":species})
    return render_template("index.html",result=species)

# code for run
if __name__=="__main__":
    app.run(debug=True , port=config.PORT, host=config.HOST)


