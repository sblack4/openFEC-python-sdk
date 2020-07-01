# swagger_client.CandidateApi

All URIs are relative to *https://localhost/v1*

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
> CandidateDetailPage candidate_candidate_id_get(api_key, candidate_id, federal_funds_flag=federal_funds_flag, cycle=cycle, sort=sort, year=year, state=state, name=name, sort_nulls_last=sort_nulls_last, sort_hide_null=sort_hide_null, per_page=per_page, district=district, page=page, incumbent_challenge=incumbent_challenge, party=party, has_raised_funds=has_raised_funds, sort_null_only=sort_null_only, candidate_status=candidate_status, office=office, election_year=election_year)



 This endpoint is useful for finding detailed information about a particular candidate. Use the `candidate_id` to find the most recent information about that candidate.  

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
api_instance = swagger_client.CandidateApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. 
federal_funds_flag = true # bool | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. (optional)
cycle = [56] # list[int] |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.  (optional)
sort = 'name' # str | Provide a field to sort by. Use - for descending order. (optional) (default to name)
year = 'year_example' # str | See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. (optional)
state = ['state_example'] # list[str] | US state or territory where a candidate runs for office (optional)
name = ['name_example'] # list[str] | Name (candidate or committee) to search for. Alias for 'q'. (optional)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
district = ['district_example'] # list[str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
incumbent_challenge = ['incumbent_challenge_example'] # list[str] | One-letter code ('I', 'C', 'O') explaining if the candidate is an incumbent, a challenger, or if the seat is open. (optional)
party = ['party_example'] # list[str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
has_raised_funds = true # bool | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) (optional)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
candidate_status = ['candidate_status_example'] # list[str] | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  (optional)
office = ['office_example'] # list[str] | Federal office candidate runs for: H, S or P (optional)
election_year = [56] # list[int] | Year of election (optional)

try:
    api_response = api_instance.candidate_candidate_id_get(api_key, candidate_id, federal_funds_flag=federal_funds_flag, cycle=cycle, sort=sort, year=year, state=state, name=name, sort_nulls_last=sort_nulls_last, sort_hide_null=sort_hide_null, per_page=per_page, district=district, page=page, incumbent_challenge=incumbent_challenge, party=party, has_raised_funds=has_raised_funds, sort_null_only=sort_null_only, candidate_status=candidate_status, office=office, election_year=election_year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CandidateApi->candidate_candidate_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **candidate_id** | **str**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | 
 **federal_funds_flag** | **bool**| A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. | [optional] 
 **cycle** | [**list[int]**](int.md)|  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | [optional] 
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to name]
 **year** | **str**| See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. | [optional] 
 **state** | [**list[str]**](str.md)| US state or territory where a candidate runs for office | [optional] 
 **name** | [**list[str]**](str.md)| Name (candidate or committee) to search for. Alias for &#39;q&#39;. | [optional] 
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **district** | [**list[str]**](str.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **incumbent_challenge** | [**list[str]**](str.md)| One-letter code (&#39;I&#39;, &#39;C&#39;, &#39;O&#39;) explaining if the candidate is an incumbent, a challenger, or if the seat is open. | [optional] 
 **party** | [**list[str]**](str.md)| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
 **has_raised_funds** | **bool**| A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) | [optional] 
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **candidate_status** | [**list[str]**](str.md)| One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  | [optional] 
 **office** | [**list[str]**](str.md)| Federal office candidate runs for: H, S or P | [optional] 
 **election_year** | [**list[int]**](int.md)| Year of election | [optional] 

### Return type

[**CandidateDetailPage**](CandidateDetailPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidate_candidate_id_history_cycle_get**
> CandidateHistoryPage candidate_candidate_id_history_cycle_get(api_key, cycle, candidate_id, election_full=election_full, page=page, per_page=per_page, sort_nulls_last=sort_nulls_last, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)



 Find out a candidate's characteristics over time. This is particularly useful if the candidate runs for the same office in different districts or you want to know more about a candidate's previous races.  This information is organized by `candidate_id`, so it won't help you find a candidate who ran for different offices over time; candidates get a new ID for each office. 

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
api_instance = swagger_client.CandidateApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
cycle = 56 # int |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag. 
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. 
election_full = true # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to true)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
sort = '-two_year_period' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -two_year_period)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)

