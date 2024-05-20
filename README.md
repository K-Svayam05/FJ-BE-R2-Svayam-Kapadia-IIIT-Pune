# FJ-BE-R2-Svayam-Kapadia-IIIT-Pune

This is a Django-based web application for managing personal finances, allowing users to track their expenses, income, and set up a budget. The application includes features like OAuth integration for Google login and an email notification system for budget overruns.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Features
- User registration and authentication.
- A well-defined database structure implemented using Django models.
- Allow users to add, edit, and delete income and expense transactions.
- Expense and income tracking.
- Develop a user-friendly dashboard that provides an overview of the user's financial status,
including graphical representations of income, expenses, and savings.
- Responsive and user-friendly interface.

## Installation
Follow these steps to set up the project locally:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/K-Svayam05/FJ-BE-R2-Svayam-Kapadia-IIIT-Pune.git
    cd FJ-BE-R2-Svayam-Kapadia-IIIT-Pune
    ```

2. **Create a virtual environment and activate it:**
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```sh
    python manage.py migrate
    ```

5. **Create a superuser (optional):**
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

## Configuration

### Google OAuth Integration

1. **Create a project in the [Google Developers Console](https://console.developers.google.com/).**
2. **Enable the Google+ API and create OAuth 2.0 credentials.**
3. **Add the client ID and secret to your Django settings:**

    ```python
    SOCIALACCOUNT_PROVIDERS = {
        'google': {
            'SCOPE': [
                'profile',
                'email',
            ],
            'AUTH_PARAMS': {
                'access_type': 'online',
            }
        }
    }

    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '<your-client-id>'
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '<your-client-secret>'
    ```

### Email Notification System

1. **Sign up for SendGrid or any other email service.**
2. **Add the API key and other settings to your Django settings:**

    ```python
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.sendgrid.net'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = 'apikey'  # This is the string 'apikey'
    EMAIL_HOST_PASSWORD = '<your-sendgrid-api-key>'
    DEFAULT_FROM_EMAIL = 'your-email@example.com'
    ```

## Usage
- Visit `http://127.0.0.1:8000` to access the application.
- Register a new account or login using Google.
- Add your income and expenses to track your finances.
- Set up a budget and receive email notifications for any budget overruns.

## Deployment
### Deploying on Vercel or Netlify

1. **Ensure you have a `vercel.json` or `netlify.toml` file with the appropriate configurations for deployment.**
2. **Push your code to GitHub.**
3. **Connect your repository to Vercel or Netlify through their respective dashboards.**
4. **Deploy the application.**

Ensure that your Django app is configured to serve static files and handle database migrations properly in the production environment.



---

Developed by Svayam Kapadia, IIIT Pune.


## Screenshots:


![image](https://github.com/K-Svayam05/FJ-BE-R2-Svayam-Kapadia-IIIT-Pune/assets/141111900/6d4b54b0-3178-4d46-a057-e66667c2c03a)
![image](https://github.com/K-Svayam05/FJ-BE-R2-Svayam-Kapadia-IIIT-Pune/assets/141111900/ab6f8aec-d9c6-4cf4-9b97-1089d145ee9b)
![image](https://github.com/K-Svayam05/FJ-BE-R2-Svayam-Kapadia-IIIT-Pune/assets/141111900/f284e2a4-4718-4b3e-8c4d-5cd40993685a)
![image](https://github.com/K-Svayam05/FJ-BE-R2-Svayam-Kapadia-IIIT-Pune/assets/141111900/6f926881-1901-4542-b575-ef2f7f2a096e)
![image](https://github.com/K-Svayam05/FJ-BE-R2-Svayam-Kapadia-IIIT-Pune/assets/141111900/ce0139e8-ffb7-49ad-b721-631e0abf77a4)
