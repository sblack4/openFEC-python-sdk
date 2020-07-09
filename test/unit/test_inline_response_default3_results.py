# coding: utf-8

"""
    OpenFEC

    This API allows you to explore the way candidates and committees fund their campaigns.    The FEC API is a RESTful web service supporting full-text and field-specific searches on FEC data. [Bulk downloads](https://www.fec.gov/data/advanced/?tab=bulk-data) are available on the current site. Information is tied to the underlying forms by file ID and image ID. Data is updated nightly.    There is a lot of data, but a good place to start is to use search to find interesting candidates and committees. Then, you can use their IDs to find report or line item details with the other endpoints. If you are interested in individual donors, check out contributor information in schedule_a.    Get an [API key here](https://api.data.gov/signup/). That will enable you to place up to 1,000 calls an hour. Each call is limited to 100 results per page. You can email questions, comments or a request to get a key for 120 calls per minute to [APIinfo@fec.gov](mailto:apiinfo@fec.gov). You can also ask questions and discuss the data in the [FEC data Google Group](https://groups.google.com/forum/#!forum/fec-data). API changes will also be added to this group in advance of the change.    The model definitions and schema are available at [/swagger](/swagger/). This is useful for making wrappers and exploring the data.    A few restrictions limit the way you can use FEC data. For example, you can’t use contributor lists for commercial purposes or to solicit donations. [Learn more here](https://www.fec.gov/updates/sale-or-use-contributor-information/).    [View our source code](https://github.com/fecgov/openFEC). We welcome issues and pull requests!  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openfec_sdk
from openfec_sdk.models.inline_response_default3_results import InlineResponseDefault3Results  # noqa: E501
from openfec_sdk.rest import ApiException

class TestInlineResponseDefault3Results(unittest.TestCase):
    """InlineResponseDefault3Results unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponseDefault3Results
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openfec_sdk.models.inline_response_default3_results.InlineResponseDefault3Results()  # noqa: E501
        if include_optional :
            return InlineResponseDefault3Results(
                action_code = '0',
                action_code_full = '0',
                candidate_first_name = '0',
                candidate_id = '0',
                candidate_last_name = '0',
                candidate_middle_name = '0',
                candidate_name = '0',
                candidate_office = '0',
                candidate_office_district = '0',
                candidate_office_full = '0',
                candidate_office_state = '0',
                candidate_office_state_full = '0',
                candidate_prefix = '0',
                candidate_suffix = '0',
                committee = openfec_sdk.models.committee_history.CommitteeHistory(
                    affiliated_committee_name = '0',
                    candidate_ids = [
                        '0'
                        ],
                    city = '0',
                    committee_id = '0',
                    committee_type = '0',
                    committee_type_full = '0',
                    cycle = 56,
                    cycles = [
                        56
                        ],
                    cycles_has_activity = [
                        56
                        ],
                    cycles_has_financial = [
                        56
                        ],
                    designation = '0',
                    designation_full = '0',
                    filing_frequency = '0',
                    is_active = True,
                    last_cycle_has_activity = 56,
                    last_cycle_has_financial = 56,
                    name = '0',
                    organization_type = '0',
                    organization_type_full = '0',
                    party = '0',
                    party_full = '0',
                    state = '0',
                    state_full = '0',
                    street_1 = '0',
                    street_2 = '0',
                    treasurer_name = '0',
                    zip = '0', ),
                committee_id = '0',
                cycle = 56,
                due_date_terms = '0',
                election_type = '0',
                election_type_full = '0',
                entity_type = '0',
                entity_type_full = '0',
                fec_committee_id = '0',
                fec_election_type_full = '0',
                fec_election_type_year = '0',
                file_number = 56,
                filing_form = '0',
                image_number = '0',
                incurred_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                interest_rate_terms = '0',
                line_number = '0',
                link_id = 56,
                load_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                loan_balance = 1.337,
                loan_source_city = '0',
                loan_source_first_name = '0',
                loan_source_last_name = '0',
                loan_source_middle_name = '0',
                loan_source_name = '0',
                loan_source_prefix = '0',
                loan_source_state = '0',
                loan_source_street_1 = '0',
                loan_source_street_2 = '0',
                loan_source_suffix = '0',
                loan_source_zip = 56,
                memo_code = '0',
                memo_text = '0',
                original_loan_amount = 1.337,
                original_sub_id = 56,
                payment_to_date = 1.337,
                pdf_url = '0',
                personally_funded = '0',
                report_type = '0',
                report_year = 56,
                schedule_a_line_number = 56,
                schedule_type = '0',
                schedule_type_full = '0',
                secured_ind = '0',
                sub_id = '0',
                transaction_id = '0'
            )
        else :
            return InlineResponseDefault3Results(
        )

    def testInlineResponseDefault3Results(self):
        """Test InlineResponseDefault3Results"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
