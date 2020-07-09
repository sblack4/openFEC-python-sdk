# openfec_sdk.CommitteeApi

All URIs are relative to *http://localhost/v1*

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
> committee_detail_page.CommitteeDetailPage candidate_candidate_id_committees_get(candidate_id)



 This endpoint is useful for finding detailed information about a particular committee or filer. Use the `committee_id` to find the most recent information about the committee.

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
    api_instance = openfec_sdk.CommitteeApi(api_client)
    candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
designation = ['designation_example'] # [str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
organization_type = ['organization_type_example'] # [str] | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
filing_frequency = ['filing_frequency_example'] # [str] | The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
sort = 'name' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of 'name'
page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
year = [56] # [int] | A year that the committee was active— (after original registration date     or filing but before expiration date) (optional)
committee_type = ['committee_type_example'] # [str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
cycle = [56] # [int] |  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.candidate_candidate_id_committees_get(candidate_id)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CommitteeApi->candidate_candidate_id_committees_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.candidate_candidate_id_committees_get(candidate_id, sort_hide_null=sort_hide_null, designation=designation, organization_type=organization_type, sort_null_only=sort_null_only, filing_frequency=filing_frequency, per_page=per_page, sort=sort, page=page, year=year, committee_type=committee_type, sort_nulls_last=sort_nulls_last, cycle=cycle)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CommitteeApi->candidate_candidate_id_committees_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **candidate_id** | **str**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  |
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **designation** | **[str]**| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional]
 **organization_type** | **[str]**| The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **filing_frequency** | **[str]**| The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived  | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of 'name'
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **year** | **[int]**| A year that the committee was active— (after original registration date     or filing but before expiration date) | [optional]
 **committee_type** | **[str]**| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **cycle** | **[int]**|  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.  | [optional]

### Return type

[**committee_detail_page.CommitteeDetailPage**](CommitteeDetailPage.md)

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

# **candidate_candidate_id_committees_history_cycle_get**
> committee_history_page.CommitteeHistoryPage candidate_candidate_id_committees_history_cycle_get(cycle, candidate_id)



 Explore a filer's characteristics over time. This can be particularly useful if the committees change treasurers, designation, or `committee_type`.

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
    api_instance = openfec_sdk.CommitteeApi(api_client)
    cycle = 56 # int |  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.
    candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
designation = ['designation_example'] # [str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
sort = '-cycle' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of '-cycle'
page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.candidate_candidate_id_committees_history_cycle_get(cycle, candidate_id)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CommitteeApi->candidate_candidate_id_committees_history_cycle_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.candidate_candidate_id_committees_history_cycle_get(cycle, candidate_id, sort_hide_null=sort_hide_null, designation=designation, sort_null_only=sort_null_only, per_page=per_page, sort=sort, page=page, sort_nulls_last=sort_nulls_last, election_full=election_full)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CommitteeApi->candidate_candidate_id_committees_history_cycle_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cycle** | **int**|  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.  |
 **candidate_id** | **str**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  |
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **designation** | **[str]**| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of '-cycle'
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] if omitted the server will use the default value of True

### Return type

[**committee_history_page.CommitteeHistoryPage**](CommitteeHistoryPage.md)

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

# **candidate_candidate_id_committees_history_get**
> committee_history_page.CommitteeHistoryPage candidate_candidate_id_committees_history_get(candidate_id)



 Explore a filer's characteristics over time. This can be particularly useful if the committees change treasurers, designation, or `committee_type`.

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
    api_instance = openfec_sdk.CommitteeApi(api_client)
    candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
designation = ['designation_example'] # [str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
sort = '-cycle' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of '-cycle'
page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.candidate_candidate_id_committees_history_get(candidate_id)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CommitteeApi->candidate_candidate_id_committees_history_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.candidate_candidate_id_committees_history_get(candidate_id, sort_hide_null=sort_hide_null, designation=designation, sort_null_only=sort_null_only, per_page=per_page, sort=sort, page=page, sort_nulls_last=sort_nulls_last, election_full=election_full)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CommitteeApi->candidate_candidate_id_committees_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **candidate_id** | **str**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  |
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **designation** | **[str]**| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of '-cycle'
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] if omitted the server will use the default value of True

