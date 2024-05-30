from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=["POST"])
def inbound_sms():
    """Process incoming SMS messages."""

    from_number = request.form["From"]
    message_body = request.form["Body"]

    # Log or perform actions based on the message content (optional)
    print(f"Received SMS from {from_number}: {message_body}")

    # Optionally send a reply using TwiML
    resp = MessagingResponse()
    resp.message(f"Thanks for your message! You sent: {message_body}")
    return str(resp)


