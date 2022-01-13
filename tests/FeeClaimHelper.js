const { expect } = require("chai");
const { ethers, waffle } = require("hardhat");
const fs = require("fs");
const { impersonateAccount } = require("../testUtils.js");

describe("Oracle Test", () => {
  let accounts;
  let admin, adminAddress;
  let whaleAddress = "0x4c180462a051ab67d8237ede2c987590df2fbbe6";
  let whale;

  let wsSquid = "0x3b1388eB39c72D2145f092C01067C02Bb627d4BE";
  let weth = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2";
  let claimHelper;
  let uint256Max =
    "115792089237316195423570985008687907853269984665640564039457584007913129639935";

  beforeEach(async () => {
    whale = await impersonateAccount(whaleAddress);
    accounts = await ethers.getSigners();
    admin = accounts[0];
    adminAddress = await admin.getAddress();
    claimContractFactory = await ethers.getContractFactory("FeeClaimHelper");
    claimHelper = await claimContractFactory.deploy();
  });
  it("claim", async () => {
    erc20Factory = await ethers.getContractFactory("ERC20Token");
    wethContract = erc20Factory.attach(weth);
    wsSquidContract = erc20Factory.attach(wsSquid);
    vewsSquid = "0x58807E624b9953C2279E0eFae5EDcf9C7DA08c7B";
    await wethContract
      .connect(whale)
      .approve(claimHelper.address, uint256Max, { gasLimit: 1000000 });
    await wsSquidContract
      .connect(whale)
      .approve(vewsSquid, uint256Max, { gasLimit: 1000000 });
    await claimHelper.connect(whale).claimAndLockWsSquid({ gasLimit: 1000000 });
  });
  it("claim2", async () => {
    erc20Factory = await ethers.getContractFactory("ERC20Token");
    wethContract = erc20Factory.attach(weth);
    wsSquidContract = erc20Factory.attach(wsSquid);
    vewsSquid = "0x58807E624b9953C2279E0eFae5EDcf9C7DA08c7B";
    await wethContract
      .connect(whale)
      .approve(claimHelper.address, uint256Max, { gasLimit: 1000000 });
    await wsSquidContract
      .connect(whale)
      .approve(vewsSquid, uint256Max, { gasLimit: 1000000 });
    await claimHelper
      .connect(whale)
      .claimWethAndswapForvewsSquid({ gasLimit: 2000000 });
  });
});
