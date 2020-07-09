# openfec_sdk.IndependentExpendituresApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schedules_schedule_e_by_candidate_get**](IndependentExpendituresApi.md#schedules_schedule_e_by_candidate_get) | **GET** /schedules/schedule_e/by_candidate/ |
[**schedules_schedule_e_efile_get**](IndependentExpendituresApi.md#schedules_schedule_e_efile_get) | **GET** /schedules/schedule_e/efile/ |
[**schedules_schedule_e_get**](IndependentExpendituresApi.md#schedules_schedule_e_get) | **GET** /schedules/schedule_e/ |
[**schedules_schedule_e_totals_by_candidate_get**](IndependentExpendituresApi.md#schedules_schedule_e_totals_by_candidate_get) | **GET** /schedules/schedule_e/totals/by_candidate/ |


# **schedules_schedule_e_by_candidate_get**
> schedule_e_by_candidate_page.ScheduleEByCandidatePage schedules_schedule_e_by_candidate_get()



 Schedule E receipts aggregated by recipient candidate. To avoid double counting, memoed items are not included.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import openfec_sdk
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
    api_instance = openfec_sdk.IndependentExpendituresApi(api_client)
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
state = 'state_example' # str | US state or territory where a candidate runs for office (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
sort = 'null' # str, none_type | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of 'null'
district = 'district_example' # str | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
candidate_id = ['candidate_id_example'] # [str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
committee_id = ['committee_id_example'] # [str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
support_oppose = 'null' # str, none_type | Support or opposition (optional) if omitted the server will use the default value of 'null'
page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
office = 'office_example' # str | Federal office candidate runs for: H, S or P (optional)
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) if omitted the server will use the default value of True
cycle = [56] # [int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.schedules_schedule_e_by_candidate_get()
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling IndependentExpendituresApi->schedules_schedule_e_by_candidate_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.schedules_schedule_e_by_candidate_get(sort_hide_null=sort_hide_null, state=state, sort_null_only=sort_null_only, per_page=per_page, sort=sort, district=district, candidate_id=candidate_id, committee_id=committee_id, support_oppose=support_oppose, page=page, sort_nulls_last=sort_nulls_last, office=office, election_full=election_full, cycle=cycle)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling IndependentExpendituresApi->schedules_schedule_e_by_candidate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **state** | **str**| US state or territory where a candidate runs for office | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **sort** | **str, none_type**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of 'null'
 **district** | **str**| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional]
 **candidate_id** | **[str]**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional]
 **committee_id** | **[str]**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional]
 **support_oppose** | **str, none_type**| Support or opposition | [optional] if omitted the server will use the default value of 'null'
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **office** | **str**| Federal office candidate runs for: H, S or P | [optional]
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] if omitted the server will use the default value of True
 **cycle** | **[int]**|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional]

### Return type

[**schedule_e_by_candidate_page.ScheduleEByCandidatePage**](ScheduleEByCandidatePage.md)

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

