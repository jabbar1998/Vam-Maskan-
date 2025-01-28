# Bank Checker with Selenium

This application is designed to check a specific website to determine whether a bank service is open or closed. Built using Selenium, it automates interactions with the website and verifies the availability of a particular bank.

---

## Features

- Automates navigation and interactions with the target website.
- Logs into the website using a phone number and OTP.
- Checks for specific text or elements to identify the status of the bank.
- Handles dynamic page content and retries actions in case of errors.

---

## Prerequisites

To use this application, ensure you have the following installed:

1. **Python** (Version 3.8 or higher)
2. **Google Chrome** (Latest stable version)
3. **ChromeDriver** (Compatible with your Chrome version)
4. Required Python libraries (see `requirements.txt`)

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/bank-checker.git
   cd bank-checker
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure that the `chromedriver` executable is in your PATH or in the project directory.

---

## Usage

1. Update the script with the necessary login details:

   - Replace the phone number in the `entery_form` method with your own:

     ```python
     username_field.send_keys("YOUR_PHONE_NUMBER")
     ```

2. Run the application:

   ```bash
   python app.py
   ```

3. The application will:

   - Navigate to the website.
   - Log in using the provided phone number.
   - Check the availability of a specific bank (e.g., "Sépah").
   - Refresh and retry in case of errors or if the bank is closed.

4. The status of the bank (open or closed) will be printed in the console.

---

## File Structure

- `app.py`: Main script that runs the Selenium automation.
- `requirements.txt`: List of required Python libraries.
- `README.md`: Documentation for the project.

---

## Dependencies

The following Python libraries are required:

- `selenium`

Install them using:

```bash
pip install selenium
```

---

## Notes

- Ensure the target website (https://saman.mrud.ir/) is accessible before running the script.
- Replace hardcoded values (e.g., phone number) with your own.
- The script is for educational and personal use only. Please respect website terms of service.
- Adjust timeouts in the methods (`wait_for_element`, `click_element`, etc.) as needed for your internet speed or website performance.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for any feature requests or bugs.

---

## Contact

For any questions or support, contact [abduljabbar.raeisi1998@gmail.com].
