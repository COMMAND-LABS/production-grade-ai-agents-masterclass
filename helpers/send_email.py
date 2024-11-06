import requests
import os

def send_email():
    print("Sending email...")
    requests.post(
      "<YOUR_MAILGUN_DOMAIN_HERE",
      auth=("api", os.getenv("MAILGUN_API_KEY")),
      data={
        "from": "Wishbliss A.I. News Reporter <noreply@noreply.com>",
        "to": ["<YOUR_AUTHORIZED_EMAIL_HERE>"],
        "subject": "Hello",
        "text": "Testing !!! some !!! weirdness"
      }
    )
