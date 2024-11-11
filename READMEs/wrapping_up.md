# WRAPPING UP

As promised, here’s how you can easily tear down this GCP project and avoid incurring charges.

First, let’s undo what we’ve built up till this point…

ie:

Delete the cron-job - `gcloud scheduler jobs delete cron-job-for-first-crj-ever --location=us-east1 --project=$PROJECT_ID`
Delete the crj -`gcloud run jobs delete first-crj-ever --region=us-east1 --project=$PROJECT_ID`
Delete the Artifact Repository - `gcloud artifacts repositories delete repo-for-job-1 --location=us-east1 --project=$PROJECT_ID`
Delete the Service Accounts - `gcloud iam service-accounts delete cron-job-sa@hthtogcrj.iam.gserviceaccount.com --project=$PROJECT_ID`
Delete the Service Accounts - `gcloud iam service-accounts delete hthtogcrj-cicd-sa@hthtogcrj.iam.gserviceaccount.com --project=$PROJECT_ID`

Delete the Secrets
```sh
gcloud secrets delete AGENTOPS_API_KEY --project=$PROJECT_ID
gcloud secrets delete AI_NEWS_RECIPIENTS --project=$PROJECT_ID
gcloud secrets delete MAILGUN_API_KEY --project=$PROJECT_ID
gcloud secrets delete OPENAI_API_KEY --project=$PROJECT_ID
```

After then deleting the resources we’ve provisioned, shut down the project on the Project Dashboard > Project Settings page to mark any stray resources for deletion after 30 days.