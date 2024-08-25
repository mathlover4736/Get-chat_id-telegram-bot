import os , sys
import logging 
import asyncio 
SCRIPT_DIR = str(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(-1,(SCRIPT_DIR))

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Get a logger instance specific to your application
logger = logging.getLogger(__name__)




from Classes.CliClass import Get_Chat 

if __name__ == "__main__":
    Get_Chat().run()