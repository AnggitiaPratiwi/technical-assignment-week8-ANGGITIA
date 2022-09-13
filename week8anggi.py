import pymongo #mengimport library pymongo      
import datetime
from flask import Flask, request 

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://anggitia:anggi@cluster0.oqxl1kl.mongodb.net/?retryWrites=true&w=majority")
db = client['week8']
my_collections = db['anggitia']
timestamp = datetime.datetime.now()

@app.route('/semangat',methods=['GET','POST'])
def semangat():
    kecepatan = request.args.get('kecepatan')
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    
    if request.method == 'POST':
    
       results = my_collections.insert_one({"kecepatan":kecepatan,"latitude":latitude,"longitude":longitude, "timestamp":timestamp})
       print(results)
       return {
            "kecepatan":kecepatan,
            "latitude":latitude,
            "longitude":longitude,
            "timestamp":timestamp
                }

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 8001, debug = True)