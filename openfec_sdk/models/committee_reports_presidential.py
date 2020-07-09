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


class CommitteeReportsPresidential(ModelNormal):
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
            'amendment_chain': ([float], none_type,),  # noqa: E501
            'amendment_indicator': (str, none_type,),  # noqa: E501
            'amendment_indicator_full': (str, none_type,),  # noqa: E501
            'beginning_image_number': (str,),  # noqa: E501
            'candidate_contribution_period': (float, none_type,),  # noqa: E501
            'candidate_contribution_ytd': (float, none_type,),  # noqa: E501
            'cash_on_hand_beginning_period': (float, none_type,),  # noqa: E501
            'cash_on_hand_end_period': (float, none_type,),  # noqa: E501
            'committee_id': (str, none_type,),  # noqa: E501
            'committee_name': (str, none_type,),  # noqa: E501
            'committee_type': (str,),  # noqa: E501
            'coverage_end_date': (datetime, none_type,),  # noqa: E501
            'coverage_start_date': (datetime, none_type,),  # noqa: E501
            'csv_url': (str,),  # noqa: E501
            'cycle': (int, none_type,),  # noqa: E501
            'debts_owed_by_committee': (float, none_type,),  # noqa: E501
            'debts_owed_to_committee': (float, none_type,),  # noqa: E501
            'document_description': (str,),  # noqa: E501
            'end_image_number': (str,),  # noqa: E501
            'exempt_legal_accounting_disbursement_period': (float, none_type,),  # noqa: E501
            'exempt_legal_accounting_disbursement_ytd': (float, none_type,),  # noqa: E501
            'expenditure_subject_to_limits': (float, none_type,),  # noqa: E501
            'fec_file_id': (str,),  # noqa: E501
            'fec_url': (str,),  # noqa: E501
            'federal_funds_period': (float, none_type,),  # noqa: E501
            'federal_funds_ytd': (float, none_type,),  # noqa: E501
            'file_number': (int, none_type,),  # noqa: E501
            'fundraising_disbursements_period': (float, none_type,),  # noqa: E501
            'fundraising_disbursements_ytd': (float, none_type,),  # noqa: E501
            'html_url': (str, none_type,),  # noqa: E501
            'individual_itemized_contributions_period': (float, none_type,),  # noqa: E501
            'individual_itemized_contributions_ytd': (float, none_type,),  # noqa: E501
            'individual_unitemized_contributions_period': (float, none_type,),  # noqa: E501
            'individual_unitemized_contributions_ytd': (float, none_type,),  # noqa: E501
            'is_amended': (bool, none_type,),  # noqa: E501
            'items_on_hand_liquidated': (float, none_type,),  # noqa: E501
            'loans_received_from_candidate_period': (float, none_type,),  # noqa: E501
            'loans_received_from_candidate_ytd': (float, none_type,),  # noqa: E501
            'means_filed': (str, none_type,),  # noqa: E501
            'most_recent': (bool, none_type,),  # noqa: E501
            'most_recent_file_number': (float, none_type,),  # noqa: E501
            'net_contributions_cycle_to_date': (float, none_type,),  # noqa: E501
            'net_operating_expenditures_cycle_to_date': (float, none_type,),  # noqa: E501
            'offsets_to_fundraising_expenditures_period': (float, none_type,),  # noqa: E501
            'offsets_to_fundraising_expenditures_ytd': (float, none_type,),  # noqa: E501
            'offsets_to_legal_accounting_period': (float, none_type,),  # noqa: E501
            'offsets_to_legal_accounting_ytd': (float, none_type,),  # noqa: E501
            'offsets_to_operating_expenditures_period': (float, none_type,),  # noqa: E501
            'offsets_to_operating_expenditures_ytd': (float, none_type,),  # noqa: E501
            'operating_expenditures_period': (float, none_type,),  # noqa: E501
            'operating_expenditures_ytd': (float, none_type,),  # noqa: E501
            'other_disbursements_period': (float, none_type,),  # noqa: E501
            'other_disbursements_ytd': (float, none_type,),  # noqa: E501
            'other_loans_received_period': (float, none_type,),  # noqa: E501
            'other_loans_received_ytd': (float, none_type,),  # noqa: E501
            'other_political_committee_contributions_period': (float, none_type,),  # noqa: E501
            'other_political_committee_contributions_ytd': (float, none_type,),  # noqa: E501
            'other_receipts_period': (float, none_type,),  # noqa: E501
            'other_receipts_ytd': (float, none_type,),  # noqa: E501
            'pdf_url': (str,),  # noqa: E501
            'political_party_committee_contributions_period': (float, none_type,),  # noqa: E501
            'political_party_committee_contributions_ytd': (float, none_type,),  # noqa: E501
            'previous_file_number': (float, none_type,),  # noqa: E501
            'receipt_date': (date, none_type,),  # noqa: E501
            'refunded_individual_contributions_period': (float, none_type,),  # noqa: E501
            'refunded_individual_contributions_ytd': (float, none_type,),  # noqa: E501
            'refunded_other_political_committee_contributions_period': (float, none_type,),  # noqa: E501
            'refunded_other_political_committee_contributions_ytd': (float, none_type,),  # noqa: E501
            'refunded_political_party_committee_contributions_period': (float, none_type,),  # noqa: E501
            'refunded_political_party_committee_contributions_ytd': (float, none_type,),  # noqa: E501
            'repayments_loans_made_by_candidate_period': (float, none_type,),  # noqa: E501
            'repayments_loans_made_candidate_ytd': (float, none_type,),  # noqa: E501
            'repayments_other_loans_period': (float, none_type,),  # noqa: E501
            'repayments_other_loans_ytd': (float, none_type,),  # noqa: E501
            'report_form': (str,),  # noqa: E501
            'report_type': (str, none_type,),  # noqa: E501
            'report_type_full': (str, none_type,),  # noqa: E501
            'report_year': (int, none_type,),  # noqa: E501
            'subtotal_summary_period': (float, none_type,),  # noqa: E501
            'total_contribution_refunds_period': (float, none_type,),  # noqa: E501
            'total_contribution_refunds_ytd': (float, none_type,),  # noqa: E501
            'total_contributions_period': (float, none_type,),  # noqa: E501
            'total_contributions_ytd': (float, none_type,),  # noqa: E501
            'total_disbursements_period': (float, none_type,),  # noqa: E501
            'total_disbursements_ytd': (float, none_type,),  # noqa: E501
            'total_individual_contributions_period': (float, none_type,),  # noqa: E501
            'total_individual_contributions_ytd': (float, none_type,),  # noqa: E501
            'total_loan_repayments_made_period': (float, none_type,),  # noqa: E501
            'total_loan_repayments_made_ytd': (float, none_type,),  # noqa: E501
            'total_loans_received_period': (float, none_type,),  # noqa: E501
            'total_loans_received_ytd': (float, none_type,),  # noqa: E501
            'total_offsets_to_operating_expenditures_period': (float, none_type,),  # noqa: E501
            'total_offsets_to_operating_expenditures_ytd': (float, none_type,),  # noqa: E501
            'total_period': (float, none_type,),  # noqa: E501
            'total_receipts_period': (float, none_type,),  # noqa: E501
            'total_receipts_ytd': (float, none_type,),  # noqa: E501
            'total_ytd': (float, none_type,),  # noqa: E501
            'transfers_from_affiliated_committee_period': (float, none_type,),  # noqa: E501
            'transfers_from_affiliated_committee_ytd': (float, none_type,),  # noqa: E501
            'transfers_to_other_authorized_committee_period': (float, none_type,),  # noqa: E501
            'transfers_to_other_authorized_committee_ytd': (float, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        'amendment_chain': 'amendment_chain',  # noqa: E501
        'amendment_indicator': 'amendment_indicator',  # noqa: E501
        'amendment_indicator_full': 'amendment_indicator_full',  # noqa: E501
        'beginning_image_number': 'beginning_image_number',  # noqa: E501
        'candidate_contribution_period': 'candidate_contribution_period',  # noqa: E501
        'candidate_contribution_ytd': 'candidate_contribution_ytd',  # noqa: E501
        'cash_on_hand_beginning_period': 'cash_on_hand_beginning_period',  # noqa: E501
        'cash_on_hand_end_period': 'cash_on_hand_end_period',  # noqa: E501
        'committee_id': 'committee_id',  # noqa: E501
        'committee_name': 'committee_name',  # noqa: E501
        'committee_type': 'committee_type',  # noqa: E501
        'coverage_end_date': 'coverage_end_date',  # noqa: E501
        'coverage_start_date': 'coverage_start_date',  # noqa: E501
        'csv_url': 'csv_url',  # noqa: E501
        'cycle': 'cycle',  # noqa: E501
        'debts_owed_by_committee': 'debts_owed_by_committee',  # noqa: E501
        'debts_owed_to_committee': 'debts_owed_to_committee',  # noqa: E501
        'document_description': 'document_description',  # noqa: E501
        'end_image_number': 'end_image_number',  # noqa: E501
        'exempt_legal_accounting_disbursement_period': 'exempt_legal_accounting_disbursement_period',  # noqa: E501
        'exempt_legal_accounting_disbursement_ytd': 'exempt_legal_accounting_disbursement_ytd',  # noqa: E501
        'expenditure_subject_to_limits': 'expenditure_subject_to_limits',  # noqa: E501
        'fec_file_id': 'fec_file_id',  # noqa: E501
        'fec_url': 'fec_url',  # noqa: E501
        'federal_funds_period': 'federal_funds_period',  # noqa: E501
        'federal_funds_ytd': 'federal_funds_ytd',  # noqa: E501
        'file_number': 'file_number',  # noqa: E501
        'fundraising_disbursements_period': 'fundraising_disbursements_period',  # noqa: E501
        'fundraising_disbursements_ytd': 'fundraising_disbursements_ytd',  # noqa: E501
        'html_url': 'html_url',  # noqa: E501
        'individual_itemized_contributions_period': 'individual_itemized_contributions_period',  # noqa: E501
        'individual_itemized_contributions_ytd': 'individual_itemized_contributions_ytd',  # noqa: E501
        'individual_unitemized_contributions_period': 'individual_unitemized_contributions_period',  # noqa: E501
        'individual_unitemized_contributions_ytd': 'individual_unitemized_contributions_ytd',  # noqa: E501
        'is_amended': 'is_amended',  # noqa: E501
        'items_on_hand_liquidated': 'items_on_hand_liquidated',  # noqa: E501
        'loans_received_from_candidate_period': 'loans_received_from_candidate_period',  # noqa: E501
        'loans_received_from_candidate_ytd': 'loans_received_from_candidate_ytd',  # noqa: E501
        'means_filed': 'means_filed',  # noqa: E501
        'most_recent': 'most_recent',  # noqa: E501
        'most_recent_file_number': 'most_recent_file_number',  # noqa: E501
        'net_contributions_cycle_to_date': 'net_contributions_cycle_to_date',  # noqa: E501
        'net_operating_expenditures_cycle_to_date': 'net_operating_expenditures_cycle_to_date',  # noqa: E501
        'offsets_to_fundraising_expenditures_period': 'offsets_to_fundraising_expenditures_period',  # noqa: E501
        'offsets_to_fundraising_expenditures_ytd': 'offsets_to_fundraising_expenditures_ytd',  # noqa: E501
        'offsets_to_legal_accounting_period': 'offsets_to_legal_accounting_period',  # noqa: E501
        'offsets_to_legal_accounting_ytd': 'offsets_to_legal_accounting_ytd',  # noqa: E501
        'offsets_to_operating_expenditures_period': 'offsets_to_operating_expenditures_period',  # noqa: E501
        'offsets_to_operating_expenditures_ytd': 'offsets_to_operating_expenditures_ytd',  # noqa: E501
        'operating_expenditures_period': 'operating_expenditures_period',  # noqa: E501
        'operating_expenditures_ytd': 'operating_expenditures_ytd',  # noqa: E501
        'other_disbursements_period': 'other_disbursements_period',  # noqa: E501
        'other_disbursements_ytd': 'other_disbursements_ytd',  # noqa: E501
        'other_loans_received_period': 'other_loans_received_period',  # noqa: E501
        'other_loans_received_ytd': 'other_loans_received_ytd',  # noqa: E501
        'other_political_committee_contributions_period': 'other_political_committee_contributions_period',  # noqa: E501
        'other_political_committee_contributions_ytd': 'other_political_committee_contributions_ytd',  # noqa: E501
        'other_receipts_period': 'other_receipts_period',  # noqa: E501
        'other_receipts_ytd': 'other_receipts_ytd',  # noqa: E501
        'pdf_url': 'pdf_url',  # noqa: E501
        'political_party_committee_contributions_period': 'political_party_committee_contributions_period',  # noqa: E501
        'political_party_committee_contributions_ytd': 'political_party_committee_contributions_ytd',  # noqa: E501
        'previous_file_number': 'previous_file_number',  # noqa: E501
        'receipt_date': 'receipt_date',  # noqa: E501
        'refunded_individual_contributions_period': 'refunded_individual_contributions_period',  # noqa: E501
        'refunded_individual_contributions_ytd': 'refunded_individual_contributions_ytd',  # noqa: E501
        'refunded_other_political_committee_contributions_period': 'refunded_other_political_committee_contributions_period',  # noqa: E501
        'refunded_other_political_committee_contributions_ytd': 'refunded_other_political_committee_contributions_ytd',  # noqa: E501
        'refunded_political_party_committee_contributions_period': 'refunded_political_party_committee_contributions_period',  # noqa: E501
        'refunded_political_party_committee_contributions_ytd': 'refunded_political_party_committee_contributions_ytd',  # noqa: E501
        'repayments_loans_made_by_candidate_period': 'repayments_loans_made_by_candidate_period',  # noqa: E501
        'repayments_loans_made_candidate_ytd': 'repayments_loans_made_candidate_ytd',  # noqa: E501
        'repayments_other_loans_period': 'repayments_other_loans_period',  # noqa: E501
        'repayments_other_loans_ytd': 'repayments_other_loans_ytd',  # noqa: E501
        'report_form': 'report_form',  # noqa: E501
        'report_type': 'report_type',  # noqa: E501
        'report_type_full': 'report_type_full',  # noqa: E501
        'report_year': 'report_year',  # noqa: E501
        'subtotal_summary_period': 'subtotal_summary_period',  # noqa: E501
        'total_contribution_refunds_period': 'total_contribution_refunds_period',  # noqa: E501
        'total_contribution_refunds_ytd': 'total_contribution_refunds_ytd',  # noqa: E501
        'total_contributions_period': 'total_contributions_period',  # noqa: E501
        'total_contributions_ytd': 'total_contributions_ytd',  # noqa: E501
        'total_disbursements_period': 'total_disbursements_period',  # noqa: E501
        'total_disbursements_ytd': 'total_disbursements_ytd',  # noqa: E501
        'total_individual_contributions_period': 'total_individual_contributions_period',  # noqa: E501
        'total_individual_contributions_ytd': 'total_individual_contributions_ytd',  # noqa: E501
        'total_loan_repayments_made_period': 'total_loan_repayments_made_period',  # noqa: E501
        'total_loan_repayments_made_ytd': 'total_loan_repayments_made_ytd',  # noqa: E501
        'total_loans_received_period': 'total_loans_received_period',  # noqa: E501
        'total_loans_received_ytd': 'total_loans_received_ytd',  # noqa: E501
        'total_offsets_to_operating_expenditures_period': 'total_offsets_to_operating_expenditures_period',  # noqa: E501
        'total_offsets_to_operating_expenditures_ytd': 'total_offsets_to_operating_expenditures_ytd',  # noqa: E501
        'total_period': 'total_period',  # noqa: E501
        'total_receipts_period': 'total_receipts_period',  # noqa: E501
        'total_receipts_ytd': 'total_receipts_ytd',  # noqa: E501
        'total_ytd': 'total_ytd',  # noqa: E501
        'transfers_from_affiliated_committee_period': 'transfers_from_affiliated_committee_period',  # noqa: E501
        'transfers_from_affiliated_committee_ytd': 'transfers_from_affiliated_committee_ytd',  # noqa: E501
        'transfers_to_other_authorized_committee_period': 'transfers_to_other_authorized_committee_period',  # noqa: E501
        'transfers_to_other_authorized_committee_ytd': 'transfers_to_other_authorized_committee_ytd',  # noqa: E501
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
        """committee_reports_presidential.CommitteeReportsPresidential - a model defined in OpenAPI

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
            amendment_chain ([float], none_type):  The first value in the chain is the original filing.  The ordering in the chain reflects the order the amendments were filed up to the amendment being viewed. . [optional]  # noqa: E501
            amendment_indicator (str, none_type): [optional]  # noqa: E501
            amendment_indicator_full (str, none_type): [optional]  # noqa: E501
            beginning_image_number (str): [optional]  # noqa: E501
            candidate_contribution_period (float, none_type): [optional]  # noqa: E501
            candidate_contribution_ytd (float, none_type): [optional]  # noqa: E501
            cash_on_hand_beginning_period (float, none_type): Balance for the committee at the start of the two-year period. [optional]  # noqa: E501
            cash_on_hand_end_period (float, none_type): Ending cash balance on the most recent filing. [optional]  # noqa: E501
            committee_id (str, none_type):  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. . [optional]  # noqa: E501
            committee_name (str, none_type): The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records.. [optional]  # noqa: E501
            committee_type (str): [optional]  # noqa: E501
            coverage_end_date (datetime, none_type): Ending date of the reporting period. [optional]  # noqa: E501
            coverage_start_date (datetime, none_type): Beginning date of the reporting period. [optional]  # noqa: E501
            csv_url (str): [optional]  # noqa: E501
            cycle (int, none_type):  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year. . [optional]  # noqa: E501
            debts_owed_by_committee (float, none_type): Debts owed by the committee. [optional]  # noqa: E501
            debts_owed_to_committee (float, none_type): Debts owed to the committee. [optional]  # noqa: E501
            document_description (str): [optional]  # noqa: E501
            end_image_number (str): [optional]  # noqa: E501
            exempt_legal_accounting_disbursement_period (float, none_type): [optional]  # noqa: E501
            exempt_legal_accounting_disbursement_ytd (float, none_type): [optional]  # noqa: E501
            expenditure_subject_to_limits (float, none_type): [optional]  # noqa: E501
            fec_file_id (str): [optional]  # noqa: E501
            fec_url (str): [optional]  # noqa: E501
            federal_funds_period (float, none_type): [optional]  # noqa: E501
            federal_funds_ytd (float, none_type): [optional]  # noqa: E501
            file_number (int, none_type): [optional]  # noqa: E501
            fundraising_disbursements_period (float, none_type): [optional]  # noqa: E501
            fundraising_disbursements_ytd (float, none_type): [optional]  # noqa: E501
            html_url (str, none_type):  HTML link to the filing. . [optional]  # noqa: E501
            individual_itemized_contributions_period (float, none_type): Individual itemized contributions are from individuals whose aggregate contributions total over $200 per individual per year. Be aware, some filers choose to itemize donations $200 or less. total for the reporting period. [optional]  # noqa: E501
            individual_itemized_contributions_ytd (float, none_type): Individual itemized contributions are from individuals whose aggregate contributions total over $200 per individual per year. Be aware, some filers choose to itemize donations $200 or less. total for the year to date. [optional]  # noqa: E501
            individual_unitemized_contributions_period (float, none_type): Unitemized contributions are made individuals whose aggregate contributions total $200 or less per individual per year. Be aware, some filers choose to itemize donations $200 or less and in that case those donations will appear in the itemized total. total for the reporting period. [optional]  # noqa: E501
            individual_unitemized_contributions_ytd (float, none_type): Unitemized contributions are made individuals whose aggregate contributions total $200 or less per individual per year. Be aware, some filers choose to itemize donations $200 or less and in that case those donations will appear in the itemized total. total for the year to date. [optional]  # noqa: E501
            is_amended (bool, none_type):  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment. . [optional]  # noqa: E501
            items_on_hand_liquidated (float, none_type): [optional]  # noqa: E501
            loans_received_from_candidate_period (float, none_type): [optional]  # noqa: E501
            loans_received_from_candidate_ytd (float, none_type): [optional]  # noqa: E501
            means_filed (str, none_type): The method used to file with the FEC, either electronic or on paper.. [optional]  # noqa: E501
            most_recent (bool, none_type):  Report is either new or is the most-recently filed amendment . [optional]  # noqa: E501
            most_recent_file_number (float, none_type): [optional]  # noqa: E501
            net_contributions_cycle_to_date (float, none_type): [optional]  # noqa: E501
            net_operating_expenditures_cycle_to_date (float, none_type): [optional]  # noqa: E501
            offsets_to_fundraising_expenditures_period (float, none_type): [optional]  # noqa: E501
            offsets_to_fundraising_expenditures_ytd (float, none_type): [optional]  # noqa: E501
            offsets_to_legal_accounting_period (float, none_type): [optional]  # noqa: E501
            offsets_to_legal_accounting_ytd (float, none_type): [optional]  # noqa: E501
            offsets_to_operating_expenditures_period (float, none_type): Offsets to operating expenditures total for the reporting period. [optional]  # noqa: E501
            offsets_to_operating_expenditures_ytd (float, none_type): Offsets to operating expenditures total for the year to date. [optional]  # noqa: E501
            operating_expenditures_period (float, none_type): [optional]  # noqa: E501
            operating_expenditures_ytd (float, none_type): [optional]  # noqa: E501
            other_disbursements_period (float, none_type): Other disbursements total for the reporting period. [optional]  # noqa: E501
            other_disbursements_ytd (float, none_type): Other disbursements total for the year to date. [optional]  # noqa: E501
            other_loans_received_period (float, none_type): [optional]  # noqa: E501
            other_loans_received_ytd (float, none_type): [optional]  # noqa: E501
            other_political_committee_contributions_period (float, none_type): Other committees contributions total for the reporting period. [optional]  # noqa: E501
            other_political_committee_contributions_ytd (float, none_type): Other committees contributions total for the year to date. [optional]  # noqa: E501
            other_receipts_period (float, none_type): [optional]  # noqa: E501
            other_receipts_ytd (float, none_type): [optional]  # noqa: E501
            pdf_url (str): [optional]  # noqa: E501
            political_party_committee_contributions_period (float, none_type): Party committees contributions total for the reporting period. [optional]  # noqa: E501
            political_party_committee_contributions_ytd (float, none_type): Party committees contributions total for the year to date. [optional]  # noqa: E501
            previous_file_number (float, none_type): [optional]  # noqa: E501
            receipt_date (date, none_type): Date the FEC received the electronic or paper record. [optional]  # noqa: E501
            refunded_individual_contributions_period (float, none_type): Individual refunds total for the reporting period. [optional]  # noqa: E501
            refunded_individual_contributions_ytd (float, none_type): Individual refunds total for the year to date. [optional]  # noqa: E501
            refunded_other_political_committee_contributions_period (float, none_type): Other committee refunds total for the reporting period. [optional]  # noqa: E501
            refunded_other_political_committee_contributions_ytd (float, none_type): Other committee refunds total for the year to date. [optional]  # noqa: E501
            refunded_political_party_committee_contributions_period (float, none_type): Political party refunds total for the reporting period. [optional]  # noqa: E501
            refunded_political_party_committee_contributions_ytd (float, none_type): Political party refunds total for the year to date. [optional]  # noqa: E501
            repayments_loans_made_by_candidate_period (float, none_type): [optional]  # noqa: E501
            repayments_loans_made_candidate_ytd (float, none_type): [optional]  # noqa: E501
            repayments_other_loans_period (float, none_type): [optional]  # noqa: E501
            repayments_other_loans_ytd (float, none_type): [optional]  # noqa: E501
            report_form (str): [optional]  # noqa: E501
            report_type (str, none_type): Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE) . [optional]  # noqa: E501
            report_type_full (str, none_type): Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE) . [optional]  # noqa: E501
            report_year (int, none_type):  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date. . [optional]  # noqa: E501
            subtotal_summary_period (float, none_type): [optional]  # noqa: E501
            total_contribution_refunds_period (float, none_type): Total contribution refunds total for the reporting period. [optional]  # noqa: E501
            total_contribution_refunds_ytd (float, none_type): Total contribution refunds total for the year to date. [optional]  # noqa: E501
            total_contributions_period (float, none_type): Contribution total for the reporting period. [optional]  # noqa: E501
            total_contributions_ytd (float, none_type): Contribution total for the year to date. [optional]  # noqa: E501
            total_disbursements_period (float, none_type): Disbursements total for the reporting period. [optional]  # noqa: E501
            total_disbursements_ytd (float, none_type): Disbursements total for the year to date. [optional]  # noqa: E501
            total_individual_contributions_period (float, none_type): Individual contributions total for the reporting period. [optional]  # noqa: E501
            total_individual_contributions_ytd (float, none_type): Individual contributions total for the year to date. [optional]  # noqa: E501
            total_loan_repayments_made_period (float, none_type): [optional]  # noqa: E501
            total_loan_repayments_made_ytd (float, none_type): [optional]  # noqa: E501
            total_loans_received_period (float, none_type): [optional]  # noqa: E501
            total_loans_received_ytd (float, none_type): [optional]  # noqa: E501
            total_offsets_to_operating_expenditures_period (float, none_type): [optional]  # noqa: E501
            total_offsets_to_operating_expenditures_ytd (float, none_type): [optional]  # noqa: E501
            total_period (float, none_type): [optional]  # noqa: E501
            total_receipts_period (float, none_type): Anything of value (money, goods, services or property) received by a political committee total for the reporting period. [optional]  # noqa: E501
            total_receipts_ytd (float, none_type): Anything of value (money, goods, services or property) received by a political committee total for the year to date. [optional]  # noqa: E501
            total_ytd (float, none_type): [optional]  # noqa: E501
            transfers_from_affiliated_committee_period (float, none_type): [optional]  # noqa: E501
            transfers_from_affiliated_committee_ytd (float, none_type): [optional]  # noqa: E501
            transfers_to_other_authorized_committee_period (float, none_type): [optional]  # noqa: E501
            transfers_to_other_authorized_committee_ytd (float, none_type): [optional]  # noqa: E501
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
