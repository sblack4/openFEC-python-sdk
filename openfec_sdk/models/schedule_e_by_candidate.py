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


class ScheduleEByCandidate(object):
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
        'candidate_id': 'str',
        'candidate_name': 'str',
        'committee_id': 'str',
        'committee_name': 'str',
        'count': 'int',
        'cycle': 'int',
        'support_oppose_indicator': 'str',
        'total': 'float'
    }

    attribute_map = {
        'candidate_id': 'candidate_id',
        'candidate_name': 'candidate_name',
        'committee_id': 'committee_id',
        'committee_name': 'committee_name',
        'count': 'count',
        'cycle': 'cycle',
        'support_oppose_indicator': 'support_oppose_indicator',
        'total': 'total'
    }

    def __init__(self, candidate_id=None, candidate_name=None, committee_id=None, committee_name=None, count=None, cycle=None, support_oppose_indicator=None, total=None, local_vars_configuration=None):  # noqa: E501
        """ScheduleEByCandidate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._candidate_id = None
        self._candidate_name = None
        self._committee_id = None
        self._committee_name = None
        self._count = None
        self._cycle = None
        self._support_oppose_indicator = None
        self._total = None
        self.discriminator = None

        if candidate_id is not None:
            self.candidate_id = candidate_id
        if candidate_name is not None:
            self.candidate_name = candidate_name
        if committee_id is not None:
            self.committee_id = committee_id
        if committee_name is not None:
            self.committee_name = committee_name
        self.count = count
        self.cycle = cycle
        self.support_oppose_indicator = support_oppose_indicator
        self.total = total

    @property
    def candidate_id(self):
        """Gets the candidate_id of this ScheduleEByCandidate.  # noqa: E501


        :return: The candidate_id of this ScheduleEByCandidate.  # noqa: E501
        :rtype: str
        """
        return self._candidate_id

    @candidate_id.setter
    def candidate_id(self, candidate_id):
        """Sets the candidate_id of this ScheduleEByCandidate.


        :param candidate_id: The candidate_id of this ScheduleEByCandidate.  # noqa: E501
        :type: str
        """

        self._candidate_id = candidate_id

    @property
    def candidate_name(self):
        """Gets the candidate_name of this ScheduleEByCandidate.  # noqa: E501


        :return: The candidate_name of this ScheduleEByCandidate.  # noqa: E501
        :rtype: str
        """
        return self._candidate_name

    @candidate_name.setter
    def candidate_name(self, candidate_name):
        """Sets the candidate_name of this ScheduleEByCandidate.


        :param candidate_name: The candidate_name of this ScheduleEByCandidate.  # noqa: E501
        :type: str
        """

        self._candidate_name = candidate_name

    @property
    def committee_id(self):
        """Gets the committee_id of this ScheduleEByCandidate.  # noqa: E501


        :return: The committee_id of this ScheduleEByCandidate.  # noqa: E501
        :rtype: str
        """
        return self._committee_id

    @committee_id.setter
    def committee_id(self, committee_id):
        """Sets the committee_id of this ScheduleEByCandidate.


        :param committee_id: The committee_id of this ScheduleEByCandidate.  # noqa: E501
        :type: str
        """

        self._committee_id = committee_id

    @property
    def committee_name(self):
        """Gets the committee_name of this ScheduleEByCandidate.  # noqa: E501


        :return: The committee_name of this ScheduleEByCandidate.  # noqa: E501
        :rtype: str
        """
        return self._committee_name

    @committee_name.setter
    def committee_name(self, committee_name):
        """Sets the committee_name of this ScheduleEByCandidate.


        :param committee_name: The committee_name of this ScheduleEByCandidate.  # noqa: E501
        :type: str
        """

        self._committee_name = committee_name

    @property
    def count(self):
        """Gets the count of this ScheduleEByCandidate.  # noqa: E501

         Number of records making up the total.   # noqa: E501

        :return: The count of this ScheduleEByCandidate.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ScheduleEByCandidate.

         Number of records making up the total.   # noqa: E501

        :param count: The count of this ScheduleEByCandidate.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def cycle(self):
        """Gets the cycle of this ScheduleEByCandidate.  # noqa: E501

         Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.   # noqa: E501

        :return: The cycle of this ScheduleEByCandidate.  # noqa: E501
        :rtype: int
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        """Sets the cycle of this ScheduleEByCandidate.

         Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.   # noqa: E501

        :param cycle: The cycle of this ScheduleEByCandidate.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and cycle is None:  # noqa: E501
            raise ValueError('Invalid value for `cycle`, must not be `None`')  # noqa: E501

        self._cycle = cycle

    @property
    def support_oppose_indicator(self):
        """Gets the support_oppose_indicator of this ScheduleEByCandidate.  # noqa: E501

        Explains if the money was spent in order to support or oppose a candidate or candidates. (Coded S or O for support or oppose.) This indicator applies to independent expenditures and communication costs.  # noqa: E501

        :return: The support_oppose_indicator of this ScheduleEByCandidate.  # noqa: E501
        :rtype: str
        """
        return self._support_oppose_indicator

    @support_oppose_indicator.setter
    def support_oppose_indicator(self, support_oppose_indicator):
        """Sets the support_oppose_indicator of this ScheduleEByCandidate.

        Explains if the money was spent in order to support or oppose a candidate or candidates. (Coded S or O for support or oppose.) This indicator applies to independent expenditures and communication costs.  # noqa: E501

        :param support_oppose_indicator: The support_oppose_indicator of this ScheduleEByCandidate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and support_oppose_indicator is None:  # noqa: E501
            raise ValueError('Invalid value for `support_oppose_indicator`, must not be `None`')  # noqa: E501

        self._support_oppose_indicator = support_oppose_indicator

    @property
    def total(self):
        """Gets the total of this ScheduleEByCandidate.  # noqa: E501

        Sum of transactions  # noqa: E501

        :return: The total of this ScheduleEByCandidate.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ScheduleEByCandidate.

        Sum of transactions  # noqa: E501

        :param total: The total of this ScheduleEByCandidate.  # noqa: E501
        :type: float
        """

        self._total = total

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
        if not isinstance(other, ScheduleEByCandidate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScheduleEByCandidate):
            return True

        return self.to_dict() != other.to_dict()
