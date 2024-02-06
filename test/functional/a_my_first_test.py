from collections import defaultdict
from test_framework.test_framework import BitcoinTestFramework
from test_framework.util import (
    assert_equal,
)

from test_framework.wallet import (
    MiniWallet,
    MiniWalletMode,
)

class ExampleTest(BitcoinTestFramework):
    def add_options(self, parser):
        self.add_wallet_options(parser)

    def set_test_params(self):
        self.setup_clean_chain = False
        self.num_nodes = 3
        self.extra_args = [[], ["-logips"], []]
    
    def skip_test_if_missing_module(self):
        self.skip_if_no_wallet()

    #def custom_method(self):
    #    """Do some custom behaviour for this test

    #    Define it in a method here because you're going to use it repeatedly.
    #    If you think it's useful in general, consider moving it to the base
    #    BitcoinTestFramework class so other tests can use it."""

    #    self.log.info("Running custom_method")

    def run_test(self):
        """Main test logic"""
              
        assert_equal (self.nodes[0].get_deterministic_priv_key().address, 'mjTkW3DjgyZck4KbiRusZsqTgaYTxdSz6z')
        
        # Node RPC
        print(self.nodes[0].getblockchaininfo())

        # Wallet RPCS
        print(MiniWallet(self.nodes[0]).get_balance())


if __name__ == '__main__':
    ExampleTest().main()
