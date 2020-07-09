# openfec_sdk.SearchApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**names_candidates_get**](SearchApi.md#names_candidates_get) | **GET** /names/candidates/ |
[**names_committees_get**](SearchApi.md#names_committees_get) | **GET** /names/committees/ |


# **names_candidates_get**
> candidate_search_list.CandidateSearchList names_candidates_get(q)



 Search for candidates or committees by name. If you're looking for information on a particular person or group, using a name to find the `candidate_id` or `committee_id` on this endpoint can be a helpful first step.

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
    api_instance = openfec_sdk.SearchApi(api_client)
    q = ['q_example'] # [str] | Name (candidate or committee) to search for

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.names_candidates_get(q)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling SearchApi->names_candidates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **[str]**| Name (candidate or committee) to search for |
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'

### Return type

[**candidate_search_list.CandidateSearchList**](CandidateSearchList.md)

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

# **names_committees_get**
> committee_search_list.CommitteeSearchList names_committees_get(q)



 Search for candidates or committees by name. If you're looking for information on a particular person or group, using a name to find the `candidate_id` or `committee_id` on this endpoint can be a helpful first step.

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
    api_instance = openfec_sdk.SearchApi(api_client)
    q = ['q_example'] # [str] | Name (candidate or committee) to search for

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.names_committees_get(q)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling SearchApi->names_committees_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **[str]**| Name (candidate or committee) to search for |
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'

### Return type

[**committee_search_list.CommitteeSearchList**](CommitteeSearchList.md)

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
