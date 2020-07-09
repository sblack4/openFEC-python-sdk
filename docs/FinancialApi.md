# openfec_sdk.FinancialApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**committee_committee_id_reports_get**](FinancialApi.md#committee_committee_id_reports_get) | **GET** /committee/{committee_id}/reports/ |
[**committee_committee_id_totals_get**](FinancialApi.md#committee_committee_id_totals_get) | **GET** /committee/{committee_id}/totals/ |
[**elections_get**](FinancialApi.md#elections_get) | **GET** /elections/ |
[**elections_search_get**](FinancialApi.md#elections_search_get) | **GET** /elections/search/ |
[**elections_summary_get**](FinancialApi.md#elections_summary_get) | **GET** /elections/summary/ |
[**reports_committee_type_get**](FinancialApi.md#reports_committee_type_get) | **GET** /reports/{committee_type}/ |
[**totals_by_entity_get**](FinancialApi.md#totals_by_entity_get) | **GET** /totals/by_entity/ |
[**totals_committee_type_get**](FinancialApi.md#totals_committee_type_get) | **GET** /totals/{committee_type}/ |


# **committee_committee_id_reports_get**
> CommitteeReportsPage committee_committee_id_reports_get(api_key, committee_id, sort_hide_null=sort_hide_null, is_amended=is_amended, min_total_contributions=min_total_contributions, max_disbursements_amount=max_disbursements_amount, candidate_id=candidate_id, min_debts_owed_amount=min_debts_owed_amount, min_cash_on_hand_end_period_amount=min_cash_on_hand_end_period_amount, max_total_contributions=max_total_contributions, page=page, type=type, beginning_image_number=beginning_image_number, max_debts_owed_expenditures=max_debts_owed_expenditures, cycle=cycle, max_independent_expenditures=max_independent_expenditures, max_cash_on_hand_end_period_amount=max_cash_on_hand_end_period_amount, report_type=report_type, min_independent_expenditures=min_independent_expenditures, min_receipts_amount=min_receipts_amount, sort_null_only=sort_null_only, per_page=per_page, sort=sort, max_receipts_amount=max_receipts_amount, year=year, min_disbursements_amount=min_disbursements_amount, max_party_coordinated_expenditures=max_party_coordinated_expenditures, min_party_coordinated_expenditures=min_party_coordinated_expenditures, sort_nulls_last=sort_nulls_last)



 Each report represents the summary information from FEC Form 3, Form 3X and Form 3P. These reports have key statistics that illuminate the financial status of a given committee. Things like cash on hand, debts owed by committee, total receipts, and total disbursements are especially helpful for understanding a committee's financial dealings.  By default, this endpoint includes both amended and final versions of each report. To restrict to only the final versions of each report, use `is_amended=false`; to view only reports that have been amended, use `is_amended=true`.  Several different reporting structures exist, depending on the type of organization that submits financial information. To see an example of these reporting requirements, look at the summary and detailed summary pages of FEC Form 3, Form 3X, and Form 3P.  DISCLAIMER: The field labels contained within this resource are subject to change.  We are attempting to succinctly label these fields while conveying clear meaning to ensure accessibility for all users.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openfec_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openfec_sdk.FinancialApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
is_amended = True # bool |  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  (optional)
min_total_contributions = 'min_total_contributions_example' # str |  Filter for all amounts greater than a value.  (optional)
max_disbursements_amount = 'max_disbursements_amount_example' # str |  Filter for all amounts less than a value.  (optional)
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
min_debts_owed_amount = 'min_debts_owed_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
min_cash_on_hand_end_period_amount = 'min_cash_on_hand_end_period_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
max_total_contributions = 'max_total_contributions_example' # str |  Filter for all amounts less than a value.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
type = ['type_example'] # list[str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
beginning_image_number = ['beginning_image_number_example'] # list[str] |  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  (optional)
max_debts_owed_expenditures = 'max_debts_owed_expenditures_example' # str |  Filter for all amounts less than a value.  (optional)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
max_independent_expenditures = 'max_independent_expenditures_example' # str |  Filter for all amounts less than a value.  (optional)
max_cash_on_hand_end_period_amount = 'max_cash_on_hand_end_period_amount_example' # str |  Filter for all amounts less than a value.  (optional)
report_type = ['report_type_example'] # list[str] | Report type; prefix with \"-\" to exclude. Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND  (optional)
min_independent_expenditures = 'min_independent_expenditures_example' # str |  Filter for all amounts greater than a value.  (optional)
min_receipts_amount = 'min_receipts_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort = ["-coverage_end_date"] # list[str] | Provide a field to sort by. Use - for descending order. (optional) (default to ["-coverage_end_date"])
max_receipts_amount = 'max_receipts_amount_example' # str |  Filter for all amounts less than a value.  (optional)
year = [56] # list[int] |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  (optional)
min_disbursements_amount = 'min_disbursements_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
max_party_coordinated_expenditures = 'max_party_coordinated_expenditures_example' # str |  Filter for all amounts less than a value.  (optional)
min_party_coordinated_expenditures = 'min_party_coordinated_expenditures_example' # str |  Filter for all amounts greater than a value.  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)

    try:
        api_response = api_instance.committee_committee_id_reports_get(api_key, committee_id, sort_hide_null=sort_hide_null, is_amended=is_amended, min_total_contributions=min_total_contributions, max_disbursements_amount=max_disbursements_amount, candidate_id=candidate_id, min_debts_owed_amount=min_debts_owed_amount, min_cash_on_hand_end_period_amount=min_cash_on_hand_end_period_amount, max_total_contributions=max_total_contributions, page=page, type=type, beginning_image_number=beginning_image_number, max_debts_owed_expenditures=max_debts_owed_expenditures, cycle=cycle, max_independent_expenditures=max_independent_expenditures, max_cash_on_hand_end_period_amount=max_cash_on_hand_end_period_amount, report_type=report_type, min_independent_expenditures=min_independent_expenditures, min_receipts_amount=min_receipts_amount, sort_null_only=sort_null_only, per_page=per_page, sort=sort, max_receipts_amount=max_receipts_amount, year=year, min_disbursements_amount=min_disbursements_amount, max_party_coordinated_expenditures=max_party_coordinated_expenditures, min_party_coordinated_expenditures=min_party_coordinated_expenditures, sort_nulls_last=sort_nulls_last)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinancialApi->committee_committee_id_reports_get: %s\n" % e)
```

* Api Key Authentication (ApiKeyQueryAuth):
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openfec_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openfec_sdk.FinancialApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
is_amended = True # bool |  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  (optional)
min_total_contributions = 'min_total_contributions_example' # str |  Filter for all amounts greater than a value.  (optional)
max_disbursements_amount = 'max_disbursements_amount_example' # str |  Filter for all amounts less than a value.  (optional)
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
min_debts_owed_amount = 'min_debts_owed_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
min_cash_on_hand_end_period_amount = 'min_cash_on_hand_end_period_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
max_total_contributions = 'max_total_contributions_example' # str |  Filter for all amounts less than a value.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
type = ['type_example'] # list[str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
beginning_image_number = ['beginning_image_number_example'] # list[str] |  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  (optional)
max_debts_owed_expenditures = 'max_debts_owed_expenditures_example' # str |  Filter for all amounts less than a value.  (optional)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
max_independent_expenditures = 'max_independent_expenditures_example' # str |  Filter for all amounts less than a value.  (optional)
max_cash_on_hand_end_period_amount = 'max_cash_on_hand_end_period_amount_example' # str |  Filter for all amounts less than a value.  (optional)
report_type = ['report_type_example'] # list[str] | Report type; prefix with \"-\" to exclude. Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND  (optional)
min_independent_expenditures = 'min_independent_expenditures_example' # str |  Filter for all amounts greater than a value.  (optional)
min_receipts_amount = 'min_receipts_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort = ["-coverage_end_date"] # list[str] | Provide a field to sort by. Use - for descending order. (optional) (default to ["-coverage_end_date"])
max_receipts_amount = 'max_receipts_amount_example' # str |  Filter for all amounts less than a value.  (optional)
year = [56] # list[int] |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  (optional)
min_disbursements_amount = 'min_disbursements_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
max_party_coordinated_expenditures = 'max_party_coordinated_expenditures_example' # str |  Filter for all amounts less than a value.  (optional)
min_party_coordinated_expenditures = 'min_party_coordinated_expenditures_example' # str |  Filter for all amounts greater than a value.  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)

    try:
        api_response = api_instance.committee_committee_id_reports_get(api_key, committee_id, sort_hide_null=sort_hide_null, is_amended=is_amended, min_total_contributions=min_total_contributions, max_disbursements_amount=max_disbursements_amount, candidate_id=candidate_id, min_debts_owed_amount=min_debts_owed_amount, min_cash_on_hand_end_period_amount=min_cash_on_hand_end_period_amount, max_total_contributions=max_total_contributions, page=page, type=type, beginning_image_number=beginning_image_number, max_debts_owed_expenditures=max_debts_owed_expenditures, cycle=cycle, max_independent_expenditures=max_independent_expenditures, max_cash_on_hand_end_period_amount=max_cash_on_hand_end_period_amount, report_type=report_type, min_independent_expenditures=min_independent_expenditures, min_receipts_amount=min_receipts_amount, sort_null_only=sort_null_only, per_page=per_page, sort=sort, max_receipts_amount=max_receipts_amount, year=year, min_disbursements_amount=min_disbursements_amount, max_party_coordinated_expenditures=max_party_coordinated_expenditures, min_party_coordinated_expenditures=min_party_coordinated_expenditures, sort_nulls_last=sort_nulls_last)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinancialApi->committee_committee_id_reports_get: %s\n" % e)
```

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openfec_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openfec_sdk.FinancialApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
is_amended = True # bool |  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  (optional)
min_total_contributions = 'min_total_contributions_example' # str |  Filter for all amounts greater than a value.  (optional)
max_disbursements_amount = 'max_disbursements_amount_example' # str |  Filter for all amounts less than a value.  (optional)
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
min_debts_owed_amount = 'min_debts_owed_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
min_cash_on_hand_end_period_amount = 'min_cash_on_hand_end_period_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
max_total_contributions = 'max_total_contributions_example' # str |  Filter for all amounts less than a value.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
type = ['type_example'] # list[str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
beginning_image_number = ['beginning_image_number_example'] # list[str] |  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  (optional)
max_debts_owed_expenditures = 'max_debts_owed_expenditures_example' # str |  Filter for all amounts less than a value.  (optional)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
max_independent_expenditures = 'max_independent_expenditures_example' # str |  Filter for all amounts less than a value.  (optional)
max_cash_on_hand_end_period_amount = 'max_cash_on_hand_end_period_amount_example' # str |  Filter for all amounts less than a value.  (optional)
report_type = ['report_type_example'] # list[str] | Report type; prefix with \"-\" to exclude. Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND  (optional)
min_independent_expenditures = 'min_independent_expenditures_example' # str |  Filter for all amounts greater than a value.  (optional)
min_receipts_amount = 'min_receipts_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort = ["-coverage_end_date"] # list[str] | Provide a field to sort by. Use - for descending order. (optional) (default to ["-coverage_end_date"])
max_receipts_amount = 'max_receipts_amount_example' # str |  Filter for all amounts less than a value.  (optional)
year = [56] # list[int] |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  (optional)
min_disbursements_amount = 'min_disbursements_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
max_party_coordinated_expenditures = 'max_party_coordinated_expenditures_example' # str |  Filter for all amounts less than a value.  (optional)
min_party_coordinated_expenditures = 'min_party_coordinated_expenditures_example' # str |  Filter for all amounts greater than a value.  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)

    try:
        api_response = api_instance.committee_committee_id_reports_get(api_key, committee_id, sort_hide_null=sort_hide_null, is_amended=is_amended, min_total_contributions=min_total_contributions, max_disbursements_amount=max_disbursements_amount, candidate_id=candidate_id, min_debts_owed_amount=min_debts_owed_amount, min_cash_on_hand_end_period_amount=min_cash_on_hand_end_period_amount, max_total_contributions=max_total_contributions, page=page, type=type, beginning_image_number=beginning_image_number, max_debts_owed_expenditures=max_debts_owed_expenditures, cycle=cycle, max_independent_expenditures=max_independent_expenditures, max_cash_on_hand_end_period_amount=max_cash_on_hand_end_period_amount, report_type=report_type, min_independent_expenditures=min_independent_expenditures, min_receipts_amount=min_receipts_amount, sort_null_only=sort_null_only, per_page=per_page, sort=sort, max_receipts_amount=max_receipts_amount, year=year, min_disbursements_amount=min_disbursements_amount, max_party_coordinated_expenditures=max_party_coordinated_expenditures, min_party_coordinated_expenditures=min_party_coordinated_expenditures, sort_nulls_last=sort_nulls_last)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinancialApi->committee_committee_id_reports_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **committee_id** | **str**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  |
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **is_amended** | **bool**|  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  | [optional]
 **min_total_contributions** | **str**|  Filter for all amounts greater than a value.  | [optional]
 **max_disbursements_amount** | **str**|  Filter for all amounts less than a value.  | [optional]
 **candidate_id** | **str**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional]
 **min_debts_owed_amount** | **str**|  Filter for all amounts greater than a value.  | [optional]
 **min_cash_on_hand_end_period_amount** | **str**|  Filter for all amounts greater than a value.  | [optional]
 **max_total_contributions** | **str**|  Filter for all amounts less than a value.  | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **type** | [**list[str]**](str.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional]
 **beginning_image_number** | [**list[str]**](str.md)|  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  | [optional]
 **max_debts_owed_expenditures** | **str**|  Filter for all amounts less than a value.  | [optional]
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional]
 **max_independent_expenditures** | **str**|  Filter for all amounts less than a value.  | [optional]
 **max_cash_on_hand_end_period_amount** | **str**|  Filter for all amounts less than a value.  | [optional]
 **report_type** | [**list[str]**](str.md)| Report type; prefix with \&quot;-\&quot; to exclude. Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND  | [optional]
 **min_independent_expenditures** | **str**|  Filter for all amounts greater than a value.  | [optional]
 **min_receipts_amount** | **str**|  Filter for all amounts greater than a value.  | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Provide a field to sort by. Use - for descending order. | [optional] [default to [&quot;-coverage_end_date&quot;]]
 **max_receipts_amount** | **str**|  Filter for all amounts less than a value.  | [optional]
 **year** | [**list[int]**](int.md)|  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional]
 **min_disbursements_amount** | **str**|  Filter for all amounts greater than a value.  | [optional]
 **max_party_coordinated_expenditures** | **str**|  Filter for all amounts less than a value.  | [optional]
 **min_party_coordinated_expenditures** | **str**|  Filter for all amounts greater than a value.  | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]

### Return type

[**CommitteeReportsPage**](CommitteeReportsPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **committee_committee_id_totals_get**
> CommitteeTotalsPage committee_committee_id_totals_get(api_key, committee_id, sort_hide_null=sort_hide_null, designation=designation, sort_null_only=sort_null_only, per_page=per_page, sort=sort, page=page, type=type, sort_nulls_last=sort_nulls_last, cycle=cycle)



 This endpoint provides information about a committee's Form 3, Form 3X, or Form 3P financial reports, which are aggregated by two-year period. We refer to two-year periods as a `cycle`.  The cycle is named after the even-numbered year and includes the year before it. To see totals from 2013 and 2014, you would use 2014. In odd-numbered years, the current cycle is the next year — for example, in 2015, the current cycle is 2016.  For presidential and Senate candidates, multiple two-year cycles exist between elections.  Parameter `full_election` is replaced by `election_full`. Please use `election_full` instead.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openfec_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openfec_sdk.FinancialApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
designation = 'designation_example' # str | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort = '-cycle' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-cycle')
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
type = 'type_example' # str | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)

    try:
        api_response = api_instance.committee_committee_id_totals_get(api_key, committee_id, sort_hide_null=sort_hide_null, designation=designation, sort_null_only=sort_null_only, per_page=per_page, sort=sort, page=page, type=type, sort_nulls_last=sort_nulls_last, cycle=cycle)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinancialApi->committee_committee_id_totals_get: %s\n" % e)
```

* Api Key Authentication (ApiKeyQueryAuth):
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openfec_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openfec_sdk.FinancialApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
designation = 'designation_example' # str | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort = '-cycle' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-cycle')
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
type = 'type_example' # str | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)

    try:
        api_response = api_instance.committee_committee_id_totals_get(api_key, committee_id, sort_hide_null=sort_hide_null, designation=designation, sort_null_only=sort_null_only, per_page=per_page, sort=sort, page=page, type=type, sort_nulls_last=sort_nulls_last, cycle=cycle)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinancialApi->committee_committee_id_totals_get: %s\n" % e)
```

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openfec_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openfec_sdk.FinancialApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
designation = 'designation_example' # str | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort = '-cycle' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-cycle')
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
type = 'type_example' # str | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)

    try:
        api_response = api_instance.committee_committee_id_totals_get(api_key, committee_id, sort_hide_null=sort_hide_null, designation=designation, sort_null_only=sort_null_only, per_page=per_page, sort=sort, page=page, type=type, sort_nulls_last=sort_nulls_last, cycle=cycle)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinancialApi->committee_committee_id_totals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **committee_id** | **str**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  |
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **designation** | **str**| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-cycle&#39;]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **type** | **str**| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional]

### Return type

[**CommitteeTotalsPage**](CommitteeTotalsPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **elections_get**
> ElectionPage elections_get(api_key, office, cycle, sort_hide_null=sort_hide_null, state=state, sort_null_only=sort_null_only, per_page=per_page, sort=sort, district=district, page=page, sort_nulls_last=sort_nulls_last, election_full=election_full)



 Look at the top-level financial information for all candidates running for the same office.  Choose a 2-year cycle, and `house`, `senate` or `presidential`.  If you are looking for a Senate seat, you will need to select the state using a two-letter abbreviation.  House races require state and a two-digit district number.  Since this endpoint reflects financial information, it will only have candidates once they file financial reporting forms. Query the `/candidates` endpoint to see an up to date list of all the candidates that filed to run for a particular seat.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openfec_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openfec_sdk.FinancialApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
office = 'office_example' # str | Federal office candidate runs for: H, S or P
cycle = 56 # int |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
state = 'state_example' # str | US state or territory where a candidate runs for office (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort = '-total_receipts' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-total_receipts')
district = 'district_example' # str | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)

    try:
        api_response = api_instance.elections_get(api_key, office, cycle, sort_hide_null=sort_hide_null, state=state, sort_null_only=sort_null_only, per_page=per_page, sort=sort, district=district, page=page, sort_nulls_last=sort_nulls_last, election_full=election_full)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinancialApi->elections_get: %s\n" % e)
```

* Api Key Authentication (ApiKeyQueryAuth):
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openfec_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openfec_sdk.FinancialApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
office = 'office_example' # str | Federal office candidate runs for: H, S or P
cycle = 56 # int |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
state = 'state_example' # str | US state or territory where a candidate runs for office (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort = '-total_receipts' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-total_receipts')
district = 'district_example' # str | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)

    try:
        api_response = api_instance.elections_get(api_key, office, cycle, sort_hide_null=sort_hide_null, state=state, sort_null_only=sort_null_only, per_page=per_page, sort=sort, district=district, page=page, sort_nulls_last=sort_nulls_last, election_full=election_full)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinancialApi->elections_get: %s\n" % e)
```

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openfec_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openfec_sdk.FinancialApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
office = 'office_example' # str | Federal office candidate runs for: H, S or P
cycle = 56 # int |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
state = 'state_example' # str | US state or territory where a candidate runs for office (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort = '-total_receipts' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-total_receipts')
district = 'district_example' # str | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)

    try:
        api_response = api_instance.elections_get(api_key, office, cycle, sort_hide_null=sort_hide_null, state=state, sort_null_only=sort_null_only, per_page=per_page, sort=sort, district=district, page=page, sort_nulls_last=sort_nulls_last, election_full=election_full)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinancialApi->elections_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **office** | **str**| Federal office candidate runs for: H, S or P |
 **cycle** | **int**|  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  |
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **state** | **str**| US state or territory where a candidate runs for office | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-total_receipts&#39;]
 **district** | **str**| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to True]

### Return type

[**ElectionPage**](ElectionPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **elections_search_get**
> ElectionsListPage elections_search_get(api_key, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort=sort, per_page=per_page, office=office, zip=zip, page=page, sort_nulls_last=sort_nulls_last, state=state, district=district, cycle=cycle)



 List elections by cycle, office, state, and district.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openfec_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openfec_sdk.FinancialApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
sort = ["sort_order","district"] # list[str] | Provide a field to sort by. Use - for descending order. (optional) (default to ["sort_order","district"])
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
office = ['office_example'] # list[str] |  (optional)
zip = [56] # list[int] | Zip code (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
state = ['state_example'] # list[str] | US state or territory where a candidate runs for office (optional)
district = ['district_example'] # list[str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
cycle = [56] # list[int] |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.  (optional)

    try:
        api_response = api_instance.elections_search_get(api_key, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort=sort, per_page=per_page, office=office, zip=zip, page=page, sort_nulls_last=sort_nulls_last, state=state, district=district, cycle=cycle)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinancialApi->elections_search_get: %s\n" % e)
```

* Api Key Authentication (ApiKeyQueryAuth):
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openfec_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openfec_sdk.FinancialApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
sort = ["sort_order","district"] # list[str] | Provide a field to sort by. Use - for descending order. (optional) (default to ["sort_order","district"])
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
office = ['office_example'] # list[str] |  (optional)
zip = [56] # list[int] | Zip code (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
state = ['state_example'] # list[str] | US state or territory where a candidate runs for office (optional)
district = ['district_example'] # list[str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
cycle = [56] # list[int] |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.  (optional)

    try:
        api_response = api_instance.elections_search_get(api_key, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort=sort, per_page=per_page, office=office, zip=zip, page=page, sort_nulls_last=sort_nulls_last, state=state, district=district, cycle=cycle)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinancialApi->elections_search_get: %s\n" % e)
```

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openfec_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openfec_sdk.FinancialApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
sort = ["sort_order","district"] # list[str] | Provide a field to sort by. Use - for descending order. (optional) (default to ["sort_order","district"])
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
office = ['office_example'] # list[str] |  (optional)
zip = [56] # list[int] | Zip code (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
state = ['state_example'] # list[str] | US state or territory where a candidate runs for office (optional)
district = ['district_example'] # list[str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
cycle = [56] # list[int] |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.  (optional)

    try:
        api_response = api_instance.elections_search_get(api_key, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort=sort, per_page=per_page, office=office, zip=zip, page=page, sort_nulls_last=sort_nulls_last, state=state, district=district, cycle=cycle)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinancialApi->elections_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort** | [**list[str]**](str.md)| Provide a field to sort by. Use - for descending order. | [optional] [default to [&quot;sort_order&quot;,&quot;district&quot;]]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **office** | [**list[str]**](str.md)|  | [optional]
 **zip** | [**list[int]**](int.md)| Zip code | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **state** | [**list[str]**](str.md)| US state or territory where a candidate runs for office | [optional]
 **district** | [**list[str]**](str.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional]
 **cycle** | [**list[int]**](int.md)|  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | [optional]

### Return type

[**ElectionsListPage**](ElectionsListPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **elections_summary_get**
> ElectionSummary elections_summary_get(api_key, office, cycle, district=district, state=state, election_full=election_full)



 List elections by cycle, office, state, and district.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openfec_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openfec_sdk.FinancialApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
office = 'office_example' # str | Federal office candidate runs for: H, S or P
cycle = 56 # int |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.
district = 'district_example' # str | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
state = 'state_example' # str | US state or territory where a candidate runs for office (optional)
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)

    try:
        api_response = api_instance.elections_summary_get(api_key, office, cycle, district=district, state=state, election_full=election_full)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinancialApi->elections_summary_get: %s\n" % e)
```

* Api Key Authentication (ApiKeyQueryAuth):
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openfec_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openfec_sdk.FinancialApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
office = 'office_example' # str | Federal office candidate runs for: H, S or P
cycle = 56 # int |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.
district = 'district_example' # str | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
state = 'state_example' # str | US state or territory where a candidate runs for office (optional)
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)

    try:
        api_response = api_instance.elections_summary_get(api_key, office, cycle, district=district, state=state, election_full=election_full)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinancialApi->elections_summary_get: %s\n" % e)
```

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openfec_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openfec_sdk.FinancialApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
office = 'office_example' # str | Federal office candidate runs for: H, S or P
cycle = 56 # int |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.
district = 'district_example' # str | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
state = 'state_example' # str | US state or territory where a candidate runs for office (optional)
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)

    try:
        api_response = api_instance.elections_summary_get(api_key, office, cycle, district=district, state=state, election_full=election_full)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinancialApi->elections_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **office** | **str**| Federal office candidate runs for: H, S or P |
 **cycle** | **int**|  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  |
 **district** | **str**| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional]
 **state** | **str**| US state or territory where a candidate runs for office | [optional]
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to True]

### Return type

[**ElectionSummary**](ElectionSummary.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_committee_type_get**
> CommitteeReportsPage reports_committee_type_get(api_key, committee_type, sort_hide_null=sort_hide_null, is_amended=is_amended, min_total_contributions=min_total_contributions, min_cash_on_hand_end_period_amount=min_cash_on_hand_end_period_amount, max_total_contributions=max_total_contributions, page=page, min_receipt_date=min_receipt_date, type=type, beginning_image_number=beginning_image_number, max_debts_owed_expenditures=max_debts_owed_expenditures, max_independent_expenditures=max_independent_expenditures, report_type=report_type, min_independent_expenditures=min_independent_expenditures, min_receipts_amount=min_receipts_amount, per_page=per_page, max_receipts_amount=max_receipts_amount, year=year, sort_nulls_last=sort_nulls_last, amendment_indicator=amendment_indicator, most_recent=most_recent, max_disbursements_amount=max_disbursements_amount, candidate_id=candidate_id, committee_id=committee_id, min_debts_owed_amount=min_debts_owed_amount, cycle=cycle, min_party_coordinated_expenditures=min_party_coordinated_expenditures, max_cash_on_hand_end_period_amount=max_cash_on_hand_end_period_amount, sort_null_only=sort_null_only, sort=sort, max_receipt_date=max_receipt_date, filer_type=filer_type, max_party_coordinated_expenditures=max_party_coordinated_expenditures, min_disbursements_amount=min_disbursements_amount)



 Each report represents the summary information from FEC Form 3, Form 3X and Form 3P. These reports have key statistics that illuminate the financial status of a given committee. Things like cash on hand, debts owed by committee, total receipts, and total disbursements are especially helpful for understanding a committee's financial dealings.  By default, this endpoint includes both amended and final versions of each report. To restrict to only the final versions of each report, use `is_amended=false`; to view only reports that have been amended, use `is_amended=true`.  Several different reporting structures exist, depending on the type of organization that submits financial information. To see an example of these reporting requirements, look at the summary and detailed summary pages of FEC Form 3, Form 3X, and Form 3P.  DISCLAIMER: The field labels contained within this resource are subject to change.  We are attempting to succinctly label these fields while conveying clear meaning to ensure accessibility for all users.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openfec_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openfec_sdk.FinancialApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
committee_type = 'committee_type_example' # str | House, Senate, presidential, independent expenditure only
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
is_amended = True # bool |  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  (optional)
min_total_contributions = 'min_total_contributions_example' # str |  Filter for all amounts greater than a value.  (optional)
min_cash_on_hand_end_period_amount = 'min_cash_on_hand_end_period_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
max_total_contributions = 'max_total_contributions_example' # str |  Filter for all amounts less than a value.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
min_receipt_date = '2013-10-20' # date |  Selects all items received by FEC after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
type = ['type_example'] # list[str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
beginning_image_number = ['beginning_image_number_example'] # list[str] |  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  (optional)
max_debts_owed_expenditures = 'max_debts_owed_expenditures_example' # str |  Filter for all amounts less than a value.  (optional)
max_independent_expenditures = 'max_independent_expenditures_example' # str |  Filter for all amounts less than a value.  (optional)
report_type = ['report_type_example'] # list[str] | Report type; prefix with \"-\" to exclude. Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND  (optional)
min_independent_expenditures = 'min_independent_expenditures_example' # str |  Filter for all amounts greater than a value.  (optional)
min_receipts_amount = 'min_receipts_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
max_receipts_amount = 'max_receipts_amount_example' # str |  Filter for all amounts less than a value.  (optional)
year = [56] # list[int] |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
amendment_indicator = ['amendment_indicator_example'] # list[str] | Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment.  (optional)
most_recent = True # bool |  Report is either new or is the most-recently filed amendment  (optional)
max_disbursements_amount = 'max_disbursements_amount_example' # str |  Filter for all amounts less than a value.  (optional)
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
min_debts_owed_amount = 'min_debts_owed_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
min_party_coordinated_expenditures = 'min_party_coordinated_expenditures_example' # str |  Filter for all amounts greater than a value.  (optional)
max_cash_on_hand_end_period_amount = 'max_cash_on_hand_end_period_amount_example' # str |  Filter for all amounts less than a value.  (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
sort = ["-coverage_end_date"] # list[str] | Provide a field to sort by. Use - for descending order. (optional) (default to ["-coverage_end_date"])
max_receipt_date = '2013-10-20' # date |  Selects all items received by FEC before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
filer_type = 'filer_type_example' # str | The method used to file with the FEC, either electronic or on paper. (optional)
max_party_coordinated_expenditures = 'max_party_coordinated_expenditures_example' # str |  Filter for all amounts less than a value.  (optional)
min_disbursements_amount = 'min_disbursements_amount_example' # str |  Filter for all amounts greater than a value.  (optional)

    try:
        api_response = api_instance.reports_committee_type_get(api_key, committee_type, sort_hide_null=sort_hide_null, is_amended=is_amended, min_total_contributions=min_total_contributions, min_cash_on_hand_end_period_amount=min_cash_on_hand_end_period_amount, max_total_contributions=max_total_contributions, page=page, min_receipt_date=min_receipt_date, type=type, beginning_image_number=beginning_image_number, max_debts_owed_expenditures=max_debts_owed_expenditures, max_independent_expenditures=max_independent_expenditures, report_type=report_type, min_independent_expenditures=min_independent_expenditures, min_receipts_amount=min_receipts_amount, per_page=per_page, max_receipts_amount=max_receipts_amount, year=year, sort_nulls_last=sort_nulls_last, amendment_indicator=amendment_indicator, most_recent=most_recent, max_disbursements_amount=max_disbursements_amount, candidate_id=candidate_id, committee_id=committee_id, min_debts_owed_amount=min_debts_owed_amount, cycle=cycle, min_party_coordinated_expenditures=min_party_coordinated_expenditures, max_cash_on_hand_end_period_amount=max_cash_on_hand_end_period_amount, sort_null_only=sort_null_only, sort=sort, max_receipt_date=max_receipt_date, filer_type=filer_type, max_party_coordinated_expenditures=max_party_coordinated_expenditures, min_disbursements_amount=min_disbursements_amount)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinancialApi->reports_committee_type_get: %s\n" % e)
```

* Api Key Authentication (ApiKeyQueryAuth):
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openfec_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openfec_sdk.FinancialApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
committee_type = 'committee_type_example' # str | House, Senate, presidential, independent expenditure only
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
is_amended = True # bool |  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  (optional)
min_total_contributions = 'min_total_contributions_example' # str |  Filter for all amounts greater than a value.  (optional)
min_cash_on_hand_end_period_amount = 'min_cash_on_hand_end_period_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
max_total_contributions = 'max_total_contributions_example' # str |  Filter for all amounts less than a value.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
min_receipt_date = '2013-10-20' # date |  Selects all items received by FEC after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
type = ['type_example'] # list[str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
beginning_image_number = ['beginning_image_number_example'] # list[str] |  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  (optional)
max_debts_owed_expenditures = 'max_debts_owed_expenditures_example' # str |  Filter for all amounts less than a value.  (optional)
max_independent_expenditures = 'max_independent_expenditures_example' # str |  Filter for all amounts less than a value.  (optional)
report_type = ['report_type_example'] # list[str] | Report type; prefix with \"-\" to exclude. Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND  (optional)
min_independent_expenditures = 'min_independent_expenditures_example' # str |  Filter for all amounts greater than a value.  (optional)
min_receipts_amount = 'min_receipts_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
max_receipts_amount = 'max_receipts_amount_example' # str |  Filter for all amounts less than a value.  (optional)
year = [56] # list[int] |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
amendment_indicator = ['amendment_indicator_example'] # list[str] | Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment.  (optional)
most_recent = True # bool |  Report is either new or is the most-recently filed amendment  (optional)
max_disbursements_amount = 'max_disbursements_amount_example' # str |  Filter for all amounts less than a value.  (optional)
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
min_debts_owed_amount = 'min_debts_owed_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
min_party_coordinated_expenditures = 'min_party_coordinated_expenditures_example' # str |  Filter for all amounts greater than a value.  (optional)
max_cash_on_hand_end_period_amount = 'max_cash_on_hand_end_period_amount_example' # str |  Filter for all amounts less than a value.  (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
sort = ["-coverage_end_date"] # list[str] | Provide a field to sort by. Use - for descending order. (optional) (default to ["-coverage_end_date"])
max_receipt_date = '2013-10-20' # date |  Selects all items received by FEC before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
filer_type = 'filer_type_example' # str | The method used to file with the FEC, either electronic or on paper. (optional)
max_party_coordinated_expenditures = 'max_party_coordinated_expenditures_example' # str |  Filter for all amounts less than a value.  (optional)
min_disbursements_amount = 'min_disbursements_amount_example' # str |  Filter for all amounts greater than a value.  (optional)

    try:
        api_response = api_instance.reports_committee_type_get(api_key, committee_type, sort_hide_null=sort_hide_null, is_amended=is_amended, min_total_contributions=min_total_contributions, min_cash_on_hand_end_period_amount=min_cash_on_hand_end_period_amount, max_total_contributions=max_total_contributions, page=page, min_receipt_date=min_receipt_date, type=type, beginning_image_number=beginning_image_number, max_debts_owed_expenditures=max_debts_owed_expenditures, max_independent_expenditures=max_independent_expenditures, report_type=report_type, min_independent_expenditures=min_independent_expenditures, min_receipts_amount=min_receipts_amount, per_page=per_page, max_receipts_amount=max_receipts_amount, year=year, sort_nulls_last=sort_nulls_last, amendment_indicator=amendment_indicator, most_recent=most_recent, max_disbursements_amount=max_disbursements_amount, candidate_id=candidate_id, committee_id=committee_id, min_debts_owed_amount=min_debts_owed_amount, cycle=cycle, min_party_coordinated_expenditures=min_party_coordinated_expenditures, max_cash_on_hand_end_period_amount=max_cash_on_hand_end_period_amount, sort_null_only=sort_null_only, sort=sort, max_receipt_date=max_receipt_date, filer_type=filer_type, max_party_coordinated_expenditures=max_party_coordinated_expenditures, min_disbursements_amount=min_disbursements_amount)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinancialApi->reports_committee_type_get: %s\n" % e)
```

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openfec_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openfec_sdk.FinancialApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
committee_type = 'committee_type_example' # str | House, Senate, presidential, independent expenditure only
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
is_amended = True # bool |  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  (optional)
min_total_contributions = 'min_total_contributions_example' # str |  Filter for all amounts greater than a value.  (optional)
min_cash_on_hand_end_period_amount = 'min_cash_on_hand_end_period_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
max_total_contributions = 'max_total_contributions_example' # str |  Filter for all amounts less than a value.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
min_receipt_date = '2013-10-20' # date |  Selects all items received by FEC after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
type = ['type_example'] # list[str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
beginning_image_number = ['beginning_image_number_example'] # list[str] |  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  (optional)
max_debts_owed_expenditures = 'max_debts_owed_expenditures_example' # str |  Filter for all amounts less than a value.  (optional)
max_independent_expenditures = 'max_independent_expenditures_example' # str |  Filter for all amounts less than a value.  (optional)
report_type = ['report_type_example'] # list[str] | Report type; prefix with \"-\" to exclude. Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND  (optional)
min_independent_expenditures = 'min_independent_expenditures_example' # str |  Filter for all amounts greater than a value.  (optional)
min_receipts_amount = 'min_receipts_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
max_receipts_amount = 'max_receipts_amount_example' # str |  Filter for all amounts less than a value.  (optional)
year = [56] # list[int] |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
amendment_indicator = ['amendment_indicator_example'] # list[str] | Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment.  (optional)
most_recent = True # bool |  Report is either new or is the most-recently filed amendment  (optional)
max_disbursements_amount = 'max_disbursements_amount_example' # str |  Filter for all amounts less than a value.  (optional)
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
min_debts_owed_amount = 'min_debts_owed_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
min_party_coordinated_expenditures = 'min_party_coordinated_expenditures_example' # str |  Filter for all amounts greater than a value.  (optional)
max_cash_on_hand_end_period_amount = 'max_cash_on_hand_end_period_amount_example' # str |  Filter for all amounts less than a value.  (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
sort = ["-coverage_end_date"] # list[str] | Provide a field to sort by. Use - for descending order. (optional) (default to ["-coverage_end_date"])
max_receipt_date = '2013-10-20' # date |  Selects all items received by FEC before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
filer_type = 'filer_type_example' # str | The method used to file with the FEC, either electronic or on paper. (optional)
max_party_coordinated_expenditures = 'max_party_coordinated_expenditures_example' # str |  Filter for all amounts less than a value.  (optional)
min_disbursements_amount = 'min_disbursements_amount_example' # str |  Filter for all amounts greater than a value.  (optional)

    try:
        api_response = api_instance.reports_committee_type_get(api_key, committee_type, sort_hide_null=sort_hide_null, is_amended=is_amended, min_total_contributions=min_total_contributions, min_cash_on_hand_end_period_amount=min_cash_on_hand_end_period_amount, max_total_contributions=max_total_contributions, page=page, min_receipt_date=min_receipt_date, type=type, beginning_image_number=beginning_image_number, max_debts_owed_expenditures=max_debts_owed_expenditures, max_independent_expenditures=max_independent_expenditures, report_type=report_type, min_independent_expenditures=min_independent_expenditures, min_receipts_amount=min_receipts_amount, per_page=per_page, max_receipts_amount=max_receipts_amount, year=year, sort_nulls_last=sort_nulls_last, amendment_indicator=amendment_indicator, most_recent=most_recent, max_disbursements_amount=max_disbursements_amount, candidate_id=candidate_id, committee_id=committee_id, min_debts_owed_amount=min_debts_owed_amount, cycle=cycle, min_party_coordinated_expenditures=min_party_coordinated_expenditures, max_cash_on_hand_end_period_amount=max_cash_on_hand_end_period_amount, sort_null_only=sort_null_only, sort=sort, max_receipt_date=max_receipt_date, filer_type=filer_type, max_party_coordinated_expenditures=max_party_coordinated_expenditures, min_disbursements_amount=min_disbursements_amount)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinancialApi->reports_committee_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **committee_type** | **str**| House, Senate, presidential, independent expenditure only |
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **is_amended** | **bool**|  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  | [optional]
 **min_total_contributions** | **str**|  Filter for all amounts greater than a value.  | [optional]
 **min_cash_on_hand_end_period_amount** | **str**|  Filter for all amounts greater than a value.  | [optional]
 **max_total_contributions** | **str**|  Filter for all amounts less than a value.  | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **min_receipt_date** | **date**|  Selects all items received by FEC after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **type** | [**list[str]**](str.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional]
 **beginning_image_number** | [**list[str]**](str.md)|  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  | [optional]
 **max_debts_owed_expenditures** | **str**|  Filter for all amounts less than a value.  | [optional]
 **max_independent_expenditures** | **str**|  Filter for all amounts less than a value.  | [optional]
 **report_type** | [**list[str]**](str.md)| Report type; prefix with \&quot;-\&quot; to exclude. Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND  | [optional]
 **min_independent_expenditures** | **str**|  Filter for all amounts greater than a value.  | [optional]
 **min_receipts_amount** | **str**|  Filter for all amounts greater than a value.  | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **max_receipts_amount** | **str**|  Filter for all amounts less than a value.  | [optional]
 **year** | [**list[int]**](int.md)|  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **amendment_indicator** | [**list[str]**](str.md)| Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment.  | [optional]
 **most_recent** | **bool**|  Report is either new or is the most-recently filed amendment  | [optional]
 **max_disbursements_amount** | **str**|  Filter for all amounts less than a value.  | [optional]
 **candidate_id** | **str**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional]
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional]
 **min_debts_owed_amount** | **str**|  Filter for all amounts greater than a value.  | [optional]
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional]
 **min_party_coordinated_expenditures** | **str**|  Filter for all amounts greater than a value.  | [optional]
 **max_cash_on_hand_end_period_amount** | **str**|  Filter for all amounts less than a value.  | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort** | [**list[str]**](str.md)| Provide a field to sort by. Use - for descending order. | [optional] [default to [&quot;-coverage_end_date&quot;]]
 **max_receipt_date** | **date**|  Selects all items received by FEC before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **filer_type** | **str**| The method used to file with the FEC, either electronic or on paper. | [optional]
 **max_party_coordinated_expenditures** | **str**|  Filter for all amounts less than a value.  | [optional]
 **min_disbursements_amount** | **str**|  Filter for all amounts greater than a value.  | [optional]

