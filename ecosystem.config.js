module.exports = {
    apps : [{
      name      : 'tvks',
      script    : 'uvicorn', // assuming Unicorn is installed in a virtual environment
      args: "main:app --host 0.0.0.0 --port 8000",
      env: {
        // NODE_ENV: "production"
      },
      instances: 1
    }]
  }