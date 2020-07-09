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


class CommitteeHistory(ModelNormal):
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
        ('affiliated_committee_name',): {
            'max_length': 100,
        },
        ('city',): {
            'max_length': 50,
        },
        ('committee_type',): {
            'max_length': 1,
        },
        ('committee_type_full',): {
            'max_length': 50,
        },
        ('designation',): {
            'max_length': 1,
        },
        ('designation_full',): {
            'max_length': 25,
        },
        ('filing_frequency',): {
            'max_length': 1,
        },
        ('name',): {
            'max_length': 100,
        },
        ('organization_type',): {
            'max_length': 1,
        },
        ('organization_type_full',): {
            'max_length': 100,
        },
        ('party',): {
            'max_length': 3,
        },
        ('party_full',): {
            'max_length': 50,
        },
        ('state',): {
            'max_length': 2,
        },
        ('state_full',): {
            'max_length': 50,
        },
        ('street_1',): {
            'max_length': 50,
        },
        ('street_2',): {
            'max_length': 50,
        },
        ('treasurer_name',): {
            'max_length': 100,
        },
        ('zip',): {
            'max_length': 9,
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
            'committee_id': (str,),  # noqa: E501
            'cycle': (int,),  # noqa: E501
            'affiliated_committee_name': (str, none_type,),  # noqa: E501
            'candidate_ids': ([str], none_type,),  # noqa: E501
            'city': (str, none_type,),  # noqa: E501
            'committee_type': (str, none_type,),  # noqa: E501
            'committee_type_full': (str, none_type,),  # noqa: E501
            'cycles': ([int], none_type,),  # noqa: E501
            'cycles_has_activity': ([int], none_type,),  # noqa: E501
            'cycles_has_financial': ([int], none_type,),  # noqa: E501
            'designation': (str, none_type,),  # noqa: E501
            'designation_full': (str, none_type,),  # noqa: E501
            'filing_frequency': (str, none_type,),  # noqa: E501
            'is_active': (bool, none_type,),  # noqa: E501
            'last_cycle_has_activity': (int, none_type,),  # noqa: E501
            'last_cycle_has_financial': (int, none_type,),  # noqa: E501
            'name': (str, none_type,),  # noqa: E501
            'organization_type': (str, none_type,),  # noqa: E501
            'organization_type_full': (str, none_type,),  # noqa: E501
            'party': (str, none_type,),  # noqa: E501
            'party_full': (str, none_type,),  # noqa: E501
            'state': (str, none_type,),  # noqa: E501
            'state_full': (str, none_type,),  # noqa: E501
            'street_1': (str, none_type,),  # noqa: E501
            'street_2': (str, none_type,),  # noqa: E501
            'treasurer_name': (str, none_type,),  # noqa: E501
            'zip': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        'committee_id': 'committee_id',  # noqa: E501
        'cycle': 'cycle',  # noqa: E501
        'affiliated_committee_name': 'affiliated_committee_name',  # noqa: E501
        'candidate_ids': 'candidate_ids',  # noqa: E501
        'city': 'city',  # noqa: E501
        'committee_type': 'committee_type',  # noqa: E501
        'committee_type_full': 'committee_type_full',  # noqa: E501
        'cycles': 'cycles',  # noqa: E501
        'cycles_has_activity': 'cycles_has_activity',  # noqa: E501
        'cycles_has_financial': 'cycles_has_financial',  # noqa: E501
        'designation': 'designation',  # noqa: E501
        'designation_full': 'designation_full',  # noqa: E501
        'filing_frequency': 'filing_frequency',  # noqa: E501
        'is_active': 'is_active',  # noqa: E501
        'last_cycle_has_activity': 'last_cycle_has_activity',  # noqa: E501
        'last_cycle_has_financial': 'last_cycle_has_financial',  # noqa: E501
        'name': 'name',  # noqa: E501
        'organization_type': 'organization_type',  # noqa: E501
        'organization_type_full': 'organization_type_full',  # noqa: E501
        'party': 'party',  # noqa: E501
        'party_full': 'party_full',  # noqa: E501
        'state': 'state',  # noqa: E501
        'state_full': 'state_full',  # noqa: E501
        'street_1': 'street_1',  # noqa: E501
        'street_2': 'street_2',  # noqa: E501
        'treasurer_name': 'treasurer_name',  # noqa: E501
        'zip': 'zip',  # noqa: E501
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
    def __init__(self, committee_id, cycle, _check_type=True, _from_server=False, _path_to_item=(), _configuration=None, _visited_composed_classes=(), **kwargs):  # noqa: E501
        """committee_history.CommitteeHistory - a model defined in OpenAPI

        Args:
            committee_id (str):  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.
            cycle (int):  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.

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
            affiliated_committee_name (str, none_type):  Affiliated committee or connected organization . [optional]  # noqa: E501
            candidate_ids ([str], none_type):  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. . [optional]  # noqa: E501
            city (str, none_type):  City of committee as reported on the Form 1 . [optional]  # noqa: E501
            committee_type (str, none_type): The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account . [optional]  # noqa: E501
            committee_type_full (str, none_type): The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account . [optional]  # noqa: E501
            cycles ([int], none_type):  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year. . [optional]  # noqa: E501
            cycles_has_activity ([int], none_type):  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1), and the committee has filling activity during the cycle . [optional]  # noqa: E501
            cycles_has_financial ([int], none_type):  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s), and the commitee files the financial reports (&#39;F3&#39;, &#39;F3X&#39;, &#39;F3P&#39;, &#39;F3L&#39;, &#39;F4&#39;, &#39;F5&#39;, &#39;F7&#39;, &#39;F13&#39;) during this cycle. . [optional]  # noqa: E501
            designation (str, none_type): The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC . [optional]  # noqa: E501
            designation_full (str, none_type): The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC . [optional]  # noqa: E501
            filing_frequency (str, none_type): The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived . [optional]  # noqa: E501
            is_active (bool, none_type):  True indicates that a committee is active. . [optional]  # noqa: E501
            last_cycle_has_activity (int, none_type):  The latest two year election cycle that the committee has filings . [optional]  # noqa: E501
            last_cycle_has_financial (int, none_type):  The latest two year election cycle that the committee files the financial reports (&#39;F3&#39;, &#39;F3X&#39;, &#39;F3P&#39;, &#39;F3L&#39;, &#39;F4&#39;, &#39;F5&#39;, &#39;F7&#39;, &#39;F13&#39;). . [optional]  # noqa: E501
            name (str, none_type): The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records.. [optional]  # noqa: E501
            organization_type (str, none_type): The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock . [optional]  # noqa: E501
            organization_type_full (str, none_type): The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock . [optional]  # noqa: E501
            party (str, none_type): Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.. [optional]  # noqa: E501
            party_full (str, none_type): Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party.. [optional]  # noqa: E501
            state (str, none_type):  State of the committee&#39;s address as filed on the Form 1 . [optional]  # noqa: E501
            state_full (str, none_type):  State of committee as reported on the Form 1 . [optional]  # noqa: E501
            street_1 (str, none_type):  Street address of committee as reported on the Form 1 . [optional]  # noqa: E501
            street_2 (str, none_type):  Second line of street address of committee as reported on the Form 1 . [optional]  # noqa: E501
            treasurer_name (str, none_type): Name of the Committee&#39;s treasurer. If multiple treasurers for the committee, the most recent treasurer will be shown.. [optional]  # noqa: E501
            zip (str, none_type):  Zip code of committee as reported on the Form 1 . [optional]  # noqa: E501
        """

        self._data_store = {}
        self._check_type = _check_type
        self._from_server = _from_server
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.committee_id = committee_id
        self.cycle = cycle
        for var_name, var_value in six.iteritems(kwargs):
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
