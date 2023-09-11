from app.create_app import create_app

# Create an instance of the Flask application using the create_app function
app = create_app()

if __name__ == "__main__":
    # Set the secret key for the Flask application
    # ! In a production environment, it's advisable to set the secret key as an environment variable
    # ! to keep it secure and not expose it in the source code.
    app.secret_key = "7143e934ad2e62ce3eaa66b30f554504"
    
    # Run the Flask application in debug mode
    app.run(debug=True)
