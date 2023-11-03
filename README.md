# bruteforce_algorithm_on_web_project
Web secuirity - Bruteforce Algorith in action.

```markdown
# Brute Force Password Cracker

This project is a simple brute force password cracker implemented in Python using the `httpx` library. It attempts to crack a user's password by iterating through a list of possible passwords and making HTTP requests to a login endpoint.

## Prerequisites

To run this project, you need to have Python installed on your machine. Additionally, you'll need to install the `httpx` library. You can install it using the following command:

```
pip install httpx
```

## Usage

1. Clone the repository or download the `bruteforce1.py` file.
2. Open the file in a text editor or IDE of your choice.
3. Uncomment lines 8-10 to read passwords from a file if you have a password list stored in `password_new.txt`. Alternatively, use the generated passwords list.
4. Run the script using the command `python bruteforce1.py`.
5. Enter the username you want to target for the password cracking.
6. The script will start making HTTP requests to the login endpoint with different passwords.
7. If a correct password is found, it will be displayed, and the script will stop.

**Note:** This project is provided for educational purposes only. Unauthorized access to systems or accounts is illegal and unethical. Use this script responsibly and with proper authorization.

## License

This project is licensed under the [MIT License](LICENSE).
```
