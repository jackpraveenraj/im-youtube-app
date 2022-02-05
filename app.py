
from flask import Flask, jsonify
from flask import request
from googleapiclient.discovery import build


app = Flask(__name__)

# routes
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # get data
    
    #data = request.get_json
    data = request.args['t']
    cat = request.args['cat]
    
    newurl = data.replace('https://www.youtube.com/watch?v=', '')
    newurl = newurl.split("&ab_channel", 1)

    api_key = 'AIzaSyALffU0NRLBe-jQPCnFDsl5uO6XP52HCJQ'
    youtube = build('youtube', 'v3', developerKey=api_key)

    request1 = youtube.videos().list(
            part='topicDetails',
            id = newurl[0]
        )
    response = request1.execute()
    res = response['items'][0]['topicDetails']['topicCategories']

    predictions = 0
    cats = cat.split(",")
                       
    for i in res:
      for j in cats:
        if j == "game":
          if ((i.find('game') != -1) or (i.find('gaming') != -1)):
            predictions = 1
            break
        elif j == "entertainment":
          if ((i.find('entertainment') != -1) or (i.find('movie') != -1) or (i.find('movies') != -1) or (i.find('film') != -1) or (i.find('films') != -1) or (i.find('tv') != -1)):
            predictions = 1
            break
        elif j == "sport":
          if ((i.find('sport') != -1) or (i.find('sports') != -1)):
            predictions = 1
            break
        elif j == "education":
          if ((i.find('education') != -1) or (i.find('knowledge') != -1) or (i.find('science') != -1) or (i.find('mathematics') != -1) or (i.find('academics') != -1)):
            predictions = 1
            break

    output = {'results': predictions}
    return jsonify(results=output)

@app.errorhandler(500)
def internal_error(error):

    return "500 error"

if __name__ == '__main__':
    app.run(port = 5000, debug=True)
