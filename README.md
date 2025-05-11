# ad-creator-in-gcp

This package is designed to create advertisements using Large Language Models (LLMs) and host the service in Google Cloud Platform (GCP).

## Development in GitHub Codespaces

To develop this package in GitHub Codespaces, follow these steps:

### Prerequisites
1. Ensure you have access to GitHub Codespaces.
2. Verify that your repository is configured to support Codespaces.

### Steps
1. Open the repository in GitHub and click on the **Code** button.
2. Select the **Codespaces** tab and click **Create codespace on main** (or the desired branch).
3. Wait for the Codespace environment to initialize.

### Development Workflow
1. Once the Codespace is ready, the development environment will be pre-configured with the necessary tools.
2. Use the terminal to install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the application locally for testing:
    ```bash
    python main.py
    ```
4. Make changes to the code and test iteratively.

### Testing
Run the test suite to ensure your changes work as expected:
```bash
pytest
```

### Deployment
Follow the deployment instructions in the `DEPLOYMENT.md` file to host the service in GCP.

For further assistance, refer to the documentation or open an issue in the repository.
### Managing GitHub Actions for Deployment

If the GitHub Actions workflow for deployment is already set up in the package, follow these steps to manage and monitor it:

#### Triggering the Workflow
1. Push changes to the `main` branch (or the branch specified in the workflow file) to automatically trigger the deployment workflow.
2. Ensure your commits include all necessary updates before pushing.

#### Monitoring Workflow Runs
1. Navigate to the **Actions** tab in your GitHub repository.
2. Select the relevant workflow (e.g., "Deploy to GCP") from the list of workflows.
3. Click on the latest run to view detailed logs and monitor the progress of the deployment.

#### Debugging Failures
1. If a workflow run fails, review the logs in the **Actions** tab to identify the issue.
2. Common issues include:
    - Missing or invalid GCP credentials.
    - Errors in the application code or dependencies.
    - Misconfigured GCP project settings.

#### Rerunning a Workflow
1. In the **Actions** tab, locate the failed workflow run.
2. Click the **Re-run jobs** button to retry the workflow after addressing the issue.

#### Updating the Workflow
1. If changes are needed in the workflow, edit the `.github/workflows/deploy.yml` file.
2. Commit and push the changes to apply the updates.

For further assistance, refer to the GitHub Actions documentation or open an issue in the repository.

### Google Cloud Configuration

Before deploying the application, ensure the following steps are completed in Google Cloud:

1. **Enable Required APIs**:
   - Go to the **APIs & Services** > **Library** in the GCP Console.
   - Enable the following APIs:
     - Cloud Build API
     - App Engine Admin API
     - Cloud Storage API

2. **Create an App Engine Application**:
   - Navigate to **App Engine** in the GCP Console.
   - Click **Create Application** and select your region.

3. **Set Up a Service Account**:
   - Go to **IAM & Admin** > **Service Accounts**.
   - Create a service account with the necessary roles:
     - App Engine Admin
     - Cloud Build Editor
   - Download the service account key as a JSON file.

4. **Configure Billing**:
   - Ensure your GCP project has billing enabled.

### Accessing the Application

After deployment, you can access the application using the URL provided by App Engine:

1. Navigate to the **App Engine** > **Dashboard** in the GCP Console.
2. Copy the URL of your deployed application (e.g., `https://<your-project-id>.appspot.com`).
3. Open the URL in your browser to access the web page.

For troubleshooting or further customization, refer to the GCP documentation or open an issue in the repository.