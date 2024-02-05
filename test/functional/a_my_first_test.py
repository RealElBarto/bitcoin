from collections import defaultdict
from test_framework.test_framework import BitcoinTestFramework
from test_framework.util import (
    assert_equal,
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
        assert_equal (self.nodes[0].get_deterministic_priv_key().key, 'cVpF924EspNh8KjYsfhgY96mmxvT6DgdWiTYMtMjuM74hJaU5psW')
        assert_equal (self.nodes[0].getblockcount(), self.nodes[0].getblockchaininfo()["blocks"])
        print(self.nodes[0].getblockchaininfo())
        
if __name__ == '__main__':
    ExampleTest().main()
