from flask import Flask, request, Response, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'Presentation'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Presentation'

mongo = PyMongo(app)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
	"""Respond to incoming messages with a friendly SMS."""
	#print("check")
	from_number = request.values.get('From')
	print(from_number)
	body = request.values.get('Body')
	print(body)
	mongo.db.Users.insert({'Number' : from_number, 'Replies' : body})
	# Start our response
	resp = MessagingResponse()

    # Add a message
	resp.message("Hello! Thanks for sending in your findings!")

	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)