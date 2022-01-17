from datetime import datetime
from brownie import FeeDistributor, VotingEscrow, Contract
from brownie.network import accounts

BROWNIE_ACCOUNT_ID = 'squid_deployer'
MULTISIG_ADDRESS = '0x42E61987A5CbA002880b3cc5c800952a5804a1C5'
WETH_ADDRESS = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
VE_WS_SQUID_ADDRESS = '0x58807E624b9953C2279E0eFae5EDcf9C7DA08c7B'

def main():
    deployer = accounts.load(BROWNIE_ACCOUNT_ID)

    start_time = int(datetime.now().timestamp())
    fee_distributor = FeeDistributor.deploy(VE_WS_SQUID_ADDRESS, start_time, WETH_ADDRESS, deployer, MULTISIG_ADDRESS, {'from': deployer}, publish_source=True)

    print('FeeDistributor:', fee_distributor.address)
