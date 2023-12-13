# Two-Factor Authentication (2FA) Flask App

This Flask app provides a simple and secure Two-Factor Authentication (2FA) system using the `pyotp` Python package. It implements a RESTful API with two endpoints – one for generating OTPs (One-Time Passwords) and another for authentication.

## Features

- **OTP Generation Endpoint**: `/generate_otp` - Generates a time-based OTP.
  
- **Authentication Endpoint**: `/authenticate` - Validates the provided OTP.

- **Email OTP Option**: Setup the app with your Gmail ID and app password to receive OTPs via email. [Learn how to set up a Gmail App Password](https://support.google.com/accounts/answer/185833?hl=en).

## Getting Started

1. **Setup**:

    Run the following command to initialize the project. This setup will ask for your Gmail ID and app password.

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
        - Body: { "mail": "userEmail@mail.com" }
        - Parameters: None
        - Returns: A successful Response will be 200.

    - **Authenticate**: `http://localhost:5000/authenticate`
        - Method: `POST`
        - Body: 
            - {`otp`: The OTP to be verified }
        - Returns: A successful Response will be 200.

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

---

Thank you for using this Two-Factor Authentication Flask App. We hope it enhances the security of your application by implementing 2FA seamlessly.
