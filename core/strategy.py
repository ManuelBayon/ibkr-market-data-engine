import pandas as pd
from src.core.indicators import calculate_sma


def sma_crossover(df, short_window, long_window):
    # ------------      Initialisation        --------------------
    transactions = pd.DataFrame(columns=['symbol', 'action', 'quantity', 'price', 'timestamp', 'status'])

    # Calcul des moyennes mobiles simples 50 et 200
    df['short'] = calculate_sma(df, short_window)
    df['long'] = calculate_sma(df, long_window)

    # Paramètres de la stratégie
    position_size = 1

    # Variables pour la gestion de la position
    position_open = False
    position_type = None  # 'long' ou 'short'
    entry_price = None

    # Boucle de backtest
    for index, row in df.iterrows():
        current_time = row['date']
        current_price = row['close']

        # Signal d'achat : croisement haussier
        if not position_open and current_price > row['short']:
            position_open = True
            position_type = 'long'
            entry_price = current_price
            quantity = position_size

            new_transaction = pd.DataFrame([{
                'symbol': 'MNQ',  # Exemple de symbole
                'action': 'buy',
                'quantity': quantity,
                'price': entry_price,
                'timestamp': current_time,
                'status': 'open'
            }])
            if transactions.empty:
                transactions = new_transaction
            else:
                transactions = pd.concat([transactions, new_transaction], ignore_index=True)

        # Signal de vente : croisement baissier
        elif not position_open and current_price < row['short']:
            position_open = True
            position_type = 'short'
            entry_price = current_price
            quantity = position_size

            new_transaction = pd.DataFrame([{
                'symbol': 'MNQ',  # Exemple de symbole
                'action': 'sell',
                'quantity': quantity,
                'price': entry_price,
                'timestamp': current_time,
                'status': 'open'
            }])

            if transactions.empty:
                transactions = new_transaction
            else:
                transactions = pd.concat([transactions, new_transaction], ignore_index=True)

    return transactions
