from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import chromedriver_autoinstaller

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>✅ Flask Server Running on Render!</h1>"


def login_to_oura(email, password):
    """ Automates Oura login using Selenium """

    print(f"🟢 Logging in: {email}")

    # Ensure ChromeDriver is installed
    chromedriver_autoinstaller.install()

    # Setup Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in background
    driver = webdriver.Chrome(options=options)

    try:
        print("🌍 Navigating to Oura login page...")
        driver.get("https://cloud.ouraring.com/user/sign-in")
        time.sleep(5)  # Wait for page to load

        # ✅ Find and fill email field
        email_field = driver.find_element(By.NAME, "email")
        email_field.send_keys(email)

        # ✅ Find and fill password field
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys(password)

        # ✅ Click login button
        password_field.send_keys(Keys.RETURN)
        time.sleep(5)  # Wait for login

        print(f"✅ Successfully logged in: {email}")
        driver.quit()
        return True

    except Exception as e:
        print(f"❌ Selenium Error: {e}")
        driver.quit()
        return False


@app.route("/auto-login", methods=["GET"])
def auto_login():
    """ API Endpoint to trigger Selenium login """

    email = request.args.get("email")
    password = request.args.get("password")

    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400

    success = login_to_oura(email, password)

    if success:
        return jsonify({"message": "✅ Auto-login successful!"})
    else:
        return jsonify({"message": "❌ Auto-login failed"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
