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
> CandidateDetailPage candidate_candidate_id_get(api_key, candidate_id, year=year, sort=sort, name=name, district=district, sort_nulls_last=sort_nulls_last, sort_null_only=sort_null_only, election_year=election_year, incumbent_challenge=incumbent_challenge, state=state, candidate_status=candidate_status, per_page=per_page, federal_funds_flag=federal_funds_flag, sort_hide_null=sort_hide_null, party=party, has_raised_funds=has_raised_funds, cycle=cycle, page=page, office=office)



 This endpoint is useful for finding detailed information about a particular candidate. Use the `candidate_id` to find the most recent information about that candidate.

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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.
year = 'year_example' # str | See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. (optional)
sort = 'name' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'name')
name = ['name_example'] # list[str] | Name (candidate or committee) to search for. Alias for 'q'. (optional)
district = ['district_example'] # list[str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
election_year = [56] # list[int] | Year of election (optional)
incumbent_challenge = ['incumbent_challenge_example'] # list[str] | One-letter code ('I', 'C', 'O') explaining if the candidate is an incumbent, a challenger, or if the seat is open. (optional)
state = ['state_example'] # list[str] | US state or territory where a candidate runs for office (optional)
candidate_status = ['candidate_status_example'] # list[str] | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
federal_funds_flag = True # bool | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
party = ['party_example'] # list[str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
has_raised_funds = True # bool | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) (optional)
cycle = [56] # list[int] |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
office = ['office_example'] # list[str] | Federal office candidate runs for: H, S or P (optional)

    try:
        api_response = api_instance.candidate_candidate_id_get(api_key, candidate_id, year=year, sort=sort, name=name, district=district, sort_nulls_last=sort_nulls_last, sort_null_only=sort_null_only, election_year=election_year, incumbent_challenge=incumbent_challenge, state=state, candidate_status=candidate_status, per_page=per_page, federal_funds_flag=federal_funds_flag, sort_hide_null=sort_hide_null, party=party, has_raised_funds=has_raised_funds, cycle=cycle, page=page, office=office)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->candidate_candidate_id_get: %s\n" % e)
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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.
year = 'year_example' # str | See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. (optional)
sort = 'name' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'name')
name = ['name_example'] # list[str] | Name (candidate or committee) to search for. Alias for 'q'. (optional)
district = ['district_example'] # list[str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
election_year = [56] # list[int] | Year of election (optional)
incumbent_challenge = ['incumbent_challenge_example'] # list[str] | One-letter code ('I', 'C', 'O') explaining if the candidate is an incumbent, a challenger, or if the seat is open. (optional)
state = ['state_example'] # list[str] | US state or territory where a candidate runs for office (optional)
candidate_status = ['candidate_status_example'] # list[str] | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
federal_funds_flag = True # bool | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
party = ['party_example'] # list[str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
has_raised_funds = True # bool | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) (optional)
cycle = [56] # list[int] |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
office = ['office_example'] # list[str] | Federal office candidate runs for: H, S or P (optional)

    try:
        api_response = api_instance.candidate_candidate_id_get(api_key, candidate_id, year=year, sort=sort, name=name, district=district, sort_nulls_last=sort_nulls_last, sort_null_only=sort_null_only, election_year=election_year, incumbent_challenge=incumbent_challenge, state=state, candidate_status=candidate_status, per_page=per_page, federal_funds_flag=federal_funds_flag, sort_hide_null=sort_hide_null, party=party, has_raised_funds=has_raised_funds, cycle=cycle, page=page, office=office)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->candidate_candidate_id_get: %s\n" % e)
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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.
year = 'year_example' # str | See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. (optional)
sort = 'name' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'name')
name = ['name_example'] # list[str] | Name (candidate or committee) to search for. Alias for 'q'. (optional)
district = ['district_example'] # list[str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
election_year = [56] # list[int] | Year of election (optional)
incumbent_challenge = ['incumbent_challenge_example'] # list[str] | One-letter code ('I', 'C', 'O') explaining if the candidate is an incumbent, a challenger, or if the seat is open. (optional)
state = ['state_example'] # list[str] | US state or territory where a candidate runs for office (optional)
candidate_status = ['candidate_status_example'] # list[str] | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
federal_funds_flag = True # bool | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
party = ['party_example'] # list[str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
has_raised_funds = True # bool | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) (optional)
cycle = [56] # list[int] |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
office = ['office_example'] # list[str] | Federal office candidate runs for: H, S or P (optional)

    try:
        api_response = api_instance.candidate_candidate_id_get(api_key, candidate_id, year=year, sort=sort, name=name, district=district, sort_nulls_last=sort_nulls_last, sort_null_only=sort_null_only, election_year=election_year, incumbent_challenge=incumbent_challenge, state=state, candidate_status=candidate_status, per_page=per_page, federal_funds_flag=federal_funds_flag, sort_hide_null=sort_hide_null, party=party, has_raised_funds=has_raised_funds, cycle=cycle, page=page, office=office)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->candidate_candidate_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **candidate_id** | **str**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  |
 **year** | **str**| See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. | [optional]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;name&#39;]
 **name** | [**list[str]**](str.md)| Name (candidate or committee) to search for. Alias for &#39;q&#39;. | [optional]
 **district** | [**list[str]**](str.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **election_year** | [**list[int]**](int.md)| Year of election | [optional]
 **incumbent_challenge** | [**list[str]**](str.md)| One-letter code (&#39;I&#39;, &#39;C&#39;, &#39;O&#39;) explaining if the candidate is an incumbent, a challenger, or if the seat is open. | [optional]
 **state** | [**list[str]**](str.md)| US state or territory where a candidate runs for office | [optional]
 **candidate_status** | [**list[str]**](str.md)| One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **federal_funds_flag** | **bool**| A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. | [optional]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **party** | [**list[str]**](str.md)| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional]
 **has_raised_funds** | **bool**| A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) | [optional]
 **cycle** | [**list[int]**](int.md)|  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **office** | [**list[str]**](str.md)| Federal office candidate runs for: H, S or P | [optional]

### Return type

