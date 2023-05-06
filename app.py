# Import Flask
from flask import Flask, render_template
import os
import socket

# Create a Flask app
app = Flask(__name__)

# Register a route
@app.route("/")
def index():
    return render_template('index.html')

# Run the app
if __name__ == "__main__":

    # Start the Flask app
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
