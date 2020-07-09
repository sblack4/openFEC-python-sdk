# openapi_client.FinancialApi

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
> committee_reports_page.CommitteeReportsPage committee_committee_id_reports_get(committee_id)



 Each report represents the summary information from FEC Form 3, Form 3X and Form 3P. These reports have key statistics that illuminate the financial status of a given committee. Things like cash on hand, debts owed by committee, total receipts, and total disbursements are especially helpful for understanding a committee's financial dealings.  By default, this endpoint includes both amended and final versions of each report. To restrict to only the final versions of each report, use `is_amended=false`; to view only reports that have been amended, use `is_amended=true`.  Several different reporting structures exist, depending on the type of organization that submits financial information. To see an example of these reporting requirements, look at the summary and detailed summary pages of FEC Form 3, Form 3X, and Form 3P.  DISCLAIMER: The field labels contained within this resource are subject to change.  We are attempting to succinctly label these fields while conveying clear meaning to ensure accessibility for all users.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FinancialApi(api_client)
    committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.
    max_receipts_amount = 'max_receipts_amount_example' # str |  Filter for all amounts less than a value.  (optional)
max_debts_owed_expenditures = 'max_debts_owed_expenditures_example' # str |  Filter for all amounts less than a value.  (optional)
type = ['type_example'] # [str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
max_independent_expenditures = 'max_independent_expenditures_example' # str |  Filter for all amounts less than a value.  (optional)
min_party_coordinated_expenditures = 'min_party_coordinated_expenditures_example' # str |  Filter for all amounts greater than a value.  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
sort = ["-coverage_end_date"] # [str], none_type | Provide a field to sort by. Use - for descending order. (optional) if omitted the server will use the default value of ["-coverage_end_date"]
min_receipts_amount = 'min_receipts_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
year = [56] # [int] |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  (optional)
max_cash_on_hand_end_period_amount = 'max_cash_on_hand_end_period_amount_example' # str |  Filter for all amounts less than a value.  (optional)
cycle = [56] # [int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
max_party_coordinated_expenditures = 'max_party_coordinated_expenditures_example' # str |  Filter for all amounts less than a value.  (optional)
max_total_contributions = 'max_total_contributions_example' # str |  Filter for all amounts less than a value.  (optional)
is_amended = True # bool |  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
min_independent_expenditures = 'min_independent_expenditures_example' # str |  Filter for all amounts greater than a value.  (optional)
min_total_contributions = 'min_total_contributions_example' # str |  Filter for all amounts greater than a value.  (optional)
beginning_image_number = ['beginning_image_number_example'] # [str] |  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  (optional)
max_disbursements_amount = 'max_disbursements_amount_example' # str |  Filter for all amounts less than a value.  (optional)
min_cash_on_hand_end_period_amount = 'min_cash_on_hand_end_period_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
min_disbursements_amount = 'min_disbursements_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
min_debts_owed_amount = 'min_debts_owed_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
report_type = ['report_type_example'] # [str] | Report type; prefix with \"-\" to exclude. Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.committee_committee_id_reports_get(committee_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FinancialApi->committee_committee_id_reports_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.committee_committee_id_reports_get(committee_id, max_receipts_amount=max_receipts_amount, max_debts_owed_expenditures=max_debts_owed_expenditures, type=type, page=page, sort_nulls_last=sort_nulls_last, max_independent_expenditures=max_independent_expenditures, min_party_coordinated_expenditures=min_party_coordinated_expenditures, per_page=per_page, sort=sort, min_receipts_amount=min_receipts_amount, sort_hide_null=sort_hide_null, candidate_id=candidate_id, year=year, max_cash_on_hand_end_period_amount=max_cash_on_hand_end_period_amount, cycle=cycle, max_party_coordinated_expenditures=max_party_coordinated_expenditures, max_total_contributions=max_total_contributions, is_amended=is_amended, sort_null_only=sort_null_only, min_independent_expenditures=min_independent_expenditures, min_total_contributions=min_total_contributions, beginning_image_number=beginning_image_number, max_disbursements_amount=max_disbursements_amount, min_cash_on_hand_end_period_amount=min_cash_on_hand_end_period_amount, min_disbursements_amount=min_disbursements_amount, min_debts_owed_amount=min_debts_owed_amount, report_type=report_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FinancialApi->committee_committee_id_reports_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **committee_id** | **str**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  |
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **max_receipts_amount** | **str**|  Filter for all amounts less than a value.  | [optional]
 **max_debts_owed_expenditures** | **str**|  Filter for all amounts less than a value.  | [optional]
 **type** | **[str]**| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **max_independent_expenditures** | **str**|  Filter for all amounts less than a value.  | [optional]
 **min_party_coordinated_expenditures** | **str**|  Filter for all amounts greater than a value.  | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **sort** | **[str], none_type**| Provide a field to sort by. Use - for descending order. | [optional] if omitted the server will use the default value of ["-coverage_end_date"]
 **min_receipts_amount** | **str**|  Filter for all amounts greater than a value.  | [optional]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **candidate_id** | **str**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional]
 **year** | **[int]**|  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional]
 **max_cash_on_hand_end_period_amount** | **str**|  Filter for all amounts less than a value.  | [optional]
 **cycle** | **[int]**|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional]
 **max_party_coordinated_expenditures** | **str**|  Filter for all amounts less than a value.  | [optional]
 **max_total_contributions** | **str**|  Filter for all amounts less than a value.  | [optional]
 **is_amended** | **bool**|  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **min_independent_expenditures** | **str**|  Filter for all amounts greater than a value.  | [optional]
 **min_total_contributions** | **str**|  Filter for all amounts greater than a value.  | [optional]
 **beginning_image_number** | **[str]**|  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  | [optional]
 **max_disbursements_amount** | **str**|  Filter for all amounts less than a value.  | [optional]
 **min_cash_on_hand_end_period_amount** | **str**|  Filter for all amounts greater than a value.  | [optional]
 **min_disbursements_amount** | **str**|  Filter for all amounts greater than a value.  | [optional]
 **min_debts_owed_amount** | **str**|  Filter for all amounts greater than a value.  | [optional]
 **report_type** | **[str]**| Report type; prefix with \&quot;-\&quot; to exclude. Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND  | [optional]

