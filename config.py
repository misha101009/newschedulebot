import logging
import os

from dotenv import load_dotenv

load_dotenv()


logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(filename)s:%(lineno)d #%(levelname)-8s "
    "[%(asctime)s] - %(name)s - %(message)s",
)

TOKEN = os.getenv("TOKEN_BOT")
UID = int(os.getenv("U_ID"))
