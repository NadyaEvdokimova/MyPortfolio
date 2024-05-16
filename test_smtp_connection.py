import socket

def test_smtp_connection():
    try:
        smtp_server = "smtp.gmail.com"
        port = 587
        socket.create_connection((smtp_server, port), timeout=10)
        print("Connection to SMTP server successful")
    except Exception as e:
        print(f"Failed to connect to SMTP server: {e}")

if __name__ == "__main__":
    test_smtp_connection()