### Return type

[**committee_reports_page.CommitteeReportsPage**](CommitteeReportsPage.md)

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
> committee_totals_page.CommitteeTotalsPage committee_committee_id_totals_get(committee_id)



 This endpoint provides information about a committee's Form 3, Form 3X, or Form 3P financial reports, which are aggregated by two-year period. We refer to two-year periods as a `cycle`.  The cycle is named after the even-numbered year and includes the year before it. To see totals from 2013 and 2014, you would use 2014. In odd-numbered years, the current cycle is the next year — for example, in 2015, the current cycle is 2016.  For presidential and Senate candidates, multiple two-year cycles exist between elections.  Parameter `full_election` is replaced by `election_full`. Please use `election_full` instead.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FinancialApi(api_client)
    committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.
    type = 'type_example' # str | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
designation = 'designation_example' # str | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
sort = '-cycle' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of '-cycle'
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
cycle = [56] # [int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.committee_committee_id_totals_get(committee_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FinancialApi->committee_committee_id_totals_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.committee_committee_id_totals_get(committee_id, type=type, page=page, sort_nulls_last=sort_nulls_last, designation=designation, sort_null_only=sort_null_only, per_page=per_page, sort=sort, sort_hide_null=sort_hide_null, cycle=cycle)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FinancialApi->committee_committee_id_totals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **committee_id** | **str**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  |
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **type** | **str**| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **designation** | **str**| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of '-cycle'
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **cycle** | **[int]**|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional]

### Return type

[**committee_totals_page.CommitteeTotalsPage**](CommitteeTotalsPage.md)

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
> election_page.ElectionPage elections_get(cycle, office)



 Look at the top-level financial information for all candidates running for the same office.  Choose a 2-year cycle, and `house`, `senate` or `presidential`.  If you are looking for a Senate seat, you will need to select the state using a two-letter abbreviation.  House races require state and a two-digit district number.  Since this endpoint reflects financial information, it will only have candidates once they file financial reporting forms. Query the `/candidates` endpoint to see an up to date list of all the candidates that filed to run for a particular seat.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FinancialApi(api_client)
    cycle = 56 # int |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.
    office = 'office_example' # str | Federal office candidate runs for: H, S or P
    page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) if omitted the server will use the default value of True
