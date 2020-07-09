# openfec_sdk.CandidateApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**candidate_candidate_id_get**](CandidateApi.md#candidate_candidate_id_get) | **GET** /candidate/{candidate_id}/ |
[**candidate_candidate_id_history_cycle_get**](CandidateApi.md#candidate_candidate_id_history_cycle_get) | **GET** /candidate/{candidate_id}/history/{cycle}/ |
[**candidate_candidate_id_history_get**](CandidateApi.md#candidate_candidate_id_history_get) | **GET** /candidate/{candidate_id}/history/ |
[**candidate_candidate_id_totals_get**](CandidateApi.md#candidate_candidate_id_totals_get) | **GET** /candidate/{candidate_id}/totals/ |
[**candidates_get**](CandidateApi.md#candidates_get) | **GET** /candidates/ |
[**candidates_search_get**](CandidateApi.md#candidates_search_get) | **GET** /candidates/search/ |
[**candidates_totals_by_office_by_party_get**](CandidateApi.md#candidates_totals_by_office_by_party_get) | **GET** /candidates/totals/by_office/by_party/ |
[**candidates_totals_by_office_get**](CandidateApi.md#candidates_totals_by_office_get) | **GET** /candidates/totals/by_office/ |
[**candidates_totals_get**](CandidateApi.md#candidates_totals_get) | **GET** /candidates/totals/ |
[**committee_committee_id_candidates_get**](CandidateApi.md#committee_committee_id_candidates_get) | **GET** /committee/{committee_id}/candidates/ |
[**committee_committee_id_candidates_history_cycle_get**](CandidateApi.md#committee_committee_id_candidates_history_cycle_get) | **GET** /committee/{committee_id}/candidates/history/{cycle}/ |
[**committee_committee_id_candidates_history_get**](CandidateApi.md#committee_committee_id_candidates_history_get) | **GET** /committee/{committee_id}/candidates/history/ |


# **candidate_candidate_id_get**
> candidate_detail_page.CandidateDetailPage candidate_candidate_id_get(candidate_id)



 This endpoint is useful for finding detailed information about a particular candidate. Use the `candidate_id` to find the most recent information about that candidate.

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
    api_instance = openfec_sdk.CandidateApi(api_client)
    candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.
    page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
incumbent_challenge = ['incumbent_challenge_example'] # [str] | One-letter code ('I', 'C', 'O') explaining if the candidate is an incumbent, a challenger, or if the seat is open. (optional)
federal_funds_flag = True # bool | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
election_year = [56] # [int] | Year of election (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
sort = 'name' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of 'name'
office = ['office_example'] # [str] | Federal office candidate runs for: H, S or P (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
year = 'year_example' # str | See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. (optional)
cycle = [56] # [int] |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.  (optional)
has_raised_funds = True # bool | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) (optional)
party = ['party_example'] # [str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
district = ['district_example'] # [str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
name = ['name_example'] # [str] | Name (candidate or committee) to search for. Alias for 'q'. (optional)
candidate_status = ['candidate_status_example'] # [str] | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  (optional)
state = ['state_example'] # [str] | US state or territory where a candidate runs for office (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.candidate_candidate_id_get(candidate_id)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CandidateApi->candidate_candidate_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.candidate_candidate_id_get(candidate_id, page=page, incumbent_challenge=incumbent_challenge, federal_funds_flag=federal_funds_flag, sort_nulls_last=sort_nulls_last, election_year=election_year, per_page=per_page, sort=sort, office=office, sort_hide_null=sort_hide_null, year=year, cycle=cycle, has_raised_funds=has_raised_funds, party=party, sort_null_only=sort_null_only, district=district, name=name, candidate_status=candidate_status, state=state)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CandidateApi->candidate_candidate_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **candidate_id** | **str**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  |
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **incumbent_challenge** | **[str]**| One-letter code (&#39;I&#39;, &#39;C&#39;, &#39;O&#39;) explaining if the candidate is an incumbent, a challenger, or if the seat is open. | [optional]
 **federal_funds_flag** | **bool**| A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **election_year** | **[int]**| Year of election | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of 'name'
 **office** | **[str]**| Federal office candidate runs for: H, S or P | [optional]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **year** | **str**| See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. | [optional]
 **cycle** | **[int]**|  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | [optional]
 **has_raised_funds** | **bool**| A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) | [optional]
 **party** | **[str]**| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **district** | **[str]**| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional]
 **name** | **[str]**| Name (candidate or committee) to search for. Alias for &#39;q&#39;. | [optional]
 **candidate_status** | **[str]**| One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  | [optional]
 **state** | **[str]**| US state or territory where a candidate runs for office | [optional]

### Return type

[**candidate_detail_page.CandidateDetailPage**](CandidateDetailPage.md)

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

# **candidate_candidate_id_history_cycle_get**
> candidate_history_page.CandidateHistoryPage candidate_candidate_id_history_cycle_get(cycle, candidate_id)



 Find out a candidate's characteristics over time. This is particularly useful if the candidate runs for the same office in different districts or you want to know more about a candidate's previous races.  This information is organized by `candidate_id`, so it won't help you find a candidate who ran for different offices over time; candidates get a new ID for each office.

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
    api_instance = openfec_sdk.CandidateApi(api_client)
    cycle = 56 # int |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.
    candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
sort = '-two_year_period' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of '-two_year_period'
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.candidate_candidate_id_history_cycle_get(cycle, candidate_id)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CandidateApi->candidate_candidate_id_history_cycle_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.candidate_candidate_id_history_cycle_get(cycle, candidate_id, per_page=per_page, page=page, sort_nulls_last=sort_nulls_last, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, election_full=election_full)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CandidateApi->candidate_candidate_id_history_cycle_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cycle** | **int**|  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  |
 **candidate_id** | **str**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  |
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of '-two_year_period'
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] if omitted the server will use the default value of True

### Return type

[**candidate_history_page.CandidateHistoryPage**](CandidateHistoryPage.md)

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

# **candidate_candidate_id_history_get**
> candidate_history_page.CandidateHistoryPage candidate_candidate_id_history_get(candidate_id)



 Find out a candidate's characteristics over time. This is particularly useful if the candidate runs for the same office in different districts or you want to know more about a candidate's previous races.  This information is organized by `candidate_id`, so it won't help you find a candidate who ran for different offices over time; candidates get a new ID for each office.

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
    api_instance = openfec_sdk.CandidateApi(api_client)
    candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
sort = '-two_year_period' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of '-two_year_period'
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.candidate_candidate_id_history_get(candidate_id)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CandidateApi->candidate_candidate_id_history_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.candidate_candidate_id_history_get(candidate_id, per_page=per_page, page=page, sort_nulls_last=sort_nulls_last, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, election_full=election_full)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CandidateApi->candidate_candidate_id_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **candidate_id** | **str**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  |
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of '-two_year_period'
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] if omitted the server will use the default value of True

### Return type

[**candidate_history_page.CandidateHistoryPage**](CandidateHistoryPage.md)

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

# **candidate_candidate_id_totals_get**
> committee_totals_page.CommitteeTotalsPage candidate_candidate_id_totals_get(candidate_id)



 This endpoint provides information about a committee's Form 3, Form 3X, or Form 3P financial reports, which are aggregated by two-year period. We refer to two-year periods as a `cycle`.  The cycle is named after the even-numbered year and includes the year before it. To see totals from 2013 and 2014, you would use 2014. In odd-numbered years, the current cycle is the next year — for example, in 2015, the current cycle is 2016.  For presidential and Senate candidates, multiple two-year cycles exist between elections.  Parameter `full_election` is replaced by `election_full`. Please use `election_full` instead.

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
    api_instance = openfec_sdk.CandidateApi(api_client)
    candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.
    page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
full_election = True # bool | Parameter `full_election` is replaced by `election_full`. Please use `election_full` instead. (optional)
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
sort = '-cycle' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of '-cycle'
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
cycle = [56] # [int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.candidate_candidate_id_totals_get(candidate_id)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CandidateApi->candidate_candidate_id_totals_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.candidate_candidate_id_totals_get(candidate_id, page=page, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, full_election=full_election, election_full=election_full, per_page=per_page, sort=sort, sort_hide_null=sort_hide_null, cycle=cycle)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CandidateApi->candidate_candidate_id_totals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **candidate_id** | **str**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  |
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **full_election** | **bool**| Parameter &#x60;full_election&#x60; is replaced by &#x60;election_full&#x60;. Please use &#x60;election_full&#x60; instead. | [optional]
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional]
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

# **candidates_get**
> candidate_page.CandidatePage candidates_get()



 Fetch basic information about candidates, and use parameters to filter results to the candidates you're looking for.  Each result reflects a unique FEC candidate ID. That ID is particular to the candidate for a particular office sought. If a candidate runs for the same office multiple times, the ID stays the same. If the same person runs for another office — for example, a House candidate runs for a Senate office — that candidate will get a unique ID for each office.

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
    api_instance = openfec_sdk.CandidateApi(api_client)
    page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
incumbent_challenge = ['incumbent_challenge_example'] # [str] | One-letter code ('I', 'C', 'O') explaining if the candidate is an incumbent, a challenger, or if the seat is open. (optional)
federal_funds_flag = True # bool | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. (optional)
max_first_file_date = '2013-10-20' # date | Selects all candidates whose first filing was received by the FEC before this date. (optional)
is_active_candidate = True # bool |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
q = ['q_example'] # [str] | Name of candidate running for office (optional)
election_year = [56] # [int] | Year of election (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
sort = 'name' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of 'name'
office = ['office_example'] # [str] | Federal office candidate runs for: H, S or P (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
candidate_id = ['candidate_id_example'] # [str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
year = 'year_example' # str | See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. (optional)
cycle = [56] # [int] |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.  (optional)
has_raised_funds = True # bool | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) (optional)
party = ['party_example'] # [str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
district = ['district_example'] # [str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
name = ['name_example'] # [str] | Name (candidate or committee) to search for. Alias for 'q'. (optional)
candidate_status = ['candidate_status_example'] # [str] | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  (optional)
min_first_file_date = '2013-10-20' # date | Selects all candidates whose first filing was received by the FEC after this date. (optional)
state = ['state_example'] # [str] | US state or territory where a candidate runs for office (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.candidates_get()
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CandidateApi->candidates_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.candidates_get(page=page, incumbent_challenge=incumbent_challenge, federal_funds_flag=federal_funds_flag, max_first_file_date=max_first_file_date, is_active_candidate=is_active_candidate, sort_nulls_last=sort_nulls_last, q=q, election_year=election_year, per_page=per_page, sort=sort, office=office, sort_hide_null=sort_hide_null, candidate_id=candidate_id, year=year, cycle=cycle, has_raised_funds=has_raised_funds, party=party, sort_null_only=sort_null_only, district=district, name=name, candidate_status=candidate_status, min_first_file_date=min_first_file_date, state=state)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CandidateApi->candidates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **incumbent_challenge** | **[str]**| One-letter code (&#39;I&#39;, &#39;C&#39;, &#39;O&#39;) explaining if the candidate is an incumbent, a challenger, or if the seat is open. | [optional]
 **federal_funds_flag** | **bool**| A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. | [optional]
 **max_first_file_date** | **date**| Selects all candidates whose first filing was received by the FEC before this date. | [optional]
 **is_active_candidate** | **bool**|  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **q** | **[str]**| Name of candidate running for office | [optional]
 **election_year** | **[int]**| Year of election | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of 'name'
 **office** | **[str]**| Federal office candidate runs for: H, S or P | [optional]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **candidate_id** | **[str]**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional]
 **year** | **str**| See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. | [optional]
 **cycle** | **[int]**|  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | [optional]
 **has_raised_funds** | **bool**| A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) | [optional]
 **party** | **[str]**| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **district** | **[str]**| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional]
 **name** | **[str]**| Name (candidate or committee) to search for. Alias for &#39;q&#39;. | [optional]
 **candidate_status** | **[str]**| One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  | [optional]
 **min_first_file_date** | **date**| Selects all candidates whose first filing was received by the FEC after this date. | [optional]
 **state** | **[str]**| US state or territory where a candidate runs for office | [optional]

### Return type

[**candidate_page.CandidatePage**](CandidatePage.md)

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

# **candidates_search_get**
> candidate_page.CandidatePage candidates_search_get()



 Fetch basic information about candidates and their principal committees.  Each result reflects a unique FEC candidate ID. That ID is assigned to the candidate for a particular office sought. If a candidate runs for the same office over time, that ID stays the same. If the same person runs for multiple offices — for example, a House candidate runs for a Senate office — that candidate will get a unique ID for each office.  The candidate endpoints primarily use data from FEC registration [Form 1](http://www.fec.gov/pdf/forms/fecfrm1.pdf), for candidate information, and [Form 2](http://www.fec.gov/pdf/forms/fecfrm2.pdf), for committees information, with additional information to provide context.

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
    api_instance = openfec_sdk.CandidateApi(api_client)
    page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
incumbent_challenge = ['incumbent_challenge_example'] # [str] | One-letter code ('I', 'C', 'O') explaining if the candidate is an incumbent, a challenger, or if the seat is open. (optional)
federal_funds_flag = True # bool | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. (optional)
max_first_file_date = '2013-10-20' # date | Selects all candidates whose first filing was received by the FEC before this date. (optional)
is_active_candidate = True # bool |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
q = ['q_example'] # [str] | Name of candidate running for office (optional)
election_year = [56] # [int] | Year of election (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
sort = 'name' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of 'name'
office = ['office_example'] # [str] | Federal office candidate runs for: H, S or P (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
candidate_id = ['candidate_id_example'] # [str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
year = 'year_example' # str | See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. (optional)
cycle = [56] # [int] |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.  (optional)
has_raised_funds = True # bool | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) (optional)
party = ['party_example'] # [str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
district = ['district_example'] # [str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
name = ['name_example'] # [str] | Name (candidate or committee) to search for. Alias for 'q'. (optional)
candidate_status = ['candidate_status_example'] # [str] | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  (optional)
min_first_file_date = '2013-10-20' # date | Selects all candidates whose first filing was received by the FEC after this date. (optional)
state = ['state_example'] # [str] | US state or territory where a candidate runs for office (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.candidates_search_get()
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CandidateApi->candidates_search_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.candidates_search_get(page=page, incumbent_challenge=incumbent_challenge, federal_funds_flag=federal_funds_flag, max_first_file_date=max_first_file_date, is_active_candidate=is_active_candidate, sort_nulls_last=sort_nulls_last, q=q, election_year=election_year, per_page=per_page, sort=sort, office=office, sort_hide_null=sort_hide_null, candidate_id=candidate_id, year=year, cycle=cycle, has_raised_funds=has_raised_funds, party=party, sort_null_only=sort_null_only, district=district, name=name, candidate_status=candidate_status, min_first_file_date=min_first_file_date, state=state)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CandidateApi->candidates_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **incumbent_challenge** | **[str]**| One-letter code (&#39;I&#39;, &#39;C&#39;, &#39;O&#39;) explaining if the candidate is an incumbent, a challenger, or if the seat is open. | [optional]
 **federal_funds_flag** | **bool**| A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. | [optional]
 **max_first_file_date** | **date**| Selects all candidates whose first filing was received by the FEC before this date. | [optional]
 **is_active_candidate** | **bool**|  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **q** | **[str]**| Name of candidate running for office | [optional]
 **election_year** | **[int]**| Year of election | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of 'name'
 **office** | **[str]**| Federal office candidate runs for: H, S or P | [optional]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **candidate_id** | **[str]**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional]
 **year** | **str**| See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. | [optional]
 **cycle** | **[int]**|  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | [optional]
 **has_raised_funds** | **bool**| A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) | [optional]
 **party** | **[str]**| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **district** | **[str]**| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional]
 **name** | **[str]**| Name (candidate or committee) to search for. Alias for &#39;q&#39;. | [optional]
 **candidate_status** | **[str]**| One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  | [optional]
 **min_first_file_date** | **date**| Selects all candidates whose first filing was received by the FEC after this date. | [optional]
 **state** | **[str]**| US state or territory where a candidate runs for office | [optional]

### Return type

[**candidate_page.CandidatePage**](CandidatePage.md)

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

# **candidates_totals_by_office_by_party_get**
> total_by_office_by_party_page.TotalByOfficeByPartyPage candidates_totals_by_office_by_party_get()



 Aggregated candidate receipts and disbursements grouped by office by party by cycle.

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
    api_instance = openfec_sdk.CandidateApi(api_client)
    page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
is_active_candidate = True # bool |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
election_year = [56] # [int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
sort = 'null' # str, none_type | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of 'null'
office = 'office_example' # str | Federal office candidate runs for: H, S or P (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.candidates_totals_by_office_by_party_get()
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CandidateApi->candidates_totals_by_office_by_party_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.candidates_totals_by_office_by_party_get(page=page, is_active_candidate=is_active_candidate, sort_nulls_last=sort_nulls_last, sort_null_only=sort_null_only, election_year=election_year, per_page=per_page, sort=sort, office=office, sort_hide_null=sort_hide_null)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CandidateApi->candidates_totals_by_office_by_party_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **is_active_candidate** | **bool**|  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **election_year** | **[int]**|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **sort** | **str, none_type**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of 'null'
 **office** | **str**| Federal office candidate runs for: H, S or P | [optional]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False

### Return type

[**total_by_office_by_party_page.TotalByOfficeByPartyPage**](TotalByOfficeByPartyPage.md)

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

# **candidates_totals_by_office_get**
> total_by_office_page.TotalByOfficePage candidates_totals_by_office_get()



 Aggregated candidate receipts and disbursements grouped by office by cycle.

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
    api_instance = openfec_sdk.CandidateApi(api_client)
    page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
is_active_candidate = True # bool |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
election_year = [56] # [int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
sort = 'null' # str, none_type | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of 'null'
office = 'office_example' # str | Federal office candidate runs for: H, S or P (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.candidates_totals_by_office_get()
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CandidateApi->candidates_totals_by_office_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.candidates_totals_by_office_get(page=page, is_active_candidate=is_active_candidate, sort_nulls_last=sort_nulls_last, sort_null_only=sort_null_only, election_year=election_year, per_page=per_page, sort=sort, office=office, sort_hide_null=sort_hide_null)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CandidateApi->candidates_totals_by_office_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **is_active_candidate** | **bool**|  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **election_year** | **[int]**|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **sort** | **str, none_type**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of 'null'
 **office** | **str**| Federal office candidate runs for: H, S or P | [optional]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False

### Return type

[**total_by_office_page.TotalByOfficePage**](TotalByOfficePage.md)

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

# **candidates_totals_get**
> candidate_history_total_page.CandidateHistoryTotalPage candidates_totals_get()



 Aggregated candidate receipts and disbursements grouped by cycle.

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
    api_instance = openfec_sdk.CandidateApi(api_client)
    min_cash_on_hand_end_period = 'min_cash_on_hand_end_period_example' # str | Minimum cash on hand (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
federal_funds_flag = True # bool | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. (optional)
is_active_candidate = True # bool |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  (optional)
max_cash_on_hand_end_period = 'max_cash_on_hand_end_period_example' # str | Maximum cash on hand (optional)
min_receipts = 'min_receipts_example' # str | Minimum aggregated receipts (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
max_receipts = 'max_receipts_example' # str | Maximum aggregated receipts (optional)
election_year = [56] # [int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
min_debts_owed_by_committee = 'min_debts_owed_by_committee_example' # str | Minimum debt (optional)
sort = 'null' # str, none_type | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of 'null'
office = ['office_example'] # [str] | Federal office candidate runs for: H, S or P (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
candidate_id = ['candidate_id_example'] # [str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
max_debts_owed_by_committee = 'max_debts_owed_by_committee_example' # str | Maximum debt (optional)
cycle = [56] # [int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
min_disbursements = 'min_disbursements_example' # str | Minimum aggregated disbursements (optional)
has_raised_funds = True # bool | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) (optional)
party = ['party_example'] # [str] | Three-letter party code (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) if omitted the server will use the default value of True
district = ['district_example'] # [str] | District of candidate (optional)
max_disbursements = 'max_disbursements_example' # str | Maximum aggregated disbursements (optional)
q = ['q_example'] # [str] | Name of candidate running for office (optional)
state = ['state_example'] # [str] | State of candidate (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.candidates_totals_get()
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CandidateApi->candidates_totals_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.candidates_totals_get(min_cash_on_hand_end_period=min_cash_on_hand_end_period, page=page, federal_funds_flag=federal_funds_flag, is_active_candidate=is_active_candidate, max_cash_on_hand_end_period=max_cash_on_hand_end_period, min_receipts=min_receipts, sort_nulls_last=sort_nulls_last, max_receipts=max_receipts, election_year=election_year, per_page=per_page, min_debts_owed_by_committee=min_debts_owed_by_committee, sort=sort, office=office, sort_hide_null=sort_hide_null, candidate_id=candidate_id, max_debts_owed_by_committee=max_debts_owed_by_committee, cycle=cycle, min_disbursements=min_disbursements, has_raised_funds=has_raised_funds, party=party, sort_null_only=sort_null_only, election_full=election_full, district=district, max_disbursements=max_disbursements, q=q, state=state)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CandidateApi->candidates_totals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **min_cash_on_hand_end_period** | **str**| Minimum cash on hand | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **federal_funds_flag** | **bool**| A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. | [optional]
 **is_active_candidate** | **bool**|  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  | [optional]
 **max_cash_on_hand_end_period** | **str**| Maximum cash on hand | [optional]
 **min_receipts** | **str**| Minimum aggregated receipts | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **max_receipts** | **str**| Maximum aggregated receipts | [optional]
 **election_year** | **[int]**|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **min_debts_owed_by_committee** | **str**| Minimum debt | [optional]
 **sort** | **str, none_type**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of 'null'
 **office** | **[str]**| Federal office candidate runs for: H, S or P | [optional]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **candidate_id** | **[str]**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional]
 **max_debts_owed_by_committee** | **str**| Maximum debt | [optional]
 **cycle** | **[int]**|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional]
 **min_disbursements** | **str**| Minimum aggregated disbursements | [optional]
 **has_raised_funds** | **bool**| A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) | [optional]
 **party** | **[str]**| Three-letter party code | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] if omitted the server will use the default value of True
 **district** | **[str]**| District of candidate | [optional]
 **max_disbursements** | **str**| Maximum aggregated disbursements | [optional]
 **q** | **[str]**| Name of candidate running for office | [optional]
 **state** | **[str]**| State of candidate | [optional]

