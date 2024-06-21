# 📷 Blur Detection API

This API detects if an image is blurry. It is built using Python, Flask, TensorFlow, and Docker, and deployed on Google Cloud Run.

## 📜 Table of Contents
- [🛠 Requirements](#requirements)
- [⚙️ Setup](#setup)
- [💻 Running Locally](#running-locally)
- [☁️ Deploying to Google Cloud Run](#deploying-to-google-cloud-run)
- [📡 Usage](#usage)
- [📤 Example Request](#example-request)
- [📥 Example Response](#example-response)
- [🔍 Local Testing with Postman](#local-testing-with-postman)
- [⚠️ Common Issues](#common-issues)
- [🔚 Conclusion](#conclusion)

## 🛠 Requirements
- 🐍 Python 3.9+
- 🐳 Docker
- ☁️ Google Cloud SDK (for deployment)

## ⚙️ Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/frhnspwli/aireal-model-api.git
    cd blur-detection-api
    ```

2. **Create a virtual environment and install dependencies:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Place your model file:**
    - Ensure the `model.h5` file is placed inside the `app` directory.

## 💻 Running Locally

1. **Build and run the Docker container:**
    ```bash
    docker build -t blur-detection-app .
    docker run -p 8080:8080 blur-detection-app
    ```

2. **Make a request to the local server:**
    - You can use Postman or `curl` to test the API.

    Example `curl` request:
    ```bash
    curl --location "http://localhost:8080/" \
    --form "file=@\"/path/to/your/image.png\""
    ```

## ☁️ Deploying to Google Cloud Run

1. **Authenticate with Google Cloud:**
    ```bash
    gcloud auth login
    gcloud config set project your-project-id
    ```

2. **Build the Docker image and push to Google Container Registry:**
    ```bash
    docker build -t gcr.io/your-project-id/blur-detection-app .
    docker push gcr.io/your-project-id/blur-detection-app
    ```

3. **Deploy to Google Cloud Run:**
    ```bash
    gcloud run deploy blur-detection-app --image gcr.io/your-project-id/blur-detection-app --platform managed --region your-region --allow-unauthenticated
    ```

## 📡 Usage

### Endpoint
- **URL**: `https://your-cloud-run-service-url/`
- **Method**: `POST`
- **Body**: `form-data`
  - **Key**: `file`
  - **Type**: File
  - **Description**: The image file to be checked for blurriness.

### 📤 Example Request
#### Using `curl`:
```bash
curl --location "https://your-cloud-run-service-url/" \
--form "file=@\"/path/to/your/image.png\""
```

### 📥 Example Response
```json
{
  "is_blurry": false,
  "percentage": "98.43%",
  "prediction": [
    [
      0.9842818379402161
    ]
  ]
}
```

## 🔍 Local Testing with Postman
1. Open Postman.
2. Create a new POST request.
3. Set the URL to `http://localhost:8080/`.
4. In the body tab, select `form-data`.
5. Add a new key:
   - Key: `file`
   - Type: `File`
   - Value: Choose the image file you want to test.
6. Send the request and you should see a JSON response indicating whether the image is blurry.

## ⚠️ Common Issues
- **Memory Limit Exceeded**: If you encounter a memory limit error on Google Cloud Run, consider increasing the memory limit in your deployment settings.
- **Module Not Found**: Ensure all dependencies are correctly listed in the `requirements.txt` file and installed.

## 🔚 Conclusion
This API provides a simple interface to check if an image is blurry using a machine learning model. It is containerized with Docker and can be easily deployed on Google Cloud Run for scalable and serverless operation.

For any issues or contributions, please refer to the [GitHub repository](https://github.com/frhnspwli/aireal-model-api).