district = 'district_example' # str | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
sort = '-total_receipts' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of '-total_receipts'
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
state = 'state_example' # str | US state or territory where a candidate runs for office (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.elections_get(cycle, office)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FinancialApi->elections_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.elections_get(cycle, office, page=page, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, election_full=election_full, district=district, per_page=per_page, sort=sort, sort_hide_null=sort_hide_null, state=state)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FinancialApi->elections_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cycle** | **int**|  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  |
 **office** | **str**| Federal office candidate runs for: H, S or P |
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] if omitted the server will use the default value of True
 **district** | **str**| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of '-total_receipts'
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **state** | **str**| US state or territory where a candidate runs for office | [optional]

### Return type

[**election_page.ElectionPage**](ElectionPage.md)

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
> elections_list_page.ElectionsListPage elections_search_get()



 List elections by cycle, office, state, and district.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FinancialApi(api_client)
    page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
district = ['district_example'] # [str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
state = ['state_example'] # [str] | US state or territory where a candidate runs for office (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
zip = [56] # [int] | Zip code (optional)
sort = ["sort_order","district"] # [str], none_type | Provide a field to sort by. Use - for descending order. (optional) if omitted the server will use the default value of ["sort_order","district"]
office = ['office_example'] # [str] |  (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
cycle = [56] # [int] |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.elections_search_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FinancialApi->elections_search_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.elections_search_get(page=page, sort_nulls_last=sort_nulls_last, sort_null_only=sort_null_only, district=district, state=state, per_page=per_page, zip=zip, sort=sort, office=office, sort_hide_null=sort_hide_null, cycle=cycle)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FinancialApi->elections_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **district** | **[str]**| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional]
 **state** | **[str]**| US state or territory where a candidate runs for office | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **zip** | **[int]**| Zip code | [optional]
 **sort** | **[str], none_type**| Provide a field to sort by. Use - for descending order. | [optional] if omitted the server will use the default value of ["sort_order","district"]
 **office** | **[str]**|  | [optional]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **cycle** | **[int]**|  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | [optional]

### Return type

[**elections_list_page.ElectionsListPage**](ElectionsListPage.md)

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
> election_summary.ElectionSummary elections_summary_get(cycle, office)



 List elections by cycle, office, state, and district.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FinancialApi(api_client)
    cycle = 56 # int |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.
    office = 'office_example' # str | Federal office candidate runs for: H, S or P
    election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) if omitted the server will use the default value of True
district = 'district_example' # str | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
state = 'state_example' # str | US state or territory where a candidate runs for office (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.elections_summary_get(cycle, office)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FinancialApi->elections_summary_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.elections_summary_get(cycle, office, election_full=election_full, district=district, state=state)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FinancialApi->elections_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cycle** | **int**|  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  |
 **office** | **str**| Federal office candidate runs for: H, S or P |
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] if omitted the server will use the default value of True
 **district** | **str**| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional]
 **state** | **str**| US state or territory where a candidate runs for office | [optional]

### Return type

[**election_summary.ElectionSummary**](ElectionSummary.md)

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
> committee_reports_page.CommitteeReportsPage reports_committee_type_get(committee_type)



 Each report represents the summary information from FEC Form 3, Form 3X and Form 3P. These reports have key statistics that illuminate the financial status of a given committee. Things like cash on hand, debts owed by committee, total receipts, and total disbursements are especially helpful for understanding a committee's financial dealings.  By default, this endpoint includes both amended and final versions of each report. To restrict to only the final versions of each report, use `is_amended=false`; to view only reports that have been amended, use `is_amended=true`.  Several different reporting structures exist, depending on the type of organization that submits financial information. To see an example of these reporting requirements, look at the summary and detailed summary pages of FEC Form 3, Form 3X, and Form 3P.  DISCLAIMER: The field labels contained within this resource are subject to change.  We are attempting to succinctly label these fields while conveying clear meaning to ensure accessibility for all users.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FinancialApi(api_client)
    committee_type = 'committee_type_example' # str | House, Senate, presidential, independent expenditure only
    max_receipts_amount = 'max_receipts_amount_example' # str |  Filter for all amounts less than a value.  (optional)
