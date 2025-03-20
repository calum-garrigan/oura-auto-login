import os
import asyncio
import threading
from flask import Flask, request, jsonify
from playwright.async_api import async_playwright

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>✅ Flask Server Running on Render!</h1>"

def run_async_task(coroutine):
    """ Run an async function in a separate thread """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(coroutine)

async def login_to_oura(email, password):
    """ Automates Oura login using Playwright """

    print(f"🟢 Logging in: {email}")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)  # ✅ Let Playwright find Chromium
        page = await browser.new_page()

        try:
            print("🌍 Navigating to Oura login page...")
            await page.goto("https://cloud.ouraring.com/user/sign-in", timeout=60000)

            # ✅ Fill email
            await page.fill("input[name='email']", email)

            # ✅ Fill password
            await page.fill("input[name='password']", password)

            # ✅ Click login button
            await page.press("input[name='password']", "Enter")

            await page.wait_for_load_state("networkidle")
            print(f"✅ Successfully logged in: {email}")

            await browser.close()
            return True

        except Exception as e:
            print(f"❌ Playwright Error: {e}")
            await browser.close()
            return False

@app.route("/auto-login", methods=["GET"])
def auto_login():
    """ API Endpoint to trigger Playwright login """

    email = request.args.get("email")
    password = request.args.get("password")

    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400

    # ✅ Run Playwright inside a separate thread
    success = run_async_task(login_to_oura(email, password))

    if success:
        return jsonify({"message": "✅ Auto-login successful!"})
    else:
        return jsonify({"message": "❌ Auto-login failed"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