### Return type

[**candidate_history_total_page.CandidateHistoryTotalPage**](CandidateHistoryTotalPage.md)

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

# **committee_committee_id_candidates_get**
> candidate_detail_page.CandidateDetailPage committee_committee_id_candidates_get(committee_id)



 This endpoint is useful for finding detailed information about a particular candidate. Use the `candidate_id` to find the most recent information about that candidate.

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
    api_instance = openfec_sdk.CandidateApi(api_client)
    committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.
    page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
incumbent_challenge = ['incumbent_challenge_example'] # [str] | One-letter code ('I', 'C', 'O') explaining if the candidate is an incumbent, a challenger, or if the seat is open. (optional)
federal_funds_flag = True # bool | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
election_year = [56] # [int] | Year of election (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
sort = 'name' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of 'name'
office = ['office_example'] # [str] | Federal office candidate runs for: H, S or P (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
year = 'year_example' # str | See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. (optional)
cycle = [56] # [int] |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.  (optional)
has_raised_funds = True # bool | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) (optional)
party = ['party_example'] # [str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
district = ['district_example'] # [str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
name = ['name_example'] # [str] | Name (candidate or committee) to search for. Alias for 'q'. (optional)
candidate_status = ['candidate_status_example'] # [str] | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  (optional)
state = ['state_example'] # [str] | US state or territory where a candidate runs for office (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.committee_committee_id_candidates_get(committee_id)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CandidateApi->committee_committee_id_candidates_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.committee_committee_id_candidates_get(committee_id, page=page, incumbent_challenge=incumbent_challenge, federal_funds_flag=federal_funds_flag, sort_nulls_last=sort_nulls_last, election_year=election_year, per_page=per_page, sort=sort, office=office, sort_hide_null=sort_hide_null, year=year, cycle=cycle, has_raised_funds=has_raised_funds, party=party, sort_null_only=sort_null_only, district=district, name=name, candidate_status=candidate_status, state=state)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CandidateApi->committee_committee_id_candidates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **committee_id** | **str**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  |
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **incumbent_challenge** | **[str]**| One-letter code (&#39;I&#39;, &#39;C&#39;, &#39;O&#39;) explaining if the candidate is an incumbent, a challenger, or if the seat is open. | [optional]
 **federal_funds_flag** | **bool**| A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **election_year** | **[int]**| Year of election | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of 'name'
 **office** | **[str]**| Federal office candidate runs for: H, S or P | [optional]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **year** | **str**| See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. | [optional]
 **cycle** | **[int]**|  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | [optional]
 **has_raised_funds** | **bool**| A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) | [optional]
 **party** | **[str]**| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **district** | **[str]**| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional]
 **name** | **[str]**| Name (candidate or committee) to search for. Alias for &#39;q&#39;. | [optional]
 **candidate_status** | **[str]**| One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  | [optional]
 **state** | **[str]**| US state or territory where a candidate runs for office | [optional]

