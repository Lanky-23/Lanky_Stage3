from fastapi import FastAPI, Request, HTTPException, Response
from tasks import send_email_task
import logging
import os
from datetime import datetime
from config import LOG_FILE

app = FastAPI()

# Configure logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO)

@app.get("/")
async def handle_request(sendmail: str = None, talktome: bool = False):
    if sendmail:
        send_email_task.delay(sendmail)
        return {"message": f"Email queued to be sent to {sendmail}"}
    
    if talktome:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f"Current time: {current_time}")
        return {"message": f"Current time logged at {current_time}"}
    
    return {"lanky's HNG_stage3 submission"}

@app.get("/logs")
async def get_logs():
    if not os.path.exists(LOG_FILE):
        raise HTTPException(status_code=404, detail="Log file not found")
    
    try:
        with open(LOG_FILE, "r") as file:
            logs = file.readlines()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading log file: {e}")
    
    # Convert log lines to HTML
    logs_html = "<html><body><pre style='font-family: monospace;'>"
    for line in logs:
        logs_html += f"{line}<br>"
    logs_html += "</pre></body></html>"
    
    return Response(content=logs_html, media_type="text/html")

if __name__ == '__main__':
    app.worker_main()

