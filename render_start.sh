#!/bin/bash
playwright install --with-deps chromium
gunicorn --bind 0.0.0.0:10000 server:app