try:
    api_response = api_instance.candidate_candidate_id_history_cycle_get(api_key, cycle, candidate_id, election_full=election_full, page=page, per_page=per_page, sort_nulls_last=sort_nulls_last, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CandidateApi->candidate_candidate_id_history_cycle_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **cycle** | **int**|  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | 
 **candidate_id** | **str**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | 
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -two_year_period]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]

### Return type

[**CandidateHistoryPage**](CandidateHistoryPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidate_candidate_id_history_get**
> CandidateHistoryPage candidate_candidate_id_history_get(api_key, candidate_id, election_full=election_full, page=page, per_page=per_page, sort_nulls_last=sort_nulls_last, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)



 Find out a candidate's characteristics over time. This is particularly useful if the candidate runs for the same office in different districts or you want to know more about a candidate's previous races.  This information is organized by `candidate_id`, so it won't help you find a candidate who ran for different offices over time; candidates get a new ID for each office. 

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
api_instance = swagger_client.CandidateApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. 
election_full = true # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to true)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
sort = '-two_year_period' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -two_year_period)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)

try:
    api_response = api_instance.candidate_candidate_id_history_get(api_key, candidate_id, election_full=election_full, page=page, per_page=per_page, sort_nulls_last=sort_nulls_last, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CandidateApi->candidate_candidate_id_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **candidate_id** | **str**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | 
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -two_year_period]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]

### Return type

[**CandidateHistoryPage**](CandidateHistoryPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidate_candidate_id_totals_get**
> CommitteeTotalsPage candidate_candidate_id_totals_get(api_key, candidate_id, per_page=per_page, cycle=cycle, sort=sort, election_full=election_full, page=page, sort_nulls_last=sort_nulls_last, sort_hide_null=sort_hide_null, full_election=full_election, sort_null_only=sort_null_only)



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
api_instance = swagger_client.CandidateApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. 
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
sort = '-cycle' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -cycle)
election_full = true # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
full_election = true # bool | Parameter `full_election` is replaced by `election_full`. Please use `election_full` instead. (optional)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)

try:
    api_response = api_instance.candidate_candidate_id_totals_get(api_key, candidate_id, per_page=per_page, cycle=cycle, sort=sort, election_full=election_full, page=page, sort_nulls_last=sort_nulls_last, sort_hide_null=sort_hide_null, full_election=full_election, sort_null_only=sort_null_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CandidateApi->candidate_candidate_id_totals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **candidate_id** | **str**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -cycle]
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] 
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **full_election** | **bool**| Parameter &#x60;full_election&#x60; is replaced by &#x60;election_full&#x60;. Please use &#x60;election_full&#x60; instead. | [optional] 
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]

### Return type

