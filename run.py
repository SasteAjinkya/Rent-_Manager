import webview
import threading
from view import app  # Import the Flask app from view.py

def start_flask():
    """Run the Flask app."""
    app.run(debug=False, port=5000, use_reloader=False)

if __name__ == '__main__':
    # Start Flask in a separate thread
    threading.Thread(target=start_flask, daemon=True).start()

    # Set the window size and adjust the zoom level for WebView
    webview.create_window(
        title='Rent management system',
        url='http://127.0.0.1:5000',
        width=1000,  # Wider window for full content visibility
        height=600,  # Taller window for result container visibility
        resizable=True,  # Allow resizing
        zoomable=True  # Enable zoom controls (optional for user adjustability)
    )
    webview.start(debug=True)  # Enable debugging for additional inspection