max_debts_owed_expenditures = 'max_debts_owed_expenditures_example' # str |  Filter for all amounts less than a value.  (optional)
committee_id = ['committee_id_example'] # [str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
max_independent_expenditures = 'max_independent_expenditures_example' # str |  Filter for all amounts less than a value.  (optional)
filer_type = 'filer_type_example' # str | The method used to file with the FEC, either electronic or on paper. (optional)
sort = ["-coverage_end_date"] # [str], none_type | Provide a field to sort by. Use - for descending order. (optional) if omitted the server will use the default value of ["-coverage_end_date"]
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
year = [56] # [int] |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  (optional)
cycle = [56] # [int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
max_total_contributions = 'max_total_contributions_example' # str |  Filter for all amounts less than a value.  (optional)
is_amended = True # bool |  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  (optional)
min_independent_expenditures = 'min_independent_expenditures_example' # str |  Filter for all amounts greater than a value.  (optional)
min_total_contributions = 'min_total_contributions_example' # str |  Filter for all amounts greater than a value.  (optional)
beginning_image_number = ['beginning_image_number_example'] # [str] |  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  (optional)
max_disbursements_amount = 'max_disbursements_amount_example' # str |  Filter for all amounts less than a value.  (optional)
min_disbursements_amount = 'min_disbursements_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
min_cash_on_hand_end_period_amount = 'min_cash_on_hand_end_period_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
report_type = ['report_type_example'] # [str] | Report type; prefix with \"-\" to exclude. Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND  (optional)
type = ['type_example'] # [str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
min_party_coordinated_expenditures = 'min_party_coordinated_expenditures_example' # str |  Filter for all amounts greater than a value.  (optional)
amendment_indicator = ['amendment_indicator_example'] # [str] | Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment.  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
most_recent = True # bool |  Report is either new or is the most-recently filed amendment  (optional)
min_receipts_amount = 'min_receipts_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
max_cash_on_hand_end_period_amount = 'max_cash_on_hand_end_period_amount_example' # str |  Filter for all amounts less than a value.  (optional)
max_party_coordinated_expenditures = 'max_party_coordinated_expenditures_example' # str |  Filter for all amounts less than a value.  (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
min_debts_owed_amount = 'min_debts_owed_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
max_receipt_date = '2013-10-20' # date |  Selects all items received by FEC before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
min_receipt_date = '2013-10-20' # date |  Selects all items received by FEC after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.reports_committee_type_get(committee_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FinancialApi->reports_committee_type_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.reports_committee_type_get(committee_type, max_receipts_amount=max_receipts_amount, max_debts_owed_expenditures=max_debts_owed_expenditures, committee_id=committee_id, max_independent_expenditures=max_independent_expenditures, filer_type=filer_type, sort=sort, sort_hide_null=sort_hide_null, year=year, cycle=cycle, max_total_contributions=max_total_contributions, is_amended=is_amended, min_independent_expenditures=min_independent_expenditures, min_total_contributions=min_total_contributions, beginning_image_number=beginning_image_number, max_disbursements_amount=max_disbursements_amount, min_disbursements_amount=min_disbursements_amount, min_cash_on_hand_end_period_amount=min_cash_on_hand_end_period_amount, report_type=report_type, type=type, page=page, sort_nulls_last=sort_nulls_last, min_party_coordinated_expenditures=min_party_coordinated_expenditures, amendment_indicator=amendment_indicator, per_page=per_page, most_recent=most_recent, min_receipts_amount=min_receipts_amount, candidate_id=candidate_id, max_cash_on_hand_end_period_amount=max_cash_on_hand_end_period_amount, max_party_coordinated_expenditures=max_party_coordinated_expenditures, sort_null_only=sort_null_only, min_debts_owed_amount=min_debts_owed_amount, max_receipt_date=max_receipt_date, min_receipt_date=min_receipt_date)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FinancialApi->reports_committee_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **committee_type** | **str**| House, Senate, presidential, independent expenditure only |
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **max_receipts_amount** | **str**|  Filter for all amounts less than a value.  | [optional]
 **max_debts_owed_expenditures** | **str**|  Filter for all amounts less than a value.  | [optional]
 **committee_id** | **[str]**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional]
 **max_independent_expenditures** | **str**|  Filter for all amounts less than a value.  | [optional]
 **filer_type** | **str**| The method used to file with the FEC, either electronic or on paper. | [optional]
 **sort** | **[str], none_type**| Provide a field to sort by. Use - for descending order. | [optional] if omitted the server will use the default value of ["-coverage_end_date"]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **year** | **[int]**|  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional]
 **cycle** | **[int]**|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional]
 **max_total_contributions** | **str**|  Filter for all amounts less than a value.  | [optional]
 **is_amended** | **bool**|  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  | [optional]
 **min_independent_expenditures** | **str**|  Filter for all amounts greater than a value.  | [optional]
 **min_total_contributions** | **str**|  Filter for all amounts greater than a value.  | [optional]
 **beginning_image_number** | **[str]**|  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  | [optional]
 **max_disbursements_amount** | **str**|  Filter for all amounts less than a value.  | [optional]
 **min_disbursements_amount** | **str**|  Filter for all amounts greater than a value.  | [optional]
 **min_cash_on_hand_end_period_amount** | **str**|  Filter for all amounts greater than a value.  | [optional]
 **report_type** | **[str]**| Report type; prefix with \&quot;-\&quot; to exclude. Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND  | [optional]
 **type** | **[str]**| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **min_party_coordinated_expenditures** | **str**|  Filter for all amounts greater than a value.  | [optional]
 **amendment_indicator** | **[str]**| Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment.  | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **most_recent** | **bool**|  Report is either new or is the most-recently filed amendment  | [optional]
 **min_receipts_amount** | **str**|  Filter for all amounts greater than a value.  | [optional]
 **candidate_id** | **str**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional]
 **max_cash_on_hand_end_period_amount** | **str**|  Filter for all amounts less than a value.  | [optional]
 **max_party_coordinated_expenditures** | **str**|  Filter for all amounts less than a value.  | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **min_debts_owed_amount** | **str**|  Filter for all amounts greater than a value.  | [optional]
 **max_receipt_date** | **date**|  Selects all items received by FEC before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **min_receipt_date** | **date**|  Selects all items received by FEC after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional]