[**CommitteeTotalsPage**](CommitteeTotalsPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_get**
> CandidatePage candidates_get(api_key, federal_funds_flag=federal_funds_flag, cycle=cycle, sort=sort, year=year, state=state, max_first_file_date=max_first_file_date, name=name, sort_nulls_last=sort_nulls_last, q=q, sort_hide_null=sort_hide_null, is_active_candidate=is_active_candidate, min_first_file_date=min_first_file_date, per_page=per_page, office=office, candidate_id=candidate_id, district=district, page=page, has_raised_funds=has_raised_funds, incumbent_challenge=incumbent_challenge, party=party, candidate_status=candidate_status, sort_null_only=sort_null_only, election_year=election_year)



 Fetch basic information about candidates, and use parameters to filter results to the candidates you're looking for.  Each result reflects a unique FEC candidate ID. That ID is particular to the candidate for a particular office sought. If a candidate runs for the same office multiple times, the ID stays the same. If the same person runs for another office — for example, a House candidate runs for a Senate office — that candidate will get a unique ID for each office. 

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
api_instance = swagger_client.CandidateApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
federal_funds_flag = true # bool | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. (optional)
cycle = [56] # list[int] |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.  (optional)
sort = 'name' # str | Provide a field to sort by. Use - for descending order. (optional) (default to name)
year = 'year_example' # str | See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. (optional)
state = ['state_example'] # list[str] | US state or territory where a candidate runs for office (optional)
max_first_file_date = '2013-10-20' # date | Selects all candidates whose first filing was received by the FEC before this date. (optional)
name = ['name_example'] # list[str] | Name (candidate or committee) to search for. Alias for 'q'. (optional)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
q = ['q_example'] # list[str] | Name of candidate running for office (optional)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
is_active_candidate = true # bool |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  (optional)
min_first_file_date = '2013-10-20' # date | Selects all candidates whose first filing was received by the FEC after this date. (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
office = ['office_example'] # list[str] | Federal office candidate runs for: H, S or P (optional)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
district = ['district_example'] # list[str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
has_raised_funds = true # bool | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) (optional)
incumbent_challenge = ['incumbent_challenge_example'] # list[str] | One-letter code ('I', 'C', 'O') explaining if the candidate is an incumbent, a challenger, or if the seat is open. (optional)
party = ['party_example'] # list[str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
candidate_status = ['candidate_status_example'] # list[str] | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  (optional)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
election_year = [56] # list[int] | Year of election (optional)

try:
    api_response = api_instance.candidates_get(api_key, federal_funds_flag=federal_funds_flag, cycle=cycle, sort=sort, year=year, state=state, max_first_file_date=max_first_file_date, name=name, sort_nulls_last=sort_nulls_last, q=q, sort_hide_null=sort_hide_null, is_active_candidate=is_active_candidate, min_first_file_date=min_first_file_date, per_page=per_page, office=office, candidate_id=candidate_id, district=district, page=page, has_raised_funds=has_raised_funds, incumbent_challenge=incumbent_challenge, party=party, candidate_status=candidate_status, sort_null_only=sort_null_only, election_year=election_year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CandidateApi->candidates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **federal_funds_flag** | **bool**| A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. | [optional] 
 **cycle** | [**list[int]**](int.md)|  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | [optional] 
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to name]
 **year** | **str**| See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. | [optional] 
 **state** | [**list[str]**](str.md)| US state or territory where a candidate runs for office | [optional] 
 **max_first_file_date** | **date**| Selects all candidates whose first filing was received by the FEC before this date. | [optional] 
 **name** | [**list[str]**](str.md)| Name (candidate or committee) to search for. Alias for &#39;q&#39;. | [optional] 
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **q** | [**list[str]**](str.md)| Name of candidate running for office | [optional] 
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **is_active_candidate** | **bool**|  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  | [optional] 
 **min_first_file_date** | **date**| Selects all candidates whose first filing was received by the FEC after this date. | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **office** | [**list[str]**](str.md)| Federal office candidate runs for: H, S or P | [optional] 
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional] 
 **district** | [**list[str]**](str.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **has_raised_funds** | **bool**| A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) | [optional] 
 **incumbent_challenge** | [**list[str]**](str.md)| One-letter code (&#39;I&#39;, &#39;C&#39;, &#39;O&#39;) explaining if the candidate is an incumbent, a challenger, or if the seat is open. | [optional] 
 **party** | [**list[str]**](str.md)| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
 **candidate_status** | [**list[str]**](str.md)| One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  | [optional] 
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **election_year** | [**list[int]**](int.md)| Year of election | [optional] 

### Return type

[**CandidatePage**](CandidatePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_search_get**
> CandidatePage candidates_search_get(api_key, federal_funds_flag=federal_funds_flag, cycle=cycle, sort=sort, year=year, state=state, max_first_file_date=max_first_file_date, name=name, sort_nulls_last=sort_nulls_last, q=q, sort_hide_null=sort_hide_null, is_active_candidate=is_active_candidate, min_first_file_date=min_first_file_date, per_page=per_page, office=office, candidate_id=candidate_id, district=district, page=page, has_raised_funds=has_raised_funds, incumbent_challenge=incumbent_challenge, party=party, candidate_status=candidate_status, sort_null_only=sort_null_only, election_year=election_year)



 Fetch basic information about candidates and their principal committees.  Each result reflects a unique FEC candidate ID. That ID is assigned to the candidate for a particular office sought. If a candidate runs for the same office over time, that ID stays the same. If the same person runs for multiple offices — for example, a House candidate runs for a Senate office — that candidate will get a unique ID for each office.  The candidate endpoints primarily use data from FEC registration [Form 1](http://www.fec.gov/pdf/forms/fecfrm1.pdf), for candidate information, and [Form 2](http://www.fec.gov/pdf/forms/fecfrm2.pdf), for committees information, with additional information to provide context. 

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
api_instance = swagger_client.CandidateApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
federal_funds_flag = true # bool | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. (optional)
cycle = [56] # list[int] |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.  (optional)
sort = 'name' # str | Provide a field to sort by. Use - for descending order. (optional) (default to name)
year = 'year_example' # str | See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. (optional)
state = ['state_example'] # list[str] | US state or territory where a candidate runs for office (optional)
max_first_file_date = '2013-10-20' # date | Selects all candidates whose first filing was received by the FEC before this date. (optional)
name = ['name_example'] # list[str] | Name (candidate or committee) to search for. Alias for 'q'. (optional)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
q = ['q_example'] # list[str] | Name of candidate running for office (optional)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
is_active_candidate = true # bool |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  (optional)
min_first_file_date = '2013-10-20' # date | Selects all candidates whose first filing was received by the FEC after this date. (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
office = ['office_example'] # list[str] | Federal office candidate runs for: H, S or P (optional)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
district = ['district_example'] # list[str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
has_raised_funds = true # bool | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) (optional)
incumbent_challenge = ['incumbent_challenge_example'] # list[str] | One-letter code ('I', 'C', 'O') explaining if the candidate is an incumbent, a challenger, or if the seat is open. (optional)
party = ['party_example'] # list[str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
candidate_status = ['candidate_status_example'] # list[str] | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  (optional)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
election_year = [56] # list[int] | Year of election (optional)

try:
    api_response = api_instance.candidates_search_get(api_key, federal_funds_flag=federal_funds_flag, cycle=cycle, sort=sort, year=year, state=state, max_first_file_date=max_first_file_date, name=name, sort_nulls_last=sort_nulls_last, q=q, sort_hide_null=sort_hide_null, is_active_candidate=is_active_candidate, min_first_file_date=min_first_file_date, per_page=per_page, office=office, candidate_id=candidate_id, district=district, page=page, has_raised_funds=has_raised_funds, incumbent_challenge=incumbent_challenge, party=party, candidate_status=candidate_status, sort_null_only=sort_null_only, election_year=election_year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CandidateApi->candidates_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **federal_funds_flag** | **bool**| A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. | [optional] 
 **cycle** | [**list[int]**](int.md)|  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | [optional] 
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to name]
 **year** | **str**| See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. | [optional] 
 **state** | [**list[str]**](str.md)| US state or territory where a candidate runs for office | [optional] 
 **max_first_file_date** | **date**| Selects all candidates whose first filing was received by the FEC before this date. | [optional] 
 **name** | [**list[str]**](str.md)| Name (candidate or committee) to search for. Alias for &#39;q&#39;. | [optional] 
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **q** | [**list[str]**](str.md)| Name of candidate running for office | [optional] 
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **is_active_candidate** | **bool**|  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  | [optional] 
 **min_first_file_date** | **date**| Selects all candidates whose first filing was received by the FEC after this date. | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **office** | [**list[str]**](str.md)| Federal office candidate runs for: H, S or P | [optional] 
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional] 
 **district** | [**list[str]**](str.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **has_raised_funds** | **bool**| A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) | [optional] 
 **incumbent_challenge** | [**list[str]**](str.md)| One-letter code (&#39;I&#39;, &#39;C&#39;, &#39;O&#39;) explaining if the candidate is an incumbent, a challenger, or if the seat is open. | [optional] 
 **party** | [**list[str]**](str.md)| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
 **candidate_status** | [**list[str]**](str.md)| One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  | [optional] 
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **election_year** | [**list[int]**](int.md)| Year of election | [optional] 

### Return type

[**CandidatePage**](CandidatePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_totals_by_office_by_party_get**
> TotalByOfficeByPartyPage candidates_totals_by_office_by_party_get(api_key, per_page=per_page, office=office, sort=sort, page=page, sort_nulls_last=sort_nulls_last, sort_hide_null=sort_hide_null, is_active_candidate=is_active_candidate, sort_null_only=sort_null_only, election_year=election_year)



 Aggregated candidate receipts and disbursements grouped by office by party by cycle. 

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
api_instance = swagger_client.CandidateApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
office = 'office_example' # str | Federal office candidate runs for: H, S or P (optional)
sort = 'sort_example' # str | Provide a field to sort by. Use - for descending order. (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
is_active_candidate = true # bool |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  (optional)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
election_year = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)

try:
    api_response = api_instance.candidates_totals_by_office_by_party_get(api_key, per_page=per_page, office=office, sort=sort, page=page, sort_nulls_last=sort_nulls_last, sort_hide_null=sort_hide_null, is_active_candidate=is_active_candidate, sort_null_only=sort_null_only, election_year=election_year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CandidateApi->candidates_totals_by_office_by_party_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **office** | **str**| Federal office candidate runs for: H, S or P | [optional] 
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] 
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **is_active_candidate** | **bool**|  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  | [optional] 
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **election_year** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 

### Return type

[**TotalByOfficeByPartyPage**](TotalByOfficeByPartyPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_totals_by_office_get**
> TotalByOfficePage candidates_totals_by_office_get(api_key, per_page=per_page, office=office, sort=sort, page=page, sort_nulls_last=sort_nulls_last, sort_hide_null=sort_hide_null, is_active_candidate=is_active_candidate, sort_null_only=sort_null_only, election_year=election_year)



 Aggregated candidate receipts and disbursements grouped by office by cycle. 

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
api_instance = swagger_client.CandidateApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
office = 'office_example' # str | Federal office candidate runs for: H, S or P (optional)
sort = 'sort_example' # str | Provide a field to sort by. Use - for descending order. (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
is_active_candidate = true # bool |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  (optional)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
election_year = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)

try:
    api_response = api_instance.candidates_totals_by_office_get(api_key, per_page=per_page, office=office, sort=sort, page=page, sort_nulls_last=sort_nulls_last, sort_hide_null=sort_hide_null, is_active_candidate=is_active_candidate, sort_null_only=sort_null_only, election_year=election_year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CandidateApi->candidates_totals_by_office_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **office** | **str**| Federal office candidate runs for: H, S or P | [optional] 
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] 
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **is_active_candidate** | **bool**|  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  | [optional] 
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **election_year** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 

### Return type

[**TotalByOfficePage**](TotalByOfficePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_totals_get**
> CandidateHistoryTotalPage candidates_totals_get(api_key, federal_funds_flag=federal_funds_flag, min_receipts=min_receipts, cycle=cycle, sort=sort, max_debts_owed_by_committee=max_debts_owed_by_committee, state=state, sort_nulls_last=sort_nulls_last, q=q, sort_hide_null=sort_hide_null, is_active_candidate=is_active_candidate, per_page=per_page, office=office, max_disbursements=max_disbursements, candidate_id=candidate_id, max_receipts=max_receipts, district=district, election_full=election_full, page=page, min_debts_owed_by_committee=min_debts_owed_by_committee, max_cash_on_hand_end_period=max_cash_on_hand_end_period, has_raised_funds=has_raised_funds, min_cash_on_hand_end_period=min_cash_on_hand_end_period, party=party, sort_null_only=sort_null_only, min_disbursements=min_disbursements, election_year=election_year)



 Aggregated candidate receipts and disbursements grouped by cycle. 

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
api_instance = swagger_client.CandidateApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
federal_funds_flag = true # bool | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. (optional)
min_receipts = 'min_receipts_example' # str | Minimum aggregated receipts (optional)
cycle = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
sort = 'sort_example' # str | Provide a field to sort by. Use - for descending order. (optional)
max_debts_owed_by_committee = 'max_debts_owed_by_committee_example' # str | Maximum debt (optional)
state = ['state_example'] # list[str] | State of candidate (optional)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
q = ['q_example'] # list[str] | Name of candidate running for office (optional)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
is_active_candidate = true # bool |  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
office = ['office_example'] # list[str] | Federal office candidate runs for: H, S or P (optional)
max_disbursements = 'max_disbursements_example' # str | Maximum aggregated disbursements (optional)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
max_receipts = 'max_receipts_example' # str | Maximum aggregated receipts (optional)
district = ['district_example'] # list[str] | District of candidate (optional)
election_full = true # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to true)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
min_debts_owed_by_committee = 'min_debts_owed_by_committee_example' # str | Minimum debt (optional)
max_cash_on_hand_end_period = 'max_cash_on_hand_end_period_example' # str | Maximum cash on hand (optional)
has_raised_funds = true # bool | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) (optional)
min_cash_on_hand_end_period = 'min_cash_on_hand_end_period_example' # str | Minimum cash on hand (optional)
party = ['party_example'] # list[str] | Three-letter party code (optional)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
min_disbursements = 'min_disbursements_example' # str | Minimum aggregated disbursements (optional)
election_year = [56] # list[int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)

try:
    api_response = api_instance.candidates_totals_get(api_key, federal_funds_flag=federal_funds_flag, min_receipts=min_receipts, cycle=cycle, sort=sort, max_debts_owed_by_committee=max_debts_owed_by_committee, state=state, sort_nulls_last=sort_nulls_last, q=q, sort_hide_null=sort_hide_null, is_active_candidate=is_active_candidate, per_page=per_page, office=office, max_disbursements=max_disbursements, candidate_id=candidate_id, max_receipts=max_receipts, district=district, election_full=election_full, page=page, min_debts_owed_by_committee=min_debts_owed_by_committee, max_cash_on_hand_end_period=max_cash_on_hand_end_period, has_raised_funds=has_raised_funds, min_cash_on_hand_end_period=min_cash_on_hand_end_period, party=party, sort_null_only=sort_null_only, min_disbursements=min_disbursements, election_year=election_year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CandidateApi->candidates_totals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **federal_funds_flag** | **bool**| A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. | [optional] 
 **min_receipts** | **str**| Minimum aggregated receipts | [optional] 
 **cycle** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] 
 **max_debts_owed_by_committee** | **str**| Maximum debt | [optional] 
 **state** | [**list[str]**](str.md)| State of candidate | [optional] 
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **q** | [**list[str]**](str.md)| Name of candidate running for office | [optional] 
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **is_active_candidate** | **bool**|  Candidates who are actively seeking office. If no value is specified, all candidates are returned. When True is specified, only active candidates are returned. When False is specified, only inactive candidates are returned.  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **office** | [**list[str]**](str.md)| Federal office candidate runs for: H, S or P | [optional] 
 **max_disbursements** | **str**| Maximum aggregated disbursements | [optional] 
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional] 
 **max_receipts** | **str**| Maximum aggregated receipts | [optional] 
 **district** | [**list[str]**](str.md)| District of candidate | [optional] 
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **min_debts_owed_by_committee** | **str**| Minimum debt | [optional] 
 **max_cash_on_hand_end_period** | **str**| Maximum cash on hand | [optional] 
 **has_raised_funds** | **bool**| A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) | [optional] 
 **min_cash_on_hand_end_period** | **str**| Minimum cash on hand | [optional] 
 **party** | [**list[str]**](str.md)| Three-letter party code | [optional] 
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **min_disbursements** | **str**| Minimum aggregated disbursements | [optional] 
 **election_year** | [**list[int]**](int.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 

### Return type

[**CandidateHistoryTotalPage**](CandidateHistoryTotalPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **committee_committee_id_candidates_get**
> CandidateDetailPage committee_committee_id_candidates_get(api_key, committee_id, federal_funds_flag=federal_funds_flag, cycle=cycle, sort=sort, year=year, state=state, name=name, sort_nulls_last=sort_nulls_last, sort_hide_null=sort_hide_null, per_page=per_page, district=district, page=page, incumbent_challenge=incumbent_challenge, party=party, has_raised_funds=has_raised_funds, sort_null_only=sort_null_only, candidate_status=candidate_status, office=office, election_year=election_year)



 This endpoint is useful for finding detailed information about a particular candidate. Use the `candidate_id` to find the most recent information about that candidate.  

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
api_instance = swagger_client.CandidateApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
federal_funds_flag = true # bool | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. (optional)
cycle = [56] # list[int] |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag.  (optional)
sort = 'name' # str | Provide a field to sort by. Use - for descending order. (optional) (default to name)
year = 'year_example' # str | See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. (optional)
state = ['state_example'] # list[str] | US state or territory where a candidate runs for office (optional)
name = ['name_example'] # list[str] | Name (candidate or committee) to search for. Alias for 'q'. (optional)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
district = ['district_example'] # list[str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
incumbent_challenge = ['incumbent_challenge_example'] # list[str] | One-letter code ('I', 'C', 'O') explaining if the candidate is an incumbent, a challenger, or if the seat is open. (optional)
party = ['party_example'] # list[str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
has_raised_funds = true # bool | A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) (optional)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
candidate_status = ['candidate_status_example'] # list[str] | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  (optional)
office = ['office_example'] # list[str] | Federal office candidate runs for: H, S or P (optional)
election_year = [56] # list[int] | Year of election (optional)

try:
    api_response = api_instance.committee_committee_id_candidates_get(api_key, committee_id, federal_funds_flag=federal_funds_flag, cycle=cycle, sort=sort, year=year, state=state, name=name, sort_nulls_last=sort_nulls_last, sort_hide_null=sort_hide_null, per_page=per_page, district=district, page=page, incumbent_challenge=incumbent_challenge, party=party, has_raised_funds=has_raised_funds, sort_null_only=sort_null_only, candidate_status=candidate_status, office=office, election_year=election_year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CandidateApi->committee_committee_id_candidates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **committee_id** | **str**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | 
 **federal_funds_flag** | **bool**| A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. | [optional] 
 **cycle** | [**list[int]**](int.md)|  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | [optional] 
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to name]
 **year** | **str**| See records pertaining to a particular election year. The list of election years is based on a candidate filing a statement of candidacy (F2) for that year. | [optional] 
 **state** | [**list[str]**](str.md)| US state or territory where a candidate runs for office | [optional] 
 **name** | [**list[str]**](str.md)| Name (candidate or committee) to search for. Alias for &#39;q&#39;. | [optional] 
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **district** | [**list[str]**](str.md)| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **incumbent_challenge** | [**list[str]**](str.md)| One-letter code (&#39;I&#39;, &#39;C&#39;, &#39;O&#39;) explaining if the candidate is an incumbent, a challenger, or if the seat is open. | [optional] 
 **party** | [**list[str]**](str.md)| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
 **has_raised_funds** | **bool**| A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) | [optional] 
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **candidate_status** | [**list[str]**](str.md)| One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  | [optional] 
 **office** | [**list[str]**](str.md)| Federal office candidate runs for: H, S or P | [optional] 
 **election_year** | [**list[int]**](int.md)| Year of election | [optional] 

### Return type

[**CandidateDetailPage**](CandidateDetailPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **committee_committee_id_candidates_history_cycle_get**
> CandidateHistoryPage committee_committee_id_candidates_history_cycle_get(api_key, committee_id, cycle, election_full=election_full, page=page, per_page=per_page, sort_nulls_last=sort_nulls_last, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)



 Find out a candidate's characteristics over time. This is particularly useful if the candidate runs for the same office in different districts or you want to know more about a candidate's previous races.  This information is organized by `candidate_id`, so it won't help you find a candidate who ran for different offices over time; candidates get a new ID for each office. 

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
api_instance = swagger_client.CandidateApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
cycle = 56 # int |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the `election_full` flag. 
election_full = true # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to true)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
sort = '-two_year_period' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -two_year_period)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)

try:
    api_response = api_instance.committee_committee_id_candidates_history_cycle_get(api_key, committee_id, cycle, election_full=election_full, page=page, per_page=per_page, sort_nulls_last=sort_nulls_last, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CandidateApi->committee_committee_id_candidates_history_cycle_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **committee_id** | **str**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | 
 **cycle** | **int**|  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | 
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -two_year_period]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]

### Return type

[**CandidateHistoryPage**](CandidateHistoryPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **committee_committee_id_candidates_history_get**
> CandidateHistoryPage committee_committee_id_candidates_history_get(api_key, committee_id, election_full=election_full, page=page, per_page=per_page, sort_nulls_last=sort_nulls_last, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)



 Find out a candidate's characteristics over time. This is particularly useful if the candidate runs for the same office in different districts or you want to know more about a candidate's previous races.  This information is organized by `candidate_id`, so it won't help you find a candidate who ran for different offices over time; candidates get a new ID for each office. 

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
api_instance = swagger_client.CandidateApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
election_full = true # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to true)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
sort = '-two_year_period' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -two_year_period)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)

try:
    api_response = api_instance.committee_committee_id_candidates_history_get(api_key, committee_id, election_full=election_full, page=page, per_page=per_page, sort_nulls_last=sort_nulls_last, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CandidateApi->committee_committee_id_candidates_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **committee_id** | **str**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | 
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -two_year_period]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]

### Return type

[**CandidateHistoryPage**](CandidateHistoryPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

