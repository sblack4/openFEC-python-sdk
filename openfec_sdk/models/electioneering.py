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


class Electioneering(ModelNormal):
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
            'amendment_indicator': (str, none_type,),  # noqa: E501
            'beginning_image_number': (str, none_type,),  # noqa: E501
            'calculated_candidate_share': (float, none_type,),  # noqa: E501
            'candidate_district': (str, none_type,),  # noqa: E501
            'candidate_id': (str, none_type,),  # noqa: E501
            'candidate_name': (str, none_type,),  # noqa: E501
            'candidate_office': (str, none_type,),  # noqa: E501
            'candidate_state': (str, none_type,),  # noqa: E501
            'committee_id': (str, none_type,),  # noqa: E501
            'committee_name': (str, none_type,),  # noqa: E501
            'communication_date': (date, none_type,),  # noqa: E501
            'disbursement_amount': (float, none_type,),  # noqa: E501
            'disbursement_date': (date, none_type,),  # noqa: E501
            'election_type': (str,),  # noqa: E501
            'file_number': (int, none_type,),  # noqa: E501
            'link_id': (int, none_type,),  # noqa: E501
            'number_of_candidates': (float, none_type,),  # noqa: E501
            'payee_name': (str, none_type,),  # noqa: E501
            'payee_state': (str, none_type,),  # noqa: E501
            'pdf_url': (str, none_type,),  # noqa: E501
            'public_distribution_date': (date, none_type,),  # noqa: E501
            'purpose_description': (str, none_type,),  # noqa: E501
            'receipt_date': (date, none_type,),  # noqa: E501
            'report_year': (int, none_type,),  # noqa: E501
            'sb_image_num': (str, none_type,),  # noqa: E501
            'sb_link_id': (str, none_type,),  # noqa: E501
            'sub_id': (int, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        'amendment_indicator': 'amendment_indicator',  # noqa: E501
        'beginning_image_number': 'beginning_image_number',  # noqa: E501
        'calculated_candidate_share': 'calculated_candidate_share',  # noqa: E501
        'candidate_district': 'candidate_district',  # noqa: E501
        'candidate_id': 'candidate_id',  # noqa: E501
        'candidate_name': 'candidate_name',  # noqa: E501
        'candidate_office': 'candidate_office',  # noqa: E501
        'candidate_state': 'candidate_state',  # noqa: E501
        'committee_id': 'committee_id',  # noqa: E501
        'committee_name': 'committee_name',  # noqa: E501
        'communication_date': 'communication_date',  # noqa: E501
        'disbursement_amount': 'disbursement_amount',  # noqa: E501
        'disbursement_date': 'disbursement_date',  # noqa: E501
        'election_type': 'election_type',  # noqa: E501
        'file_number': 'file_number',  # noqa: E501
        'link_id': 'link_id',  # noqa: E501
        'number_of_candidates': 'number_of_candidates',  # noqa: E501
        'payee_name': 'payee_name',  # noqa: E501
        'payee_state': 'payee_state',  # noqa: E501
        'pdf_url': 'pdf_url',  # noqa: E501
        'public_distribution_date': 'public_distribution_date',  # noqa: E501
        'purpose_description': 'purpose_description',  # noqa: E501
        'receipt_date': 'receipt_date',  # noqa: E501
        'report_year': 'report_year',  # noqa: E501
        'sb_image_num': 'sb_image_num',  # noqa: E501
        'sb_link_id': 'sb_link_id',  # noqa: E501
        'sub_id': 'sub_id',  # noqa: E501
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
        """electioneering.Electioneering - a model defined in OpenAPI

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
            amendment_indicator (str, none_type): [optional]  # noqa: E501
            beginning_image_number (str, none_type): [optional]  # noqa: E501
            calculated_candidate_share (float, none_type):  \&quot;If an electioneering cost targets several candidates, the total cost is divided by the number of candidates. If it only mentions one candidate the full cost of the communication is listed.\&quot; . [optional]  # noqa: E501
            candidate_district (str, none_type): [optional]  # noqa: E501
            candidate_id (str, none_type): [optional]  # noqa: E501
            candidate_name (str, none_type): [optional]  # noqa: E501
            candidate_office (str, none_type): [optional]  # noqa: E501
            candidate_state (str, none_type): [optional]  # noqa: E501
            committee_id (str, none_type): [optional]  # noqa: E501
            committee_name (str, none_type): [optional]  # noqa: E501
            communication_date (date, none_type):  It is the airing, broadcast, cablecast or other dissemination of the communication. . [optional]  # noqa: E501
            disbursement_amount (float, none_type): [optional]  # noqa: E501
            disbursement_date (date, none_type):  Disbursement date includes actual disbursements and execution of contracts creating an obligation to make disbursements (SB date of disbursement). . [optional]  # noqa: E501
            election_type (str): [optional]  # noqa: E501
            file_number (int, none_type): [optional]  # noqa: E501
            link_id (int, none_type): [optional]  # noqa: E501
            number_of_candidates (float, none_type): [optional]  # noqa: E501
            payee_name (str, none_type):  Name of the entity that received the payment. . [optional]  # noqa: E501
            payee_state (str, none_type): [optional]  # noqa: E501
            pdf_url (str, none_type): [optional]  # noqa: E501
            public_distribution_date (date, none_type):  The pubic distribution date is the date that triggers disclosure of the electioneering communication (date reported on page 1 of Form 9). . [optional]  # noqa: E501
            purpose_description (str, none_type): [optional]  # noqa: E501
            receipt_date (date, none_type): [optional]  # noqa: E501
            report_year (int, none_type): [optional]  # noqa: E501
            sb_image_num (str, none_type): [optional]  # noqa: E501
            sb_link_id (str, none_type): [optional]  # noqa: E501
            sub_id (int, none_type):  The identifier for each electioneering record. . [optional]  # noqa: E501
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