[**CandidateDetailPage**](CandidateDetailPage.md)

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
> CandidateHistoryPage candidate_candidate_id_history_cycle_get(api_key, cycle, candidate_id, sort_nulls_last=sort_nulls_last, election_full=election_full, page=page, sort=sort, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, per_page=per_page)



 Find out a candidate's characteristics over time. This is particularly useful if the candidate runs for the same office in different districts or you want to know more about a candidate's previous races.  This information is organized by `candidate_id`, so it won't help you find a candidate who ran for different offices over time; candidates get a new ID for each office.

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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
cycle = 56 # int |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort = '-two_year_period' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-two_year_period')
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)

    try:
        api_response = api_instance.candidate_candidate_id_history_cycle_get(api_key, cycle, candidate_id, sort_nulls_last=sort_nulls_last, election_full=election_full, page=page, sort=sort, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->candidate_candidate_id_history_cycle_get: %s\n" % e)
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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
cycle = 56 # int |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort = '-two_year_period' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-two_year_period')
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)

    try:
        api_response = api_instance.candidate_candidate_id_history_cycle_get(api_key, cycle, candidate_id, sort_nulls_last=sort_nulls_last, election_full=election_full, page=page, sort=sort, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->candidate_candidate_id_history_cycle_get: %s\n" % e)
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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
cycle = 56 # int |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort = '-two_year_period' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-two_year_period')
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)

    try:
        api_response = api_instance.candidate_candidate_id_history_cycle_get(api_key, cycle, candidate_id, sort_nulls_last=sort_nulls_last, election_full=election_full, page=page, sort=sort, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->candidate_candidate_id_history_cycle_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **cycle** | **int**|  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  |
 **candidate_id** | **str**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  |
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to True]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-two_year_period&#39;]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]

### Return type

[**CandidateHistoryPage**](CandidateHistoryPage.md)

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
> CandidateHistoryPage candidate_candidate_id_history_get(api_key, candidate_id, sort_nulls_last=sort_nulls_last, election_full=election_full, page=page, sort=sort, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, per_page=per_page)



 Find out a candidate's characteristics over time. This is particularly useful if the candidate runs for the same office in different districts or you want to know more about a candidate's previous races.  This information is organized by `candidate_id`, so it won't help you find a candidate who ran for different offices over time; candidates get a new ID for each office.

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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort = '-two_year_period' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-two_year_period')
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)

    try:
        api_response = api_instance.candidate_candidate_id_history_get(api_key, candidate_id, sort_nulls_last=sort_nulls_last, election_full=election_full, page=page, sort=sort, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->candidate_candidate_id_history_get: %s\n" % e)
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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort = '-two_year_period' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-two_year_period')
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)

    try:
        api_response = api_instance.candidate_candidate_id_history_get(api_key, candidate_id, sort_nulls_last=sort_nulls_last, election_full=election_full, page=page, sort=sort, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->candidate_candidate_id_history_get: %s\n" % e)
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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort = '-two_year_period' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-two_year_period')
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)

    try:
        api_response = api_instance.candidate_candidate_id_history_get(api_key, candidate_id, sort_nulls_last=sort_nulls_last, election_full=election_full, page=page, sort=sort, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->candidate_candidate_id_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **candidate_id** | **str**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  |
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to True]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-two_year_period&#39;]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]

### Return type

[**CandidateHistoryPage**](CandidateHistoryPage.md)

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
> CommitteeTotalsPage candidate_candidate_id_totals_get(api_key, candidate_id, election_full=election_full, full_election=full_election, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle, page=page, sort_null_only=sort_null_only)



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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional)
full_election = True # bool | Parameter `full_election` is replaced by `election_full`. Please use `election_full` instead. (optional)
sort = '-cycle' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-cycle')
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)

    try:
        api_response = api_instance.candidate_candidate_id_totals_get(api_key, candidate_id, election_full=election_full, full_election=full_election, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle, page=page, sort_null_only=sort_null_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->candidate_candidate_id_totals_get: %s\n" % e)
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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional)
full_election = True # bool | Parameter `full_election` is replaced by `election_full`. Please use `election_full` instead. (optional)
sort = '-cycle' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-cycle')
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)

    try:
        api_response = api_instance.candidate_candidate_id_totals_get(api_key, candidate_id, election_full=election_full, full_election=full_election, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle, page=page, sort_null_only=sort_null_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->candidate_candidate_id_totals_get: %s\n" % e)
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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional)
full_election = True # bool | Parameter `full_election` is replaced by `election_full`. Please use `election_full` instead. (optional)
sort = '-cycle' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-cycle')
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)

    try:
        api_response = api_instance.candidate_candidate_id_totals_get(api_key, candidate_id, election_full=election_full, full_election=full_election, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, sort_nulls_last=sort_nulls_last, cycle=cycle, page=page, sort_null_only=sort_null_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->candidate_candidate_id_totals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **candidate_id** | **str**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  |
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional]
 **full_election** | **bool**| Parameter &#x60;full_election&#x60; is replaced by &#x60;election_full&#x60;. Please use &#x60;election_full&#x60; instead. | [optional]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-cycle&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]

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

