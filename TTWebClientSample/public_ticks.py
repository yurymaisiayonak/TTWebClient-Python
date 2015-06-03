#!/usr/bin/python3
__author__ = 'ivan.shynkarenka'


import argparse
from TTWebClient.TickTraderWebClient import TickTraderWebClient


def main():
    parser = argparse.ArgumentParser(description='TickTrader Web API sample')
    parser.add_argument('web_api_address', help='TickTrader Web API address')
    args = parser.parse_args()

    # Create instance of the TickTrader Web API client
    client = TickTraderWebClient(args.web_api_address)

    # Public feed ticks
    ticks = client.get_public_all_ticks()
    for t in ticks:
        print('{0} tick: {1} {2}'.format(t['Symbol'], t['BestBid']['Price'], t['BestAsk']['Price']))

    tick = client.get_public_tick(ticks[0]['Symbol'])
    print("{0} tick timestamp: {1}".format(tick['Symbol'], tick['Timestamp']))


if __name__ == '__main__':
    main()