# Two-Factor Authentication (2FA) Flask App

This Flask app provides a simple and secure Two-Factor Authentication (2FA) system using the `pyotp` Python package. It implements a RESTful API with two endpoints – one for generating OTPs (One-Time Passwords) and another for authentication.

## Features

- **OTP Generation Endpoint**: `/generate_otp` - Generates a time-based OTP.
  
- **Authentication Endpoint**: `/authenticate` - Validates the provided OTP.

- **Email OTP Option**: Setup the app with your Gmail ID and app password to receive OTPs via email. [Learn how to set up a Gmail App Password](https://support.google.com/accounts/answer/185833?hl=en).

## Getting Started

1. **Setup**:

    Run the following command to initialize the project. This setup will ask for your Gmail ID and app password. If you choose Google Authenticator, this step is exempt.

    ```bash
    python init.py
    ```

2. **Run the Flask App**:

    ```bash
    python app.py
    ```

3. **Endpoints**:

    - **Generate OTP**: `http://localhost:5000/generate_otp`
        - Method: `POST`
        - Parameters: None
        - Returns: JSON with generated OTP and provisioning URL for Google Authenticator.

    - **Authenticate**: `http://localhost:5000/authenticate`
        - Method: `POST`
        - Parameters: 
            - `otp`: The OTP to be verified.
            - `email` (optional): If using email OTP, provide the email address.

## Example Usage

- **Generate OTP**:

    ```bash
    curl -X POST http://localhost:5000/generate_otp
    ```

- **Authenticate**:

    ```bash
    curl -X POST -d "otp=123456" http://localhost:5000/authenticate
    ```

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or want to contribute new features, please open an issue or a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contact

For questions or inquiries, feel free to contact the project maintainer:

- Your Name
- Your Email Address

---

Thank you for using this Two-Factor Authentication Flask App. We hope it enhances the security of your application by implementing 2FA seamlessly.