# **candidates_get**
> CandidatePage candidates_get(api_key, year=year, max_first_file_date=max_first_file_date, sort=sort, q=q, candidate_id=candidate_id, name=name, is_active_candidate=is_active_candidate, district=district, sort_nulls_last=sort_nulls_last, sort_null_only=sort_null_only, election_year=election_year, incumbent_challenge=incumbent_challenge, state=state, candidate_status=candidate_status, per_page=per_page, federal_funds_flag=federal_funds_flag, sort_hide_null=sort_hide_null, party=party, has_raised_funds=has_raised_funds, cycle=cycle, page=page, min_first_file_date=min_first_file_date, office=office)



 Fetch basic information about candidates, and use parameters to filter results to the candidates you're looking for.  Each result reflects a unique FEC candidate ID. That ID is particular to the candidate for a particular office sought. If a candidate runs for the same office multiple times, the ID stays the same. If the same person runs for another office — for example, a House candidate runs for a Senate office — that candidate will get a unique ID for each office.

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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
year = 'year_example' # str | See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. (optional)
max_first_file_date = '2013-10-20' # date | Selects all candidates whose first filing was received by the FEC before this date. (optional)
sort = 'name' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'name')
q = ['q_example'] # list[str] | Name of candidate running for office (optional)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
name = ['name_example'] # list[str] | Name (candidate or committee) to search for. Alias for 'q'. (optional)
is_active_candidate = True # bool |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  (optional)
district = ['district_example'] # list[str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
election_year = [56] # list[int] | Year of election (optional)
incumbent_challenge = ['incumbent_challenge_example'] # list[str] | One-letter code ('I', 'C', 'O') explaining if the candidate is an incumbent, a challenger, or if the seat is open. (optional)
state = ['state_example'] # list[str] | US state or territory where a candidate runs for office (optional)
candidate_status = ['candidate_status_example'] # list[str] | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
federal_funds_flag = True # bool | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
party = ['party_example'] # list[str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
has_raised_funds = True # bool | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) (optional)
cycle = [56] # list[int] |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
min_first_file_date = '2013-10-20' # date | Selects all candidates whose first filing was received by the FEC after this date. (optional)
office = ['office_example'] # list[str] | Federal office candidate runs for: H, S or P (optional)

    try:
        api_response = api_instance.candidates_get(api_key, year=year, max_first_file_date=max_first_file_date, sort=sort, q=q, candidate_id=candidate_id, name=name, is_active_candidate=is_active_candidate, district=district, sort_nulls_last=sort_nulls_last, sort_null_only=sort_null_only, election_year=election_year, incumbent_challenge=incumbent_challenge, state=state, candidate_status=candidate_status, per_page=per_page, federal_funds_flag=federal_funds_flag, sort_hide_null=sort_hide_null, party=party, has_raised_funds=has_raised_funds, cycle=cycle, page=page, min_first_file_date=min_first_file_date, office=office)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->candidates_get: %s\n" % e)
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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
year = 'year_example' # str | See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. (optional)
max_first_file_date = '2013-10-20' # date | Selects all candidates whose first filing was received by the FEC before this date. (optional)
sort = 'name' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'name')
q = ['q_example'] # list[str] | Name of candidate running for office (optional)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
name = ['name_example'] # list[str] | Name (candidate or committee) to search for. Alias for 'q'. (optional)
is_active_candidate = True # bool |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  (optional)
district = ['district_example'] # list[str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
election_year = [56] # list[int] | Year of election (optional)
incumbent_challenge = ['incumbent_challenge_example'] # list[str] | One-letter code ('I', 'C', 'O') explaining if the candidate is an incumbent, a challenger, or if the seat is open. (optional)
state = ['state_example'] # list[str] | US state or territory where a candidate runs for office (optional)
candidate_status = ['candidate_status_example'] # list[str] | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
federal_funds_flag = True # bool | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
party = ['party_example'] # list[str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
has_raised_funds = True # bool | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) (optional)
cycle = [56] # list[int] |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
min_first_file_date = '2013-10-20' # date | Selects all candidates whose first filing was received by the FEC after this date. (optional)
office = ['office_example'] # list[str] | Federal office candidate runs for: H, S or P (optional)

    try:
        api_response = api_instance.candidates_get(api_key, year=year, max_first_file_date=max_first_file_date, sort=sort, q=q, candidate_id=candidate_id, name=name, is_active_candidate=is_active_candidate, district=district, sort_nulls_last=sort_nulls_last, sort_null_only=sort_null_only, election_year=election_year, incumbent_challenge=incumbent_challenge, state=state, candidate_status=candidate_status, per_page=per_page, federal_funds_flag=federal_funds_flag, sort_hide_null=sort_hide_null, party=party, has_raised_funds=has_raised_funds, cycle=cycle, page=page, min_first_file_date=min_first_file_date, office=office)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->candidates_get: %s\n" % e)
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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
year = 'year_example' # str | See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. (optional)
max_first_file_date = '2013-10-20' # date | Selects all candidates whose first filing was received by the FEC before this date. (optional)
sort = 'name' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'name')
q = ['q_example'] # list[str] | Name of candidate running for office (optional)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
name = ['name_example'] # list[str] | Name (candidate or committee) to search for. Alias for 'q'. (optional)
is_active_candidate = True # bool |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  (optional)
district = ['district_example'] # list[str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
election_year = [56] # list[int] | Year of election (optional)
incumbent_challenge = ['incumbent_challenge_example'] # list[str] | One-letter code ('I', 'C', 'O') explaining if the candidate is an incumbent, a challenger, or if the seat is open. (optional)
state = ['state_example'] # list[str] | US state or territory where a candidate runs for office (optional)
candidate_status = ['candidate_status_example'] # list[str] | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
federal_funds_flag = True # bool | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
party = ['party_example'] # list[str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
has_raised_funds = True # bool | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) (optional)
cycle = [56] # list[int] |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
min_first_file_date = '2013-10-20' # date | Selects all candidates whose first filing was received by the FEC after this date. (optional)
office = ['office_example'] # list[str] | Federal office candidate runs for: H, S or P (optional)

    try:
        api_response = api_instance.candidates_get(api_key, year=year, max_first_file_date=max_first_file_date, sort=sort, q=q, candidate_id=candidate_id, name=name, is_active_candidate=is_active_candidate, district=district, sort_nulls_last=sort_nulls_last, sort_null_only=sort_null_only, election_year=election_year, incumbent_challenge=incumbent_challenge, state=state, candidate_status=candidate_status, per_page=per_page, federal_funds_flag=federal_funds_flag, sort_hide_null=sort_hide_null, party=party, has_raised_funds=has_raised_funds, cycle=cycle, page=page, min_first_file_date=min_first_file_date, office=office)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->candidates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **year** | **str**| See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. | [optional]
 **max_first_file_date** | **date**| Selects all candidates whose first filing was received by the FEC before this date. | [optional]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;name&#39;]
 **q** | [**list[str]**](str.md)| Name of candidate running for office | [optional]
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional]
 **name** | [**list[str]**](str.md)| Name (candidate or committee) to search for. Alias for &#39;q&#39;. | [optional]
 **is_active_candidate** | **bool**|  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  | [optional]
 **district** | [**list[str]**](str.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **election_year** | [**list[int]**](int.md)| Year of election | [optional]
 **incumbent_challenge** | [**list[str]**](str.md)| One-letter code (&#39;I&#39;, &#39;C&#39;, &#39;O&#39;) explaining if the candidate is an incumbent, a challenger, or if the seat is open. | [optional]
 **state** | [**list[str]**](str.md)| US state or territory where a candidate runs for office | [optional]
 **candidate_status** | [**list[str]**](str.md)| One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **federal_funds_flag** | **bool**| A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. | [optional]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **party** | [**list[str]**](str.md)| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional]
 **has_raised_funds** | **bool**| A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) | [optional]
 **cycle** | [**list[int]**](int.md)|  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **min_first_file_date** | **date**| Selects all candidates whose first filing was received by the FEC after this date. | [optional]
 **office** | [**list[str]**](str.md)| Federal office candidate runs for: H, S or P | [optional]