### Return type

[**candidate_detail_page.CandidateDetailPage**](CandidateDetailPage.md)

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

# **committee_committee_id_candidates_history_cycle_get**
> candidate_history_page.CandidateHistoryPage committee_committee_id_candidates_history_cycle_get(committee_id, cycle)



 Find out a candidate's characteristics over time. This is particularly useful if the candidate runs for the same office in different districts or you want to know more about a candidate's previous races.  This information is organized by `candidate_id`, so it won't help you find a candidate who ran for different offices over time; candidates get a new ID for each office.

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
    api_instance = openfec_sdk.CandidateApi(api_client)
    committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.
    cycle = 56 # int |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
sort = '-two_year_period' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of '-two_year_period'
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.committee_committee_id_candidates_history_cycle_get(committee_id, cycle)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CandidateApi->committee_committee_id_candidates_history_cycle_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.committee_committee_id_candidates_history_cycle_get(committee_id, cycle, per_page=per_page, page=page, sort_nulls_last=sort_nulls_last, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, election_full=election_full)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CandidateApi->committee_committee_id_candidates_history_cycle_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **committee_id** | **str**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  |
 **cycle** | **int**|  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  |
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of '-two_year_period'
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] if omitted the server will use the default value of True

### Return type

[**candidate_history_page.CandidateHistoryPage**](CandidateHistoryPage.md)

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

# **committee_committee_id_candidates_history_get**
> candidate_history_page.CandidateHistoryPage committee_committee_id_candidates_history_get(committee_id)



 Find out a candidate's characteristics over time. This is particularly useful if the candidate runs for the same office in different districts or you want to know more about a candidate's previous races.  This information is organized by `candidate_id`, so it won't help you find a candidate who ran for different offices over time; candidates get a new ID for each office.

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
    api_instance = openfec_sdk.CandidateApi(api_client)
    committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
sort = '-two_year_period' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of '-two_year_period'
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.committee_committee_id_candidates_history_get(committee_id)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CandidateApi->committee_committee_id_candidates_history_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.committee_committee_id_candidates_history_get(committee_id, per_page=per_page, page=page, sort_nulls_last=sort_nulls_last, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only, election_full=election_full)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CandidateApi->committee_committee_id_candidates_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **committee_id** | **str**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  |
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of '-two_year_period'
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] if omitted the server will use the default value of True

### Return type

[**candidate_history_page.CandidateHistoryPage**](CandidateHistoryPage.md)

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
