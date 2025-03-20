#!/bin/bash
# ✅ Install Chromium in a specific directory
playwright install --with-deps chromium

# ✅ Ensure the Chromium path is set correctly
export PLAYWRIGHT_BROWSERS_PATH=/opt/render/.cache/ms-playwright

# ✅ Start the Flask app
gunicorn --bind 0.0.0.0:10000 server:app