### Return type

[**CandidatePage**](CandidatePage.md)

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
> CandidatePage candidates_search_get(api_key, year=year, max_first_file_date=max_first_file_date, sort=sort, q=q, candidate_id=candidate_id, name=name, is_active_candidate=is_active_candidate, district=district, sort_nulls_last=sort_nulls_last, sort_null_only=sort_null_only, election_year=election_year, incumbent_challenge=incumbent_challenge, state=state, candidate_status=candidate_status, per_page=per_page, federal_funds_flag=federal_funds_flag, sort_hide_null=sort_hide_null, party=party, has_raised_funds=has_raised_funds, cycle=cycle, page=page, min_first_file_date=min_first_file_date, office=office)



 Fetch basic information about candidates and their principal committees.  Each result reflects a unique FEC candidate ID. That ID is assigned to the candidate for a particular office sought. If a candidate runs for the same office over time, that ID stays the same. If the same person runs for multiple offices — for example, a House candidate runs for a Senate office — that candidate will get a unique ID for each office.  The candidate endpoints primarily use data from FEC registration [Form 1](http://www.fec.gov/pdf/forms/fecfrm1.pdf), for candidate information, and [Form 2](http://www.fec.gov/pdf/forms/fecfrm2.pdf), for committees information, with additional information to provide context.

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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
year = 'year_example' # str | See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. (optional)
max_first_file_date = '2013-10-20' # date | Selects all candidates whose first filing was received by the FEC before this date. (optional)
sort = 'name' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'name')
q = ['q_example'] # list[str] | Name of candidate running for office (optional)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
name = ['name_example'] # list[str] | Name (candidate or committee) to search for. Alias for 'q'. (optional)
is_active_candidate = True # bool |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  (optional)
district = ['district_example'] # list[str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
election_year = [56] # list[int] | Year of election (optional)
incumbent_challenge = ['incumbent_challenge_example'] # list[str] | One-letter code ('I', 'C', 'O') explaining if the candidate is an incumbent, a challenger, or if the seat is open. (optional)
state = ['state_example'] # list[str] | US state or territory where a candidate runs for office (optional)
candidate_status = ['candidate_status_example'] # list[str] | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
federal_funds_flag = True # bool | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
party = ['party_example'] # list[str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
has_raised_funds = True # bool | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) (optional)
cycle = [56] # list[int] |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
min_first_file_date = '2013-10-20' # date | Selects all candidates whose first filing was received by the FEC after this date. (optional)
office = ['office_example'] # list[str] | Federal office candidate runs for: H, S or P (optional)

    try:
        api_response = api_instance.candidates_search_get(api_key, year=year, max_first_file_date=max_first_file_date, sort=sort, q=q, candidate_id=candidate_id, name=name, is_active_candidate=is_active_candidate, district=district, sort_nulls_last=sort_nulls_last, sort_null_only=sort_null_only, election_year=election_year, incumbent_challenge=incumbent_challenge, state=state, candidate_status=candidate_status, per_page=per_page, federal_funds_flag=federal_funds_flag, sort_hide_null=sort_hide_null, party=party, has_raised_funds=has_raised_funds, cycle=cycle, page=page, min_first_file_date=min_first_file_date, office=office)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->candidates_search_get: %s\n" % e)
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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
year = 'year_example' # str | See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. (optional)
max_first_file_date = '2013-10-20' # date | Selects all candidates whose first filing was received by the FEC before this date. (optional)
sort = 'name' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'name')
q = ['q_example'] # list[str] | Name of candidate running for office (optional)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
name = ['name_example'] # list[str] | Name (candidate or committee) to search for. Alias for 'q'. (optional)
is_active_candidate = True # bool |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  (optional)
district = ['district_example'] # list[str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
election_year = [56] # list[int] | Year of election (optional)
incumbent_challenge = ['incumbent_challenge_example'] # list[str] | One-letter code ('I', 'C', 'O') explaining if the candidate is an incumbent, a challenger, or if the seat is open. (optional)
state = ['state_example'] # list[str] | US state or territory where a candidate runs for office (optional)
candidate_status = ['candidate_status_example'] # list[str] | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
federal_funds_flag = True # bool | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
party = ['party_example'] # list[str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
has_raised_funds = True # bool | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) (optional)
cycle = [56] # list[int] |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
min_first_file_date = '2013-10-20' # date | Selects all candidates whose first filing was received by the FEC after this date. (optional)
office = ['office_example'] # list[str] | Federal office candidate runs for: H, S or P (optional)

    try:
        api_response = api_instance.candidates_search_get(api_key, year=year, max_first_file_date=max_first_file_date, sort=sort, q=q, candidate_id=candidate_id, name=name, is_active_candidate=is_active_candidate, district=district, sort_nulls_last=sort_nulls_last, sort_null_only=sort_null_only, election_year=election_year, incumbent_challenge=incumbent_challenge, state=state, candidate_status=candidate_status, per_page=per_page, federal_funds_flag=federal_funds_flag, sort_hide_null=sort_hide_null, party=party, has_raised_funds=has_raised_funds, cycle=cycle, page=page, min_first_file_date=min_first_file_date, office=office)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->candidates_search_get: %s\n" % e)
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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
year = 'year_example' # str | See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. (optional)
max_first_file_date = '2013-10-20' # date | Selects all candidates whose first filing was received by the FEC before this date. (optional)
sort = 'name' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'name')
q = ['q_example'] # list[str] | Name of candidate running for office (optional)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
name = ['name_example'] # list[str] | Name (candidate or committee) to search for. Alias for 'q'. (optional)
is_active_candidate = True # bool |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  (optional)
district = ['district_example'] # list[str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
election_year = [56] # list[int] | Year of election (optional)
incumbent_challenge = ['incumbent_challenge_example'] # list[str] | One-letter code ('I', 'C', 'O') explaining if the candidate is an incumbent, a challenger, or if the seat is open. (optional)
state = ['state_example'] # list[str] | US state or territory where a candidate runs for office (optional)
candidate_status = ['candidate_status_example'] # list[str] | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
federal_funds_flag = True # bool | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
party = ['party_example'] # list[str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
has_raised_funds = True # bool | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) (optional)
cycle = [56] # list[int] |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
min_first_file_date = '2013-10-20' # date | Selects all candidates whose first filing was received by the FEC after this date. (optional)
office = ['office_example'] # list[str] | Federal office candidate runs for: H, S or P (optional)

    try:
        api_response = api_instance.candidates_search_get(api_key, year=year, max_first_file_date=max_first_file_date, sort=sort, q=q, candidate_id=candidate_id, name=name, is_active_candidate=is_active_candidate, district=district, sort_nulls_last=sort_nulls_last, sort_null_only=sort_null_only, election_year=election_year, incumbent_challenge=incumbent_challenge, state=state, candidate_status=candidate_status, per_page=per_page, federal_funds_flag=federal_funds_flag, sort_hide_null=sort_hide_null, party=party, has_raised_funds=has_raised_funds, cycle=cycle, page=page, min_first_file_date=min_first_file_date, office=office)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->candidates_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **year** | **str**| See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. | [optional]
 **max_first_file_date** | **date**| Selects all candidates whose first filing was received by the FEC before this date. | [optional]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;name&#39;]
 **q** | [**list[str]**](str.md)| Name of candidate running for office | [optional]
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional]
 **name** | [**list[str]**](str.md)| Name (candidate or committee) to search for. Alias for &#39;q&#39;. | [optional]
 **is_active_candidate** | **bool**|  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  | [optional]
 **district** | [**list[str]**](str.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **election_year** | [**list[int]**](int.md)| Year of election | [optional]
 **incumbent_challenge** | [**list[str]**](str.md)| One-letter code (&#39;I&#39;, &#39;C&#39;, &#39;O&#39;) explaining if the candidate is an incumbent, a challenger, or if the seat is open. | [optional]
 **state** | [**list[str]**](str.md)| US state or territory where a candidate runs for office | [optional]
 **candidate_status** | [**list[str]**](str.md)| One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **federal_funds_flag** | **bool**| A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. | [optional]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **party** | [**list[str]**](str.md)| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional]
 **has_raised_funds** | **bool**| A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) | [optional]
 **cycle** | [**list[int]**](int.md)|  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **min_first_file_date** | **date**| Selects all candidates whose first filing was received by the FEC after this date. | [optional]
 **office** | [**list[str]**](str.md)| Federal office candidate runs for: H, S or P | [optional]

