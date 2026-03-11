import subprocess
import threading
import time

def run_streamlit():
    """Starts the streamlit app in a subprocess."""
    # We need to run streamlit in a separate thread, so it doesn't block
    # the function from returning a response.
    subprocess.run(["streamlit", "run", "app.py", "--server.port", "8501"])

def handler(event, context):
    """Netlify function handler."""
    # Start streamlit in a background thread
    thread = threading.Thread(target=run_streamlit)
    thread.start()

    # Give streamlit a moment to start up
    time.sleep(5)

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": f'"""<iframe src="http://localhost:8501" style="width: 100%; height: 100vh; border: none;"></iframe>"""',
    }
