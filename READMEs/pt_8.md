# PT. 8 - Adding AgentOps

The process of integrating with AgentOps is very similar to the process of integrating with OpenAI’s platform

First come over to https://app.agentops.ai/ and sign up if you haven’t already

Then find the page for provisioning API keys

I found it by opening the “Profile” dropdown and selecting the “API keys” option

On the API keys page, you should see a default API key that you can copy

##

Let’s add this API key to our project by adding a new line in our .env file that reads `AGENTOPS_API_KEY=`

Once we have the API key set up we can install the agentops package by adding another entry to the requirements.txt file

```sh
agentops==0.3.14
```

And running the `pip install process…` in the development environemt

And then we can initialize the agentops tracker in our main.py file like so…

```
import agentops
agentops.init(os.getenv("AGENTOPS_API_KEY"))
```

Make sure agentops is initialized BEFORE our Agents get to work

(PAUSE)

And if we run our application now, we should see some info in the AgentOps console…

- Showcase the AgentOps dashboard

(PAUSE)

To set up AgentOps in GCP aka in our Production Environment, we have to add the AGENTOPS_API_KEY as a secret in “Secret Manager”

```
echo "YOUR_NEW_SECRET_VALUE" | gcloud secrets create AGENTOPS_API_KEY --data-file=-
```

And give our Default Compute Service Account permissions to access it

```sh
gcloud secrets add-iam-policy-binding AGENTOPS_API_KEY \
  --member="serviceAccount:$PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor"
```

And then we reference it in the “—set-secrets” flag of our CICD script…

--set-secrets “AGENTOPS_API_KEY=projects/${{ env.PROJECT_NUMBER }}/secrets/AGENTOPS_API_KEY:latest” \

Now let’s push this code to update our job in GCP

And when we trigger our Cloud Run job we should still be seeing data being fed into AgentOps from our Agents running in GCP…

gcloud run jobs execute first-crj-ever --region us-east1 --project $PROJECT_ID

NOTE TO SELF: After AgentOps is showing the session running in GCP

After confirming that’s working, let’s move on to the final section!