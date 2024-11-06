# PT. 6 - Add Mailgun

Next up we’ll integrate email into our application…

There are many email providers we could use, but for demonstration purposes we’ll go with Mailgun…

##

I’m suggesting Mailgun as I found their integration process to be relatively straightforward but Feel free to use another email provider if you prefer…

Anyways! Come over to https://signup.mailgun.com/new/signup…

After signing up you’ll have to verify your account via an Authorization Code that you’ll receive in either your inbox or on your phone…

After you complete this account verification process, you can then provision an API key

This API key is what will authenticate our application with Mailgun’s Email API

We can store this API key in the .env file by adding an entry that reads MAILGUN_API_KEY=<API_KEY_HERE>

##

Next let’s come over to the domains page of the Mailgun console (https://app.mailgun.com/mg/sending/domains). And we can see that Mailgun provides us with a free domain for testing…

We will be able to send emails FROM this domain TO any email we list as an authorized recipient here…

To authorize a recipient, we enter and submit an email address using this form AND will need the owner of the address to accept the invitation they’ll receive in their INBOX

##

After we authorize some email we have access to, let’s test out our Mailgun setup by adding the following code to our application…

###

```sh
touch helpers/send_email.py
```
```python
import requests
import os

def send_email():
    print("Sending email...")
    requests.post(
      "https://api.mailgun.net/v3/sandboxd7c358e02f26415dbb7329dd994a8334.mailgun.org/messages",
      auth=("api", os.getenv("MAILGUN_API_KEY")),
      data={"from": "Wishbliss Test Mailing List <mailgun@sandboxd7c358e02f26415dbb7329dd994a8334.mailgun.org>",
        "to": ["tad@cmdlabs.io"],
        "subject": "Testing Mailgun",
        "text": "Testing !!! some !!! weirdness"})
```

###

edit the main.py on line 71

```python
send_email()
```

After adding this code, we can test our script again and should receive an email in our SPAM folder

PRO TIP: let’s comment out most of our code and just test that emailing works…

`python main.py`

And we should see an email arrive, likely in our SPAM folder

##

If you don’t mind finishing this walkthrough with emails being delivered to SPAM then skip ahead to PART 7

BUT if you’d like the emails to be delivered to people’s INBOX as expected, here are the steps you’ll need to take…

Come over to the https://app.mailgun.com/mg/sending/domains page again and click “Add new domain”

Then specify the subdomain of some domain you own for example I used the name mail.wishbliss.link (where my domain is wishbliss.link)

After you add your domain you’ll be presented with a list of records that you’ll need to add to your domain’s DNS settings

After these records are added to our DNS we can click `Verify` to have Mailgun confirm that we’re indeed the owner of this domain

And now, when we send emails from our verified domain with Mailgun, the emails should land in our INBOX as expected

ie: noreply@wishbliss.link

##

If you have issues purchasing a domain or verifying it with your email provider, leave a comment or paste detailed descriptions of your issues into either Google or ChatGPT. If you’ve gotten this far, don’t be discouraged. Setting up emailing for a custom domain is not too difficult but can be a bit tricky at times. If someone in the community knows of a simpler way to implement email integrations, leave a comment and I’ll pin it to the top of the comments.

Let’s move on to PART 7
