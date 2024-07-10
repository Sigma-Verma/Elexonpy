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
from elexonpy.api.generation_forecast_api import GenerationForecastApi  # noqa: E501
from elexonpy.rest import ApiException


class TestGenerationForecastApi(unittest.TestCase):
    """GenerationForecastApi unit test stubs"""

    def setUp(self):
        self.api = GenerationForecastApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_forecast_availability_daily_evolution_get(self):
        """Test case for forecast_availability_daily_evolution_get

        Evolution of the fourteen-day generation capacity forecast over time (FOU2T14D)  # noqa: E501
        """
        pass

    def test_forecast_availability_daily_get(self):
        """Test case for forecast_availability_daily_get

        Fourteen-day generation capacity forecast (FOU2T14D)  # noqa: E501
        """
        pass

    def test_forecast_availability_daily_history_get(self):
        """Test case for forecast_availability_daily_history_get

        History of the fourteen-day generation capacity forecast (FOU2T14D)  # noqa: E501
        """
        pass

    def test_forecast_availability_summary14_d_get(self):
        """Test case for forecast_availability_summary14_d_get

        Down-sampled fourteen-day generation forecast (FOU2T14D)  # noqa: E501
        """
        pass

    def test_forecast_availability_summary3_yw_get(self):
        """Test case for forecast_availability_summary3_yw_get

        Down-sampled three-year generation forecast (FOU2T3YW)  # noqa: E501
        """
        pass

    def test_forecast_availability_weekly_evolution_get(self):
        """Test case for forecast_availability_weekly_evolution_get

        Evolution of the three-year generation capacity forecast over time (FOU2T3YW)  # noqa: E501
        """
        pass

    def test_forecast_availability_weekly_get(self):
        """Test case for forecast_availability_weekly_get

        Three-year generation capacity forecast (FOU2T3YW)  # noqa: E501
        """
        pass

    def test_forecast_availability_weekly_history_get(self):
        """Test case for forecast_availability_weekly_history_get

        History of the three-year generation capacity forecast (FOU2T3YW)  # noqa: E501
        """
        pass

    def test_forecast_generation_day_ahead_get(self):
        """Test case for forecast_generation_day_ahead_get

        Day-ahead aggregated generation (DAG/B1430)  # noqa: E501
        """
        pass

    def test_forecast_generation_wind_and_solar_day_ahead_get(self):
        """Test case for forecast_generation_wind_and_solar_day_ahead_get

        Day-ahead generation forecast for wind and solar (DGWS/B1440)  # noqa: E501
        """
        pass

    def test_forecast_generation_wind_earliest_get(self):
        """Test case for forecast_generation_wind_earliest_get

        Historic view of the earliest forecasted wind generation (WINDFOR)  # noqa: E501
        """
        pass

    def test_forecast_generation_wind_earliest_stream_get(self):
        """Test case for forecast_generation_wind_earliest_stream_get

        Historic view of the earliest forecasted wind generation (WINDFOR) stream  # noqa: E501
        """
        pass

    def test_forecast_generation_wind_evolution_get(self):
        """Test case for forecast_generation_wind_evolution_get

        Evolution of the wind generation forecast over time (WINDFOR)  # noqa: E501
        """
        pass

    def test_forecast_generation_wind_get(self):
        """Test case for forecast_generation_wind_get

        Current wind generation forecast (WINDFOR)  # noqa: E501
        """
        pass

    def test_forecast_generation_wind_history_get(self):
        """Test case for forecast_generation_wind_history_get

        History of the wind generation forecast (WINDFOR)  # noqa: E501
        """
        pass

    def test_forecast_generation_wind_latest_get(self):
        """Test case for forecast_generation_wind_latest_get

        Historic view of the latest forecasted wind generation (WINDFOR)  # noqa: E501
        """
        pass

    def test_forecast_generation_wind_latest_stream_get(self):
        """Test case for forecast_generation_wind_latest_stream_get

        Historic view of the latest forecasted wind generation (WINDFOR) stream  # noqa: E501
        """
        pass

    def test_forecast_generation_wind_peak_get(self):
        """Test case for forecast_generation_wind_peak_get

        Peak wind generation forecast for each day (WINDFOR)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()