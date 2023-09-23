from app.create_app import create_app
import os

# Create an instance of the Flask application using the create_app function
app = create_app()

if __name__ == "__main__":
    # Set the secret key for the Flask application
    app.secret_key = os.environ.get("SECRET_KEY")
    
    # Run the Flask application in debug mode
    app.run(debug=True)
