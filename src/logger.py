

import logging

# Configure logging to save into app.log
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Functions to log messages
def log_message(message):
    logging.info(message)   # Normal log message

def log_error(error):
    logging.error(error)    # Error message


# Example usage
if __name__ == "__main__":
    log_message("Application started")
    log_error("Something went wrong!")
