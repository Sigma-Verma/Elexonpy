# coding: utf-8

"""
    Insights.Api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import elexonpy
from elexonpy.api.market_index_api import MarketIndexApi  # noqa: E501
from elexonpy.rest import ApiException


class TestMarketIndexApi(unittest.TestCase):
    """MarketIndexApi unit test stubs"""

    def setUp(self):
        self.api = MarketIndexApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_balancing_pricing_market_index_get(self):
        """Test case for balancing_pricing_market_index_get

        Market Index Data (MID) price time series  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()