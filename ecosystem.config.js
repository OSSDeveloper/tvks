module.exports = {
    apps : [{
      name      : 'tvks',
      script    : '/opt/apps/tvks/.venv/bin/uvicorn', // assuming Unicorn is installed in a virtual environment
      args: ["main:app", "--host", "0.0.0.0", "--port", "8000"],
      env: {
        // NODE_ENV: "production"
      }
    }],
    exec_mode: 'fork',
    instances: 1
  }