### Return type

[**CandidatePage**](CandidatePage.md)

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
> TotalByOfficeByPartyPage candidates_totals_by_office_by_party_get(api_key, election_year=election_year, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, is_active_candidate=is_active_candidate, sort_nulls_last=sort_nulls_last, page=page, sort_null_only=sort_null_only, office=office)



 Aggregated candidate receipts and disbursements grouped by office by party by cycle.

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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
election_year = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
is_active_candidate = True # bool |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
office = 'office_example' # str | Federal office candidate runs for: H, S or P (optional)

    try:
        api_response = api_instance.candidates_totals_by_office_by_party_get(api_key, election_year=election_year, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, is_active_candidate=is_active_candidate, sort_nulls_last=sort_nulls_last, page=page, sort_null_only=sort_null_only, office=office)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->candidates_totals_by_office_by_party_get: %s\n" % e)
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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
election_year = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
is_active_candidate = True # bool |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
office = 'office_example' # str | Federal office candidate runs for: H, S or P (optional)

    try:
        api_response = api_instance.candidates_totals_by_office_by_party_get(api_key, election_year=election_year, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, is_active_candidate=is_active_candidate, sort_nulls_last=sort_nulls_last, page=page, sort_null_only=sort_null_only, office=office)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->candidates_totals_by_office_by_party_get: %s\n" % e)
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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
election_year = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
is_active_candidate = True # bool |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
office = 'office_example' # str | Federal office candidate runs for: H, S or P (optional)

    try:
        api_response = api_instance.candidates_totals_by_office_by_party_get(api_key, election_year=election_year, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, is_active_candidate=is_active_candidate, sort_nulls_last=sort_nulls_last, page=page, sort_null_only=sort_null_only, office=office)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->candidates_totals_by_office_by_party_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **election_year** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;null&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **is_active_candidate** | **bool**|  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **office** | **str**| Federal office candidate runs for: H, S or P | [optional]

### Return type

[**TotalByOfficeByPartyPage**](TotalByOfficeByPartyPage.md)

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
> TotalByOfficePage candidates_totals_by_office_get(api_key, election_year=election_year, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, is_active_candidate=is_active_candidate, sort_nulls_last=sort_nulls_last, page=page, sort_null_only=sort_null_only, office=office)



 Aggregated candidate receipts and disbursements grouped by office by cycle.

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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
election_year = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
is_active_candidate = True # bool |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
office = 'office_example' # str | Federal office candidate runs for: H, S or P (optional)

    try:
        api_response = api_instance.candidates_totals_by_office_get(api_key, election_year=election_year, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, is_active_candidate=is_active_candidate, sort_nulls_last=sort_nulls_last, page=page, sort_null_only=sort_null_only, office=office)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->candidates_totals_by_office_get: %s\n" % e)
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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
election_year = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
is_active_candidate = True # bool |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
office = 'office_example' # str | Federal office candidate runs for: H, S or P (optional)

    try:
        api_response = api_instance.candidates_totals_by_office_get(api_key, election_year=election_year, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, is_active_candidate=is_active_candidate, sort_nulls_last=sort_nulls_last, page=page, sort_null_only=sort_null_only, office=office)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->candidates_totals_by_office_get: %s\n" % e)
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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
election_year = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
is_active_candidate = True # bool |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
office = 'office_example' # str | Federal office candidate runs for: H, S or P (optional)

    try:
        api_response = api_instance.candidates_totals_by_office_get(api_key, election_year=election_year, sort=sort, sort_hide_null=sort_hide_null, per_page=per_page, is_active_candidate=is_active_candidate, sort_nulls_last=sort_nulls_last, page=page, sort_null_only=sort_null_only, office=office)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->candidates_totals_by_office_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **election_year** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;null&#39;]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **is_active_candidate** | **bool**|  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **office** | **str**| Federal office candidate runs for: H, S or P | [optional]

