# swagger_client.FinancialApi

All URIs are relative to *https://localhost/v1*

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
> CommitteeReportsPage committee_committee_id_reports_get(api_key, committee_id, min_cash_on_hand_end_period_amount=min_cash_on_hand_end_period_amount, cycle=cycle, sort=sort, year=year, beginning_image_number=beginning_image_number, max_debts_owed_expenditures=max_debts_owed_expenditures, max_party_coordinated_expenditures=max_party_coordinated_expenditures, min_disbursements_amount=min_disbursements_amount, is_amended=is_amended, sort_nulls_last=sort_nulls_last, sort_hide_null=sort_hide_null, max_receipts_amount=max_receipts_amount, report_type=report_type, min_debts_owed_amount=min_debts_owed_amount, max_disbursements_amount=max_disbursements_amount, max_independent_expenditures=max_independent_expenditures, per_page=per_page, type=type, candidate_id=candidate_id, min_total_contributions=min_total_contributions, min_receipts_amount=min_receipts_amount, page=page, min_party_coordinated_expenditures=min_party_coordinated_expenditures, max_cash_on_hand_end_period_amount=max_cash_on_hand_end_period_amount, max_total_contributions=max_total_contributions, sort_null_only=sort_null_only, min_independent_expenditures=min_independent_expenditures)



 Each report represents the summary information from FEC Form 3, Form 3X and Form 3P. These reports have key statistics that illuminate the financial status of a given committee. Things like cash on hand, debts owed by committee, total receipts, and total disbursements are especially helpful for understanding a committee's financial dealings.  By default, this endpoint includes both amended and final versions of each report. To restrict to only the final versions of each report, use `is_amended=false`; to view only reports that have been amended, use `is_amended=true`.  Several different reporting structures exist, depending on the type of organization that submits financial information. To see an example of these reporting requirements, look at the summary and detailed summary pages of FEC Form 3, Form 3X, and Form 3P.  DISCLAIMER: The field labels contained within this resource are subject to change.  We are attempting to succinctly label these fields while conveying clear meaning to ensure accessibility for all users. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyHeaderAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'
# Configure API key authorization: ApiKeyQueryAuth
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.FinancialApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
min_cash_on_hand_end_period_amount = 'min_cash_on_hand_end_period_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
sort = ['[-coverage_end_date]'] # list[str] | Provide a field to sort by. Use - for descending order. (optional) (default to [-coverage_end_date])
year = [56] # list[int] |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  (optional)
beginning_image_number = ['beginning_image_number_example'] # list[str] |  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  (optional)
max_debts_owed_expenditures = 'max_debts_owed_expenditures_example' # str |  Filter for all amounts less than a value.  (optional)
max_party_coordinated_expenditures = 'max_party_coordinated_expenditures_example' # str |  Filter for all amounts less than a value.  (optional)
min_disbursements_amount = 'min_disbursements_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
is_amended = true # bool |  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  (optional)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
max_receipts_amount = 'max_receipts_amount_example' # str |  Filter for all amounts less than a value.  (optional)
report_type = ['report_type_example'] # list[str] | Report type; prefix with \"-\" to exclude. Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND  (optional)
min_debts_owed_amount = 'min_debts_owed_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
max_disbursements_amount = 'max_disbursements_amount_example' # str |  Filter for all amounts less than a value.  (optional)
max_independent_expenditures = 'max_independent_expenditures_example' # str |  Filter for all amounts less than a value.  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
type = ['type_example'] # list[str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
min_total_contributions = 'min_total_contributions_example' # str |  Filter for all amounts greater than a value.  (optional)
min_receipts_amount = 'min_receipts_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
min_party_coordinated_expenditures = 'min_party_coordinated_expenditures_example' # str |  Filter for all amounts greater than a value.  (optional)
max_cash_on_hand_end_period_amount = 'max_cash_on_hand_end_period_amount_example' # str |  Filter for all amounts less than a value.  (optional)
max_total_contributions = 'max_total_contributions_example' # str |  Filter for all amounts less than a value.  (optional)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
min_independent_expenditures = 'min_independent_expenditures_example' # str |  Filter for all amounts greater than a value.  (optional)

