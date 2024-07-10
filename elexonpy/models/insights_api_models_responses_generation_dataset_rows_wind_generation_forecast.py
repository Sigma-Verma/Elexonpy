# coding: utf-8

"""
    Insights.Api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InsightsApiModelsResponsesGenerationDatasetRowsWindGenerationForecast(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'dataset': 'str',
        'publish_time': 'datetime',
        'start_time': 'datetime',
        'generation': 'int'
    }

    attribute_map = {
        'dataset': 'dataset',
        'publish_time': 'publishTime',
        'start_time': 'startTime',
        'generation': 'generation'
    }

    def __init__(self, dataset=None, publish_time=None, start_time=None, generation=None):  # noqa: E501
        """InsightsApiModelsResponsesGenerationDatasetRowsWindGenerationForecast - a model defined in Swagger"""  # noqa: E501
        self._dataset = None
        self._publish_time = None
        self._start_time = None
        self._generation = None
        self.discriminator = None
        if dataset is not None:
            self.dataset = dataset
        if publish_time is not None:
            self.publish_time = publish_time
        if start_time is not None:
            self.start_time = start_time
        if generation is not None:
            self.generation = generation

    @property
    def dataset(self):
        """Gets the dataset of this InsightsApiModelsResponsesGenerationDatasetRowsWindGenerationForecast.  # noqa: E501


        :return: The dataset of this InsightsApiModelsResponsesGenerationDatasetRowsWindGenerationForecast.  # noqa: E501
        :rtype: str
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this InsightsApiModelsResponsesGenerationDatasetRowsWindGenerationForecast.


        :param dataset: The dataset of this InsightsApiModelsResponsesGenerationDatasetRowsWindGenerationForecast.  # noqa: E501
        :type: str
        """

        self._dataset = dataset

    @property
    def publish_time(self):
        """Gets the publish_time of this InsightsApiModelsResponsesGenerationDatasetRowsWindGenerationForecast.  # noqa: E501


        :return: The publish_time of this InsightsApiModelsResponsesGenerationDatasetRowsWindGenerationForecast.  # noqa: E501
        :rtype: datetime
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        """Sets the publish_time of this InsightsApiModelsResponsesGenerationDatasetRowsWindGenerationForecast.


        :param publish_time: The publish_time of this InsightsApiModelsResponsesGenerationDatasetRowsWindGenerationForecast.  # noqa: E501
        :type: datetime
        """

        self._publish_time = publish_time

    @property
    def start_time(self):
        """Gets the start_time of this InsightsApiModelsResponsesGenerationDatasetRowsWindGenerationForecast.  # noqa: E501


        :return: The start_time of this InsightsApiModelsResponsesGenerationDatasetRowsWindGenerationForecast.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this InsightsApiModelsResponsesGenerationDatasetRowsWindGenerationForecast.


        :param start_time: The start_time of this InsightsApiModelsResponsesGenerationDatasetRowsWindGenerationForecast.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def generation(self):
        """Gets the generation of this InsightsApiModelsResponsesGenerationDatasetRowsWindGenerationForecast.  # noqa: E501


        :return: The generation of this InsightsApiModelsResponsesGenerationDatasetRowsWindGenerationForecast.  # noqa: E501
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this InsightsApiModelsResponsesGenerationDatasetRowsWindGenerationForecast.


        :param generation: The generation of this InsightsApiModelsResponsesGenerationDatasetRowsWindGenerationForecast.  # noqa: E501
        :type: int
        """

        self._generation = generation

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InsightsApiModelsResponsesGenerationDatasetRowsWindGenerationForecast, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InsightsApiModelsResponsesGenerationDatasetRowsWindGenerationForecast):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other