### Return type

[**TotalByOfficePage**](TotalByOfficePage.md)

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
> CandidateHistoryTotalPage candidates_totals_get(api_key, election_full=election_full, sort=sort, q=q, min_debts_owed_by_committee=min_debts_owed_by_committee, candidate_id=candidate_id, max_receipts=max_receipts, min_receipts=min_receipts, is_active_candidate=is_active_candidate, district=district, sort_nulls_last=sort_nulls_last, sort_null_only=sort_null_only, max_debts_owed_by_committee=max_debts_owed_by_committee, min_cash_on_hand_end_period=min_cash_on_hand_end_period, election_year=election_year, max_disbursements=max_disbursements, state=state, max_cash_on_hand_end_period=max_cash_on_hand_end_period, sort_hide_null=sort_hide_null, per_page=per_page, federal_funds_flag=federal_funds_flag, party=party, has_raised_funds=has_raised_funds, cycle=cycle, page=page, min_disbursements=min_disbursements, office=office)



 Aggregated candidate receipts and disbursements grouped by cycle.

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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
q = ['q_example'] # list[str] | Name of candidate running for office (optional)
min_debts_owed_by_committee = 'min_debts_owed_by_committee_example' # str | Minimum debt (optional)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
max_receipts = 'max_receipts_example' # str | Maximum aggregated receipts (optional)
min_receipts = 'min_receipts_example' # str | Minimum aggregated receipts (optional)
is_active_candidate = True # bool |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  (optional)
district = ['district_example'] # list[str] | District of candidate (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
max_debts_owed_by_committee = 'max_debts_owed_by_committee_example' # str | Maximum debt (optional)
min_cash_on_hand_end_period = 'min_cash_on_hand_end_period_example' # str | Minimum cash on hand (optional)
election_year = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
max_disbursements = 'max_disbursements_example' # str | Maximum aggregated disbursements (optional)
state = ['state_example'] # list[str] | State of candidate (optional)
max_cash_on_hand_end_period = 'max_cash_on_hand_end_period_example' # str | Maximum cash on hand (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
federal_funds_flag = True # bool | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. (optional)
party = ['party_example'] # list[str] | Three-letter party code (optional)
has_raised_funds = True # bool | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) (optional)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
min_disbursements = 'min_disbursements_example' # str | Minimum aggregated disbursements (optional)
office = ['office_example'] # list[str] | Federal office candidate runs for: H, S or P (optional)

    try:
        api_response = api_instance.candidates_totals_get(api_key, election_full=election_full, sort=sort, q=q, min_debts_owed_by_committee=min_debts_owed_by_committee, candidate_id=candidate_id, max_receipts=max_receipts, min_receipts=min_receipts, is_active_candidate=is_active_candidate, district=district, sort_nulls_last=sort_nulls_last, sort_null_only=sort_null_only, max_debts_owed_by_committee=max_debts_owed_by_committee, min_cash_on_hand_end_period=min_cash_on_hand_end_period, election_year=election_year, max_disbursements=max_disbursements, state=state, max_cash_on_hand_end_period=max_cash_on_hand_end_period, sort_hide_null=sort_hide_null, per_page=per_page, federal_funds_flag=federal_funds_flag, party=party, has_raised_funds=has_raised_funds, cycle=cycle, page=page, min_disbursements=min_disbursements, office=office)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->candidates_totals_get: %s\n" % e)
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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
q = ['q_example'] # list[str] | Name of candidate running for office (optional)
min_debts_owed_by_committee = 'min_debts_owed_by_committee_example' # str | Minimum debt (optional)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
max_receipts = 'max_receipts_example' # str | Maximum aggregated receipts (optional)
min_receipts = 'min_receipts_example' # str | Minimum aggregated receipts (optional)
is_active_candidate = True # bool |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  (optional)
district = ['district_example'] # list[str] | District of candidate (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
max_debts_owed_by_committee = 'max_debts_owed_by_committee_example' # str | Maximum debt (optional)
min_cash_on_hand_end_period = 'min_cash_on_hand_end_period_example' # str | Minimum cash on hand (optional)
election_year = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
max_disbursements = 'max_disbursements_example' # str | Maximum aggregated disbursements (optional)
state = ['state_example'] # list[str] | State of candidate (optional)
max_cash_on_hand_end_period = 'max_cash_on_hand_end_period_example' # str | Maximum cash on hand (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
federal_funds_flag = True # bool | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. (optional)
party = ['party_example'] # list[str] | Three-letter party code (optional)
has_raised_funds = True # bool | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) (optional)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
min_disbursements = 'min_disbursements_example' # str | Minimum aggregated disbursements (optional)
office = ['office_example'] # list[str] | Federal office candidate runs for: H, S or P (optional)

    try:
        api_response = api_instance.candidates_totals_get(api_key, election_full=election_full, sort=sort, q=q, min_debts_owed_by_committee=min_debts_owed_by_committee, candidate_id=candidate_id, max_receipts=max_receipts, min_receipts=min_receipts, is_active_candidate=is_active_candidate, district=district, sort_nulls_last=sort_nulls_last, sort_null_only=sort_null_only, max_debts_owed_by_committee=max_debts_owed_by_committee, min_cash_on_hand_end_period=min_cash_on_hand_end_period, election_year=election_year, max_disbursements=max_disbursements, state=state, max_cash_on_hand_end_period=max_cash_on_hand_end_period, sort_hide_null=sort_hide_null, per_page=per_page, federal_funds_flag=federal_funds_flag, party=party, has_raised_funds=has_raised_funds, cycle=cycle, page=page, min_disbursements=min_disbursements, office=office)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->candidates_totals_get: %s\n" % e)
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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
q = ['q_example'] # list[str] | Name of candidate running for office (optional)
min_debts_owed_by_committee = 'min_debts_owed_by_committee_example' # str | Minimum debt (optional)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
max_receipts = 'max_receipts_example' # str | Maximum aggregated receipts (optional)
min_receipts = 'min_receipts_example' # str | Minimum aggregated receipts (optional)
is_active_candidate = True # bool |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  (optional)
district = ['district_example'] # list[str] | District of candidate (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
max_debts_owed_by_committee = 'max_debts_owed_by_committee_example' # str | Maximum debt (optional)
min_cash_on_hand_end_period = 'min_cash_on_hand_end_period_example' # str | Minimum cash on hand (optional)
election_year = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
max_disbursements = 'max_disbursements_example' # str | Maximum aggregated disbursements (optional)
state = ['state_example'] # list[str] | State of candidate (optional)
max_cash_on_hand_end_period = 'max_cash_on_hand_end_period_example' # str | Maximum cash on hand (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
federal_funds_flag = True # bool | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. (optional)
party = ['party_example'] # list[str] | Three-letter party code (optional)
has_raised_funds = True # bool | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) (optional)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
min_disbursements = 'min_disbursements_example' # str | Minimum aggregated disbursements (optional)
office = ['office_example'] # list[str] | Federal office candidate runs for: H, S or P (optional)

    try:
        api_response = api_instance.candidates_totals_get(api_key, election_full=election_full, sort=sort, q=q, min_debts_owed_by_committee=min_debts_owed_by_committee, candidate_id=candidate_id, max_receipts=max_receipts, min_receipts=min_receipts, is_active_candidate=is_active_candidate, district=district, sort_nulls_last=sort_nulls_last, sort_null_only=sort_null_only, max_debts_owed_by_committee=max_debts_owed_by_committee, min_cash_on_hand_end_period=min_cash_on_hand_end_period, election_year=election_year, max_disbursements=max_disbursements, state=state, max_cash_on_hand_end_period=max_cash_on_hand_end_period, sort_hide_null=sort_hide_null, per_page=per_page, federal_funds_flag=federal_funds_flag, party=party, has_raised_funds=has_raised_funds, cycle=cycle, page=page, min_disbursements=min_disbursements, office=office)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->candidates_totals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to True]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;null&#39;]
 **q** | [**list[str]**](str.md)| Name of candidate running for office | [optional]
 **min_debts_owed_by_committee** | **str**| Minimum debt | [optional]
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional]
 **max_receipts** | **str**| Maximum aggregated receipts | [optional]
 **min_receipts** | **str**| Minimum aggregated receipts | [optional]
 **is_active_candidate** | **bool**|  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  | [optional]
 **district** | [**list[str]**](str.md)| District of candidate | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **max_debts_owed_by_committee** | **str**| Maximum debt | [optional]
 **min_cash_on_hand_end_period** | **str**| Minimum cash on hand | [optional]
 **election_year** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional]
 **max_disbursements** | **str**| Maximum aggregated disbursements | [optional]
 **state** | [**list[str]**](str.md)| State of candidate | [optional]
 **max_cash_on_hand_end_period** | **str**| Maximum cash on hand | [optional]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **federal_funds_flag** | **bool**| A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. | [optional]
 **party** | [**list[str]**](str.md)| Three-letter party code | [optional]
 **has_raised_funds** | **bool**| A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) | [optional]
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **min_disbursements** | **str**| Minimum aggregated disbursements | [optional]
 **office** | [**list[str]**](str.md)| Federal office candidate runs for: H, S or P | [optional]

