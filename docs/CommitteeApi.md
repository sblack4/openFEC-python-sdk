# swagger_client.CommitteeApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**candidate_candidate_id_committees_get**](CommitteeApi.md#candidate_candidate_id_committees_get) | **GET** /candidate/{candidate_id}/committees/ | 
[**candidate_candidate_id_committees_history_cycle_get**](CommitteeApi.md#candidate_candidate_id_committees_history_cycle_get) | **GET** /candidate/{candidate_id}/committees/history/{cycle}/ | 
[**candidate_candidate_id_committees_history_get**](CommitteeApi.md#candidate_candidate_id_committees_history_get) | **GET** /candidate/{candidate_id}/committees/history/ | 
[**committee_committee_id_get**](CommitteeApi.md#committee_committee_id_get) | **GET** /committee/{committee_id}/ | 
[**committee_committee_id_history_cycle_get**](CommitteeApi.md#committee_committee_id_history_cycle_get) | **GET** /committee/{committee_id}/history/{cycle}/ | 
[**committee_committee_id_history_get**](CommitteeApi.md#committee_committee_id_history_get) | **GET** /committee/{committee_id}/history/ | 
[**committees_get**](CommitteeApi.md#committees_get) | **GET** /committees/ | 


# **candidate_candidate_id_committees_get**
> CommitteeDetailPage candidate_candidate_id_committees_get(api_key, candidate_id, per_page=per_page, designation=designation, cycle=cycle, year=year, filing_frequency=filing_frequency, organization_type=organization_type, sort=sort, committee_type=committee_type, page=page, sort_nulls_last=sort_nulls_last, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)



 This endpoint is useful for finding detailed information about a particular committee or filer. Use the `committee_id` to find the most recent information about the committee. 

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
api_instance = swagger_client.CommitteeApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. 
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
designation = ['designation_example'] # list[str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
cycle = [56] # list[int] |  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.  (optional)
year = [56] # list[int] | A year that the committee was active— (after original registration date     or filing but before expiration date) (optional)
filing_frequency = ['filing_frequency_example'] # list[str] | The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived  (optional)
organization_type = ['organization_type_example'] # list[str] | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  (optional)
sort = 'name' # str | Provide a field to sort by. Use - for descending order. (optional) (default to name)
committee_type = ['committee_type_example'] # list[str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)

try:
    api_response = api_instance.candidate_candidate_id_committees_get(api_key, candidate_id, per_page=per_page, designation=designation, cycle=cycle, year=year, filing_frequency=filing_frequency, organization_type=organization_type, sort=sort, committee_type=committee_type, page=page, sort_nulls_last=sort_nulls_last, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommitteeApi->candidate_candidate_id_committees_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **candidate_id** | **str**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **designation** | [**list[str]**](str.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
 **cycle** | [**list[int]**](int.md)|  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **year** | [**list[int]**](int.md)| A year that the committee was active— (after original registration date     or filing but before expiration date) | [optional] 
 **filing_frequency** | [**list[str]**](str.md)| The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived  | [optional] 
 **organization_type** | [**list[str]**](str.md)| The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] 
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to name]
 **committee_type** | [**list[str]**](str.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]

### Return type

[**CommitteeDetailPage**](CommitteeDetailPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidate_candidate_id_committees_history_cycle_get**
> CommitteeHistoryPage candidate_candidate_id_committees_history_cycle_get(api_key, cycle, candidate_id, designation=designation, per_page=per_page, sort=sort, election_full=election_full, page=page, sort_nulls_last=sort_nulls_last, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)



 Explore a filer's characteristics over time. This can be particularly useful if the committees change treasurers, designation, or `committee_type`. 

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
api_instance = swagger_client.CommitteeApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
cycle = 56 # int |  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year. 
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. 
designation = ['designation_example'] # list[str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort = '-cycle' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -cycle)
election_full = true # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to true)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)

try:
    api_response = api_instance.candidate_candidate_id_committees_history_cycle_get(api_key, cycle, candidate_id, designation=designation, per_page=per_page, sort=sort, election_full=election_full, page=page, sort_nulls_last=sort_nulls_last, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommitteeApi->candidate_candidate_id_committees_history_cycle_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **cycle** | **int**|  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.  | 
 **candidate_id** | **str**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | 
 **designation** | [**list[str]**](str.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -cycle]
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]

### Return type

[**CommitteeHistoryPage**](CommitteeHistoryPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidate_candidate_id_committees_history_get**
> CommitteeHistoryPage candidate_candidate_id_committees_history_get(api_key, candidate_id, designation=designation, per_page=per_page, sort=sort, election_full=election_full, page=page, sort_nulls_last=sort_nulls_last, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)



 Explore a filer's characteristics over time. This can be particularly useful if the committees change treasurers, designation, or `committee_type`. 

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
api_instance = swagger_client.CommitteeApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. 
designation = ['designation_example'] # list[str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort = '-cycle' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -cycle)
election_full = true # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to true)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)

try:
    api_response = api_instance.candidate_candidate_id_committees_history_get(api_key, candidate_id, designation=designation, per_page=per_page, sort=sort, election_full=election_full, page=page, sort_nulls_last=sort_nulls_last, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommitteeApi->candidate_candidate_id_committees_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **candidate_id** | **str**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | 
 **designation** | [**list[str]**](str.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -cycle]
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]

### Return type

[**CommitteeHistoryPage**](CommitteeHistoryPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **committee_committee_id_get**
> CommitteeDetailPage committee_committee_id_get(api_key, committee_id, per_page=per_page, designation=designation, cycle=cycle, year=year, filing_frequency=filing_frequency, organization_type=organization_type, sort=sort, committee_type=committee_type, page=page, sort_nulls_last=sort_nulls_last, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)



 This endpoint is useful for finding detailed information about a particular committee or filer. Use the `committee_id` to find the most recent information about the committee. 

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
api_instance = swagger_client.CommitteeApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
designation = ['designation_example'] # list[str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
cycle = [56] # list[int] |  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.  (optional)
year = [56] # list[int] | A year that the committee was active— (after original registration date     or filing but before expiration date) (optional)
filing_frequency = ['filing_frequency_example'] # list[str] | The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived  (optional)
organization_type = ['organization_type_example'] # list[str] | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  (optional)
sort = 'name' # str | Provide a field to sort by. Use - for descending order. (optional) (default to name)
committee_type = ['committee_type_example'] # list[str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)

try:
    api_response = api_instance.committee_committee_id_get(api_key, committee_id, per_page=per_page, designation=designation, cycle=cycle, year=year, filing_frequency=filing_frequency, organization_type=organization_type, sort=sort, committee_type=committee_type, page=page, sort_nulls_last=sort_nulls_last, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommitteeApi->committee_committee_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **committee_id** | **str**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **designation** | [**list[str]**](str.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
 **cycle** | [**list[int]**](int.md)|  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **year** | [**list[int]**](int.md)| A year that the committee was active— (after original registration date     or filing but before expiration date) | [optional] 
 **filing_frequency** | [**list[str]**](str.md)| The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived  | [optional] 
 **organization_type** | [**list[str]**](str.md)| The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] 
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to name]
 **committee_type** | [**list[str]**](str.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]

### Return type

[**CommitteeDetailPage**](CommitteeDetailPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **committee_committee_id_history_cycle_get**
> CommitteeHistoryPage committee_committee_id_history_cycle_get(api_key, committee_id, cycle, designation=designation, per_page=per_page, sort=sort, election_full=election_full, page=page, sort_nulls_last=sort_nulls_last, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)



 Explore a filer's characteristics over time. This can be particularly useful if the committees change treasurers, designation, or `committee_type`. 

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
api_instance = swagger_client.CommitteeApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
cycle = 56 # int |  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year. 
designation = ['designation_example'] # list[str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort = '-cycle' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -cycle)
election_full = true # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to true)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)

try:
    api_response = api_instance.committee_committee_id_history_cycle_get(api_key, committee_id, cycle, designation=designation, per_page=per_page, sort=sort, election_full=election_full, page=page, sort_nulls_last=sort_nulls_last, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommitteeApi->committee_committee_id_history_cycle_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **committee_id** | **str**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | 
 **cycle** | **int**|  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.  | 
 **designation** | [**list[str]**](str.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -cycle]
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]

### Return type

[**CommitteeHistoryPage**](CommitteeHistoryPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **committee_committee_id_history_get**
> CommitteeHistoryPage committee_committee_id_history_get(api_key, committee_id, designation=designation, per_page=per_page, sort=sort, election_full=election_full, page=page, sort_nulls_last=sort_nulls_last, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)



 Explore a filer's characteristics over time. This can be particularly useful if the committees change treasurers, designation, or `committee_type`. 

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
api_instance = swagger_client.CommitteeApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
designation = ['designation_example'] # list[str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort = '-cycle' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -cycle)
election_full = true # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) (default to true)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)

try:
    api_response = api_instance.committee_committee_id_history_get(api_key, committee_id, designation=designation, per_page=per_page, sort=sort, election_full=election_full, page=page, sort_nulls_last=sort_nulls_last, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommitteeApi->committee_committee_id_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **committee_id** | **str**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | 
 **designation** | [**list[str]**](str.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -cycle]
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] [default to true]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]

### Return type

[**CommitteeHistoryPage**](CommitteeHistoryPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **committees_get**
> CommitteePage committees_get(api_key, cycle=cycle, organization_type=organization_type, sort=sort, designation=designation, year=year, min_last_f1_date=min_last_f1_date, state=state, max_first_file_date=max_first_file_date, committee_type=committee_type, sort_nulls_last=sort_nulls_last, q=q, sort_hide_null=sort_hide_null, max_last_f1_date=max_last_f1_date, min_first_file_date=min_first_file_date, committee_id=committee_id, per_page=per_page, filing_frequency=filing_frequency, treasurer_name=treasurer_name, candidate_id=candidate_id, page=page, party=party, sort_null_only=sort_null_only)



 Fetch basic information about committees and filers. Use parameters to filter for particular characteristics.  

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
api_instance = swagger_client.CommitteeApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
cycle = [56] # list[int] |  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.  (optional)
organization_type = ['organization_type_example'] # list[str] | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  (optional)
sort = 'name' # str | Provide a field to sort by. Use - for descending order. (optional) (default to name)
designation = ['designation_example'] # list[str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
year = [56] # list[int] | A year that the committee was active— (after original registration date     or filing but before expiration date) (optional)
min_last_f1_date = '2013-10-20' # date | Filter for committees whose latest Form 1 was received on or after this date. (optional)
state = ['state_example'] # list[str] | US state or territory (optional)
max_first_file_date = '2013-10-20' # date | Filter for committees whose first filing was received on or before this date. (optional)
committee_type = ['committee_type_example'] # list[str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
q = ['q_example'] # list[str] | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. (optional)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
max_last_f1_date = '2013-10-20' # date | Filter for committees whose latest Form 1 was received on or before this date. (optional)
min_first_file_date = '2013-10-20' # date | Filter for committees whose first filing was received on or after this date. (optional)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
filing_frequency = ['filing_frequency_example'] # list[str] | The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived  (optional)
treasurer_name = ['treasurer_name_example'] # list[str] | Name of the Committee's treasurer. If multiple treasurers for the committee, the most recent treasurer will be shown. (optional)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
party = ['party_example'] # list[str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)

try:
    api_response = api_instance.committees_get(api_key, cycle=cycle, organization_type=organization_type, sort=sort, designation=designation, year=year, min_last_f1_date=min_last_f1_date, state=state, max_first_file_date=max_first_file_date, committee_type=committee_type, sort_nulls_last=sort_nulls_last, q=q, sort_hide_null=sort_hide_null, max_last_f1_date=max_last_f1_date, min_first_file_date=min_first_file_date, committee_id=committee_id, per_page=per_page, filing_frequency=filing_frequency, treasurer_name=treasurer_name, candidate_id=candidate_id, page=page, party=party, sort_null_only=sort_null_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommitteeApi->committees_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **cycle** | [**list[int]**](int.md)|  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **organization_type** | [**list[str]**](str.md)| The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] 
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to name]
 **designation** | [**list[str]**](str.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
 **year** | [**list[int]**](int.md)| A year that the committee was active— (after original registration date     or filing but before expiration date) | [optional] 
 **min_last_f1_date** | **date**| Filter for committees whose latest Form 1 was received on or after this date. | [optional] 
 **state** | [**list[str]**](str.md)| US state or territory | [optional] 
 **max_first_file_date** | **date**| Filter for committees whose first filing was received on or before this date. | [optional] 
 **committee_type** | [**list[str]**](str.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **q** | [**list[str]**](str.md)| The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. | [optional] 
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **max_last_f1_date** | **date**| Filter for committees whose latest Form 1 was received on or before this date. | [optional] 
 **min_first_file_date** | **date**| Filter for committees whose first filing was received on or after this date. | [optional] 
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **filing_frequency** | [**list[str]**](str.md)| The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived  | [optional] 
 **treasurer_name** | [**list[str]**](str.md)| Name of the Committee&#39;s treasurer. If multiple treasurers for the committee, the most recent treasurer will be shown. | [optional] 
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional] 
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **party** | [**list[str]**](str.md)| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]

### Return type

[**CommitteePage**](CommitteePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

