module.exports = {
    apps : [{
      name      : 'tvks',
      script    : 'python', // assuming Unicorn is installed in a virtual environment
      args: "main.py",
      env: {
        NODE_ENV: "production",
        PORT: 8000
      }
    }]
  }