from app.create_app import create_app

app = create_app()

if __name__ == "__main__":
    app.secret_key = "7143e934ad2e62ce3eaa66b30f554504"
    app.run(debug=True)