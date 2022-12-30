## Imports / Импорты
from binance_chain.wallet import Wallet
from binance_chain.environment import BinanceEnvironment

testnet_env = BinanceEnvironment.get_testnet_env()
wallet = Wallet('private_key_string', env=testnet_env)
print(wallet.address)
print(wallet.private_key)
print(wallet.public_key_hex)
