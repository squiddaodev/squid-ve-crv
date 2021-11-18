from brownie import Contract, FeeDistributor, VotingEscrow, VewsSQUIDHelper
from brownie.network import accounts

DAY = 86400
WEEK = 7 * DAY

def test_create_lock(accounts, chain):
    admin = accounts.at('0x42E61987A5CbA002880b3cc5c800952a5804a1C5', force=True)
    user = accounts.at('0x4f618A165031233f1384f4d3413B7b93c76E8907', force=True)

    s_squid = Contract.from_explorer("0x9d49BfC921F36448234b0eFa67B5f91b3C691515")
    ws_squid = Contract.from_explorer("0x3b1388eB39c72D2145f092C01067C02Bb627d4BE")

    vews_squid = VotingEscrow.deploy(ws_squid, 'Vote-escrowed wsSQUID', 'vewsSQUID', 'vewsSQUID_1.0.0', {'from': admin})
    fee_distributor = FeeDistributor.deploy(vews_squid, 1637280000, ws_squid, admin, admin, {'from': admin})
    helper = VewsSQUIDHelper.deploy(s_squid, ws_squid, vews_squid, {'from': admin})

    vews_squid.set_helper(helper, {'from': admin})

    # Move to timing which is good for testing - beginning of a UTC week
    chain.sleep((chain[-1].timestamp // WEEK + 1) * WEEK - chain[-1].timestamp)
    chain.mine()

    amount = s_squid.balanceOf(user)
    s_squid.approve(helper, amount, {'from': user})
    helper.createLock(amount, chain[-1].timestamp + 8 * WEEK, {'from': user})

    assert s_squid.balanceOf(user) == 0
    assert vews_squid.balanceOf(user) > 0

    chain.sleep(8 * WEEK + 1)
    chain.mine()

    helper.withdraw({'from': user})
    assert s_squid.balanceOf(user) > 0

    # TODO: test fee claiming