# **schedules_schedule_e_efile_get**
> schedule_e_efile_page.ScheduleEEfilePage schedules_schedule_e_efile_get()



 Efiling endpoints provide real-time campaign finance data received from electronic filers. Efiling endpoints only contain the most recent four months of data and don't contain the processed and coded data that you can find on other endpoints.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import openfec_sdk
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
    api_instance = openfec_sdk.IndependentExpendituresApi(api_client)
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
max_dissemination_date = '2013-10-20' # date | Selects all items distributed by this committee before this date (optional)
most_recent = True # bool |  The report associated with the transaction is either new or is the most-recently filed amendment. Undetermined version (`null`) is always included.  (optional)
image_number = ['image_number_example'] # [str] |  An unique identifier for each page where the electronic or paper filing is reported.  (optional)
min_expenditure_amount = 56 # int | Selects all items expended by this committee greater than this amount (optional)
filing_form = ['filing_form_example'] # [str] | The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  (optional)
max_expenditure_date = '2013-10-20' # date | Selects all items expended by this committee before this date (optional)
min_filed_date = '2013-10-20' # date | Timestamp of electronic or paper record that FEC received (optional)
candidate_id = ['candidate_id_example'] # [str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
payee_name = ['payee_name_example'] # [str] |  Name of the entity that received the payment.  (optional)
committee_id = ['committee_id_example'] # [str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
candidate_office_state = ['candidate_office_state_example'] # [str] | US state or territory where a candidate runs for office (optional)
candidate_office_district = ['candidate_office_district_example'] # [str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
min_expenditure_date = '2013-10-20' # date | Selects all items expended by this committee after this date (optional)
is_notice = True # bool |  Record filed as 24- or 48-hour notice.  (optional)
max_filed_date = '2013-10-20' # date | Timestamp of electronic or paper record that FEC received (optional)
candidate_office = 'candidate_office_example' # str | Federal office candidate runs for: H, S or P (optional)
candidate_party = ['candidate_party_example'] # [str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
sort = '-expenditure_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of '-expenditure_date'
max_expenditure_amount = 56 # int | Selects all items expended by this committee less than this amount (optional)
candidate_search = ['candidate_search_example'] # [str] |  Search for candidates by candiate id or candidate first or last name  (optional)
support_oppose_indicator = ['support_oppose_indicator_example'] # [str] | Explains if the money was spent in order to support or oppose a candidate or candidates. (Coded S or O for support or oppose.) This indicator applies to independent expenditures and communication costs. (optional)
min_dissemination_date = '2013-10-20' # date | Selects all items distributed by this committee after this date (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
spender_name = ['spender_name_example'] # [str] | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.schedules_schedule_e_efile_get()
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling IndependentExpendituresApi->schedules_schedule_e_efile_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.schedules_schedule_e_efile_get(sort_hide_null=sort_hide_null, max_dissemination_date=max_dissemination_date, most_recent=most_recent, image_number=image_number, min_expenditure_amount=min_expenditure_amount, filing_form=filing_form, max_expenditure_date=max_expenditure_date, min_filed_date=min_filed_date, candidate_id=candidate_id, payee_name=payee_name, committee_id=committee_id, candidate_office_state=candidate_office_state, candidate_office_district=candidate_office_district, page=page, min_expenditure_date=min_expenditure_date, is_notice=is_notice, max_filed_date=max_filed_date, candidate_office=candidate_office, candidate_party=candidate_party, sort_null_only=sort_null_only, per_page=per_page, sort=sort, max_expenditure_amount=max_expenditure_amount, candidate_search=candidate_search, support_oppose_indicator=support_oppose_indicator, min_dissemination_date=min_dissemination_date, sort_nulls_last=sort_nulls_last, spender_name=spender_name)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling IndependentExpendituresApi->schedules_schedule_e_efile_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **max_dissemination_date** | **date**| Selects all items distributed by this committee before this date | [optional]
 **most_recent** | **bool**|  The report associated with the transaction is either new or is the most-recently filed amendment. Undetermined version (&#x60;null&#x60;) is always included.  | [optional]
 **image_number** | **[str]**|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional]
 **min_expenditure_amount** | **int**| Selects all items expended by this committee greater than this amount | [optional]
 **filing_form** | **[str]**| The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  | [optional]
 **max_expenditure_date** | **date**| Selects all items expended by this committee before this date | [optional]
 **min_filed_date** | **date**| Timestamp of electronic or paper record that FEC received | [optional]
 **candidate_id** | **[str]**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional]
 **payee_name** | **[str]**|  Name of the entity that received the payment.  | [optional]
 **committee_id** | **[str]**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional]
 **candidate_office_state** | **[str]**| US state or territory where a candidate runs for office | [optional]
 **candidate_office_district** | **[str]**| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **min_expenditure_date** | **date**| Selects all items expended by this committee after this date | [optional]
 **is_notice** | **bool**|  Record filed as 24- or 48-hour notice.  | [optional]
 **max_filed_date** | **date**| Timestamp of electronic or paper record that FEC received | [optional]
 **candidate_office** | **str**| Federal office candidate runs for: H, S or P | [optional]
 **candidate_party** | **[str]**| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of '-expenditure_date'
 **max_expenditure_amount** | **int**| Selects all items expended by this committee less than this amount | [optional]
 **candidate_search** | **[str]**|  Search for candidates by candiate id or candidate first or last name  | [optional]
 **support_oppose_indicator** | **[str]**| Explains if the money was spent in order to support or oppose a candidate or candidates. (Coded S or O for support or oppose.) This indicator applies to independent expenditures and communication costs. | [optional]
 **min_dissemination_date** | **date**| Selects all items distributed by this committee after this date | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **spender_name** | **[str]**| The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. | [optional]