### Return type

[**CandidateHistoryTotalPage**](CandidateHistoryTotalPage.md)

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
> CandidateDetailPage committee_committee_id_candidates_get(api_key, committee_id, year=year, sort=sort, name=name, district=district, sort_nulls_last=sort_nulls_last, sort_null_only=sort_null_only, election_year=election_year, incumbent_challenge=incumbent_challenge, state=state, candidate_status=candidate_status, per_page=per_page, federal_funds_flag=federal_funds_flag, sort_hide_null=sort_hide_null, party=party, has_raised_funds=has_raised_funds, cycle=cycle, page=page, office=office)



 This endpoint is useful for finding detailed information about a particular candidate. Use the `candidate_id` to find the most recent information about that candidate.

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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.
year = 'year_example' # str | See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. (optional)
sort = 'name' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'name')
name = ['name_example'] # list[str] | Name (candidate or committee) to search for. Alias for 'q'. (optional)
district = ['district_example'] # list[str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
election_year = [56] # list[int] | Year of election (optional)
incumbent_challenge = ['incumbent_challenge_example'] # list[str] | One-letter code ('I', 'C', 'O') explaining if the candidate is an incumbent, a challenger, or if the seat is open. (optional)
state = ['state_example'] # list[str] | US state or territory where a candidate runs for office (optional)
candidate_status = ['candidate_status_example'] # list[str] | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
federal_funds_flag = True # bool | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
party = ['party_example'] # list[str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
has_raised_funds = True # bool | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) (optional)
cycle = [56] # list[int] |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
office = ['office_example'] # list[str] | Federal office candidate runs for: H, S or P (optional)

    try:
        api_response = api_instance.committee_committee_id_candidates_get(api_key, committee_id, year=year, sort=sort, name=name, district=district, sort_nulls_last=sort_nulls_last, sort_null_only=sort_null_only, election_year=election_year, incumbent_challenge=incumbent_challenge, state=state, candidate_status=candidate_status, per_page=per_page, federal_funds_flag=federal_funds_flag, sort_hide_null=sort_hide_null, party=party, has_raised_funds=has_raised_funds, cycle=cycle, page=page, office=office)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->committee_committee_id_candidates_get: %s\n" % e)
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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.
year = 'year_example' # str | See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. (optional)
sort = 'name' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'name')
name = ['name_example'] # list[str] | Name (candidate or committee) to search for. Alias for 'q'. (optional)
district = ['district_example'] # list[str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
election_year = [56] # list[int] | Year of election (optional)
incumbent_challenge = ['incumbent_challenge_example'] # list[str] | One-letter code ('I', 'C', 'O') explaining if the candidate is an incumbent, a challenger, or if the seat is open. (optional)
state = ['state_example'] # list[str] | US state or territory where a candidate runs for office (optional)
candidate_status = ['candidate_status_example'] # list[str] | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
federal_funds_flag = True # bool | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
party = ['party_example'] # list[str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
has_raised_funds = True # bool | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) (optional)
cycle = [56] # list[int] |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
office = ['office_example'] # list[str] | Federal office candidate runs for: H, S or P (optional)

    try:
        api_response = api_instance.committee_committee_id_candidates_get(api_key, committee_id, year=year, sort=sort, name=name, district=district, sort_nulls_last=sort_nulls_last, sort_null_only=sort_null_only, election_year=election_year, incumbent_challenge=incumbent_challenge, state=state, candidate_status=candidate_status, per_page=per_page, federal_funds_flag=federal_funds_flag, sort_hide_null=sort_hide_null, party=party, has_raised_funds=has_raised_funds, cycle=cycle, page=page, office=office)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->committee_committee_id_candidates_get: %s\n" % e)
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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.
year = 'year_example' # str | See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. (optional)
sort = 'name' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'name')
name = ['name_example'] # list[str] | Name (candidate or committee) to search for. Alias for 'q'. (optional)
district = ['district_example'] # list[str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
election_year = [56] # list[int] | Year of election (optional)
incumbent_challenge = ['incumbent_challenge_example'] # list[str] | One-letter code ('I', 'C', 'O') explaining if the candidate is an incumbent, a challenger, or if the seat is open. (optional)
state = ['state_example'] # list[str] | US state or territory where a candidate runs for office (optional)
candidate_status = ['candidate_status_example'] # list[str] | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
federal_funds_flag = True # bool | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
party = ['party_example'] # list[str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
has_raised_funds = True # bool | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) (optional)
cycle = [56] # list[int] |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
office = ['office_example'] # list[str] | Federal office candidate runs for: H, S or P (optional)

    try:
        api_response = api_instance.committee_committee_id_candidates_get(api_key, committee_id, year=year, sort=sort, name=name, district=district, sort_nulls_last=sort_nulls_last, sort_null_only=sort_null_only, election_year=election_year, incumbent_challenge=incumbent_challenge, state=state, candidate_status=candidate_status, per_page=per_page, federal_funds_flag=federal_funds_flag, sort_hide_null=sort_hide_null, party=party, has_raised_funds=has_raised_funds, cycle=cycle, page=page, office=office)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->committee_committee_id_candidates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **committee_id** | **str**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  |
 **year** | **str**| See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. | [optional]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;name&#39;]
 **name** | [**list[str]**](str.md)| Name (candidate or committee) to search for. Alias for &#39;q&#39;. | [optional]
 **district** | [**list[str]**](str.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **election_year** | [**list[int]**](int.md)| Year of election | [optional]
 **incumbent_challenge** | [**list[str]**](str.md)| One-letter code (&#39;I&#39;, &#39;C&#39;, &#39;O&#39;) explaining if the candidate is an incumbent, a challenger, or if the seat is open. | [optional]
 **state** | [**list[str]**](str.md)| US state or territory where a candidate runs for office | [optional]
 **candidate_status** | [**list[str]**](str.md)| One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **federal_funds_flag** | **bool**| A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. | [optional]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **party** | [**list[str]**](str.md)| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional]
 **has_raised_funds** | **bool**| A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) | [optional]
 **cycle** | [**list[int]**](int.md)|  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **office** | [**list[str]**](str.md)| Federal office candidate runs for: H, S or P | [optional]

