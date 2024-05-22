module.exports = {
    apps : [{
      name      : 'tvks',
      script    : './venv/bin/uvicorn', // assuming Unicorn is installed in a virtual environment
      args: ['main:app', '--workers', '1'],
      env: {
        "FAST_API_HOST": "0.0.0.0",
        "FAST_API_PORT": "8000"
      }
    }]
  }