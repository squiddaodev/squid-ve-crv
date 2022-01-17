from brownie import FeeClaimHelper
from brownie.network import accounts

BROWNIE_ACCOUNT_ID = 'squid_deployer'

def main():
    deployer = accounts.load(BROWNIE_ACCOUNT_ID)
    helper = FeeClaimHelper.deploy({ "from": deployer, "nonce": 432 })
