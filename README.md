# SnapHub

Snaphub is a signup module developed using Python and Django framework. It allows users to sign up with their basic information like first name, last name, mobile number, and email address. Upon signup, a verification email is sent to the provided email address for authentication.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Overview

Snaphub is a simple yet effective signup module designed to capture user information securely and efficiently. It follows standard practices seen across various websites like Zomato, Flipkart, and MakeMyTrip. The primary goal of Snaphub is to provide a seamless signup experience for users while ensuring the security and authenticity of their information.

## Features

- User-friendly signup form with fields for first name, last name, mobile number, and email address.
- Email verification system to authenticate user email addresses.
- Responsive design for seamless user experience across devices.

## Installation

To install and run Snaphub locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/divyesh1099/snapHub.git
    ```

2. Navigate to the project directory:

    ```bash
    cd snaphub
    ```

3. Install the project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables for Gmail SMTP configuration (SMTP_EMAIL and SMTP_PASSWORD) in your operating system or create a `.env` file in the project directory with the following content:

    ```
    SMTP_EMAIL=your-email@gmail.com
    SMTP_PASSWORD=your-email-password
    ```

5. Run Django migrations:

    ```bash
    python manage.py migrate
    ```

6. Start the development server:

    ```bash
    python manage.py runserver
    ```

7. Access the application in your web browser at `http://localhost:8000/`.

## Usage

To use Snaphub, follow these steps:

1. Navigate to the signup page at `http://localhost:8000/signup`.
2. Fill in the required fields: first name, last name, mobile number, and email address.
3. Click on the "Sign Up" button to submit the form.
4. Check your email inbox for the verification link sent by Snaphub.
5. Click on the verification link to authenticate your email address and complete the signup process.

## Technologies Used

- Python
- Django
- Tailwind CSS
- Gmail SMTP (for email verification)

## Deployment

Snaphub is deployed on PythonAnywhere at [https://snaphub.pythonanywhere.com/](https://snaphub.pythonanywhere.com/).

## Contributing

If you'd like to contribute to Snaphub, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to modify and enhance the README.md to include any additional information or customization specific to your project.

## Acknowledgements
- Techyon F2F Interview
- Moti❤️