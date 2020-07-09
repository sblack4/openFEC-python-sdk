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


class CommitteeReportsIEOnly(object):
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
        'beginning_image_number': 'str',
        'committee_id': 'str',
        'committee_type': 'str',
        'coverage_end_date': 'datetime',
        'coverage_start_date': 'datetime',
        'csv_url': 'str',
        'cycle': 'int',
        'document_description': 'str',
        'end_image_number': 'str',
        'fec_file_id': 'str',
        'fec_url': 'str',
        'independent_contributions_period': 'float',
        'independent_expenditures_period': 'float',
        'is_amended': 'bool',
        'means_filed': 'str',
        'pdf_url': 'str',
        'receipt_date': 'date',
        'report_form': 'str',
        'report_type': 'str',
        'report_type_full': 'str',
        'report_year': 'int'
    }

    attribute_map = {
        'beginning_image_number': 'beginning_image_number',
        'committee_id': 'committee_id',
        'committee_type': 'committee_type',
        'coverage_end_date': 'coverage_end_date',
        'coverage_start_date': 'coverage_start_date',
        'csv_url': 'csv_url',
        'cycle': 'cycle',
        'document_description': 'document_description',
        'end_image_number': 'end_image_number',
        'fec_file_id': 'fec_file_id',
        'fec_url': 'fec_url',
        'independent_contributions_period': 'independent_contributions_period',
        'independent_expenditures_period': 'independent_expenditures_period',
        'is_amended': 'is_amended',
        'means_filed': 'means_filed',
        'pdf_url': 'pdf_url',
        'receipt_date': 'receipt_date',
        'report_form': 'report_form',
        'report_type': 'report_type',
        'report_type_full': 'report_type_full',
        'report_year': 'report_year'
    }

    def __init__(self, beginning_image_number=None, committee_id=None, committee_type=None, coverage_end_date=None, coverage_start_date=None, csv_url=None, cycle=None, document_description=None, end_image_number=None, fec_file_id=None, fec_url=None, independent_contributions_period=None, independent_expenditures_period=None, is_amended=None, means_filed=None, pdf_url=None, receipt_date=None, report_form=None, report_type=None, report_type_full=None, report_year=None, local_vars_configuration=None):  # noqa: E501
        """CommitteeReportsIEOnly - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._beginning_image_number = None
        self._committee_id = None
        self._committee_type = None
        self._coverage_end_date = None
        self._coverage_start_date = None
        self._csv_url = None
        self._cycle = None
        self._document_description = None
        self._end_image_number = None
        self._fec_file_id = None
        self._fec_url = None
        self._independent_contributions_period = None
        self._independent_expenditures_period = None
        self._is_amended = None
        self._means_filed = None
        self._pdf_url = None
        self._receipt_date = None
        self._report_form = None
        self._report_type = None
        self._report_type_full = None
        self._report_year = None
        self.discriminator = None

        if beginning_image_number is not None:
            self.beginning_image_number = beginning_image_number
        self.committee_id = committee_id
        if committee_type is not None:
            self.committee_type = committee_type
        self.coverage_end_date = coverage_end_date
        self.coverage_start_date = coverage_start_date
        if csv_url is not None:
            self.csv_url = csv_url
        self.cycle = cycle
        if document_description is not None:
            self.document_description = document_description
        if end_image_number is not None:
            self.end_image_number = end_image_number
        if fec_file_id is not None:
            self.fec_file_id = fec_file_id
        if fec_url is not None:
            self.fec_url = fec_url
        self.independent_contributions_period = independent_contributions_period
        self.independent_expenditures_period = independent_expenditures_period
        self.is_amended = is_amended
        self.means_filed = means_filed
        if pdf_url is not None:
            self.pdf_url = pdf_url
        self.receipt_date = receipt_date
        if report_form is not None:
            self.report_form = report_form
        self.report_type = report_type
        self.report_type_full = report_type_full
        self.report_year = report_year

    @property
    def beginning_image_number(self):
        """Gets the beginning_image_number of this CommitteeReportsIEOnly.  # noqa: E501


        :return: The beginning_image_number of this CommitteeReportsIEOnly.  # noqa: E501
        :rtype: str
        """
        return self._beginning_image_number

    @beginning_image_number.setter
    def beginning_image_number(self, beginning_image_number):
        """Sets the beginning_image_number of this CommitteeReportsIEOnly.


        :param beginning_image_number: The beginning_image_number of this CommitteeReportsIEOnly.  # noqa: E501
        :type: str
        """

        self._beginning_image_number = beginning_image_number

    @property
    def committee_id(self):
        """Gets the committee_id of this CommitteeReportsIEOnly.  # noqa: E501


        :return: The committee_id of this CommitteeReportsIEOnly.  # noqa: E501
        :rtype: str
        """
        return self._committee_id

    @committee_id.setter
    def committee_id(self, committee_id):
        """Sets the committee_id of this CommitteeReportsIEOnly.


        :param committee_id: The committee_id of this CommitteeReportsIEOnly.  # noqa: E501
        :type: str
        """

        self._committee_id = committee_id

    @property
    def committee_type(self):
        """Gets the committee_type of this CommitteeReportsIEOnly.  # noqa: E501


        :return: The committee_type of this CommitteeReportsIEOnly.  # noqa: E501
        :rtype: str
        """
        return self._committee_type

    @committee_type.setter
    def committee_type(self, committee_type):
        """Sets the committee_type of this CommitteeReportsIEOnly.


        :param committee_type: The committee_type of this CommitteeReportsIEOnly.  # noqa: E501
        :type: str
        """

        self._committee_type = committee_type

    @property
    def coverage_end_date(self):
        """Gets the coverage_end_date of this CommitteeReportsIEOnly.  # noqa: E501


        :return: The coverage_end_date of this CommitteeReportsIEOnly.  # noqa: E501
        :rtype: datetime
        """
        return self._coverage_end_date

    @coverage_end_date.setter
    def coverage_end_date(self, coverage_end_date):
        """Sets the coverage_end_date of this CommitteeReportsIEOnly.


        :param coverage_end_date: The coverage_end_date of this CommitteeReportsIEOnly.  # noqa: E501
        :type: datetime
        """

        self._coverage_end_date = coverage_end_date

    @property
    def coverage_start_date(self):
        """Gets the coverage_start_date of this CommitteeReportsIEOnly.  # noqa: E501


        :return: The coverage_start_date of this CommitteeReportsIEOnly.  # noqa: E501
        :rtype: datetime
        """
        return self._coverage_start_date

    @coverage_start_date.setter
    def coverage_start_date(self, coverage_start_date):
        """Sets the coverage_start_date of this CommitteeReportsIEOnly.


        :param coverage_start_date: The coverage_start_date of this CommitteeReportsIEOnly.  # noqa: E501
        :type: datetime
        """

        self._coverage_start_date = coverage_start_date

    @property
    def csv_url(self):
        """Gets the csv_url of this CommitteeReportsIEOnly.  # noqa: E501


        :return: The csv_url of this CommitteeReportsIEOnly.  # noqa: E501
        :rtype: str
        """
        return self._csv_url

    @csv_url.setter
    def csv_url(self, csv_url):
        """Sets the csv_url of this CommitteeReportsIEOnly.


        :param csv_url: The csv_url of this CommitteeReportsIEOnly.  # noqa: E501
        :type: str
        """

        self._csv_url = csv_url

    @property
    def cycle(self):
        """Gets the cycle of this CommitteeReportsIEOnly.  # noqa: E501


        :return: The cycle of this CommitteeReportsIEOnly.  # noqa: E501
        :rtype: int
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        """Sets the cycle of this CommitteeReportsIEOnly.


        :param cycle: The cycle of this CommitteeReportsIEOnly.  # noqa: E501
        :type: int
        """

        self._cycle = cycle

    @property
    def document_description(self):
        """Gets the document_description of this CommitteeReportsIEOnly.  # noqa: E501


        :return: The document_description of this CommitteeReportsIEOnly.  # noqa: E501
        :rtype: str
        """
        return self._document_description

    @document_description.setter
    def document_description(self, document_description):
        """Sets the document_description of this CommitteeReportsIEOnly.


        :param document_description: The document_description of this CommitteeReportsIEOnly.  # noqa: E501
        :type: str
        """

        self._document_description = document_description

    @property
    def end_image_number(self):
        """Gets the end_image_number of this CommitteeReportsIEOnly.  # noqa: E501


        :return: The end_image_number of this CommitteeReportsIEOnly.  # noqa: E501
        :rtype: str
        """
        return self._end_image_number

    @end_image_number.setter
    def end_image_number(self, end_image_number):
        """Sets the end_image_number of this CommitteeReportsIEOnly.


        :param end_image_number: The end_image_number of this CommitteeReportsIEOnly.  # noqa: E501
        :type: str
        """

        self._end_image_number = end_image_number

    @property
    def fec_file_id(self):
        """Gets the fec_file_id of this CommitteeReportsIEOnly.  # noqa: E501


        :return: The fec_file_id of this CommitteeReportsIEOnly.  # noqa: E501
        :rtype: str
        """
        return self._fec_file_id

    @fec_file_id.setter
    def fec_file_id(self, fec_file_id):
        """Sets the fec_file_id of this CommitteeReportsIEOnly.


        :param fec_file_id: The fec_file_id of this CommitteeReportsIEOnly.  # noqa: E501
        :type: str
        """

        self._fec_file_id = fec_file_id

    @property
    def fec_url(self):
        """Gets the fec_url of this CommitteeReportsIEOnly.  # noqa: E501


        :return: The fec_url of this CommitteeReportsIEOnly.  # noqa: E501
        :rtype: str
        """
        return self._fec_url

    @fec_url.setter
    def fec_url(self, fec_url):
        """Sets the fec_url of this CommitteeReportsIEOnly.


        :param fec_url: The fec_url of this CommitteeReportsIEOnly.  # noqa: E501
        :type: str
        """

        self._fec_url = fec_url

    @property
    def independent_contributions_period(self):
        """Gets the independent_contributions_period of this CommitteeReportsIEOnly.  # noqa: E501


        :return: The independent_contributions_period of this CommitteeReportsIEOnly.  # noqa: E501
        :rtype: float
        """
        return self._independent_contributions_period

    @independent_contributions_period.setter
    def independent_contributions_period(self, independent_contributions_period):
        """Sets the independent_contributions_period of this CommitteeReportsIEOnly.


        :param independent_contributions_period: The independent_contributions_period of this CommitteeReportsIEOnly.  # noqa: E501
        :type: float
        """

        self._independent_contributions_period = independent_contributions_period

    @property
    def independent_expenditures_period(self):
        """Gets the independent_expenditures_period of this CommitteeReportsIEOnly.  # noqa: E501


        :return: The independent_expenditures_period of this CommitteeReportsIEOnly.  # noqa: E501
        :rtype: float
        """
        return self._independent_expenditures_period

    @independent_expenditures_period.setter
    def independent_expenditures_period(self, independent_expenditures_period):
        """Sets the independent_expenditures_period of this CommitteeReportsIEOnly.


        :param independent_expenditures_period: The independent_expenditures_period of this CommitteeReportsIEOnly.  # noqa: E501
        :type: float
        """

        self._independent_expenditures_period = independent_expenditures_period

    @property
    def is_amended(self):
        """Gets the is_amended of this CommitteeReportsIEOnly.  # noqa: E501

         False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.   # noqa: E501

        :return: The is_amended of this CommitteeReportsIEOnly.  # noqa: E501
        :rtype: bool
        """
        return self._is_amended

    @is_amended.setter
    def is_amended(self, is_amended):
        """Sets the is_amended of this CommitteeReportsIEOnly.

         False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.   # noqa: E501

        :param is_amended: The is_amended of this CommitteeReportsIEOnly.  # noqa: E501
        :type: bool
        """

        self._is_amended = is_amended

    @property
    def means_filed(self):
        """Gets the means_filed of this CommitteeReportsIEOnly.  # noqa: E501

        The method used to file with the FEC, either electronic or on paper.  # noqa: E501

        :return: The means_filed of this CommitteeReportsIEOnly.  # noqa: E501
        :rtype: str
        """
        return self._means_filed

    @means_filed.setter
    def means_filed(self, means_filed):
        """Sets the means_filed of this CommitteeReportsIEOnly.

        The method used to file with the FEC, either electronic or on paper.  # noqa: E501

        :param means_filed: The means_filed of this CommitteeReportsIEOnly.  # noqa: E501
        :type: str
        """

        self._means_filed = means_filed

    @property
    def pdf_url(self):
        """Gets the pdf_url of this CommitteeReportsIEOnly.  # noqa: E501


        :return: The pdf_url of this CommitteeReportsIEOnly.  # noqa: E501
        :rtype: str
        """
        return self._pdf_url

    @pdf_url.setter
    def pdf_url(self, pdf_url):
        """Sets the pdf_url of this CommitteeReportsIEOnly.


        :param pdf_url: The pdf_url of this CommitteeReportsIEOnly.  # noqa: E501
        :type: str
        """

        self._pdf_url = pdf_url

    @property
    def receipt_date(self):
        """Gets the receipt_date of this CommitteeReportsIEOnly.  # noqa: E501

        Date the FEC received the electronic or paper record  # noqa: E501

        :return: The receipt_date of this CommitteeReportsIEOnly.  # noqa: E501
        :rtype: date
        """
        return self._receipt_date

    @receipt_date.setter
    def receipt_date(self, receipt_date):
        """Sets the receipt_date of this CommitteeReportsIEOnly.

        Date the FEC received the electronic or paper record  # noqa: E501

        :param receipt_date: The receipt_date of this CommitteeReportsIEOnly.  # noqa: E501
        :type: date
        """

        self._receipt_date = receipt_date

    @property
    def report_form(self):
        """Gets the report_form of this CommitteeReportsIEOnly.  # noqa: E501


        :return: The report_form of this CommitteeReportsIEOnly.  # noqa: E501
        :rtype: str
        """
        return self._report_form

    @report_form.setter
    def report_form(self, report_form):
        """Sets the report_form of this CommitteeReportsIEOnly.


        :param report_form: The report_form of this CommitteeReportsIEOnly.  # noqa: E501
        :type: str
        """

        self._report_form = report_form

    @property
    def report_type(self):
        """Gets the report_type of this CommitteeReportsIEOnly.  # noqa: E501


        :return: The report_type of this CommitteeReportsIEOnly.  # noqa: E501
        :rtype: str
        """
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        """Sets the report_type of this CommitteeReportsIEOnly.


        :param report_type: The report_type of this CommitteeReportsIEOnly.  # noqa: E501
        :type: str
        """

        self._report_type = report_type

    @property
    def report_type_full(self):
        """Gets the report_type_full of this CommitteeReportsIEOnly.  # noqa: E501


        :return: The report_type_full of this CommitteeReportsIEOnly.  # noqa: E501
        :rtype: str
        """
        return self._report_type_full

    @report_type_full.setter
    def report_type_full(self, report_type_full):
        """Sets the report_type_full of this CommitteeReportsIEOnly.


        :param report_type_full: The report_type_full of this CommitteeReportsIEOnly.  # noqa: E501
        :type: str
        """

        self._report_type_full = report_type_full

    @property
    def report_year(self):
        """Gets the report_year of this CommitteeReportsIEOnly.  # noqa: E501


        :return: The report_year of this CommitteeReportsIEOnly.  # noqa: E501
        :rtype: int
        """
        return self._report_year

    @report_year.setter
    def report_year(self, report_year):
        """Sets the report_year of this CommitteeReportsIEOnly.


        :param report_year: The report_year of this CommitteeReportsIEOnly.  # noqa: E501
        :type: int
        """

        self._report_year = report_year

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
        if not isinstance(other, CommitteeReportsIEOnly):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CommitteeReportsIEOnly):
            return True

        return self.to_dict() != other.to_dict()
