#!/usr/bin/env bash

# Navigate to the tvks application directory
cd /opt/apps/tvks || exit 1

pwd
whoami
ls -lrt

# Activate the virtual environment (replace .venv with your actual path)
. .venv/bin/activate || exit 1

# Start the uvicorn application using pm2
pm2 start "uvicorn main:app --host 0.0.0.0 --port 8000 --reload" --name tvks -i 1

# Exit script on any error
exit $?
