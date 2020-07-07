# openfec_sdk.DebtsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schedules_schedule_d_get**](DebtsApi.md#schedules_schedule_d_get) | **GET** /schedules/schedule_d/ |
[**schedules_schedule_d_sub_id_get**](DebtsApi.md#schedules_schedule_d_sub_id_get) | **GET** /schedules/schedule_d/{sub_id}/ |


# **schedules_schedule_d_get**
> InlineResponseDefault4 schedules_schedule_d_get(api_key, max_payment_period=max_payment_period, sort=sort, max_amount=max_amount, min_image_number=min_image_number, creditor_debtor_name=creditor_debtor_name, min_amount_incurred=min_amount_incurred, sort_nulls_last=sort_nulls_last, min_payment_period=min_payment_period, sort_hide_null=sort_hide_null, min_date=min_date, line_number=line_number, max_date=max_date, committee_id=committee_id, per_page=per_page, min_amount=min_amount, candidate_id=candidate_id, nature_of_debt=nature_of_debt, image_number=image_number, page=page, sort_null_only=sort_null_only, max_amount_incurred=max_amount_incurred, max_image_number=max_image_number)



 Schedule D, it shows debts and obligations owed to or by the committee that are required to be disclosed.

### Example
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'
# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = openfec_sdk.DebtsApi(openfec_sdk.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
max_payment_period = 3.4 # float |  (optional)
sort = 'load_date' # str | Provide a field to sort by. Use - for descending order. (optional) (default to load_date)
max_amount = 'max_amount_example' # str | Filter for all amounts less than a value. (optional)
min_image_number = 'min_image_number_example' # str |  (optional)
creditor_debtor_name = ['creditor_debtor_name_example'] # list[str] |  (optional)
min_amount_incurred = 3.4 # float |  (optional)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
min_payment_period = 3.4 # float |  (optional)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
min_date = '2013-10-20' # date | Minimum date (optional)
line_number = 'line_number_example' # str | Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`. (optional)
max_date = '2013-10-20' # date | Maximum date (optional)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
min_amount = 'min_amount_example' # str | Filter for all amounts greater than a value. (optional)
candidate_id = ['candidate_id_example'] # list[str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
nature_of_debt = 'nature_of_debt_example' # str |  (optional)
image_number = ['image_number_example'] # list[str] | The image number of the page where the schedule item is reported (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
max_amount_incurred = 3.4 # float |  (optional)
max_image_number = 'max_image_number_example' # str |  (optional)

try:
    api_response = api_instance.schedules_schedule_d_get(api_key, max_payment_period=max_payment_period, sort=sort, max_amount=max_amount, min_image_number=min_image_number, creditor_debtor_name=creditor_debtor_name, min_amount_incurred=min_amount_incurred, sort_nulls_last=sort_nulls_last, min_payment_period=min_payment_period, sort_hide_null=sort_hide_null, min_date=min_date, line_number=line_number, max_date=max_date, committee_id=committee_id, per_page=per_page, min_amount=min_amount, candidate_id=candidate_id, nature_of_debt=nature_of_debt, image_number=image_number, page=page, sort_null_only=sort_null_only, max_amount_incurred=max_amount_incurred, max_image_number=max_image_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebtsApi->schedules_schedule_d_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **max_payment_period** | **float**|  | [optional]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to load_date]
 **max_amount** | **str**| Filter for all amounts less than a value. | [optional]
 **min_image_number** | **str**|  | [optional]
 **creditor_debtor_name** | [**list[str]**](str.md)|  | [optional]
 **min_amount_incurred** | **float**|  | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **min_payment_period** | **float**|  | [optional]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **min_date** | **date**| Minimum date | [optional]
 **line_number** | **str**| Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;. | [optional]
 **max_date** | **date**| Maximum date | [optional]
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **min_amount** | **str**| Filter for all amounts greater than a value. | [optional]
 **candidate_id** | [**list[str]**](str.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional]
 **nature_of_debt** | **str**|  | [optional]
 **image_number** | [**list[str]**](str.md)| The image number of the page where the schedule item is reported | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **max_amount_incurred** | **float**|  | [optional]
 **max_image_number** | **str**|  | [optional]

### Return type

[**InlineResponseDefault4**](InlineResponseDefault4.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_schedule_d_sub_id_get**
> InlineResponseDefault4 schedules_schedule_d_sub_id_get(api_key, sub_id, page=page, per_page=per_page, sort_nulls_last=sort_nulls_last, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)



 Schedule D, it shows debts and obligations owed to or by the committee that are required to be disclosed.

### Example
```python
from __future__ import print_function
import time
import openfec_sdk
from openfec_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openfec_sdk.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'
# Configure API key authorization: ApiKeyQueryAuth
configuration = openfec_sdk.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Configure API key authorization: apiKey
configuration = openfec_sdk.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = openfec_sdk.DebtsApi(openfec_sdk.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sub_id = 'sub_id_example' # str |
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
sort = 'load_date' # str | Provide a field to sort by. Use - for descending order. (optional) (default to load_date)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)

try:
    api_response = api_instance.schedules_schedule_d_sub_id_get(api_key, sub_id, page=page, per_page=per_page, sort_nulls_last=sort_nulls_last, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebtsApi->schedules_schedule_d_sub_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sub_id** | **str**|  |
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to load_date]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]

### Return type

[**InlineResponseDefault4**](InlineResponseDefault4.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
