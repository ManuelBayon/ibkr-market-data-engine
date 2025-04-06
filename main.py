from numpy.ma.extras import column_stack

from src.broker.ibkr_wrapper import TWSConnection
from pathlib import Path
from src.config.settings import LOG_DIR
from src.data_loader.hist_dataLoader import hist_dataLoader
from utils.logger import get_logger

# Instantiation of a logger
logger = get_logger (
    name=Path(__file__).stem,
    log_path= LOG_DIR,
    debug=True )

def connect_to_ibkr():

    logger.info("Connecting to IBKR")
    ibkr = TWSConnection()
    try:
        connection = ibkr.connect(host="127.0.0.1",port=7497, client_id=2)
        logger.info("connection established")
        return ibkr, connection
    except Exception as e:
        logger.error(f"connection failed {e}")
        return None, None

def disconnect_from_ibkr(ibkr):
    try:
        ibkr.disconnect()
        logger.info(f"disconnected from IBKR")
    except Exception as e:
        logger.error(f"disconnection failed {e}")

def load_historical_data(ibkr):

    # Initialisation
    logger.info("loading data")
    loader = hist_dataLoader(ibkr)

    # Load historical data
    try:
        data = loader.getContFuture(symbol="MNQ", exchange="CME", barSizeSetting="1 day", durationStr="100 D")
        logger.info("data loaded")
        return data
    except Exception as e:
        logger.error(f"data loading failed : {e}")
        return None

def main():

    #Initialisation
    ibkr, connection = connect_to_ibkr()

    #Loading data
    if connection:
        data = load_historical_data(ibkr)

        #Saving data to excel file
        if not data.empty:
            try:
                # Save date, open, high, low, close columns
                data.drop(columns=["volume", "average", "barCount"]).to_excel("data_debug.xlsx", index=False)
                logger.info("data saved")
            except Exception as e:
                logger.error(f"data saving failed : {e}")

    # Disconnect from ibkr
    disconnect_from_ibkr(ibkr)

if __name__ == "__main__":
    main()
