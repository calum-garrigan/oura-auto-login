from flask import Flask, request, jsonify, render_template_string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

app = Flask(__name__)

# ✅ Oura Login Page
OURA_LOGIN_URL = "https://cloud.ouraring.com/user/sign-in"

def login_to_oura(email, password):
    """Uses Selenium to log into Oura automatically."""
    
    options = Options()
    options.add_argument("--headless")  # Run in headless mode (no GUI)
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280x1024")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get(OURA_LOGIN_URL)
        print(f"🔑 Navigated to {OURA_LOGIN_URL}")

        # ✅ Enter Email
        email_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='email']")))
        email_field.clear()
        email_field.send_keys(email)

        # ✅ Enter Password
        password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='password']")))
        password_field.clear()
        password_field.send_keys(password)

        # ✅ Click Sign-In
        sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Sign In"]')))
        driver.execute_script("arguments[0].click();", sign_in_button)
        
        time.sleep(5)  # Wait for login process
        
        print(f"✅ Successfully logged into Oura for {email}")

        return True  # Login successful
    
    except Exception as e:
        print(f"❌ Login Failed: {e}")
        return False

    finally:
        driver.quit()

@app.route('/')
def home():
    return "🎯 Flask Server Running on Render!"

@app.route('/auto-login', methods=['GET'])
def auto_login():
    email = request.args.get("email")
    password = request.args.get("password")

    if not email or not password:
        return jsonify({"error": "Missing login credentials"}), 400

    print(f"🟢 Logging in: {email}")
    success = login_to_oura(email, password)

    if success:
        return jsonify({"message": "✅ Logged into Oura successfully!"})
    else:
        return jsonify({"error": "❌ Login failed"}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000, debug=True)
