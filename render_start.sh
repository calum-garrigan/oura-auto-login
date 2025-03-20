#!/bin/bash
# ✅ Ensure Playwright browsers are fully installed
npx playwright install --with-deps chromium

# ✅ Set the environment variable for Playwright's browser path
export PLAYWRIGHT_BROWSERS_PATH="/opt/render/.cache/ms-playwright"

# ✅ Debug: Print installed Chromium versions
ls -R /opt/render/.cache/ms-playwright

# ✅ Start the Flask app
gunicorn --bind 0.0.0.0:10000 server:app