### Return type

[**CommitteeReportsPage**](CommitteeReportsPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **totals_by_entity_get**
> EntityReceiptDisbursementTotalsPage totals_by_entity_get(api_key, cycle, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, per_page=per_page, sort_nulls_last=sort_nulls_last, sort=sort, page=page)



 Provides cumulative receipt totals by entity type, over a two year cycle. Totals are adjusted to avoid double counting.  This is [the sql](https://github.com/fecgov/openFEC/blob/develop/data/migrations/V41__large_aggregates.sql) that creates these calculations.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openfec_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openfec_sdk.FinancialApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
cycle = 56 # int |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
sort = 'end_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'end_date')
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)

    try:
        api_response = api_instance.totals_by_entity_get(api_key, cycle, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, per_page=per_page, sort_nulls_last=sort_nulls_last, sort=sort, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinancialApi->totals_by_entity_get: %s\n" % e)
```

* Api Key Authentication (ApiKeyQueryAuth):
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openfec_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openfec_sdk.FinancialApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
cycle = 56 # int |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
sort = 'end_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'end_date')
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)

    try:
        api_response = api_instance.totals_by_entity_get(api_key, cycle, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, per_page=per_page, sort_nulls_last=sort_nulls_last, sort=sort, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinancialApi->totals_by_entity_get: %s\n" % e)
```

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openfec_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openfec_sdk.FinancialApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
cycle = 56 # int |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
sort = 'end_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'end_date')
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)

    try:
        api_response = api_instance.totals_by_entity_get(api_key, cycle, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, per_page=per_page, sort_nulls_last=sort_nulls_last, sort=sort, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinancialApi->totals_by_entity_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **cycle** | **int**|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  |
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;end_date&#39;]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]

### Return type

[**EntityReceiptDisbursementTotalsPage**](EntityReceiptDisbursementTotalsPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **totals_committee_type_get**
> CommitteeTotalsPage totals_committee_type_get(api_key, committee_type, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort=sort, per_page=per_page, committee_id=committee_id, sort_nulls_last=sort_nulls_last, page=page, committee_type_full=committee_type_full, committee_designation_full=committee_designation_full, cycle=cycle)



 This endpoint provides information about a committee's Form 3, Form 3X, or Form 3P financial reports, which are aggregated by two-year period. We refer to two-year periods as a `cycle`.  The cycle is named after the even-numbered year and includes the year before it. To see totals from 2013 and 2014, you would use 2014. In odd-numbered years, the current cycle is the next year — for example, in 2015, the current cycle is 2016.  For presidential and Senate candidates, multiple two-year cycles exist between elections.  Parameter `full_election` is replaced by `election_full`. Please use `election_full` instead.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openfec_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openfec_sdk.FinancialApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
committee_type = 'committee_type_example' # str | House, Senate, presidential, independent expenditure only
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
sort = '-cycle' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-cycle')
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
committee_type_full = 'committee_type_full_example' # str | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
committee_designation_full = 'committee_designation_full_example' # str | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)

    try:
        api_response = api_instance.totals_committee_type_get(api_key, committee_type, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort=sort, per_page=per_page, committee_id=committee_id, sort_nulls_last=sort_nulls_last, page=page, committee_type_full=committee_type_full, committee_designation_full=committee_designation_full, cycle=cycle)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinancialApi->totals_committee_type_get: %s\n" % e)
```

* Api Key Authentication (ApiKeyQueryAuth):
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openfec_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openfec_sdk.FinancialApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
committee_type = 'committee_type_example' # str | House, Senate, presidential, independent expenditure only
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
sort = '-cycle' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-cycle')
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
committee_type_full = 'committee_type_full_example' # str | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
committee_designation_full = 'committee_designation_full_example' # str | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)

    try:
        api_response = api_instance.totals_committee_type_get(api_key, committee_type, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort=sort, per_page=per_page, committee_id=committee_id, sort_nulls_last=sort_nulls_last, page=page, committee_type_full=committee_type_full, committee_designation_full=committee_designation_full, cycle=cycle)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinancialApi->totals_committee_type_get: %s\n" % e)
```

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openfec_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openfec_sdk.FinancialApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
committee_type = 'committee_type_example' # str | House, Senate, presidential, independent expenditure only
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
sort = '-cycle' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-cycle')
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
committee_type_full = 'committee_type_full_example' # str | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
committee_designation_full = 'committee_designation_full_example' # str | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)

    try:
        api_response = api_instance.totals_committee_type_get(api_key, committee_type, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, sort=sort, per_page=per_page, committee_id=committee_id, sort_nulls_last=sort_nulls_last, page=page, committee_type_full=committee_type_full, committee_designation_full=committee_designation_full, cycle=cycle)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinancialApi->totals_committee_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **committee_type** | **str**| House, Senate, presidential, independent expenditure only |
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-cycle&#39;]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **committee_id** | **str**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **committee_type_full** | **str**| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional]
 **committee_designation_full** | **str**| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional]
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional]

### Return type

[**CommitteeTotalsPage**](CommitteeTotalsPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