### Return type

[**schedule_e_efile_page.ScheduleEEfilePage**](ScheduleEEfilePage.md)

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

# **schedules_schedule_e_get**
> schedule_e_page.ScheduleEPage schedules_schedule_e_get()



 Schedule E covers the line item expenditures for independent expenditures. For example, if a super PAC bought ads on TV to oppose a federal candidate, each ad purchase would be recorded here with the expenditure amount, name and id of the candidate, and whether the ad supported or opposed the candidate.  An independent expenditure is an expenditure for a communication \"expressly advocating the election or defeat of a clearly identified candidate that is not made in cooperation, consultation, or concert with, or at the request or suggestion of, a candidate, a candidate’s authorized committee, or their agents, or a political party or its agents.\"  Aggregates by candidate do not include 24 and 48 hour reports. This ensures we don't double count expenditures and the totals are more accurate. You can still find the information from 24 and 48 hour reports in `/schedule/schedule_e/`.  Due to the large quantity of Schedule E filings, this endpoint is not paginated by page number. Instead, you can request the next page of results by adding the values in the `last_indexes` object from `pagination` to the URL of your last request. For example, when sorting by `expenditure_amount`, you might receive a page of results with the following pagination information:  ```  \"pagination\": {     \"count\": 152623,     \"last_indexes\": {       \"last_index\": \"3023037\",       \"last_expenditure_amount\": -17348.5     },     \"per_page\": 20,     \"pages\": 7632   } } ```  To fetch the next page of sorted results, append `last_index=3023037` and `last_expenditure_amount=` to the URL.  We strongly advise paging through these results by using the sort indices (defaults to sort by disbursement date, e.g. `last_disbursement_date`), otherwise some resources may be unintentionally filtered out.  This resource uses keyset pagination to improve query performance and these indices are required to properly page through this large dataset.  Note: because the Schedule E data includes many records, counts for large result sets are approximate; you will want to page through the records until no records are returned.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import openfec_sdk
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
    api_instance = openfec_sdk.IndependentExpendituresApi(api_client)
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
max_image_number = 'max_image_number_example' # str |  (optional)
image_number = ['image_number_example'] # [str] | The image number of the page where the schedule item is reported (optional)
min_image_number = 'min_image_number_example' # str |  (optional)
payee_name = ['payee_name_example'] # [str] |  Name of the entity that received the payment.  (optional)
line_number = 'line_number_example' # str | Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`. (optional)
candidate_office_district = ['candidate_office_district_example'] # [str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
min_date = '2013-10-20' # date | Minimum date (optional)
is_notice = [True] # [bool] |  Record filed as 24- or 48-hour notice.  (optional)
last_expenditure_amount = openfec_sdk.float, none_type() # float, none_type |  When sorting by `expenditure_amount`, this is populated with the `expenditure_amount` of the last result. However, you will need to pass the index of that last result to `last_index` to get the next page.  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
max_filing_date = '2013-10-20' # date |  Selects all filings received before this date  (optional)
min_dissemination_date = '2013-10-20' # date | Selects all items distributed by this committee after this date (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
most_recent = True # bool |  The report associated with the transaction is either new or is the most-recently filed amendment. Undetermined version (`null`) is always included.  (optional)
filing_form = ['filing_form_example'] # [str] | The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  (optional)
committee_id = ['committee_id_example'] # [str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
min_amount = 'min_amount_example' # str | Filter for all amounts greater than a value. (optional)
candidate_id = ['candidate_id_example'] # [str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
last_office_total_ytd = openfec_sdk.float, none_type() # float, none_type |  When sorting by `office_total_ytd`, this is populated with the `office_total_ytd` of the last result. However, you will need to pass the index of that last result to `last_index` to get the next page.'  (optional)
last_expenditure_date = openfec_sdk.date, none_type() # date, none_type |  When sorting by `expenditure_date`, this is populated with the `expenditure_date` of the last result. However, you will need to pass the index of that last result to `last_index` to get the next page.  (optional)
candidate_office_state = ['candidate_office_state_example'] # [str] | US state or territory (optional)
cycle = [56] # [int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
candidate_office = ['candidate_office_example'] # [str] | Federal office candidate runs for: H, S or P (optional)
candidate_party = ['candidate_party_example'] # [str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
max_amount = 'max_amount_example' # str | Filter for all amounts less than a value. (optional)
sort = '-expenditure_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of '-expenditure_date'
last_support_oppose_indicator = 'null' # str, none_type |  When sorting by `support_oppose_indicator`, this is populated with the `support_oppose_indicator` of the last result. However, you will need to pass the index of that last result to `last_index` to get the next page.'  (optional) if omitted the server will use the default value of 'null'
last_index = openfec_sdk.int, none_type() # int, none_type | Index of last result from previous page (optional)
support_oppose_indicator = ['support_oppose_indicator_example'] # [str] | Explains if the money was spent in order to support or oppose a candidate or candidates. (Coded S or O for support or oppose.) This indicator applies to independent expenditures and communication costs. (optional)
min_filing_date = '2013-10-20' # date |  Selects all filings received after this date  (optional)
max_date = '2013-10-20' # date | Maximum date (optional)
max_dissemination_date = '2013-10-20' # date | Selects all items distributed by this committee before this date (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.schedules_schedule_e_get()
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling IndependentExpendituresApi->schedules_schedule_e_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.schedules_schedule_e_get(sort_hide_null=sort_hide_null, max_image_number=max_image_number, image_number=image_number, min_image_number=min_image_number, payee_name=payee_name, line_number=line_number, candidate_office_district=candidate_office_district, min_date=min_date, is_notice=is_notice, last_expenditure_amount=last_expenditure_amount, per_page=per_page, max_filing_date=max_filing_date, min_dissemination_date=min_dissemination_date, sort_nulls_last=sort_nulls_last, most_recent=most_recent, filing_form=filing_form, committee_id=committee_id, min_amount=min_amount, candidate_id=candidate_id, last_office_total_ytd=last_office_total_ytd, last_expenditure_date=last_expenditure_date, candidate_office_state=candidate_office_state, cycle=cycle, candidate_office=candidate_office, candidate_party=candidate_party, sort_null_only=sort_null_only, max_amount=max_amount, sort=sort, last_support_oppose_indicator=last_support_oppose_indicator, last_index=last_index, support_oppose_indicator=support_oppose_indicator, min_filing_date=min_filing_date, max_date=max_date, max_dissemination_date=max_dissemination_date)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling IndependentExpendituresApi->schedules_schedule_e_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **max_image_number** | **str**|  | [optional]
 **image_number** | **[str]**| The image number of the page where the schedule item is reported | [optional]
 **min_image_number** | **str**|  | [optional]
 **payee_name** | **[str]**|  Name of the entity that received the payment.  | [optional]
 **line_number** | **str**| Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;. | [optional]
 **candidate_office_district** | **[str]**| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional]
 **min_date** | **date**| Minimum date | [optional]
 **is_notice** | **[bool]**|  Record filed as 24- or 48-hour notice.  | [optional]
 **last_expenditure_amount** | **float, none_type**|  When sorting by &#x60;expenditure_amount&#x60;, this is populated with the &#x60;expenditure_amount&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page.  | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **max_filing_date** | **date**|  Selects all filings received before this date  | [optional]
 **min_dissemination_date** | **date**| Selects all items distributed by this committee after this date | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **most_recent** | **bool**|  The report associated with the transaction is either new or is the most-recently filed amendment. Undetermined version (&#x60;null&#x60;) is always included.  | [optional]
 **filing_form** | **[str]**| The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  | [optional]
 **committee_id** | **[str]**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional]
 **min_amount** | **str**| Filter for all amounts greater than a value. | [optional]
 **candidate_id** | **[str]**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional]
 **last_office_total_ytd** | **float, none_type**|  When sorting by &#x60;office_total_ytd&#x60;, this is populated with the &#x60;office_total_ytd&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page.&#39;  | [optional]
 **last_expenditure_date** | **date, none_type**|  When sorting by &#x60;expenditure_date&#x60;, this is populated with the &#x60;expenditure_date&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page.  | [optional]
 **candidate_office_state** | **[str]**| US state or territory | [optional]
 **cycle** | **[int]**|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional]
 **candidate_office** | **[str]**| Federal office candidate runs for: H, S or P | [optional]
 **candidate_party** | **[str]**| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **max_amount** | **str**| Filter for all amounts less than a value. | [optional]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of '-expenditure_date'
 **last_support_oppose_indicator** | **str, none_type**|  When sorting by &#x60;support_oppose_indicator&#x60;, this is populated with the &#x60;support_oppose_indicator&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page.&#39;  | [optional] if omitted the server will use the default value of 'null'
 **last_index** | **int, none_type**| Index of last result from previous page | [optional]
 **support_oppose_indicator** | **[str]**| Explains if the money was spent in order to support or oppose a candidate or candidates. (Coded S or O for support or oppose.) This indicator applies to independent expenditures and communication costs. | [optional]
 **min_filing_date** | **date**|  Selects all filings received after this date  | [optional]
 **max_date** | **date**| Maximum date | [optional]
 **max_dissemination_date** | **date**| Selects all items distributed by this committee before this date | [optional]

