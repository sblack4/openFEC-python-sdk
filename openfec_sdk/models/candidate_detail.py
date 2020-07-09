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


class CandidateDetail(object):
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
        'active_through': 'int',
        'address_city': 'str',
        'address_state': 'str',
        'address_street_1': 'str',
        'address_street_2': 'str',
        'address_zip': 'str',
        'candidate_id': 'str',
        'candidate_inactive': 'bool',
        'candidate_status': 'str',
        'cycles': 'list[int]',
        'district': 'str',
        'district_number': 'int',
        'election_districts': 'list[str]',
        'election_years': 'list[int]',
        'federal_funds_flag': 'bool',
        'first_file_date': 'date',
        'flags': 'str',
        'has_raised_funds': 'bool',
        'incumbent_challenge': 'str',
        'incumbent_challenge_full': 'str',
        'last_f2_date': 'date',
        'last_file_date': 'date',
        'load_date': 'datetime',
        'name': 'str',
        'office': 'str',
        'office_full': 'str',
        'party': 'str',
        'party_full': 'str',
        'state': 'str'
    }

    attribute_map = {
        'active_through': 'active_through',
        'address_city': 'address_city',
        'address_state': 'address_state',
        'address_street_1': 'address_street_1',
        'address_street_2': 'address_street_2',
        'address_zip': 'address_zip',
        'candidate_id': 'candidate_id',
        'candidate_inactive': 'candidate_inactive',
        'candidate_status': 'candidate_status',
        'cycles': 'cycles',
        'district': 'district',
        'district_number': 'district_number',
        'election_districts': 'election_districts',
        'election_years': 'election_years',
        'federal_funds_flag': 'federal_funds_flag',
        'first_file_date': 'first_file_date',
        'flags': 'flags',
        'has_raised_funds': 'has_raised_funds',
        'incumbent_challenge': 'incumbent_challenge',
        'incumbent_challenge_full': 'incumbent_challenge_full',
        'last_f2_date': 'last_f2_date',
        'last_file_date': 'last_file_date',
        'load_date': 'load_date',
        'name': 'name',
        'office': 'office',
        'office_full': 'office_full',
        'party': 'party',
        'party_full': 'party_full',
        'state': 'state'
    }

    def __init__(self, active_through=None, address_city=None, address_state=None, address_street_1=None, address_street_2=None, address_zip=None, candidate_id=None, candidate_inactive=None, candidate_status=None, cycles=None, district=None, district_number=None, election_districts=None, election_years=None, federal_funds_flag=None, first_file_date=None, flags=None, has_raised_funds=None, incumbent_challenge=None, incumbent_challenge_full=None, last_f2_date=None, last_file_date=None, load_date=None, name=None, office=None, office_full=None, party=None, party_full=None, state=None, local_vars_configuration=None):  # noqa: E501
        """CandidateDetail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._active_through = None
        self._address_city = None
        self._address_state = None
        self._address_street_1 = None
        self._address_street_2 = None
        self._address_zip = None
        self._candidate_id = None
        self._candidate_inactive = None
        self._candidate_status = None
        self._cycles = None
        self._district = None
        self._district_number = None
        self._election_districts = None
        self._election_years = None
        self._federal_funds_flag = None
        self._first_file_date = None
        self._flags = None
        self._has_raised_funds = None
        self._incumbent_challenge = None
        self._incumbent_challenge_full = None
        self._last_f2_date = None
        self._last_file_date = None
        self._load_date = None
        self._name = None
        self._office = None
        self._office_full = None
        self._party = None
        self._party_full = None
        self._state = None
        self.discriminator = None

        self.active_through = active_through
        self.address_city = address_city
        self.address_state = address_state
        self.address_street_1 = address_street_1
        self.address_street_2 = address_street_2
        self.address_zip = address_zip
        self.candidate_id = candidate_id
        self.candidate_inactive = candidate_inactive
        self.candidate_status = candidate_status
        self.cycles = cycles
        self.district = district
        self.district_number = district_number
        self.election_districts = election_districts
        self.election_years = election_years
        if federal_funds_flag is not None:
            self.federal_funds_flag = federal_funds_flag
        self.first_file_date = first_file_date
        self.flags = flags
        if has_raised_funds is not None:
            self.has_raised_funds = has_raised_funds
        self.incumbent_challenge = incumbent_challenge
        self.incumbent_challenge_full = incumbent_challenge_full
        self.last_f2_date = last_f2_date
        self.last_file_date = last_file_date
        self.load_date = load_date
        self.name = name
        self.office = office
        self.office_full = office_full
        self.party = party
        self.party_full = party_full
        self.state = state

    @property
    def active_through(self):
        """Gets the active_through of this CandidateDetail.  # noqa: E501

        Last year a candidate was active. This field is specific to the candidate_id so if the same person runs for another office, there may be a different record for them.  # noqa: E501

        :return: The active_through of this CandidateDetail.  # noqa: E501
        :rtype: int
        """
        return self._active_through

    @active_through.setter
    def active_through(self, active_through):
        """Sets the active_through of this CandidateDetail.

        Last year a candidate was active. This field is specific to the candidate_id so if the same person runs for another office, there may be a different record for them.  # noqa: E501

        :param active_through: The active_through of this CandidateDetail.  # noqa: E501
        :type: int
        """

        self._active_through = active_through

    @property
    def address_city(self):
        """Gets the address_city of this CandidateDetail.  # noqa: E501

        City of candidate's address, as reported on their Form 2.  # noqa: E501

        :return: The address_city of this CandidateDetail.  # noqa: E501
        :rtype: str
        """
        return self._address_city

    @address_city.setter
    def address_city(self, address_city):
        """Sets the address_city of this CandidateDetail.

        City of candidate's address, as reported on their Form 2.  # noqa: E501

        :param address_city: The address_city of this CandidateDetail.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                address_city is not None and len(address_city) > 100):
            raise ValueError('Invalid value for `address_city`, length must be less than or equal to `100`')  # noqa: E501

        self._address_city = address_city

    @property
    def address_state(self):
        """Gets the address_state of this CandidateDetail.  # noqa: E501

        State of candidate's address, as reported on their Form 2.  # noqa: E501

        :return: The address_state of this CandidateDetail.  # noqa: E501
        :rtype: str
        """
        return self._address_state

    @address_state.setter
    def address_state(self, address_state):
        """Sets the address_state of this CandidateDetail.

        State of candidate's address, as reported on their Form 2.  # noqa: E501

        :param address_state: The address_state of this CandidateDetail.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                address_state is not None and len(address_state) > 2):
            raise ValueError('Invalid value for `address_state`, length must be less than or equal to `2`')  # noqa: E501

        self._address_state = address_state

    @property
    def address_street_1(self):
        """Gets the address_street_1 of this CandidateDetail.  # noqa: E501

        Street of candidate's address, as reported on their Form 2.  # noqa: E501

        :return: The address_street_1 of this CandidateDetail.  # noqa: E501
        :rtype: str
        """
        return self._address_street_1

    @address_street_1.setter
    def address_street_1(self, address_street_1):
        """Sets the address_street_1 of this CandidateDetail.

        Street of candidate's address, as reported on their Form 2.  # noqa: E501

        :param address_street_1: The address_street_1 of this CandidateDetail.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                address_street_1 is not None and len(address_street_1) > 200):
            raise ValueError('Invalid value for `address_street_1`, length must be less than or equal to `200`')  # noqa: E501

        self._address_street_1 = address_street_1

    @property
    def address_street_2(self):
        """Gets the address_street_2 of this CandidateDetail.  # noqa: E501

        Additional street information of candidate's address, as reported on their Form 2.  # noqa: E501

        :return: The address_street_2 of this CandidateDetail.  # noqa: E501
        :rtype: str
        """
        return self._address_street_2

    @address_street_2.setter
    def address_street_2(self, address_street_2):
        """Sets the address_street_2 of this CandidateDetail.

        Additional street information of candidate's address, as reported on their Form 2.  # noqa: E501

        :param address_street_2: The address_street_2 of this CandidateDetail.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                address_street_2 is not None and len(address_street_2) > 200):
            raise ValueError('Invalid value for `address_street_2`, length must be less than or equal to `200`')  # noqa: E501

        self._address_street_2 = address_street_2

    @property
    def address_zip(self):
        """Gets the address_zip of this CandidateDetail.  # noqa: E501

        Zip code of candidate's address, as reported on their Form 2.  # noqa: E501

        :return: The address_zip of this CandidateDetail.  # noqa: E501
        :rtype: str
        """
        return self._address_zip

    @address_zip.setter
    def address_zip(self, address_zip):
        """Sets the address_zip of this CandidateDetail.

        Zip code of candidate's address, as reported on their Form 2.  # noqa: E501

        :param address_zip: The address_zip of this CandidateDetail.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                address_zip is not None and len(address_zip) > 10):
            raise ValueError('Invalid value for `address_zip`, length must be less than or equal to `10`')  # noqa: E501

        self._address_zip = address_zip

    @property
    def candidate_id(self):
        """Gets the candidate_id of this CandidateDetail.  # noqa: E501

         A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.   # noqa: E501

        :return: The candidate_id of this CandidateDetail.  # noqa: E501
        :rtype: str
        """
        return self._candidate_id

    @candidate_id.setter
    def candidate_id(self, candidate_id):
        """Sets the candidate_id of this CandidateDetail.

         A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.   # noqa: E501

        :param candidate_id: The candidate_id of this CandidateDetail.  # noqa: E501
        :type: str
        """

        self._candidate_id = candidate_id

    @property
    def candidate_inactive(self):
        """Gets the candidate_inactive of this CandidateDetail.  # noqa: E501

        True indicates that a candidate is inactive.  # noqa: E501

        :return: The candidate_inactive of this CandidateDetail.  # noqa: E501
        :rtype: bool
        """
        return self._candidate_inactive

    @candidate_inactive.setter
    def candidate_inactive(self, candidate_inactive):
        """Sets the candidate_inactive of this CandidateDetail.

        True indicates that a candidate is inactive.  # noqa: E501

        :param candidate_inactive: The candidate_inactive of this CandidateDetail.  # noqa: E501
        :type: bool
        """

        self._candidate_inactive = candidate_inactive

    @property
    def candidate_status(self):
        """Gets the candidate_status of this CandidateDetail.  # noqa: E501

        One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate   # noqa: E501

        :return: The candidate_status of this CandidateDetail.  # noqa: E501
        :rtype: str
        """
        return self._candidate_status

    @candidate_status.setter
    def candidate_status(self, candidate_status):
        """Sets the candidate_status of this CandidateDetail.

        One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate   # noqa: E501

        :param candidate_status: The candidate_status of this CandidateDetail.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                candidate_status is not None and len(candidate_status) > 1):
            raise ValueError('Invalid value for `candidate_status`, length must be less than or equal to `1`')  # noqa: E501

        self._candidate_status = candidate_status

    @property
    def cycles(self):
        """Gets the cycles of this CandidateDetail.  # noqa: E501

         Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.   # noqa: E501

        :return: The cycles of this CandidateDetail.  # noqa: E501
        :rtype: list[int]
        """
        return self._cycles

    @cycles.setter
    def cycles(self, cycles):
        """Sets the cycles of this CandidateDetail.

         Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.   # noqa: E501

        :param cycles: The cycles of this CandidateDetail.  # noqa: E501
        :type: list[int]
        """

        self._cycles = cycles

    @property
    def district(self):
        """Gets the district of this CandidateDetail.  # noqa: E501

        Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.  # noqa: E501

        :return: The district of this CandidateDetail.  # noqa: E501
        :rtype: str
        """
        return self._district

    @district.setter
    def district(self, district):
        """Sets the district of this CandidateDetail.

        Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.  # noqa: E501

        :param district: The district of this CandidateDetail.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                district is not None and len(district) > 2):
            raise ValueError('Invalid value for `district`, length must be less than or equal to `2`')  # noqa: E501

        self._district = district

    @property
    def district_number(self):
        """Gets the district_number of this CandidateDetail.  # noqa: E501

        One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate   # noqa: E501

        :return: The district_number of this CandidateDetail.  # noqa: E501
        :rtype: int
        """
        return self._district_number

    @district_number.setter
    def district_number(self, district_number):
        """Sets the district_number of this CandidateDetail.

        One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate   # noqa: E501

        :param district_number: The district_number of this CandidateDetail.  # noqa: E501
        :type: int
        """

        self._district_number = district_number

    @property
    def election_districts(self):
        """Gets the election_districts of this CandidateDetail.  # noqa: E501

        Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.  # noqa: E501

        :return: The election_districts of this CandidateDetail.  # noqa: E501
        :rtype: list[str]
        """
        return self._election_districts

    @election_districts.setter
    def election_districts(self, election_districts):
        """Sets the election_districts of this CandidateDetail.

        Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.  # noqa: E501

        :param election_districts: The election_districts of this CandidateDetail.  # noqa: E501
        :type: list[str]
        """

        self._election_districts = election_districts

    @property
    def election_years(self):
        """Gets the election_years of this CandidateDetail.  # noqa: E501

        Years in which a candidate ran for office.  # noqa: E501

        :return: The election_years of this CandidateDetail.  # noqa: E501
        :rtype: list[int]
        """
        return self._election_years

    @election_years.setter
    def election_years(self, election_years):
        """Sets the election_years of this CandidateDetail.

        Years in which a candidate ran for office.  # noqa: E501

        :param election_years: The election_years of this CandidateDetail.  # noqa: E501
        :type: list[int]
        """

        self._election_years = election_years

    @property
    def federal_funds_flag(self):
        """Gets the federal_funds_flag of this CandidateDetail.  # noqa: E501


        :return: The federal_funds_flag of this CandidateDetail.  # noqa: E501
        :rtype: bool
        """
        return self._federal_funds_flag

    @federal_funds_flag.setter
    def federal_funds_flag(self, federal_funds_flag):
        """Sets the federal_funds_flag of this CandidateDetail.


        :param federal_funds_flag: The federal_funds_flag of this CandidateDetail.  # noqa: E501
        :type: bool
        """

        self._federal_funds_flag = federal_funds_flag

    @property
    def first_file_date(self):
        """Gets the first_file_date of this CandidateDetail.  # noqa: E501

        The day the FEC received the candidate's first filing. This is a F2 candidate registration.  # noqa: E501

        :return: The first_file_date of this CandidateDetail.  # noqa: E501
        :rtype: date
        """
        return self._first_file_date

    @first_file_date.setter
    def first_file_date(self, first_file_date):
        """Sets the first_file_date of this CandidateDetail.

        The day the FEC received the candidate's first filing. This is a F2 candidate registration.  # noqa: E501

        :param first_file_date: The first_file_date of this CandidateDetail.  # noqa: E501
        :type: date
        """

        self._first_file_date = first_file_date

    @property
    def flags(self):
        """Gets the flags of this CandidateDetail.  # noqa: E501


        :return: The flags of this CandidateDetail.  # noqa: E501
        :rtype: str
        """
        return self._flags

    @flags.setter
    def flags(self, flags):
        """Sets the flags of this CandidateDetail.


        :param flags: The flags of this CandidateDetail.  # noqa: E501
        :type: str
        """

        self._flags = flags

    @property
    def has_raised_funds(self):
        """Gets the has_raised_funds of this CandidateDetail.  # noqa: E501


        :return: The has_raised_funds of this CandidateDetail.  # noqa: E501
        :rtype: bool
        """
        return self._has_raised_funds

    @has_raised_funds.setter
    def has_raised_funds(self, has_raised_funds):
        """Sets the has_raised_funds of this CandidateDetail.


        :param has_raised_funds: The has_raised_funds of this CandidateDetail.  # noqa: E501
        :type: bool
        """

        self._has_raised_funds = has_raised_funds

    @property
    def incumbent_challenge(self):
        """Gets the incumbent_challenge of this CandidateDetail.  # noqa: E501

        One-letter code ('I', 'C', 'O') explaining if the candidate is an incumbent, a challenger, or if the seat is open.  # noqa: E501

        :return: The incumbent_challenge of this CandidateDetail.  # noqa: E501
        :rtype: str
        """
        return self._incumbent_challenge

    @incumbent_challenge.setter
    def incumbent_challenge(self, incumbent_challenge):
        """Sets the incumbent_challenge of this CandidateDetail.

        One-letter code ('I', 'C', 'O') explaining if the candidate is an incumbent, a challenger, or if the seat is open.  # noqa: E501

        :param incumbent_challenge: The incumbent_challenge of this CandidateDetail.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                incumbent_challenge is not None and len(incumbent_challenge) > 1):
            raise ValueError('Invalid value for `incumbent_challenge`, length must be less than or equal to `1`')  # noqa: E501

        self._incumbent_challenge = incumbent_challenge

    @property
    def incumbent_challenge_full(self):
        """Gets the incumbent_challenge_full of this CandidateDetail.  # noqa: E501

        Explains if the candidate is an incumbent, a challenger, or if the seat is open.  # noqa: E501

        :return: The incumbent_challenge_full of this CandidateDetail.  # noqa: E501
        :rtype: str
        """
        return self._incumbent_challenge_full

    @incumbent_challenge_full.setter
    def incumbent_challenge_full(self, incumbent_challenge_full):
        """Sets the incumbent_challenge_full of this CandidateDetail.

        Explains if the candidate is an incumbent, a challenger, or if the seat is open.  # noqa: E501

        :param incumbent_challenge_full: The incumbent_challenge_full of this CandidateDetail.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                incumbent_challenge_full is not None and len(incumbent_challenge_full) > 10):
            raise ValueError('Invalid value for `incumbent_challenge_full`, length must be less than or equal to `10`')  # noqa: E501

        self._incumbent_challenge_full = incumbent_challenge_full

    @property
    def last_f2_date(self):
        """Gets the last_f2_date of this CandidateDetail.  # noqa: E501

        The day the FEC received the candidate's most recent Form 2  # noqa: E501

        :return: The last_f2_date of this CandidateDetail.  # noqa: E501
        :rtype: date
        """
        return self._last_f2_date

    @last_f2_date.setter
    def last_f2_date(self, last_f2_date):
        """Sets the last_f2_date of this CandidateDetail.

        The day the FEC received the candidate's most recent Form 2  # noqa: E501

        :param last_f2_date: The last_f2_date of this CandidateDetail.  # noqa: E501
        :type: date
        """

        self._last_f2_date = last_f2_date

    @property
    def last_file_date(self):
        """Gets the last_file_date of this CandidateDetail.  # noqa: E501

        The day the FEC received the candidate's most recent filing  # noqa: E501

        :return: The last_file_date of this CandidateDetail.  # noqa: E501
        :rtype: date
        """
        return self._last_file_date

    @last_file_date.setter
    def last_file_date(self, last_file_date):
        """Sets the last_file_date of this CandidateDetail.

        The day the FEC received the candidate's most recent filing  # noqa: E501

        :param last_file_date: The last_file_date of this CandidateDetail.  # noqa: E501
        :type: date
        """

        self._last_file_date = last_file_date

    @property
    def load_date(self):
        """Gets the load_date of this CandidateDetail.  # noqa: E501

        Date the information was loaded into the FEC systems. This can be affected by reseting systems and other factors, refer to receipt_date for the day that the FEC received the paper or electronic document. Keep in mind that paper filings take more time to process and there can be a lag between load_date and receipt_date. This field can be helpful to identify paper records that have been processed recently.  # noqa: E501

        :return: The load_date of this CandidateDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._load_date

    @load_date.setter
    def load_date(self, load_date):
        """Sets the load_date of this CandidateDetail.

        Date the information was loaded into the FEC systems. This can be affected by reseting systems and other factors, refer to receipt_date for the day that the FEC received the paper or electronic document. Keep in mind that paper filings take more time to process and there can be a lag between load_date and receipt_date. This field can be helpful to identify paper records that have been processed recently.  # noqa: E501

        :param load_date: The load_date of this CandidateDetail.  # noqa: E501
        :type: datetime
        """

        self._load_date = load_date

    @property
    def name(self):
        """Gets the name of this CandidateDetail.  # noqa: E501

        Name of candidate running for office  # noqa: E501

        :return: The name of this CandidateDetail.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CandidateDetail.

        Name of candidate running for office  # noqa: E501

        :param name: The name of this CandidateDetail.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 100):
            raise ValueError('Invalid value for `name`, length must be less than or equal to `100`')  # noqa: E501

        self._name = name

    @property
    def office(self):
        """Gets the office of this CandidateDetail.  # noqa: E501

        Federal office candidate runs for: H, S or P  # noqa: E501

        :return: The office of this CandidateDetail.  # noqa: E501
        :rtype: str
        """
        return self._office

    @office.setter
    def office(self, office):
        """Sets the office of this CandidateDetail.

        Federal office candidate runs for: H, S or P  # noqa: E501

        :param office: The office of this CandidateDetail.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                office is not None and len(office) > 1):
            raise ValueError('Invalid value for `office`, length must be less than or equal to `1`')  # noqa: E501

        self._office = office

    @property
    def office_full(self):
        """Gets the office_full of this CandidateDetail.  # noqa: E501

        Federal office candidate runs for: House, Senate or presidential  # noqa: E501

        :return: The office_full of this CandidateDetail.  # noqa: E501
        :rtype: str
        """
        return self._office_full

    @office_full.setter
    def office_full(self, office_full):
        """Sets the office_full of this CandidateDetail.

        Federal office candidate runs for: House, Senate or presidential  # noqa: E501

        :param office_full: The office_full of this CandidateDetail.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                office_full is not None and len(office_full) > 9):
            raise ValueError('Invalid value for `office_full`, length must be less than or equal to `9`')  # noqa: E501

        self._office_full = office_full

    @property
    def party(self):
        """Gets the party of this CandidateDetail.  # noqa: E501

        Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.  # noqa: E501

        :return: The party of this CandidateDetail.  # noqa: E501
        :rtype: str
        """
        return self._party

    @party.setter
    def party(self, party):
        """Sets the party of this CandidateDetail.

        Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.  # noqa: E501

        :param party: The party of this CandidateDetail.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                party is not None and len(party) > 3):
            raise ValueError('Invalid value for `party`, length must be less than or equal to `3`')  # noqa: E501

        self._party = party

    @property
    def party_full(self):
        """Gets the party_full of this CandidateDetail.  # noqa: E501

        Party affiliated with a candidate or committee  # noqa: E501

        :return: The party_full of this CandidateDetail.  # noqa: E501
        :rtype: str
        """
        return self._party_full

    @party_full.setter
    def party_full(self, party_full):
        """Sets the party_full of this CandidateDetail.

        Party affiliated with a candidate or committee  # noqa: E501

        :param party_full: The party_full of this CandidateDetail.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                party_full is not None and len(party_full) > 255):
            raise ValueError('Invalid value for `party_full`, length must be less than or equal to `255`')  # noqa: E501

        self._party_full = party_full

    @property
    def state(self):
        """Gets the state of this CandidateDetail.  # noqa: E501

        US state or territory where a candidate runs for office  # noqa: E501

        :return: The state of this CandidateDetail.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CandidateDetail.

        US state or territory where a candidate runs for office  # noqa: E501

        :param state: The state of this CandidateDetail.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                state is not None and len(state) > 2):
            raise ValueError('Invalid value for `state`, length must be less than or equal to `2`')  # noqa: E501

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
        if not isinstance(other, CandidateDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CandidateDetail):
            return True

        return self.to_dict() != other.to_dict()
