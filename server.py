import os
import subprocess
from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

app = Flask(__name__)

# ✅ Manually Install Google Chrome & ChromeDriver on Render
def install_chrome():
    print("🚀 Installing Google Chrome & ChromeDriver on Render...")

    # Install Google Chrome
    subprocess.run("wget -q -O /tmp/chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb", shell=True)
    subprocess.run("apt update && apt install -y /tmp/chrome.deb", shell=True)

    # Install ChromeDriver
    subprocess.run("wget -q -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip", shell=True)
    subprocess.run("unzip /tmp/chromedriver.zip -d /usr/local/bin/", shell=True)
    subprocess.run("chmod +x /usr/local/bin/chromedriver", shell=True)

    print("✅ Chrome & ChromeDriver Installed!")

# ✅ Call the function before running Selenium
install_chrome()

@app.route("/")
def home():
    return "<h1>✅ Flask Server Running on Render!</h1>"

def login_to_oura(email, password):
    """ Automates Oura login using Selenium """
    
    print(f"🟢 Logging in: {email}")

    # ✅ Set Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Run in background
    chrome_options.add_argument("--no-sandbox")  
    chrome_options.add_argument("--disable-dev-shm-usage")  
    chrome_options.binary_location = "/usr/bin/google-chrome"

    # ✅ Manually set ChromeDriver path
    driver = webdriver.Chrome(service=Service("/usr/local/bin/chromedriver"), options=chrome_options)

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
