from PIL import Image
from io import BytesIO
import urllib.request
from flask import Flask, jsonify
from flask import request


import requests

from googleapiclient.discovery import build


app = Flask(__name__)

# routes
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # get data
    
    #data = request.get_json
    data = request.args['t']
    newurl = data.replace('https://www.youtube.com/watch?v=', '')
    newurl = newurl.split("&ab_channel", 1)
    from googleapiclient.discovery import build

    api_key = 'AIzaSyALffU0NRLBe-jQPCnFDsl5uO6XP52HCJQ'
    youtube = build('youtube', 'v3', developerKey=api_key)

    request1 = youtube.videos().list(
            part='topicDetails',
            id = newurl[0]
        )
    response = request1.execute()
    res = response['items'][0]['topicDetails']['topicCategories']

    for i in res:
      if ((i.find('game') != -1) or (i.find('movie') != -1) or (i.find('entertainment') != -1) or (i.find('tv') != -1)) :
          predictions = 1
          break
      else:
          predictions = 0


    #predictions = model1.predict(img_array)

    output = {'results': predictions}
    return jsonify(results=output)

@app.errorhandler(500)
def internal_error(error):

    return "500 error"

if __name__ == '__main__':
    app.run(port = 5000, debug=True)
