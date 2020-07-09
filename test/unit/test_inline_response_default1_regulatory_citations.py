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
from openfec_sdk.models.inline_response_default1_regulatory_citations import InlineResponseDefault1RegulatoryCitations  # noqa: E501
from openfec_sdk.rest import ApiException

class TestInlineResponseDefault1RegulatoryCitations(unittest.TestCase):
    """InlineResponseDefault1RegulatoryCitations unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponseDefault1RegulatoryCitations
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openfec_sdk.models.inline_response_default1_regulatory_citations.InlineResponseDefault1RegulatoryCitations()  # noqa: E501
        if include_optional :
            return InlineResponseDefault1RegulatoryCitations(
                part = 56,
                section = 56,
                title = 56
            )
        else :
            return InlineResponseDefault1RegulatoryCitations(
        )

    def testInlineResponseDefault1RegulatoryCitations(self):
        """Test InlineResponseDefault1RegulatoryCitations"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