try:
    api_response = api_instance.committee_committee_id_reports_get(api_key, committee_id, min_cash_on_hand_end_period_amount=min_cash_on_hand_end_period_amount, cycle=cycle, sort=sort, year=year, beginning_image_number=beginning_image_number, max_debts_owed_expenditures=max_debts_owed_expenditures, max_party_coordinated_expenditures=max_party_coordinated_expenditures, min_disbursements_amount=min_disbursements_amount, is_amended=is_amended, sort_nulls_last=sort_nulls_last, sort_hide_null=sort_hide_null, max_receipts_amount=max_receipts_amount, report_type=report_type, min_debts_owed_amount=min_debts_owed_amount, max_disbursements_amount=max_disbursements_amount, max_independent_expenditures=max_independent_expenditures, per_page=per_page, type=type, candidate_id=candidate_id, min_total_contributions=min_total_contributions, min_receipts_amount=min_receipts_amount, page=page, min_party_coordinated_expenditures=min_party_coordinated_expenditures, max_cash_on_hand_end_period_amount=max_cash_on_hand_end_period_amount, max_total_contributions=max_total_contributions, sort_null_only=sort_null_only, min_independent_expenditures=min_independent_expenditures)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancialApi->committee_committee_id_reports_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **committee_id** | **str**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | 
 **min_cash_on_hand_end_period_amount** | **str**|  Filter for all amounts greater than a value.  | [optional] 
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sort** | [**list[str]**](str.md)| Provide a field to sort by. Use - for descending order. | [optional] [default to [-coverage_end_date]]
 **year** | [**list[int]**](int.md)|  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional] 
 **beginning_image_number** | [**list[str]**](str.md)|  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  | [optional] 
 **max_debts_owed_expenditures** | **str**|  Filter for all amounts less than a value.  | [optional] 
 **max_party_coordinated_expenditures** | **str**|  Filter for all amounts less than a value.  | [optional] 
 **min_disbursements_amount** | **str**|  Filter for all amounts greater than a value.  | [optional] 
 **is_amended** | **bool**|  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  | [optional] 
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **max_receipts_amount** | **str**|  Filter for all amounts less than a value.  | [optional] 
 **report_type** | [**list[str]**](str.md)| Report type; prefix with \&quot;-\&quot; to exclude. Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND  | [optional] 
 **min_debts_owed_amount** | **str**|  Filter for all amounts greater than a value.  | [optional] 
 **max_disbursements_amount** | **str**|  Filter for all amounts less than a value.  | [optional] 
 **max_independent_expenditures** | **str**|  Filter for all amounts less than a value.  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **type** | [**list[str]**](str.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **candidate_id** | **str**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional] 
 **min_total_contributions** | **str**|  Filter for all amounts greater than a value.  | [optional] 
 **min_receipts_amount** | **str**|  Filter for all amounts greater than a value.  | [optional] 
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **min_party_coordinated_expenditures** | **str**|  Filter for all amounts greater than a value.  | [optional] 
 **max_cash_on_hand_end_period_amount** | **str**|  Filter for all amounts less than a value.  | [optional] 
 **max_total_contributions** | **str**|  Filter for all amounts less than a value.  | [optional] 
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **min_independent_expenditures** | **str**|  Filter for all amounts greater than a value.  | [optional] 

### Return type

[**CommitteeReportsPage**](CommitteeReportsPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **committee_committee_id_totals_get**
> CommitteeTotalsPage committee_committee_id_totals_get(api_key, committee_id, per_page=per_page, designation=designation, cycle=cycle, sort=sort, type=type, sort_nulls_last=sort_nulls_last, page=page, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)



 This endpoint provides information about a committee's Form 3, Form 3X, or Form 3P financial reports, which are aggregated by two-year period. We refer to two-year periods as a `cycle`.  The cycle is named after the even-numbered year and includes the year before it. To see totals from 2013 and 2014, you would use 2014. In odd-numbered years, the current cycle is the next year — for example, in 2015, the current cycle is 2016.  For presidential and Senate candidates, multiple two-year cycles exist between elections.  Parameter `full_election` is replaced by `election_full`. Please use `election_full` instead. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyHeaderAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'
# Configure API key authorization: ApiKeyQueryAuth
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.FinancialApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
designation = 'designation_example' # str | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
sort = '-cycle' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -cycle)
type = 'type_example' # str | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)