### Return type

[**CandidateDetailPage**](CandidateDetailPage.md)

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
> CandidateHistoryPage committee_committee_id_candidates_history_cycle_get(api_key, committee_id, cycle, sort_nulls_last=sort_nulls_last, election_full=election_full, page=page, sort=sort, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, per_page=per_page)



 Find out a candidate's characteristics over time. This is particularly useful if the candidate runs for the same office in different districts or you want to know more about a candidate's previous races.  This information is organized by `candidate_id`, so it won't help you find a candidate who ran for different offices over time; candidates get a new ID for each office.

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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.
cycle = 56 # int |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort = '-two_year_period' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-two_year_period')
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)

    try:
        api_response = api_instance.committee_committee_id_candidates_history_cycle_get(api_key, committee_id, cycle, sort_nulls_last=sort_nulls_last, election_full=election_full, page=page, sort=sort, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->committee_committee_id_candidates_history_cycle_get: %s\n" % e)
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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.
cycle = 56 # int |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort = '-two_year_period' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-two_year_period')
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)

    try:
        api_response = api_instance.committee_committee_id_candidates_history_cycle_get(api_key, committee_id, cycle, sort_nulls_last=sort_nulls_last, election_full=election_full, page=page, sort=sort, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->committee_committee_id_candidates_history_cycle_get: %s\n" % e)
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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.
cycle = 56 # int |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort = '-two_year_period' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-two_year_period')
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)

    try:
        api_response = api_instance.committee_committee_id_candidates_history_cycle_get(api_key, committee_id, cycle, sort_nulls_last=sort_nulls_last, election_full=election_full, page=page, sort=sort, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->committee_committee_id_candidates_history_cycle_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **committee_id** | **str**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  |
 **cycle** | **int**|  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  |
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to True]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-two_year_period&#39;]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]

### Return type

[**CandidateHistoryPage**](CandidateHistoryPage.md)

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
> CandidateHistoryPage committee_committee_id_candidates_history_get(api_key, committee_id, sort_nulls_last=sort_nulls_last, election_full=election_full, page=page, sort=sort, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, per_page=per_page)



 Find out a candidate's characteristics over time. This is particularly useful if the candidate runs for the same office in different districts or you want to know more about a candidate's previous races.  This information is organized by `candidate_id`, so it won't help you find a candidate who ran for different offices over time; candidates get a new ID for each office.

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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort = '-two_year_period' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-two_year_period')
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)

    try:
        api_response = api_instance.committee_committee_id_candidates_history_get(api_key, committee_id, sort_nulls_last=sort_nulls_last, election_full=election_full, page=page, sort=sort, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->committee_committee_id_candidates_history_get: %s\n" % e)
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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort = '-two_year_period' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-two_year_period')
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)

    try:
        api_response = api_instance.committee_committee_id_candidates_history_get(api_key, committee_id, sort_nulls_last=sort_nulls_last, election_full=election_full, page=page, sort=sort, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->committee_committee_id_candidates_history_get: %s\n" % e)
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
    api_instance = openfec_sdk.CandidateApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to True)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort = '-two_year_period' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-two_year_period')
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)

    try:
        api_response = api_instance.committee_committee_id_candidates_history_get(api_key, committee_id, sort_nulls_last=sort_nulls_last, election_full=election_full, page=page, sort=sort, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CandidateApi->committee_committee_id_candidates_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **committee_id** | **str**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  |
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to True]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-two_year_period&#39;]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]

### Return type

[**CandidateHistoryPage**](CandidateHistoryPage.md)

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