### Return type

[**committee_history_page.CommitteeHistoryPage**](CommitteeHistoryPage.md)

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

# **committee_committee_id_get**
> committee_detail_page.CommitteeDetailPage committee_committee_id_get(committee_id)



 This endpoint is useful for finding detailed information about a particular committee or filer. Use the `committee_id` to find the most recent information about the committee.

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
    api_instance = openfec_sdk.CommitteeApi(api_client)
    committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
designation = ['designation_example'] # [str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
organization_type = ['organization_type_example'] # [str] | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
filing_frequency = ['filing_frequency_example'] # [str] | The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
sort = 'name' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of 'name'
page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
year = [56] # [int] | A year that the committee was active— (after original registration date     or filing but before expiration date) (optional)
committee_type = ['committee_type_example'] # [str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
cycle = [56] # [int] |  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.committee_committee_id_get(committee_id)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CommitteeApi->committee_committee_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.committee_committee_id_get(committee_id, sort_hide_null=sort_hide_null, designation=designation, organization_type=organization_type, sort_null_only=sort_null_only, filing_frequency=filing_frequency, per_page=per_page, sort=sort, page=page, year=year, committee_type=committee_type, sort_nulls_last=sort_nulls_last, cycle=cycle)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CommitteeApi->committee_committee_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **committee_id** | **str**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  |
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **designation** | **[str]**| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional]
 **organization_type** | **[str]**| The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **filing_frequency** | **[str]**| The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived  | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of 'name'
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **year** | **[int]**| A year that the committee was active— (after original registration date     or filing but before expiration date) | [optional]
 **committee_type** | **[str]**| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **cycle** | **[int]**|  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.  | [optional]

### Return type

[**committee_detail_page.CommitteeDetailPage**](CommitteeDetailPage.md)

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

# **committee_committee_id_history_cycle_get**
> committee_history_page.CommitteeHistoryPage committee_committee_id_history_cycle_get(cycle, committee_id)



 Explore a filer's characteristics over time. This can be particularly useful if the committees change treasurers, designation, or `committee_type`.

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
    api_instance = openfec_sdk.CommitteeApi(api_client)
    cycle = 56 # int |  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.
    committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
designation = ['designation_example'] # [str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
sort = '-cycle' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of '-cycle'
page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.committee_committee_id_history_cycle_get(cycle, committee_id)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CommitteeApi->committee_committee_id_history_cycle_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.committee_committee_id_history_cycle_get(cycle, committee_id, sort_hide_null=sort_hide_null, designation=designation, sort_null_only=sort_null_only, per_page=per_page, sort=sort, page=page, sort_nulls_last=sort_nulls_last, election_full=election_full)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CommitteeApi->committee_committee_id_history_cycle_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cycle** | **int**|  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.  |
 **committee_id** | **str**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  |
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **designation** | **[str]**| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of '-cycle'
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] if omitted the server will use the default value of True

### Return type

[**committee_history_page.CommitteeHistoryPage**](CommitteeHistoryPage.md)

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

# **committee_committee_id_history_get**
> committee_history_page.CommitteeHistoryPage committee_committee_id_history_get(committee_id)



 Explore a filer's characteristics over time. This can be particularly useful if the committees change treasurers, designation, or `committee_type`.

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
    api_instance = openfec_sdk.CommitteeApi(api_client)
    committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
designation = ['designation_example'] # [str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
sort = '-cycle' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of '-cycle'
page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
election_full = True # bool | `True` indicates that full election period of a candidate. `False` indicates that two year election cycle. (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.committee_committee_id_history_get(committee_id)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CommitteeApi->committee_committee_id_history_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.committee_committee_id_history_get(committee_id, sort_hide_null=sort_hide_null, designation=designation, sort_null_only=sort_null_only, per_page=per_page, sort=sort, page=page, sort_nulls_last=sort_nulls_last, election_full=election_full)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CommitteeApi->committee_committee_id_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **committee_id** | **str**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  |
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **designation** | **[str]**| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of '-cycle'
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **election_full** | **bool**| &#x60;True&#x60; indicates that full election period of a candidate. &#x60;False&#x60; indicates that two year election cycle. | [optional] if omitted the server will use the default value of True

