# openfec_sdk.DebtsApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schedules_schedule_d_get**](DebtsApi.md#schedules_schedule_d_get) | **GET** /schedules/schedule_d/ |
[**schedules_schedule_d_sub_id_get**](DebtsApi.md#schedules_schedule_d_sub_id_get) | **GET** /schedules/schedule_d/{sub_id}/ |


# **schedules_schedule_d_get**
> inline_response_default4.InlineResponseDefault4 schedules_schedule_d_get()



 Schedule D, it shows debts and obligations owed to or by the committee that are required to be disclosed.

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
    api_instance = openfec_sdk.DebtsApi(api_client)
    min_image_number = 'min_image_number_example' # str |  (optional)
sort = 'load_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of 'load_date'
candidate_id = ['candidate_id_example'] # [str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
max_amount_incurred = 3.4 # float |  (optional)
min_amount_incurred = 3.4 # float |  (optional)
max_payment_period = 3.4 # float |  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
min_amount = 'min_amount_example' # str | Filter for all amounts greater than a value. (optional)
max_amount = 'max_amount_example' # str | Filter for all amounts less than a value. (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
max_date = '2013-10-20' # date | Maximum date (optional)
min_date = '2013-10-20' # date | Minimum date (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
min_payment_period = 3.4 # float |  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
image_number = ['image_number_example'] # [str] | The image number of the page where the schedule item is reported (optional)
committee_id = ['committee_id_example'] # [str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
max_image_number = 'max_image_number_example' # str |  (optional)
line_number = 'line_number_example' # str | Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`. (optional)
nature_of_debt = 'nature_of_debt_example' # str |  (optional)
creditor_debtor_name = ['creditor_debtor_name_example'] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.schedules_schedule_d_get()
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling DebtsApi->schedules_schedule_d_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.schedules_schedule_d_get(min_image_number=min_image_number, sort=sort, candidate_id=candidate_id, max_amount_incurred=max_amount_incurred, min_amount_incurred=min_amount_incurred, max_payment_period=max_payment_period, sort_nulls_last=sort_nulls_last, min_amount=min_amount, max_amount=max_amount, sort_null_only=sort_null_only, max_date=max_date, min_date=min_date, sort_hide_null=sort_hide_null, min_payment_period=min_payment_period, per_page=per_page, image_number=image_number, committee_id=committee_id, page=page, max_image_number=max_image_number, line_number=line_number, nature_of_debt=nature_of_debt, creditor_debtor_name=creditor_debtor_name)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling DebtsApi->schedules_schedule_d_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **min_image_number** | **str**|  | [optional]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of 'load_date'
 **candidate_id** | **[str]**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional]
 **max_amount_incurred** | **float**|  | [optional]
 **min_amount_incurred** | **float**|  | [optional]
 **max_payment_period** | **float**|  | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **min_amount** | **str**| Filter for all amounts greater than a value. | [optional]
 **max_amount** | **str**| Filter for all amounts less than a value. | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **max_date** | **date**| Maximum date | [optional]
 **min_date** | **date**| Minimum date | [optional]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **min_payment_period** | **float**|  | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **image_number** | **[str]**| The image number of the page where the schedule item is reported | [optional]
 **committee_id** | **[str]**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **max_image_number** | **str**|  | [optional]
 **line_number** | **str**| Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;. | [optional]
 **nature_of_debt** | **str**|  | [optional]
 **creditor_debtor_name** | **[str]**|  | [optional]

### Return type

[**inline_response_default4.InlineResponseDefault4**](InlineResponseDefault4.md)

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

# **schedules_schedule_d_sub_id_get**
> inline_response_default4.InlineResponseDefault4 schedules_schedule_d_sub_id_get(sub_id)



 Schedule D, it shows debts and obligations owed to or by the committee that are required to be disclosed.

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
    api_instance = openfec_sdk.DebtsApi(api_client)
    sub_id = 'sub_id_example' # str |
    sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
sort = 'load_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of 'load_date'
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.schedules_schedule_d_sub_id_get(sub_id)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling DebtsApi->schedules_schedule_d_sub_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.schedules_schedule_d_sub_id_get(sub_id, sort_nulls_last=sort_nulls_last, page=page, sort=sort, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, per_page=per_page)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling DebtsApi->schedules_schedule_d_sub_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_id** | **str**|  |
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of 'load_date'
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20

### Return type

[**inline_response_default4.InlineResponseDefault4**](InlineResponseDefault4.md)

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
