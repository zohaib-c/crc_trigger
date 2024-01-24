# Cloud Resume Challenge - API with Azure Functions

The Cloud Resume Challenge API is implemented using Azure Functions' HTTP Trigger in Python. This API is designed to respond to GET requests from the front-end webpage. Upon receiving a request, it updates the count in the Azure Table Storage Entity and returns the updated count to the webpage.

## GitHub Actions Workflows

A single GitHub Action, `main_crctrigger.yml`, is used to build and deploy the function each time new changes are pushed to the repository. 