### Return type

[**committee_history_page.CommitteeHistoryPage**](CommitteeHistoryPage.md)

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

# **committees_get**
> committee_page.CommitteePage committees_get()



 Fetch basic information about committees and filers. Use parameters to filter for particular characteristics.

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
    api_instance = openfec_sdk.CommitteeApi(api_client)
    sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
organization_type = ['organization_type_example'] # [str] | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  (optional)
committee_id = ['committee_id_example'] # [str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
candidate_id = ['candidate_id_example'] # [str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
min_first_file_date = '2013-10-20' # date | Filter for committees whose first filing was received on or after this date. (optional)
max_last_f1_date = '2013-10-20' # date | Filter for committees whose latest Form 1 was received on or before this date. (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
state = ['state_example'] # [str] | US state or territory (optional)
cycle = [56] # [int] |  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.  (optional)
max_first_file_date = '2013-10-20' # date | Filter for committees whose first filing was received on or before this date. (optional)
designation = ['designation_example'] # [str] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
filing_frequency = ['filing_frequency_example'] # [str] | The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
sort = 'name' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of 'name'
year = [56] # [int] | A year that the committee was active— (after original registration date     or filing but before expiration date) (optional)
party = ['party_example'] # [str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
min_last_f1_date = '2013-10-20' # date | Filter for committees whose latest Form 1 was received on or after this date. (optional)
committee_type = ['committee_type_example'] # [str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
q = ['q_example'] # [str] | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. (optional)
treasurer_name = ['treasurer_name_example'] # [str] | Name of the Committee's treasurer. If multiple treasurers for the committee, the most recent treasurer will be shown. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.committees_get()
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CommitteeApi->committees_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.committees_get(sort_hide_null=sort_hide_null, organization_type=organization_type, committee_id=committee_id, candidate_id=candidate_id, min_first_file_date=min_first_file_date, max_last_f1_date=max_last_f1_date, page=page, state=state, cycle=cycle, max_first_file_date=max_first_file_date, designation=designation, sort_null_only=sort_null_only, filing_frequency=filing_frequency, per_page=per_page, sort=sort, year=year, party=party, min_last_f1_date=min_last_f1_date, committee_type=committee_type, sort_nulls_last=sort_nulls_last, q=q, treasurer_name=treasurer_name)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling CommitteeApi->committees_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **organization_type** | **[str]**| The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional]
 **committee_id** | **[str]**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional]
 **candidate_id** | **[str]**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional]
 **min_first_file_date** | **date**| Filter for committees whose first filing was received on or after this date. | [optional]
 **max_last_f1_date** | **date**| Filter for committees whose latest Form 1 was received on or before this date. | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **state** | **[str]**| US state or territory | [optional]
 **cycle** | **[int]**|  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.  | [optional]
 **max_first_file_date** | **date**| Filter for committees whose first filing was received on or before this date. | [optional]
 **designation** | **[str]**| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **filing_frequency** | **[str]**| The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived  | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of 'name'
 **year** | **[int]**| A year that the committee was active— (after original registration date     or filing but before expiration date) | [optional]
 **party** | **[str]**| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional]
 **min_last_f1_date** | **date**| Filter for committees whose latest Form 1 was received on or after this date. | [optional]
 **committee_type** | **[str]**| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **q** | **[str]**| The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. | [optional]
 **treasurer_name** | **[str]**| Name of the Committee&#39;s treasurer. If multiple treasurers for the committee, the most recent treasurer will be shown. | [optional]

### Return type

[**committee_page.CommitteePage**](CommitteePage.md)

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
