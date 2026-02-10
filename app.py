from flask import Flask
from routes.subject_routes import subject_bp

app = Flask(__name__)

app.register_blueprint(subject_bp)

if __name__ == "__main__":
    app.run(debug=True)