try:
    api_response = api_instance.committee_committee_id_totals_get(api_key, committee_id, per_page=per_page, designation=designation, cycle=cycle, sort=sort, type=type, sort_nulls_last=sort_nulls_last, page=page, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancialApi->committee_committee_id_totals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **committee_id** | **str**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **designation** | **str**| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -cycle]
 **type** | **str**| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]

### Return type

[**CommitteeTotalsPage**](CommitteeTotalsPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **elections_get**
> ElectionPage elections_get(cycle, office, api_key, per_page=per_page, sort=sort, state=state, district=district, election_full=election_full, page=page, sort_nulls_last=sort_nulls_last, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)



 Look at the top-level financial information for all candidates running for the same office.  Choose a 2-year cycle, and `house`, `senate` or `presidential`.  If you are looking for a Senate seat, you will need to select the state using a two-letter abbreviation.  House races require state and a two-digit district number.  Since this endpoint reflects financial information, it will only have candidates once they file financial reporting forms. Query the `/candidates` endpoint to see an up to date list of all the candidates that filed to run for a particular seat. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyHeaderAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'
# Configure API key authorization: ApiKeyQueryAuth
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.FinancialApi(swagger_client.ApiClient(configuration))
cycle = 56 # int |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag. 
office = 'office_example' # str | Federal office candidate runs for: H, S or P
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort = '-total_receipts' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -total_receipts)
state = 'state_example' # str | US state or territory where a candidate runs for office (optional)
district = 'district_example' # str | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
election_full = true # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to true)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)

try:
    api_response = api_instance.elections_get(cycle, office, api_key, per_page=per_page, sort=sort, state=state, district=district, election_full=election_full, page=page, sort_nulls_last=sort_nulls_last, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancialApi->elections_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cycle** | **int**|  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | 
 **office** | **str**| Federal office candidate runs for: H, S or P | 
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -total_receipts]
 **state** | **str**| US state or territory where a candidate runs for office | [optional] 
 **district** | **str**| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]

### Return type

