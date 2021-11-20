from brownie import FundMe, MockV3Aggregator, network, config
from scripts.util import deploy_mocks, get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS


def deploy_fund_me():
    account = get_account()
    price_feed_address = 0
    # pass price feed address to fun me contact

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
        print(f"The active network is {network.show_active()} ")

    publish_source = config["networks"][network.show_active()]["verify"]
    fund_me = FundMe.deploy(
        price_feed_address, {"from": account}, publish_source=publish_source
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
