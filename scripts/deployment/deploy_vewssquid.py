from datetime import datetime
from brownie import FeeDistributor, VotingEscrow, VewsSQUIDHelper
from brownie.network import accounts

BROWNIE_ACCOUNT_ID = 'squid_deployer'
MULTISIG_ADDRESS = '0x42E61987A5CbA002880b3cc5c800952a5804a1C5'
S_SQUID_ADDRESS = '0x9d49BfC921F36448234b0eFa67B5f91b3C691515'
WS_SQUID_ADDRESS = '0x3b1388eB39c72D2145f092C01067C02Bb627d4BE'

def main():
    deployer = accounts.load(BROWNIE_ACCOUNT_ID)

    vews_squid = VotingEscrow.deploy(WS_SQUID_ADDRESS, 'Vote-escrowed wsSQUID', 'vewsSQUID', 'vewsSQUID_1.0.0', {'from': deployer})
    fee_distributor = FeeDistributor.deploy(vews_squid, int(datetime.now().timestamp()), WS_SQUID_ADDRESS, deployer, MULTISIG_ADDRESS, {'from': deployer})
    helper = VewsSQUIDHelper.deploy(S_SQUID_ADDRESS, WS_SQUID_ADDRESS, vews_squid, {'from': deployer}, publish_source=True)

    print('vewsSQUID:', vews_squid.address)
    print('FeeDistributor:', fee_distributor.address)
    print('helper:', helper.address)

    vews_squid.set_helper(helper, {'from': deployer})
