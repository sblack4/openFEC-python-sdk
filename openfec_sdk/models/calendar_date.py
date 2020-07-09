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


class CalendarDate(object):
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
        'all_day': 'bool',
        'calendar_category_id': 'int',
        'category': 'str',
        'description': 'str',
        'end_date': 'str',
        'event_id': 'int',
        'location': 'str',
        'start_date': 'str',
        'state': 'list[str]',
        'summary': 'str',
        'url': 'str'
    }

    attribute_map = {
        'all_day': 'all_day',
        'calendar_category_id': 'calendar_category_id',
        'category': 'category',
        'description': 'description',
        'end_date': 'end_date',
        'event_id': 'event_id',
        'location': 'location',
        'start_date': 'start_date',
        'state': 'state',
        'summary': 'summary',
        'url': 'url'
    }

    def __init__(self, all_day=None, calendar_category_id=None, category=None, description=None, end_date=None, event_id=None, location=None, start_date=None, state=None, summary=None, url=None, local_vars_configuration=None):  # noqa: E501
        """CalendarDate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._all_day = None
        self._calendar_category_id = None
        self._category = None
        self._description = None
        self._end_date = None
        self._event_id = None
        self._location = None
        self._start_date = None
        self._state = None
        self._summary = None
        self._url = None
        self.discriminator = None

        self.all_day = all_day
        self.calendar_category_id = calendar_category_id
        self.category = category
        if description is not None:
            self.description = description
        if end_date is not None:
            self.end_date = end_date
        if event_id is not None:
            self.event_id = event_id
        self.location = location
        if start_date is not None:
            self.start_date = start_date
        self.state = state
        if summary is not None:
            self.summary = summary
        self.url = url

    @property
    def all_day(self):
        """Gets the all_day of this CalendarDate.  # noqa: E501


        :return: The all_day of this CalendarDate.  # noqa: E501
        :rtype: bool
        """
        return self._all_day

    @all_day.setter
    def all_day(self, all_day):
        """Sets the all_day of this CalendarDate.


        :param all_day: The all_day of this CalendarDate.  # noqa: E501
        :type: bool
        """

        self._all_day = all_day

    @property
    def calendar_category_id(self):
        """Gets the calendar_category_id of this CalendarDate.  # noqa: E501

         Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29   # noqa: E501

        :return: The calendar_category_id of this CalendarDate.  # noqa: E501
        :rtype: int
        """
        return self._calendar_category_id

    @calendar_category_id.setter
    def calendar_category_id(self, calendar_category_id):
        """Sets the calendar_category_id of this CalendarDate.

         Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29   # noqa: E501

        :param calendar_category_id: The calendar_category_id of this CalendarDate.  # noqa: E501
        :type: int
        """

        self._calendar_category_id = calendar_category_id

    @property
    def category(self):
        """Gets the category of this CalendarDate.  # noqa: E501

         Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29   # noqa: E501

        :return: The category of this CalendarDate.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this CalendarDate.

         Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29   # noqa: E501

        :param category: The category of this CalendarDate.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def description(self):
        """Gets the description of this CalendarDate.  # noqa: E501


        :return: The description of this CalendarDate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CalendarDate.


        :param description: The description of this CalendarDate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def end_date(self):
        """Gets the end_date of this CalendarDate.  # noqa: E501


        :return: The end_date of this CalendarDate.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this CalendarDate.


        :param end_date: The end_date of this CalendarDate.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def event_id(self):
        """Gets the event_id of this CalendarDate.  # noqa: E501

        An unique ID for an event. Useful for downloading a single event to your calendar. This ID is not a permanent, persistent ID.  # noqa: E501

        :return: The event_id of this CalendarDate.  # noqa: E501
        :rtype: int
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this CalendarDate.

        An unique ID for an event. Useful for downloading a single event to your calendar. This ID is not a permanent, persistent ID.  # noqa: E501

        :param event_id: The event_id of this CalendarDate.  # noqa: E501
        :type: int
        """

        self._event_id = event_id

    @property
    def location(self):
        """Gets the location of this CalendarDate.  # noqa: E501

         Can be state address or room.   # noqa: E501

        :return: The location of this CalendarDate.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this CalendarDate.

         Can be state address or room.   # noqa: E501

        :param location: The location of this CalendarDate.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def start_date(self):
        """Gets the start_date of this CalendarDate.  # noqa: E501


        :return: The start_date of this CalendarDate.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this CalendarDate.


        :param start_date: The start_date of this CalendarDate.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def state(self):
        """Gets the state of this CalendarDate.  # noqa: E501

        The state field only applies to election dates and reporting deadlines, reporting periods and all other dates do not have the array of states to filter on  # noqa: E501

        :return: The state of this CalendarDate.  # noqa: E501
        :rtype: list[str]
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CalendarDate.

        The state field only applies to election dates and reporting deadlines, reporting periods and all other dates do not have the array of states to filter on  # noqa: E501

        :param state: The state of this CalendarDate.  # noqa: E501
        :type: list[str]
        """

        self._state = state

    @property
    def summary(self):
        """Gets the summary of this CalendarDate.  # noqa: E501


        :return: The summary of this CalendarDate.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this CalendarDate.


        :param summary: The summary of this CalendarDate.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def url(self):
        """Gets the url of this CalendarDate.  # noqa: E501

         A url for that event   # noqa: E501

        :return: The url of this CalendarDate.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CalendarDate.

         A url for that event   # noqa: E501

        :param url: The url of this CalendarDate.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if not isinstance(other, CalendarDate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CalendarDate):
            return True

        return self.to_dict() != other.to_dict()
