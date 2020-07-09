# openfec_sdk.LoansApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schedules_schedule_c_get**](LoansApi.md#schedules_schedule_c_get) | **GET** /schedules/schedule_c/ |
[**schedules_schedule_c_sub_id_get**](LoansApi.md#schedules_schedule_c_sub_id_get) | **GET** /schedules/schedule_c/{sub_id}/ |


# **schedules_schedule_c_get**
> inline_response_default3.InlineResponseDefault3 schedules_schedule_c_get()



 Schedule C shows all loans, endorsements and loan guarantees a committee receives or makes.  The committee continues to report the loan until it is repaid.

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
    api_instance = openfec_sdk.LoansApi(api_client)
    min_payment_to_date = 56 # int |  Minimum payment to date  (optional)
min_incurred_date = openfec_sdk.date, none_type() # date, none_type |  Minimum incurred date  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
min_amount = 'min_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
committee_id = ['committee_id_example'] # [str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
sort_nulls_last = True # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of True
max_incurred_date = openfec_sdk.date, none_type() # date, none_type |  Maximum incurred date  (optional)
loan_source_name = ['loan_source_name_example'] # [str] | Source of the loan (i.e., bank loan, brokerage account, credit card, home equity line of credit,               other line of credit, or personal funds of the candidate (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
sort = '-incurred_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of '-incurred_date'
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
last_index = openfec_sdk.int, none_type() # int, none_type | Index of last result from previous page (optional)
candidate_name = ['candidate_name_example'] # [str] | Name of candidate running for office (optional)
line_number = 'line_number_example' # str |  Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`.  (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
max_image_number = 'max_image_number_example' # str |  (optional)
max_amount = 'max_amount_example' # str |  Filter for all amounts less than a value.  (optional)
image_number = ['image_number_example'] # [str] |  An unique identifier for each page where the electronic or paper filing is reported.  (optional)
min_image_number = 'min_image_number_example' # str |  (optional)
max_payment_to_date = 56 # int |  Maximum payment to date  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.schedules_schedule_c_get()
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling LoansApi->schedules_schedule_c_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.schedules_schedule_c_get(min_payment_to_date=min_payment_to_date, min_incurred_date=min_incurred_date, page=page, min_amount=min_amount, committee_id=committee_id, sort_nulls_last=sort_nulls_last, max_incurred_date=max_incurred_date, loan_source_name=loan_source_name, per_page=per_page, sort=sort, sort_hide_null=sort_hide_null, last_index=last_index, candidate_name=candidate_name, line_number=line_number, sort_null_only=sort_null_only, max_image_number=max_image_number, max_amount=max_amount, image_number=image_number, min_image_number=min_image_number, max_payment_to_date=max_payment_to_date)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling LoansApi->schedules_schedule_c_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **min_payment_to_date** | **int**|  Minimum payment to date  | [optional]
 **min_incurred_date** | **date, none_type**|  Minimum incurred date  | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **min_amount** | **str**|  Filter for all amounts greater than a value.  | [optional]
 **committee_id** | **[str]**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of True
 **max_incurred_date** | **date, none_type**|  Maximum incurred date  | [optional]
 **loan_source_name** | **[str]**| Source of the loan (i.e., bank loan, brokerage account, credit card, home equity line of credit,               other line of credit, or personal funds of the candidate | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of '-incurred_date'
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **last_index** | **int, none_type**| Index of last result from previous page | [optional]
 **candidate_name** | **[str]**| Name of candidate running for office | [optional]
 **line_number** | **str**|  Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;.  | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **max_image_number** | **str**|  | [optional]
 **max_amount** | **str**|  Filter for all amounts less than a value.  | [optional]
 **image_number** | **[str]**|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional]
 **min_image_number** | **str**|  | [optional]
 **max_payment_to_date** | **int**|  Maximum payment to date  | [optional]

### Return type

[**inline_response_default3.InlineResponseDefault3**](InlineResponseDefault3.md)

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

# **schedules_schedule_c_sub_id_get**
> inline_response_default3.InlineResponseDefault3 schedules_schedule_c_sub_id_get(sub_id)



 Schedule C shows all loans, endorsements and loan guarantees a committee receives or makes.  The committee continues to report the loan until it is repaid.

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
    api_instance = openfec_sdk.LoansApi(api_client)
    sub_id = 'sub_id_example' # str |
    per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
sort = 'null' # str, none_type | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of 'null'
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.schedules_schedule_c_sub_id_get(sub_id)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling LoansApi->schedules_schedule_c_sub_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.schedules_schedule_c_sub_id_get(sub_id, per_page=per_page, page=page, sort_nulls_last=sort_nulls_last, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling LoansApi->schedules_schedule_c_sub_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_id** | **str**|  |
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **sort** | **str, none_type**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of 'null'
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False

### Return type

[**inline_response_default3.InlineResponseDefault3**](InlineResponseDefault3.md)

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
