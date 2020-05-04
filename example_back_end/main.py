import os
import pymongo
import datetime
import requests
import urllib.parse
from twilio.twiml.messaging_response import MessagingResponse
from bson.objectid import ObjectId
from flask import Flask, request
from flask import send_file
from twilio.rest import Client 
from io import BytesIO
from PIL import Image


# accesses mongoDB account
app = Flask(__name__)
# password = urllib.parse.quote_plus("password_here")
# client = pymongo.MongoClient("mongodb+srv://admin:"+password+"@insert_url_here?retryWrites=true&w=majority")
db = client["test"]
imagesCol = db["images"]



# checks if texts are being recieved 
@app.route("/", methods=['GET', 'POST'])
def index():
    return "The server is running! The texts are actually being sent to ./sms"

# code for veiwing gage plate image
@app.route("/viewImage")
def viewImage():
    return send_file("imageView.html")
@app.route("/return_image", methods=['GET'])
def returnImage():
    try:
        data = db.images.find_one({"_id": ObjectId(request.values.get("id"))})
        image_binary = data["image"]
        #Can also open tbe image with img = Image(BytesIO(image_binary)) and procede to manipulate locally.
        return send_file(
            BytesIO(image_binary),
            mimetype='image/jpeg',
            as_attachment=True,
            attachment_filename='image.jpg')
    except Exception as e:
        return "Something failed"

# checks if sent message is an image
@app.route("/sms", methods=['GET', 'POST'])
def sms_reciever():
    #recieves sms messages sand passes them on if it is an image
    resp = MessagingResponse()
    try: 
        phoneNumber = request.values.get('From')
        imageURL = request.values.get('MediaUrl0')
        # body = request.values.get('Body', None)
        if imageURL != None:
            data = requests.get(imageURL)
            entry = {"author": phoneNumber, "image":data.content, "location":"Earth", "timestamp":datetime.datetime.utcnow()}
            entryId = imagesCol.insert_one(entry).inserted_id
            resp.message("Image being processed, here is the id of the db entry: " + str(entryId))#Your image is being processed
        else:
            # db.example.insert_one({"phone":phoneNumber, "data":body})
            resp.message("Recieved a text. Try sending an image next time. * Note, this image will be stored *")
        return str(resp)
    except:
        return "Something failed"
account_sid = 'insert_account_id_here' 
auth_token = 'insert_token_here' 
client = Client(account_sid, auth_token) 




port = int(os.getenv('PORT', 8000))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
    message = client.messages \
    # creates Twilio message
    .create(
         body='Server Up!',
         from_='+twilio_number',
         to='+devs_phone_number'
     )
