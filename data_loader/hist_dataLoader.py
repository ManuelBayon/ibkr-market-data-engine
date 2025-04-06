from ib_insync import *
import pandas as pd


class hist_dataLoader:

    def __init__(self, twsConnection):
        self.ib = twsConnection.ib

    def _request_and_format(self, contract, **kwargs):
        data = self.ib.reqHistoricalData(contract, **kwargs)
        df = pd.DataFrame(data)
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'])
        elif 'Date' in df.columns:
            df['date'] = pd.to_datetime(df['Date'])
        return df

    def getContFuture(
        self,
        symbol,
        exchange,
        currency='USD',
        endDateTime='',
        durationStr= '30 D',
        barSizeSetting='1 day',
        whatToShow='MIDPOINT',
        useRTH=False,
        ) :

        contract = ContFuture(
            symbol=symbol,
            exchange=exchange,
            currency=currency
        )

        return self._request_and_format (
            contract,
            endDateTime= endDateTime,
            durationStr= durationStr,
            barSizeSetting= barSizeSetting,
            whatToShow= whatToShow,
            useRTH= useRTH,
        )

    def getFuture(
        self,
        symbol,
        localSymbol,
        exchange,
        currency='USD',
        endDateTime='',
        durationStr='30 D',
        barSizeSetting = '1 day',
        whatToShow='MIDPOINT',
        useRTH = False,
        ) :

        contract = Future(
            symbol=symbol,
            exchange=exchange,
            currency=currency,
            localSymbol=localSymbol
        )

        return self._request_and_format (
            contract,
            endDateTime= endDateTime,
            durationStr= durationStr,
            barSizeSetting= barSizeSetting,
            whatToShow= whatToShow,
            useRTH= useRTH,
        )

    def getStock(
        self,
        symbol,
        exchange,
        currency='USD',
        endDateTime='',
        durationStr='30 D',
        barSizeSetting = '1 day',
        whatToShow='MIDPOINT',
        useRTH = False,
        ):

        contract = Stock(
            symbol=symbol,
            exchange=exchange,
            currency=currency,
        )

        bars = self.ib.reqHistoricalData(
            contract,
            endDateTime=endDateTime,
            durationStr=durationStr,
            barSizeSetting=barSizeSetting,
            whatToShow=whatToShow,
            useRTH=useRTH
        )

        df = pd.DataFrame([{
            'Date': bar.date,
            'Open': bar.open,
            'High': bar.high,
            'Low': bar.low,
            'Close': bar.close,
            'Volume': bar.volume,
            'Average': bar.average,
            'BarCount': bar.barCount
        } for bar in bars])

        df['date'] = pd.to_datetime(df['Date'])

        return df

    def getOption(
        self,
        symbol,
        lastTradeDateOrContractMonth,
        strike,
        right,
        exchange='CBOE',
        multiplier='100',
        currency='USD',
        endDateTime='',
        durationStr='7 D',
        barSizeSetting = '1 hour',
        whatToShow='TRADES',
        useRTH = False,
        ) :

        contract = Option(
            symbol=symbol,
            lastTradeDateOrContractMonth=lastTradeDateOrContractMonth,
            strike=strike,
            right=right,
            exchange=exchange,
            multiplier=multiplier,
            currency=currency,
        )

        return self._request_and_format (
            contract,
            endDateTime= endDateTime,
            durationStr= durationStr,
            barSizeSetting= barSizeSetting,
            whatToShow= whatToShow,
            useRTH= useRTH,
        )

    def getForex(
        self,
        symbol,
        currency,
        endDateTime='',
        durationStr='30 D',
        barSizeSetting = '1 day',
        whatToShow='MIDPOINT',
        useRTH = False,
        ) :

        contract = Forex(
            symbol=symbol,
            currency=currency
        )

        return self._request_and_format (
            contract,
            endDateTime= endDateTime,
            durationStr= durationStr,
            barSizeSetting= barSizeSetting,
            whatToShow= whatToShow,
            useRTH= useRTH,
        )