[**ElectionPage**](ElectionPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **elections_search_get**
> ElectionsListPage elections_search_get(api_key, cycle=cycle, per_page=per_page, sort=sort, office=office, state=state, zip=zip, district=district, sort_nulls_last=sort_nulls_last, page=page, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)



 List elections by cycle, office, state, and district. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyHeaderAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'
# Configure API key authorization: ApiKeyQueryAuth
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.FinancialApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
cycle = [56] # list[int] |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort = ['[sort_order, district]'] # list[str] | Provide a field to sort by. Use - for descending order. (optional) (default to [sort_order, district])
office = ['office_example'] # list[str] |  (optional)
state = ['state_example'] # list[str] | US state or territory where a candidate runs for office (optional)
zip = [56] # list[int] | Zip code (optional)
district = ['district_example'] # list[str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)

try:
    api_response = api_instance.elections_search_get(api_key, cycle=cycle, per_page=per_page, sort=sort, office=office, state=state, zip=zip, district=district, sort_nulls_last=sort_nulls_last, page=page, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancialApi->elections_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **cycle** | [**list[int]**](int.md)|  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | [**list[str]**](str.md)| Provide a field to sort by. Use - for descending order. | [optional] [default to [sort_order, district]]
 **office** | [**list[str]**](str.md)|  | [optional] 
 **state** | [**list[str]**](str.md)| US state or territory where a candidate runs for office | [optional] 
 **zip** | [**list[int]**](int.md)| Zip code | [optional] 
 **district** | [**list[str]**](str.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]

### Return type

[**ElectionsListPage**](ElectionsListPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **elections_summary_get**
> ElectionSummary elections_summary_get(api_key, cycle, office, district=district, election_full=election_full, state=state)



 List elections by cycle, office, state, and district. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyHeaderAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'
# Configure API key authorization: ApiKeyQueryAuth
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.FinancialApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
cycle = 56 # int |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag. 
office = 'office_example' # str | Federal office candidate runs for: H, S or P
district = 'district_example' # str | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
election_full = true # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to true)
state = 'state_example' # str | US state or territory where a candidate runs for office (optional)

try:
    api_response = api_instance.elections_summary_get(api_key, cycle, office, district=district, election_full=election_full, state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancialApi->elections_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **cycle** | **int**|  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | 
 **office** | **str**| Federal office candidate runs for: H, S or P | 
 **district** | **str**| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **state** | **str**| US state or territory where a candidate runs for office | [optional] 

### Return type

[**ElectionSummary**](ElectionSummary.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_committee_type_get**
> CommitteeReportsPage reports_committee_type_get(api_key, committee_type, sort=sort, beginning_image_number=beginning_image_number, max_debts_owed_expenditures=max_debts_owed_expenditures, max_party_coordinated_expenditures=max_party_coordinated_expenditures, min_disbursements_amount=min_disbursements_amount, is_amended=is_amended, max_receipts_amount=max_receipts_amount, min_debts_owed_amount=min_debts_owed_amount, min_receipt_date=min_receipt_date, max_disbursements_amount=max_disbursements_amount, max_independent_expenditures=max_independent_expenditures, committee_id=committee_id, type=type, candidate_id=candidate_id, min_total_contributions=min_total_contributions, page=page, min_party_coordinated_expenditures=min_party_coordinated_expenditures, sort_null_only=sort_null_only, min_independent_expenditures=min_independent_expenditures, min_cash_on_hand_end_period_amount=min_cash_on_hand_end_period_amount, cycle=cycle, year=year, sort_nulls_last=sort_nulls_last, filer_type=filer_type, sort_hide_null=sort_hide_null, amendment_indicator=amendment_indicator, report_type=report_type, most_recent=most_recent, per_page=per_page, min_receipts_amount=min_receipts_amount, max_cash_on_hand_end_period_amount=max_cash_on_hand_end_period_amount, max_receipt_date=max_receipt_date, max_total_contributions=max_total_contributions)



 Each report represents the summary information from FEC Form 3, Form 3X and Form 3P. These reports have key statistics that illuminate the financial status of a given committee. Things like cash on hand, debts owed by committee, total receipts, and total disbursements are especially helpful for understanding a committee's financial dealings.  By default, this endpoint includes both amended and final versions of each report. To restrict to only the final versions of each report, use `is_amended=false`; to view only reports that have been amended, use `is_amended=true`.  Several different reporting structures exist, depending on the type of organization that submits financial information. To see an example of these reporting requirements, look at the summary and detailed summary pages of FEC Form 3, Form 3X, and Form 3P.  DISCLAIMER: The field labels contained within this resource are subject to change.  We are attempting to succinctly label these fields while conveying clear meaning to ensure accessibility for all users. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyHeaderAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'
# Configure API key authorization: ApiKeyQueryAuth
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.FinancialApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
committee_type = 'committee_type_example' # str | House, Senate, presidential, independent expenditure only
sort = ['[-coverage_end_date]'] # list[str] | Provide a field to sort by. Use - for descending order. (optional) (default to [-coverage_end_date])
beginning_image_number = ['beginning_image_number_example'] # list[str] |  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  (optional)
max_debts_owed_expenditures = 'max_debts_owed_expenditures_example' # str |  Filter for all amounts less than a value.  (optional)
max_party_coordinated_expenditures = 'max_party_coordinated_expenditures_example' # str |  Filter for all amounts less than a value.  (optional)
min_disbursements_amount = 'min_disbursements_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
is_amended = true # bool |  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  (optional)
max_receipts_amount = 'max_receipts_amount_example' # str |  Filter for all amounts less than a value.  (optional)
min_debts_owed_amount = 'min_debts_owed_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
min_receipt_date = '2013-10-20' # date |  Selects all items received by FEC after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
max_disbursements_amount = 'max_disbursements_amount_example' # str |  Filter for all amounts less than a value.  (optional)
max_independent_expenditures = 'max_independent_expenditures_example' # str |  Filter for all amounts less than a value.  (optional)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
type = ['type_example'] # list[str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
min_total_contributions = 'min_total_contributions_example' # str |  Filter for all amounts greater than a value.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
min_party_coordinated_expenditures = 'min_party_coordinated_expenditures_example' # str |  Filter for all amounts greater than a value.  (optional)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
min_independent_expenditures = 'min_independent_expenditures_example' # str |  Filter for all amounts greater than a value.  (optional)
min_cash_on_hand_end_period_amount = 'min_cash_on_hand_end_period_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
year = [56] # list[int] |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  (optional)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
filer_type = 'filer_type_example' # str | The method used to file with the FEC, either electronic or on paper. (optional)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
amendment_indicator = ['amendment_indicator_example'] # list[str] | Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment.  (optional)
report_type = ['report_type_example'] # list[str] | Report type; prefix with \"-\" to exclude. Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND  (optional)
most_recent = true # bool |  Report is either new or is the most-recently filed amendment  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
min_receipts_amount = 'min_receipts_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
max_cash_on_hand_end_period_amount = 'max_cash_on_hand_end_period_amount_example' # str |  Filter for all amounts less than a value.  (optional)
max_receipt_date = '2013-10-20' # date |  Selects all items received by FEC before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
max_total_contributions = 'max_total_contributions_example' # str |  Filter for all amounts less than a value.  (optional)

try:
    api_response = api_instance.reports_committee_type_get(api_key, committee_type, sort=sort, beginning_image_number=beginning_image_number, max_debts_owed_expenditures=max_debts_owed_expenditures, max_party_coordinated_expenditures=max_party_coordinated_expenditures, min_disbursements_amount=min_disbursements_amount, is_amended=is_amended, max_receipts_amount=max_receipts_amount, min_debts_owed_amount=min_debts_owed_amount, min_receipt_date=min_receipt_date, max_disbursements_amount=max_disbursements_amount, max_independent_expenditures=max_independent_expenditures, committee_id=committee_id, type=type, candidate_id=candidate_id, min_total_contributions=min_total_contributions, page=page, min_party_coordinated_expenditures=min_party_coordinated_expenditures, sort_null_only=sort_null_only, min_independent_expenditures=min_independent_expenditures, min_cash_on_hand_end_period_amount=min_cash_on_hand_end_period_amount, cycle=cycle, year=year, sort_nulls_last=sort_nulls_last, filer_type=filer_type, sort_hide_null=sort_hide_null, amendment_indicator=amendment_indicator, report_type=report_type, most_recent=most_recent, per_page=per_page, min_receipts_amount=min_receipts_amount, max_cash_on_hand_end_period_amount=max_cash_on_hand_end_period_amount, max_receipt_date=max_receipt_date, max_total_contributions=max_total_contributions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancialApi->reports_committee_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **committee_type** | **str**| House, Senate, presidential, independent expenditure only | 
 **sort** | [**list[str]**](str.md)| Provide a field to sort by. Use - for descending order. | [optional] [default to [-coverage_end_date]]
 **beginning_image_number** | [**list[str]**](str.md)|  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  | [optional] 
 **max_debts_owed_expenditures** | **str**|  Filter for all amounts less than a value.  | [optional] 
 **max_party_coordinated_expenditures** | **str**|  Filter for all amounts less than a value.  | [optional] 
 **min_disbursements_amount** | **str**|  Filter for all amounts greater than a value.  | [optional] 
 **is_amended** | **bool**|  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  | [optional] 
 **max_receipts_amount** | **str**|  Filter for all amounts less than a value.  | [optional] 
 **min_debts_owed_amount** | **str**|  Filter for all amounts greater than a value.  | [optional] 
 **min_receipt_date** | **date**|  Selects all items received by FEC after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **max_disbursements_amount** | **str**|  Filter for all amounts less than a value.  | [optional] 
 **max_independent_expenditures** | **str**|  Filter for all amounts less than a value.  | [optional] 
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **type** | [**list[str]**](str.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **candidate_id** | **str**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional] 
 **min_total_contributions** | **str**|  Filter for all amounts greater than a value.  | [optional] 
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **min_party_coordinated_expenditures** | **str**|  Filter for all amounts greater than a value.  | [optional] 
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **min_independent_expenditures** | **str**|  Filter for all amounts greater than a value.  | [optional] 
 **min_cash_on_hand_end_period_amount** | **str**|  Filter for all amounts greater than a value.  | [optional] 
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **year** | [**list[int]**](int.md)|  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional] 
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **filer_type** | **str**| The method used to file with the FEC, either electronic or on paper. | [optional] 
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **amendment_indicator** | [**list[str]**](str.md)| Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment.  | [optional] 
 **report_type** | [**list[str]**](str.md)| Report type; prefix with \&quot;-\&quot; to exclude. Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND  | [optional] 
 **most_recent** | **bool**|  Report is either new or is the most-recently filed amendment  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **min_receipts_amount** | **str**|  Filter for all amounts greater than a value.  | [optional] 
 **max_cash_on_hand_end_period_amount** | **str**|  Filter for all amounts less than a value.  | [optional] 
 **max_receipt_date** | **date**|  Selects all items received by FEC before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **max_total_contributions** | **str**|  Filter for all amounts less than a value.  | [optional] 

### Return type

[**CommitteeReportsPage**](CommitteeReportsPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **totals_by_entity_get**
> EntityReceiptDisbursementTotalsPage totals_by_entity_get(api_key, cycle, page=page, per_page=per_page, sort=sort, sort_nulls_last=sort_nulls_last, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)



 Provides cumulative receipt totals by entity type, over a two year cycle. Totals are adjusted to avoid double counting.  This is [the sql](https://github.com/fecgov/openFEC/blob/develop/data/migrations/V41__large_aggregates.sql) that creates these calculations. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyHeaderAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'
# Configure API key authorization: ApiKeyQueryAuth
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.FinancialApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
cycle = 56 # int |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort = 'end_date' # str | Provide a field to sort by. Use - for descending order. (optional) (default to end_date)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)

try:
    api_response = api_instance.totals_by_entity_get(api_key, cycle, page=page, per_page=per_page, sort=sort, sort_nulls_last=sort_nulls_last, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancialApi->totals_by_entity_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **cycle** | **int**|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | 
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to end_date]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]

### Return type

[**EntityReceiptDisbursementTotalsPage**](EntityReceiptDisbursementTotalsPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **totals_committee_type_get**
> CommitteeTotalsPage totals_committee_type_get(api_key, committee_type, committee_id=committee_id, cycle=cycle, per_page=per_page, sort=sort, sort_nulls_last=sort_nulls_last, committee_designation_full=committee_designation_full, page=page, sort_hide_null=sort_hide_null, committee_type_full=committee_type_full, sort_null_only=sort_null_only)



 This endpoint provides information about a committee's Form 3, Form 3X, or Form 3P financial reports, which are aggregated by two-year period. We refer to two-year periods as a `cycle`.  The cycle is named after the even-numbered year and includes the year before it. To see totals from 2013 and 2014, you would use 2014. In odd-numbered years, the current cycle is the next year — for example, in 2015, the current cycle is 2016.  For presidential and Senate candidates, multiple two-year cycles exist between elections.  Parameter `full_election` is replaced by `election_full`. Please use `election_full` instead. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyHeaderAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'
# Configure API key authorization: ApiKeyQueryAuth
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.FinancialApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
committee_type = 'committee_type_example' # str | House, Senate, presidential, independent expenditure only
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort = '-cycle' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -cycle)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
committee_designation_full = 'committee_designation_full_example' # str | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
committee_type_full = 'committee_type_full_example' # str | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)

try:
    api_response = api_instance.totals_committee_type_get(api_key, committee_type, committee_id=committee_id, cycle=cycle, per_page=per_page, sort=sort, sort_nulls_last=sort_nulls_last, committee_designation_full=committee_designation_full, page=page, sort_hide_null=sort_hide_null, committee_type_full=committee_type_full, sort_null_only=sort_null_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancialApi->totals_committee_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **committee_type** | **str**| House, Senate, presidential, independent expenditure only | 
 **committee_id** | **str**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -cycle]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **committee_designation_full** | **str**| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **committee_type_full** | **str**| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]

### Return type

[**CommitteeTotalsPage**](CommitteeTotalsPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

