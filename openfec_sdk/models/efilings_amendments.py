# coding: utf-8

"""
    OpenFEC

    This API allows you to explore the way candidates and committees fund their campaigns.    The FEC API is a RESTful web service supporting full-text and field-specific searches on FEC data. [Bulk downloads](https://www.fec.gov/data/advanced/?tab=bulk-data) are available on the current site. Information is tied to the underlying forms by file ID and image ID. Data is updated nightly.    There is a lot of data, but a good place to start is to use search to find interesting candidates and committees. Then, you can use their IDs to find report or line item details with the other endpoints. If you are interested in individual donors, check out contributor information in schedule_a.    Get an [API key here](https://api.data.gov/signup/). That will enable you to place up to 1,000 calls an hour. Each call is limited to 100 results per page. You can email questions, comments or a request to get a key for 120 calls per minute to [APIinfo@fec.gov](mailto:apiinfo@fec.gov). You can also ask questions and discuss the data in the [FEC data Google Group](https://groups.google.com/forum/#!forum/fec-data). API changes will also be added to this group in advance of the change.    The model definitions and schema are available at [/swagger](/swagger/). This is useful for making wrappers and exploring the data.    A few restrictions limit the way you can use FEC data. For example, you can’t use contributor lists for commercial purposes or to solicit donations. [Learn more here](https://www.fec.gov/updates/sale-or-use-contributor-information/).    [View our source code](https://github.com/fecgov/openFEC). We welcome issues and pull requests!  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openfec_sdk.configuration import Configuration


class EfilingsAmendments(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'amendment_chain': 'list[float]',
        'depth': 'float',
        'file_number': 'int',
        'last': 'float',
        'longest_chain': 'list[float]',
        'most_recent_filing': 'float',
        'previous_file_number': 'float'
    }

    attribute_map = {
        'amendment_chain': 'amendment_chain',
        'depth': 'depth',
        'file_number': 'file_number',
        'last': 'last',
        'longest_chain': 'longest_chain',
        'most_recent_filing': 'most_recent_filing',
        'previous_file_number': 'previous_file_number'
    }

    def __init__(self, amendment_chain=None, depth=None, file_number=None, last=None, longest_chain=None, most_recent_filing=None, previous_file_number=None, local_vars_configuration=None):  # noqa: E501
        """EfilingsAmendments - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._amendment_chain = None
        self._depth = None
        self._file_number = None
        self._last = None
        self._longest_chain = None
        self._most_recent_filing = None
        self._previous_file_number = None
        self.discriminator = None

        self.amendment_chain = amendment_chain
        self.depth = depth
        if file_number is not None:
            self.file_number = file_number
        self.last = last
        self.longest_chain = longest_chain
        self.most_recent_filing = most_recent_filing
        self.previous_file_number = previous_file_number

    @property
    def amendment_chain(self):
        """Gets the amendment_chain of this EfilingsAmendments.  # noqa: E501


        :return: The amendment_chain of this EfilingsAmendments.  # noqa: E501
        :rtype: list[float]
        """
        return self._amendment_chain

    @amendment_chain.setter
    def amendment_chain(self, amendment_chain):
        """Sets the amendment_chain of this EfilingsAmendments.


        :param amendment_chain: The amendment_chain of this EfilingsAmendments.  # noqa: E501
        :type: list[float]
        """

        self._amendment_chain = amendment_chain

    @property
    def depth(self):
        """Gets the depth of this EfilingsAmendments.  # noqa: E501


        :return: The depth of this EfilingsAmendments.  # noqa: E501
        :rtype: float
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """Sets the depth of this EfilingsAmendments.


        :param depth: The depth of this EfilingsAmendments.  # noqa: E501
        :type: float
        """

        self._depth = depth

    @property
    def file_number(self):
        """Gets the file_number of this EfilingsAmendments.  # noqa: E501

        Filing ID number  # noqa: E501

        :return: The file_number of this EfilingsAmendments.  # noqa: E501
        :rtype: int
        """
        return self._file_number

    @file_number.setter
    def file_number(self, file_number):
        """Sets the file_number of this EfilingsAmendments.

        Filing ID number  # noqa: E501

        :param file_number: The file_number of this EfilingsAmendments.  # noqa: E501
        :type: int
        """

        self._file_number = file_number

    @property
    def last(self):
        """Gets the last of this EfilingsAmendments.  # noqa: E501


        :return: The last of this EfilingsAmendments.  # noqa: E501
        :rtype: float
        """
        return self._last

    @last.setter
    def last(self, last):
        """Sets the last of this EfilingsAmendments.


        :param last: The last of this EfilingsAmendments.  # noqa: E501
        :type: float
        """

        self._last = last

    @property
    def longest_chain(self):
        """Gets the longest_chain of this EfilingsAmendments.  # noqa: E501


        :return: The longest_chain of this EfilingsAmendments.  # noqa: E501
        :rtype: list[float]
        """
        return self._longest_chain

    @longest_chain.setter
    def longest_chain(self, longest_chain):
        """Sets the longest_chain of this EfilingsAmendments.


        :param longest_chain: The longest_chain of this EfilingsAmendments.  # noqa: E501
        :type: list[float]
        """

        self._longest_chain = longest_chain

    @property
    def most_recent_filing(self):
        """Gets the most_recent_filing of this EfilingsAmendments.  # noqa: E501


        :return: The most_recent_filing of this EfilingsAmendments.  # noqa: E501
        :rtype: float
        """
        return self._most_recent_filing

    @most_recent_filing.setter
    def most_recent_filing(self, most_recent_filing):
        """Sets the most_recent_filing of this EfilingsAmendments.


        :param most_recent_filing: The most_recent_filing of this EfilingsAmendments.  # noqa: E501
        :type: float
        """

        self._most_recent_filing = most_recent_filing

    @property
    def previous_file_number(self):
        """Gets the previous_file_number of this EfilingsAmendments.  # noqa: E501


        :return: The previous_file_number of this EfilingsAmendments.  # noqa: E501
        :rtype: float
        """
        return self._previous_file_number

    @previous_file_number.setter
    def previous_file_number(self, previous_file_number):
        """Sets the previous_file_number of this EfilingsAmendments.


        :param previous_file_number: The previous_file_number of this EfilingsAmendments.  # noqa: E501
        :type: float
        """

        self._previous_file_number = previous_file_number

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, 'to_dict') else x,
                    value
                ))
            elif hasattr(value, 'to_dict'):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], 'to_dict') else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EfilingsAmendments):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EfilingsAmendments):
            return True

        return self.to_dict() != other.to_dict()