### Return type

[**committee_reports_page.CommitteeReportsPage**](CommitteeReportsPage.md)

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
> entity_receipt_disbursement_totals_page.EntityReceiptDisbursementTotalsPage totals_by_entity_get(cycle)



 Provides cumulative receipt totals by entity type, over a two year cycle. Totals are adjusted to avoid double counting.  This is [the sql](https://github.com/fecgov/openFEC/blob/develop/data/migrations/V41__large_aggregates.sql) that creates these calculations.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FinancialApi(api_client)
    cycle = 56 # int |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
sort = 'end_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of 'end_date'
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.totals_by_entity_get(cycle)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FinancialApi->totals_by_entity_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.totals_by_entity_get(cycle, per_page=per_page, page=page, sort_nulls_last=sort_nulls_last, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FinancialApi->totals_by_entity_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cycle** | **int**|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  |
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of 'end_date'
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False

### Return type

[**entity_receipt_disbursement_totals_page.EntityReceiptDisbursementTotalsPage**](EntityReceiptDisbursementTotalsPage.md)

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
> committee_totals_page.CommitteeTotalsPage totals_committee_type_get(committee_type)



 This endpoint provides information about a committee's Form 3, Form 3X, or Form 3P financial reports, which are aggregated by two-year period. We refer to two-year periods as a `cycle`.  The cycle is named after the even-numbered year and includes the year before it. To see totals from 2013 and 2014, you would use 2014. In odd-numbered years, the current cycle is the next year — for example, in 2015, the current cycle is 2016.  For presidential and Senate candidates, multiple two-year cycles exist between elections.  Parameter `full_election` is replaced by `election_full`. Please use `election_full` instead.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FinancialApi(api_client)
    committee_type = 'committee_type_example' # str | House, Senate, presidential, independent expenditure only
    page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
committee_designation_full = 'committee_designation_full_example' # str | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
sort = '-cycle' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of '-cycle'
committee_type_full = 'committee_type_full_example' # str | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
cycle = [56] # [int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.totals_committee_type_get(committee_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FinancialApi->totals_committee_type_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.totals_committee_type_get(committee_type, page=page, committee_id=committee_id, sort_nulls_last=sort_nulls_last, committee_designation_full=committee_designation_full, sort_null_only=sort_null_only, per_page=per_page, sort=sort, committee_type_full=committee_type_full, sort_hide_null=sort_hide_null, cycle=cycle)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FinancialApi->totals_committee_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **committee_type** | **str**| House, Senate, presidential, independent expenditure only |
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **committee_id** | **str**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **committee_designation_full** | **str**| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of '-cycle'
 **committee_type_full** | **str**| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **cycle** | **[int]**|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional]

### Return type

[**committee_totals_page.CommitteeTotalsPage**](CommitteeTotalsPage.md)

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
