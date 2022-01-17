from datetime import datetime
from brownie import Contract, FeeDistributor, FeeClaimHelper
from brownie.network import accounts

abi = [
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "account",
        "type": "address"
      }
    ],
    "name": "balanceOf",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
]

def test_claim(accounts, chain):
    admin = accounts.at('0x42E61987A5CbA002880b3cc5c800952a5804a1C5', force=True)

    user = accounts.at('0x47a252b0844efec0489babbcabd0f0c60ef9895e', force=True)

    wsSQUID = Contract.from_abi("wsSQUID", "0x3b1388eB39c72D2145f092C01067C02Bb627d4BE", abi)

    weth_fee_distributor = "0x008EB46CdC6651eeE592eE23fe4b121dAEBfbb18"
    wssquid_fee_distributor = "0xF3bC8fabcFC368B52ec18016d6cA8ab8967c550A"

    wssquid = FeeDistributor.at(wssquid_fee_distributor)
    claimable = wssquid.claim.call(user)

    balance_before = wsSQUID.balanceOf(user)

    print("claimable before:", claimable)
    print("         wsSQUID:", balance_before)

    helper = FeeClaimHelper.deploy({ "from": admin })

    helper.claim([weth_fee_distributor, wssquid_fee_distributor], user, { "from": user })

    claimable_after = wssquid.claim.call(user)
    balance_after =  wsSQUID.balanceOf(user)

    print(" claimable after:", claimable_after)
    print("         wsSQUID:", balance_after)

    assert balance_before + claimable == balance_after
    assert claimable_after == 0
