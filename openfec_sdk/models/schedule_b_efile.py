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


class ScheduleBEfile(object):
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
        'amendment_indicator': 'str',
        'back_reference_schedule_name': 'str',
        'back_reference_transaction_id': 'str',
        'beginning_image_number': 'str',
        'beneficiary_committee_name': 'str',
        'candidate_office': 'str',
        'candidate_office_district': 'str',
        'committee': 'CommitteeHistory',
        'committee_id': 'str',
        'csv_url': 'str',
        'disbursement_amount': 'float',
        'disbursement_date': 'date',
        'disbursement_description': 'str',
        'disbursement_type': 'str',
        'entity_type': 'str',
        'fec_url': 'str',
        'file_number': 'int',
        'filing': 'EFilings',
        'image_number': 'str',
        'is_notice': 'bool',
        'line_number': 'str',
        'load_timestamp': 'datetime',
        'memo_code': 'str',
        'memo_text': 'str',
        'payee_name': 'str',
        'pdf_url': 'str',
        'recipient_city': 'str',
        'recipient_name': 'str',
        'recipient_prefix': 'str',
        'recipient_state': 'str',
        'recipient_suffix': 'str',
        'recipient_zip': 'str',
        'related_line_number': 'int',
        'report_type': 'str',
        'semi_annual_bundled_refund': 'int',
        'transaction_id': 'str'
    }

    attribute_map = {
        'amendment_indicator': 'amendment_indicator',
        'back_reference_schedule_name': 'back_reference_schedule_name',
        'back_reference_transaction_id': 'back_reference_transaction_id',
        'beginning_image_number': 'beginning_image_number',
        'beneficiary_committee_name': 'beneficiary_committee_name',
        'candidate_office': 'candidate_office',
        'candidate_office_district': 'candidate_office_district',
        'committee': 'committee',
        'committee_id': 'committee_id',
        'csv_url': 'csv_url',
        'disbursement_amount': 'disbursement_amount',
        'disbursement_date': 'disbursement_date',
        'disbursement_description': 'disbursement_description',
        'disbursement_type': 'disbursement_type',
        'entity_type': 'entity_type',
        'fec_url': 'fec_url',
        'file_number': 'file_number',
        'filing': 'filing',
        'image_number': 'image_number',
        'is_notice': 'is_notice',
        'line_number': 'line_number',
        'load_timestamp': 'load_timestamp',
        'memo_code': 'memo_code',
        'memo_text': 'memo_text',
        'payee_name': 'payee_name',
        'pdf_url': 'pdf_url',
        'recipient_city': 'recipient_city',
        'recipient_name': 'recipient_name',
        'recipient_prefix': 'recipient_prefix',
        'recipient_state': 'recipient_state',
        'recipient_suffix': 'recipient_suffix',
        'recipient_zip': 'recipient_zip',
        'related_line_number': 'related_line_number',
        'report_type': 'report_type',
        'semi_annual_bundled_refund': 'semi_annual_bundled_refund',
        'transaction_id': 'transaction_id'
    }

    def __init__(self, amendment_indicator=None, back_reference_schedule_name=None, back_reference_transaction_id=None, beginning_image_number=None, beneficiary_committee_name=None, candidate_office=None, candidate_office_district=None, committee=None, committee_id=None, csv_url=None, disbursement_amount=None, disbursement_date=None, disbursement_description=None, disbursement_type=None, entity_type=None, fec_url=None, file_number=None, filing=None, image_number=None, is_notice=None, line_number=None, load_timestamp=None, memo_code=None, memo_text=None, payee_name=None, pdf_url=None, recipient_city=None, recipient_name=None, recipient_prefix=None, recipient_state=None, recipient_suffix=None, recipient_zip=None, related_line_number=None, report_type=None, semi_annual_bundled_refund=None, transaction_id=None, local_vars_configuration=None):  # noqa: E501
        """ScheduleBEfile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._amendment_indicator = None
        self._back_reference_schedule_name = None
        self._back_reference_transaction_id = None
        self._beginning_image_number = None
        self._beneficiary_committee_name = None
        self._candidate_office = None
        self._candidate_office_district = None
        self._committee = None
        self._committee_id = None
        self._csv_url = None
        self._disbursement_amount = None
        self._disbursement_date = None
        self._disbursement_description = None
        self._disbursement_type = None
        self._entity_type = None
        self._fec_url = None
        self._file_number = None
        self._filing = None
        self._image_number = None
        self._is_notice = None
        self._line_number = None
        self._load_timestamp = None
        self._memo_code = None
        self._memo_text = None
        self._payee_name = None
        self._pdf_url = None
        self._recipient_city = None
        self._recipient_name = None
        self._recipient_prefix = None
        self._recipient_state = None
        self._recipient_suffix = None
        self._recipient_zip = None
        self._related_line_number = None
        self._report_type = None
        self._semi_annual_bundled_refund = None
        self._transaction_id = None
        self.discriminator = None

        self.amendment_indicator = amendment_indicator
        self.back_reference_schedule_name = back_reference_schedule_name
        self.back_reference_transaction_id = back_reference_transaction_id
        if beginning_image_number is not None:
            self.beginning_image_number = beginning_image_number
        self.beneficiary_committee_name = beneficiary_committee_name
        self.candidate_office = candidate_office
        self.candidate_office_district = candidate_office_district
        if committee is not None:
            self.committee = committee
        self.committee_id = committee_id
        if csv_url is not None:
            self.csv_url = csv_url
        self.disbursement_amount = disbursement_amount
        self.disbursement_date = disbursement_date
        self.disbursement_description = disbursement_description
        self.disbursement_type = disbursement_type
        self.entity_type = entity_type
        if fec_url is not None:
            self.fec_url = fec_url
        self.file_number = file_number
        if filing is not None:
            self.filing = filing
        self.image_number = image_number
        if is_notice is not None:
            self.is_notice = is_notice
        self.line_number = line_number
        self.load_timestamp = load_timestamp
        self.memo_code = memo_code
        self.memo_text = memo_text
        if payee_name is not None:
            self.payee_name = payee_name
        if pdf_url is not None:
            self.pdf_url = pdf_url
        self.recipient_city = recipient_city
        self.recipient_name = recipient_name
        self.recipient_prefix = recipient_prefix
        self.recipient_state = recipient_state
        self.recipient_suffix = recipient_suffix
        self.recipient_zip = recipient_zip
        self.related_line_number = related_line_number
        if report_type is not None:
            self.report_type = report_type
        self.semi_annual_bundled_refund = semi_annual_bundled_refund
        self.transaction_id = transaction_id

    @property
    def amendment_indicator(self):
        """Gets the amendment_indicator of this ScheduleBEfile.  # noqa: E501


        :return: The amendment_indicator of this ScheduleBEfile.  # noqa: E501
        :rtype: str
        """
        return self._amendment_indicator

    @amendment_indicator.setter
    def amendment_indicator(self, amendment_indicator):
        """Sets the amendment_indicator of this ScheduleBEfile.


        :param amendment_indicator: The amendment_indicator of this ScheduleBEfile.  # noqa: E501
        :type: str
        """

        self._amendment_indicator = amendment_indicator

    @property
    def back_reference_schedule_name(self):
        """Gets the back_reference_schedule_name of this ScheduleBEfile.  # noqa: E501


        :return: The back_reference_schedule_name of this ScheduleBEfile.  # noqa: E501
        :rtype: str
        """
        return self._back_reference_schedule_name

    @back_reference_schedule_name.setter
    def back_reference_schedule_name(self, back_reference_schedule_name):
        """Sets the back_reference_schedule_name of this ScheduleBEfile.


        :param back_reference_schedule_name: The back_reference_schedule_name of this ScheduleBEfile.  # noqa: E501
        :type: str
        """

        self._back_reference_schedule_name = back_reference_schedule_name

    @property
    def back_reference_transaction_id(self):
        """Gets the back_reference_transaction_id of this ScheduleBEfile.  # noqa: E501


        :return: The back_reference_transaction_id of this ScheduleBEfile.  # noqa: E501
        :rtype: str
        """
        return self._back_reference_transaction_id

    @back_reference_transaction_id.setter
    def back_reference_transaction_id(self, back_reference_transaction_id):
        """Sets the back_reference_transaction_id of this ScheduleBEfile.


        :param back_reference_transaction_id: The back_reference_transaction_id of this ScheduleBEfile.  # noqa: E501
        :type: str
        """

        self._back_reference_transaction_id = back_reference_transaction_id

    @property
    def beginning_image_number(self):
        """Gets the beginning_image_number of this ScheduleBEfile.  # noqa: E501


        :return: The beginning_image_number of this ScheduleBEfile.  # noqa: E501
        :rtype: str
        """
        return self._beginning_image_number

    @beginning_image_number.setter
    def beginning_image_number(self, beginning_image_number):
        """Sets the beginning_image_number of this ScheduleBEfile.


        :param beginning_image_number: The beginning_image_number of this ScheduleBEfile.  # noqa: E501
        :type: str
        """

        self._beginning_image_number = beginning_image_number

    @property
    def beneficiary_committee_name(self):
        """Gets the beneficiary_committee_name of this ScheduleBEfile.  # noqa: E501


        :return: The beneficiary_committee_name of this ScheduleBEfile.  # noqa: E501
        :rtype: str
        """
        return self._beneficiary_committee_name

    @beneficiary_committee_name.setter
    def beneficiary_committee_name(self, beneficiary_committee_name):
        """Sets the beneficiary_committee_name of this ScheduleBEfile.


        :param beneficiary_committee_name: The beneficiary_committee_name of this ScheduleBEfile.  # noqa: E501
        :type: str
        """

        self._beneficiary_committee_name = beneficiary_committee_name

    @property
    def candidate_office(self):
        """Gets the candidate_office of this ScheduleBEfile.  # noqa: E501


        :return: The candidate_office of this ScheduleBEfile.  # noqa: E501
        :rtype: str
        """
        return self._candidate_office

    @candidate_office.setter
    def candidate_office(self, candidate_office):
        """Sets the candidate_office of this ScheduleBEfile.


        :param candidate_office: The candidate_office of this ScheduleBEfile.  # noqa: E501
        :type: str
        """

        self._candidate_office = candidate_office

    @property
    def candidate_office_district(self):
        """Gets the candidate_office_district of this ScheduleBEfile.  # noqa: E501


        :return: The candidate_office_district of this ScheduleBEfile.  # noqa: E501
        :rtype: str
        """
        return self._candidate_office_district

    @candidate_office_district.setter
    def candidate_office_district(self, candidate_office_district):
        """Sets the candidate_office_district of this ScheduleBEfile.


        :param candidate_office_district: The candidate_office_district of this ScheduleBEfile.  # noqa: E501
        :type: str
        """

        self._candidate_office_district = candidate_office_district

    @property
    def committee(self):
        """Gets the committee of this ScheduleBEfile.  # noqa: E501


        :return: The committee of this ScheduleBEfile.  # noqa: E501
        :rtype: CommitteeHistory
        """
        return self._committee

    @committee.setter
    def committee(self, committee):
        """Sets the committee of this ScheduleBEfile.


        :param committee: The committee of this ScheduleBEfile.  # noqa: E501
        :type: CommitteeHistory
        """

        self._committee = committee

    @property
    def committee_id(self):
        """Gets the committee_id of this ScheduleBEfile.  # noqa: E501

         A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.   # noqa: E501

        :return: The committee_id of this ScheduleBEfile.  # noqa: E501
        :rtype: str
        """
        return self._committee_id

    @committee_id.setter
    def committee_id(self, committee_id):
        """Sets the committee_id of this ScheduleBEfile.

         A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.   # noqa: E501

        :param committee_id: The committee_id of this ScheduleBEfile.  # noqa: E501
        :type: str
        """

        self._committee_id = committee_id

    @property
    def csv_url(self):
        """Gets the csv_url of this ScheduleBEfile.  # noqa: E501


        :return: The csv_url of this ScheduleBEfile.  # noqa: E501
        :rtype: str
        """
        return self._csv_url

    @csv_url.setter
    def csv_url(self, csv_url):
        """Sets the csv_url of this ScheduleBEfile.


        :param csv_url: The csv_url of this ScheduleBEfile.  # noqa: E501
        :type: str
        """

        self._csv_url = csv_url

    @property
    def disbursement_amount(self):
        """Gets the disbursement_amount of this ScheduleBEfile.  # noqa: E501


        :return: The disbursement_amount of this ScheduleBEfile.  # noqa: E501
        :rtype: float
        """
        return self._disbursement_amount

    @disbursement_amount.setter
    def disbursement_amount(self, disbursement_amount):
        """Sets the disbursement_amount of this ScheduleBEfile.


        :param disbursement_amount: The disbursement_amount of this ScheduleBEfile.  # noqa: E501
        :type: float
        """

        self._disbursement_amount = disbursement_amount

    @property
    def disbursement_date(self):
        """Gets the disbursement_date of this ScheduleBEfile.  # noqa: E501


        :return: The disbursement_date of this ScheduleBEfile.  # noqa: E501
        :rtype: date
        """
        return self._disbursement_date

    @disbursement_date.setter
    def disbursement_date(self, disbursement_date):
        """Sets the disbursement_date of this ScheduleBEfile.


        :param disbursement_date: The disbursement_date of this ScheduleBEfile.  # noqa: E501
        :type: date
        """

        self._disbursement_date = disbursement_date

    @property
    def disbursement_description(self):
        """Gets the disbursement_description of this ScheduleBEfile.  # noqa: E501


        :return: The disbursement_description of this ScheduleBEfile.  # noqa: E501
        :rtype: str
        """
        return self._disbursement_description

    @disbursement_description.setter
    def disbursement_description(self, disbursement_description):
        """Sets the disbursement_description of this ScheduleBEfile.


        :param disbursement_description: The disbursement_description of this ScheduleBEfile.  # noqa: E501
        :type: str
        """

        self._disbursement_description = disbursement_description

    @property
    def disbursement_type(self):
        """Gets the disbursement_type of this ScheduleBEfile.  # noqa: E501


        :return: The disbursement_type of this ScheduleBEfile.  # noqa: E501
        :rtype: str
        """
        return self._disbursement_type

    @disbursement_type.setter
    def disbursement_type(self, disbursement_type):
        """Sets the disbursement_type of this ScheduleBEfile.


        :param disbursement_type: The disbursement_type of this ScheduleBEfile.  # noqa: E501
        :type: str
        """

        self._disbursement_type = disbursement_type

    @property
    def entity_type(self):
        """Gets the entity_type of this ScheduleBEfile.  # noqa: E501


        :return: The entity_type of this ScheduleBEfile.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this ScheduleBEfile.


        :param entity_type: The entity_type of this ScheduleBEfile.  # noqa: E501
        :type: str
        """

        self._entity_type = entity_type

    @property
    def fec_url(self):
        """Gets the fec_url of this ScheduleBEfile.  # noqa: E501


        :return: The fec_url of this ScheduleBEfile.  # noqa: E501
        :rtype: str
        """
        return self._fec_url

    @fec_url.setter
    def fec_url(self, fec_url):
        """Sets the fec_url of this ScheduleBEfile.


        :param fec_url: The fec_url of this ScheduleBEfile.  # noqa: E501
        :type: str
        """

        self._fec_url = fec_url

    @property
    def file_number(self):
        """Gets the file_number of this ScheduleBEfile.  # noqa: E501


        :return: The file_number of this ScheduleBEfile.  # noqa: E501
        :rtype: int
        """
        return self._file_number

    @file_number.setter
    def file_number(self, file_number):
        """Sets the file_number of this ScheduleBEfile.


        :param file_number: The file_number of this ScheduleBEfile.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and file_number is None:  # noqa: E501
            raise ValueError('Invalid value for `file_number`, must not be `None`')  # noqa: E501

        self._file_number = file_number

    @property
    def filing(self):
        """Gets the filing of this ScheduleBEfile.  # noqa: E501


        :return: The filing of this ScheduleBEfile.  # noqa: E501
        :rtype: EFilings
        """
        return self._filing

    @filing.setter
    def filing(self, filing):
        """Sets the filing of this ScheduleBEfile.


        :param filing: The filing of this ScheduleBEfile.  # noqa: E501
        :type: EFilings
        """

        self._filing = filing

    @property
    def image_number(self):
        """Gets the image_number of this ScheduleBEfile.  # noqa: E501

         An unique identifier for each page where the electronic or paper filing is reported.   # noqa: E501

        :return: The image_number of this ScheduleBEfile.  # noqa: E501
        :rtype: str
        """
        return self._image_number

    @image_number.setter
    def image_number(self, image_number):
        """Sets the image_number of this ScheduleBEfile.

         An unique identifier for each page where the electronic or paper filing is reported.   # noqa: E501

        :param image_number: The image_number of this ScheduleBEfile.  # noqa: E501
        :type: str
        """

        self._image_number = image_number

    @property
    def is_notice(self):
        """Gets the is_notice of this ScheduleBEfile.  # noqa: E501


        :return: The is_notice of this ScheduleBEfile.  # noqa: E501
        :rtype: bool
        """
        return self._is_notice

    @is_notice.setter
    def is_notice(self, is_notice):
        """Sets the is_notice of this ScheduleBEfile.


        :param is_notice: The is_notice of this ScheduleBEfile.  # noqa: E501
        :type: bool
        """

        self._is_notice = is_notice

    @property
    def line_number(self):
        """Gets the line_number of this ScheduleBEfile.  # noqa: E501


        :return: The line_number of this ScheduleBEfile.  # noqa: E501
        :rtype: str
        """
        return self._line_number

    @line_number.setter
    def line_number(self, line_number):
        """Sets the line_number of this ScheduleBEfile.


        :param line_number: The line_number of this ScheduleBEfile.  # noqa: E501
        :type: str
        """

        self._line_number = line_number

    @property
    def load_timestamp(self):
        """Gets the load_timestamp of this ScheduleBEfile.  # noqa: E501


        :return: The load_timestamp of this ScheduleBEfile.  # noqa: E501
        :rtype: datetime
        """
        return self._load_timestamp

    @load_timestamp.setter
    def load_timestamp(self, load_timestamp):
        """Sets the load_timestamp of this ScheduleBEfile.


        :param load_timestamp: The load_timestamp of this ScheduleBEfile.  # noqa: E501
        :type: datetime
        """

        self._load_timestamp = load_timestamp

    @property
    def memo_code(self):
        """Gets the memo_code of this ScheduleBEfile.  # noqa: E501


        :return: The memo_code of this ScheduleBEfile.  # noqa: E501
        :rtype: str
        """
        return self._memo_code

    @memo_code.setter
    def memo_code(self, memo_code):
        """Sets the memo_code of this ScheduleBEfile.


        :param memo_code: The memo_code of this ScheduleBEfile.  # noqa: E501
        :type: str
        """

        self._memo_code = memo_code

    @property
    def memo_text(self):
        """Gets the memo_text of this ScheduleBEfile.  # noqa: E501


        :return: The memo_text of this ScheduleBEfile.  # noqa: E501
        :rtype: str
        """
        return self._memo_text

    @memo_text.setter
    def memo_text(self, memo_text):
        """Sets the memo_text of this ScheduleBEfile.


        :param memo_text: The memo_text of this ScheduleBEfile.  # noqa: E501
        :type: str
        """

        self._memo_text = memo_text

    @property
    def payee_name(self):
        """Gets the payee_name of this ScheduleBEfile.  # noqa: E501


        :return: The payee_name of this ScheduleBEfile.  # noqa: E501
        :rtype: str
        """
        return self._payee_name

    @payee_name.setter
    def payee_name(self, payee_name):
        """Sets the payee_name of this ScheduleBEfile.


        :param payee_name: The payee_name of this ScheduleBEfile.  # noqa: E501
        :type: str
        """

        self._payee_name = payee_name

    @property
    def pdf_url(self):
        """Gets the pdf_url of this ScheduleBEfile.  # noqa: E501


        :return: The pdf_url of this ScheduleBEfile.  # noqa: E501
        :rtype: str
        """
        return self._pdf_url

    @pdf_url.setter
    def pdf_url(self, pdf_url):
        """Sets the pdf_url of this ScheduleBEfile.


        :param pdf_url: The pdf_url of this ScheduleBEfile.  # noqa: E501
        :type: str
        """

        self._pdf_url = pdf_url

    @property
    def recipient_city(self):
        """Gets the recipient_city of this ScheduleBEfile.  # noqa: E501


        :return: The recipient_city of this ScheduleBEfile.  # noqa: E501
        :rtype: str
        """
        return self._recipient_city

    @recipient_city.setter
    def recipient_city(self, recipient_city):
        """Sets the recipient_city of this ScheduleBEfile.


        :param recipient_city: The recipient_city of this ScheduleBEfile.  # noqa: E501
        :type: str
        """

        self._recipient_city = recipient_city

    @property
    def recipient_name(self):
        """Gets the recipient_name of this ScheduleBEfile.  # noqa: E501


        :return: The recipient_name of this ScheduleBEfile.  # noqa: E501
        :rtype: str
        """
        return self._recipient_name

    @recipient_name.setter
    def recipient_name(self, recipient_name):
        """Sets the recipient_name of this ScheduleBEfile.


        :param recipient_name: The recipient_name of this ScheduleBEfile.  # noqa: E501
        :type: str
        """

        self._recipient_name = recipient_name

    @property
    def recipient_prefix(self):
        """Gets the recipient_prefix of this ScheduleBEfile.  # noqa: E501


        :return: The recipient_prefix of this ScheduleBEfile.  # noqa: E501
        :rtype: str
        """
        return self._recipient_prefix

    @recipient_prefix.setter
    def recipient_prefix(self, recipient_prefix):
        """Sets the recipient_prefix of this ScheduleBEfile.


        :param recipient_prefix: The recipient_prefix of this ScheduleBEfile.  # noqa: E501
        :type: str
        """

        self._recipient_prefix = recipient_prefix

    @property
    def recipient_state(self):
        """Gets the recipient_state of this ScheduleBEfile.  # noqa: E501


        :return: The recipient_state of this ScheduleBEfile.  # noqa: E501
        :rtype: str
        """
        return self._recipient_state

    @recipient_state.setter
    def recipient_state(self, recipient_state):
        """Sets the recipient_state of this ScheduleBEfile.


        :param recipient_state: The recipient_state of this ScheduleBEfile.  # noqa: E501
        :type: str
        """

        self._recipient_state = recipient_state

    @property
    def recipient_suffix(self):
        """Gets the recipient_suffix of this ScheduleBEfile.  # noqa: E501


        :return: The recipient_suffix of this ScheduleBEfile.  # noqa: E501
        :rtype: str
        """
        return self._recipient_suffix

    @recipient_suffix.setter
    def recipient_suffix(self, recipient_suffix):
        """Sets the recipient_suffix of this ScheduleBEfile.


        :param recipient_suffix: The recipient_suffix of this ScheduleBEfile.  # noqa: E501
        :type: str
        """

        self._recipient_suffix = recipient_suffix

    @property
    def recipient_zip(self):
        """Gets the recipient_zip of this ScheduleBEfile.  # noqa: E501


        :return: The recipient_zip of this ScheduleBEfile.  # noqa: E501
        :rtype: str
        """
        return self._recipient_zip

    @recipient_zip.setter
    def recipient_zip(self, recipient_zip):
        """Sets the recipient_zip of this ScheduleBEfile.


        :param recipient_zip: The recipient_zip of this ScheduleBEfile.  # noqa: E501
        :type: str
        """

        self._recipient_zip = recipient_zip

    @property
    def related_line_number(self):
        """Gets the related_line_number of this ScheduleBEfile.  # noqa: E501


        :return: The related_line_number of this ScheduleBEfile.  # noqa: E501
        :rtype: int
        """
        return self._related_line_number

    @related_line_number.setter
    def related_line_number(self, related_line_number):
        """Sets the related_line_number of this ScheduleBEfile.


        :param related_line_number: The related_line_number of this ScheduleBEfile.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and related_line_number is None:  # noqa: E501
            raise ValueError('Invalid value for `related_line_number`, must not be `None`')  # noqa: E501

        self._related_line_number = related_line_number

    @property
    def report_type(self):
        """Gets the report_type of this ScheduleBEfile.  # noqa: E501


        :return: The report_type of this ScheduleBEfile.  # noqa: E501
        :rtype: str
        """
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        """Sets the report_type of this ScheduleBEfile.


        :param report_type: The report_type of this ScheduleBEfile.  # noqa: E501
        :type: str
        """

        self._report_type = report_type

    @property
    def semi_annual_bundled_refund(self):
        """Gets the semi_annual_bundled_refund of this ScheduleBEfile.  # noqa: E501


        :return: The semi_annual_bundled_refund of this ScheduleBEfile.  # noqa: E501
        :rtype: int
        """
        return self._semi_annual_bundled_refund

    @semi_annual_bundled_refund.setter
    def semi_annual_bundled_refund(self, semi_annual_bundled_refund):
        """Sets the semi_annual_bundled_refund of this ScheduleBEfile.


        :param semi_annual_bundled_refund: The semi_annual_bundled_refund of this ScheduleBEfile.  # noqa: E501
        :type: int
        """

        self._semi_annual_bundled_refund = semi_annual_bundled_refund

    @property
    def transaction_id(self):
        """Gets the transaction_id of this ScheduleBEfile.  # noqa: E501


        :return: The transaction_id of this ScheduleBEfile.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this ScheduleBEfile.


        :param transaction_id: The transaction_id of this ScheduleBEfile.  # noqa: E501
        :type: str
        """

        self._transaction_id = transaction_id

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
        if not isinstance(other, ScheduleBEfile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScheduleBEfile):
            return True

        return self.to_dict() != other.to_dict()
