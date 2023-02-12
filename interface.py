from flask import Flask , render_template, jsonify , request
from utilities import predict_species
import config

app=Flask(__name__)

@app.route("/")
def app_home():
    return render_template("index.html")

@app.route("/prediction" , methods=["post"])

def get_species_name():
    data=request.form
    species=predict_species(data)

    #return jsonify({"result":species})
    return render_template("index.html",result=species)

if __name__=="__main__":
    app.run(debug=True , port=config.PORT, host=config.HOST)