### Return type

[**schedule_e_page.ScheduleEPage**](ScheduleEPage.md)

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

# **schedules_schedule_e_totals_by_candidate_get**
> ie_totals_by_candidate_page.IETotalsByCandidatePage schedules_schedule_e_totals_by_candidate_get()



 Total independent expenditure on supported or opposed candidates by cycle or candidate election year.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import openfec_sdk
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
    api_instance = openfec_sdk.IndependentExpendituresApi(api_client)
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
sort = 'null' # str, none_type | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of 'null'
candidate_id = ['candidate_id_example'] # [str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) if omitted the server will use the default value of True
cycle = [56] # [int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.schedules_schedule_e_totals_by_candidate_get()
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling IndependentExpendituresApi->schedules_schedule_e_totals_by_candidate_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.schedules_schedule_e_totals_by_candidate_get(sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, per_page=per_page, sort=sort, candidate_id=candidate_id, page=page, sort_nulls_last=sort_nulls_last, election_full=election_full, cycle=cycle)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling IndependentExpendituresApi->schedules_schedule_e_totals_by_candidate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **sort** | **str, none_type**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of 'null'
 **candidate_id** | **[str]**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] if omitted the server will use the default value of True
 **cycle** | **[int]**|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional]

### Return type

[**ie_totals_by_candidate_page.IETotalsByCandidatePage**](IETotalsByCandidatePage.md)

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
