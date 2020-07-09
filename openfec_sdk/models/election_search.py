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


class ElectionSearch(object):
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
        'candidate_status': 'str',
        'cycle': 'int',
        'district': 'str',
        'incumbent_id': 'str',
        'incumbent_name': 'str',
        'office': 'str',
        'state': 'str'
    }

    attribute_map = {
        'candidate_status': 'candidate_status',
        'cycle': 'cycle',
        'district': 'district',
        'incumbent_id': 'incumbent_id',
        'incumbent_name': 'incumbent_name',
        'office': 'office',
        'state': 'state'
    }

    def __init__(self, candidate_status=None, cycle=None, district=None, incumbent_id=None, incumbent_name=None, office=None, state=None, local_vars_configuration=None):  # noqa: E501
        """ElectionSearch - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._candidate_status = None
        self._cycle = None
        self._district = None
        self._incumbent_id = None
        self._incumbent_name = None
        self._office = None
        self._state = None
        self.discriminator = None

        if candidate_status is not None:
            self.candidate_status = candidate_status
        if cycle is not None:
            self.cycle = cycle
        if district is not None:
            self.district = district
        if incumbent_id is not None:
            self.incumbent_id = incumbent_id
        if incumbent_name is not None:
            self.incumbent_name = incumbent_name
        if office is not None:
            self.office = office
        if state is not None:
            self.state = state

    @property
    def candidate_status(self):
        """Gets the candidate_status of this ElectionSearch.  # noqa: E501


        :return: The candidate_status of this ElectionSearch.  # noqa: E501
        :rtype: str
        """
        return self._candidate_status

    @candidate_status.setter
    def candidate_status(self, candidate_status):
        """Sets the candidate_status of this ElectionSearch.


        :param candidate_status: The candidate_status of this ElectionSearch.  # noqa: E501
        :type: str
        """

        self._candidate_status = candidate_status

    @property
    def cycle(self):
        """Gets the cycle of this ElectionSearch.  # noqa: E501


        :return: The cycle of this ElectionSearch.  # noqa: E501
        :rtype: int
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        """Sets the cycle of this ElectionSearch.


        :param cycle: The cycle of this ElectionSearch.  # noqa: E501
        :type: int
        """

        self._cycle = cycle

    @property
    def district(self):
        """Gets the district of this ElectionSearch.  # noqa: E501


        :return: The district of this ElectionSearch.  # noqa: E501
        :rtype: str
        """
        return self._district

    @district.setter
    def district(self, district):
        """Sets the district of this ElectionSearch.


        :param district: The district of this ElectionSearch.  # noqa: E501
        :type: str
        """

        self._district = district

    @property
    def incumbent_id(self):
        """Gets the incumbent_id of this ElectionSearch.  # noqa: E501


        :return: The incumbent_id of this ElectionSearch.  # noqa: E501
        :rtype: str
        """
        return self._incumbent_id

    @incumbent_id.setter
    def incumbent_id(self, incumbent_id):
        """Sets the incumbent_id of this ElectionSearch.


        :param incumbent_id: The incumbent_id of this ElectionSearch.  # noqa: E501
        :type: str
        """

        self._incumbent_id = incumbent_id

    @property
    def incumbent_name(self):
        """Gets the incumbent_name of this ElectionSearch.  # noqa: E501


        :return: The incumbent_name of this ElectionSearch.  # noqa: E501
        :rtype: str
        """
        return self._incumbent_name

    @incumbent_name.setter
    def incumbent_name(self, incumbent_name):
        """Sets the incumbent_name of this ElectionSearch.


        :param incumbent_name: The incumbent_name of this ElectionSearch.  # noqa: E501
        :type: str
        """

        self._incumbent_name = incumbent_name

    @property
    def office(self):
        """Gets the office of this ElectionSearch.  # noqa: E501


        :return: The office of this ElectionSearch.  # noqa: E501
        :rtype: str
        """
        return self._office

    @office.setter
    def office(self, office):
        """Sets the office of this ElectionSearch.


        :param office: The office of this ElectionSearch.  # noqa: E501
        :type: str
        """

        self._office = office

    @property
    def state(self):
        """Gets the state of this ElectionSearch.  # noqa: E501


        :return: The state of this ElectionSearch.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ElectionSearch.


        :param state: The state of this ElectionSearch.  # noqa: E501
        :type: str
        """

        self._state = state

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
        if not isinstance(other, ElectionSearch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ElectionSearch):
            return True

        return self.to_dict() != other.to_dict()
