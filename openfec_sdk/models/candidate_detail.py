# coding: utf-8

"""
    OpenFEC

    This API allows you to explore the way candidates and committees fund their campaigns.    The FEC API is a RESTful web service supporting full-text and field-specific searches on FEC data. [Bulk downloads](https://www.fec.gov/data/advanced/?tab=bulk-data) are available on the current site. Information is tied to the underlying forms by file ID and image ID. Data is updated nightly.    There is a lot of data, but a good place to start is to use search to find interesting candidates and committees. Then, you can use their IDs to find report or line item details with the other endpoints. If you are interested in individual donors, check out contributor information in schedule_a.    Get an [API key here](https://api.data.gov/signup/). That will enable you to place up to 1,000 calls an hour. Each call is limited to 100 results per page. You can email questions, comments or a request to get a key for 120 calls per minute to [APIinfo@fec.gov](mailto:apiinfo@fec.gov). You can also ask questions and discuss the data in the [FEC data Google Group](https://groups.google.com/forum/#!forum/fec-data). API changes will also be added to this group in advance of the change.    The model definitions and schema are available at [/swagger](/swagger/). This is useful for making wrappers and exploring the data.    A few restrictions limit the way you can use FEC data. For example, you can’t use contributor lists for commercial purposes or to solicit donations. [Learn more here](https://www.fec.gov/updates/sale-or-use-contributor-information/).    [View our source code](https://github.com/fecgov/openFEC). We welcome issues and pull requests!  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import
import re  # noqa: F401
import sys  # noqa: F401

import six  # noqa: F401
import nulltype  # noqa: F401

from openfec_sdk.model_utils import (  # noqa: F401
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    int,
    none_type,
    str,
    validate_get_composed_info,
)


class CandidateDetail(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('address_city',): {
            'max_length': 100,
        },
        ('address_state',): {
            'max_length': 2,
        },
        ('address_street_1',): {
            'max_length': 200,
        },
        ('address_street_2',): {
            'max_length': 200,
        },
        ('address_zip',): {
            'max_length': 10,
        },
        ('candidate_status',): {
            'max_length': 1,
        },
        ('district',): {
            'max_length': 2,
        },
        ('incumbent_challenge',): {
            'max_length': 1,
        },
        ('incumbent_challenge_full',): {
            'max_length': 10,
        },
        ('name',): {
            'max_length': 100,
        },
        ('office',): {
            'max_length': 1,
        },
        ('office_full',): {
            'max_length': 9,
        },
        ('party',): {
            'max_length': 3,
        },
        ('party_full',): {
            'max_length': 255,
        },
        ('state',): {
            'max_length': 2,
        },
    }

    additional_properties_type = None

    @cached_property
    def openapi_types():
        """
        This must be a class method so a model may have properties that are
        of type self, this ensures that we don't create a cyclic import

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'active_through': (int, none_type,),  # noqa: E501
            'address_city': (str, none_type,),  # noqa: E501
            'address_state': (str, none_type,),  # noqa: E501
            'address_street_1': (str, none_type,),  # noqa: E501
            'address_street_2': (str, none_type,),  # noqa: E501
            'address_zip': (str, none_type,),  # noqa: E501
            'candidate_id': (str, none_type,),  # noqa: E501
            'candidate_inactive': (bool, none_type,),  # noqa: E501
            'candidate_status': (str, none_type,),  # noqa: E501
            'cycles': ([int], none_type,),  # noqa: E501
            'district': (str, none_type,),  # noqa: E501
            'district_number': (int, none_type,),  # noqa: E501
            'election_districts': ([str], none_type,),  # noqa: E501
            'election_years': ([int], none_type,),  # noqa: E501
            'federal_funds_flag': (bool,),  # noqa: E501
            'first_file_date': (date, none_type,),  # noqa: E501
            'flags': (str, none_type,),  # noqa: E501
            'has_raised_funds': (bool,),  # noqa: E501
            'incumbent_challenge': (str, none_type,),  # noqa: E501
            'incumbent_challenge_full': (str, none_type,),  # noqa: E501
            'last_f2_date': (date, none_type,),  # noqa: E501
            'last_file_date': (date, none_type,),  # noqa: E501
            'load_date': (datetime, none_type,),  # noqa: E501
            'name': (str, none_type,),  # noqa: E501
            'office': (str, none_type,),  # noqa: E501
            'office_full': (str, none_type,),  # noqa: E501
            'party': (str, none_type,),  # noqa: E501
            'party_full': (str, none_type,),  # noqa: E501
            'state': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        'active_through': 'active_through',  # noqa: E501
        'address_city': 'address_city',  # noqa: E501
        'address_state': 'address_state',  # noqa: E501
        'address_street_1': 'address_street_1',  # noqa: E501
        'address_street_2': 'address_street_2',  # noqa: E501
        'address_zip': 'address_zip',  # noqa: E501
        'candidate_id': 'candidate_id',  # noqa: E501
        'candidate_inactive': 'candidate_inactive',  # noqa: E501
        'candidate_status': 'candidate_status',  # noqa: E501
        'cycles': 'cycles',  # noqa: E501
        'district': 'district',  # noqa: E501
        'district_number': 'district_number',  # noqa: E501
        'election_districts': 'election_districts',  # noqa: E501
        'election_years': 'election_years',  # noqa: E501
        'federal_funds_flag': 'federal_funds_flag',  # noqa: E501
        'first_file_date': 'first_file_date',  # noqa: E501
        'flags': 'flags',  # noqa: E501
        'has_raised_funds': 'has_raised_funds',  # noqa: E501
        'incumbent_challenge': 'incumbent_challenge',  # noqa: E501
        'incumbent_challenge_full': 'incumbent_challenge_full',  # noqa: E501
        'last_f2_date': 'last_f2_date',  # noqa: E501
        'last_file_date': 'last_file_date',  # noqa: E501
        'load_date': 'load_date',  # noqa: E501
        'name': 'name',  # noqa: E501
        'office': 'office',  # noqa: E501
        'office_full': 'office_full',  # noqa: E501
        'party': 'party',  # noqa: E501
        'party_full': 'party_full',  # noqa: E501
        'state': 'state',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_from_server',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, _check_type=True, _from_server=False, _path_to_item=(), _configuration=None, _visited_composed_classes=(), **kwargs):  # noqa: E501
        """candidate_detail.CandidateDetail - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _from_server (bool): True if the data is from the server
                                False if the data is from the client (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            active_through (int, none_type): Last year a candidate was active. This field is specific to the candidate_id so if the same person runs for another office, there may be a different record for them.. [optional]  # noqa: E501
            address_city (str, none_type): City of candidate&#39;s address, as reported on their Form 2.. [optional]  # noqa: E501
            address_state (str, none_type): State of candidate&#39;s address, as reported on their Form 2.. [optional]  # noqa: E501
            address_street_1 (str, none_type): Street of candidate&#39;s address, as reported on their Form 2.. [optional]  # noqa: E501
            address_street_2 (str, none_type): Additional street information of candidate&#39;s address, as reported on their Form 2.. [optional]  # noqa: E501
            address_zip (str, none_type): Zip code of candidate&#39;s address, as reported on their Form 2.. [optional]  # noqa: E501
            candidate_id (str, none_type):  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. . [optional]  # noqa: E501
            candidate_inactive (bool, none_type): True indicates that a candidate is inactive.. [optional]  # noqa: E501
            candidate_status (str, none_type): One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate . [optional]  # noqa: E501
            cycles ([int], none_type):  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag. . [optional]  # noqa: E501
            district (str, none_type): Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.. [optional]  # noqa: E501
            district_number (int, none_type): One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate . [optional]  # noqa: E501
            election_districts ([str], none_type): Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00.. [optional]  # noqa: E501
            election_years ([int], none_type): Years in which a candidate ran for office.. [optional]  # noqa: E501
            federal_funds_flag (bool): [optional]  # noqa: E501
            first_file_date (date, none_type): The day the FEC received the candidate&#39;s first filing. This is a F2 candidate registration.. [optional]  # noqa: E501
            flags (str, none_type): [optional]  # noqa: E501
            has_raised_funds (bool): [optional]  # noqa: E501
            incumbent_challenge (str, none_type): One-letter code (&#39;I&#39;, &#39;C&#39;, &#39;O&#39;) explaining if the candidate is an incumbent, a challenger, or if the seat is open.. [optional]  # noqa: E501
            incumbent_challenge_full (str, none_type): Explains if the candidate is an incumbent, a challenger, or if the seat is open.. [optional]  # noqa: E501
            last_f2_date (date, none_type): The day the FEC received the candidate&#39;s most recent Form 2. [optional]  # noqa: E501
            last_file_date (date, none_type): The day the FEC received the candidate&#39;s most recent filing. [optional]  # noqa: E501
            load_date (datetime, none_type): Date the information was loaded into the FEC systems. This can be affected by reseting systems and other factors, refer to receipt_date for the day that the FEC received the paper or electronic document. Keep in mind that paper filings take more time to process and there can be a lag between load_date and receipt_date. This field can be helpful to identify paper records that have been processed recently.. [optional]  # noqa: E501
            name (str, none_type): Name of candidate running for office. [optional]  # noqa: E501
            office (str, none_type): Federal office candidate runs for: H, S or P. [optional]  # noqa: E501
            office_full (str, none_type): Federal office candidate runs for: House, Senate or presidential. [optional]  # noqa: E501
            party (str, none_type): Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.. [optional]  # noqa: E501
            party_full (str, none_type): Party affiliated with a candidate or committee. [optional]  # noqa: E501
            state (str, none_type): US state or territory where a candidate runs for office. [optional]  # noqa: E501
        """

        self._data_store = {}
        self._check_type = _check_type
        self._from_server = _from_server
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in six.iteritems(kwargs):
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
