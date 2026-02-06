import logging
import pandas as pd

logging.basicConfig(
    filename = "test1.log",
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)
logging.debug("This is a debug message") # detailed internal state information
logging.info("This is an info message") # general information about program execution
logging.warning("This is a warning message") # something unexpected happened, but the program can continue
logging.error("This is an error message") # a more serious problem occurred, but the program can still continue
logging.critical("This is a critical message") # a very serious error occurred, and the program may not be able to continue

df = pd.read_csv("D:\\Agentic_Course\\testing\\data_out.csv")
logging.info("the code has begun")
for _, row in df.iterrows():
    if row["high_value"]:
        logging.warning(f"Customer {row['user_id']} is a high value customer")
    else : 
        logging.info(f"Customer {row['user_id']} is a low value customer")
logging.info("the code has ended")