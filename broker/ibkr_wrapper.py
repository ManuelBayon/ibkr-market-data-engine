from ib_insync import IB
import logging


class TWSConnection:

    def __init__(self):
        self.ib = IB()
        self.connected = False

    def connect(self, host='127.0.0.1', port=7497, client_id=1) -> IB:
        try:
            self.ib.connect(host, port, client_id)
            self.connected = True
            logging.info('Connection to TWS established')
            return self.ib

        except Exception as e:
            self.connected = False
            logging.error(f'Failed to connect to TWS {e}')
            raise

    def disconnect(self):
        try:
            if self.ib.isConnected():
                self.ib.disconnect()
                self.connected = False
                logging.info('Disconnected from TWS')
            else:
                logging.error('No active connection to disconnect.')

        except Exception as e:
            logging.error(f"Erreur lors de la déconnexion : {e}")
            raise

    def isConnected(self) -> bool:
        return self.ib.isConnected()