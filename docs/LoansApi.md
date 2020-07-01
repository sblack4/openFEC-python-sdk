# swagger_client.LoansApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schedules_schedule_c_get**](LoansApi.md#schedules_schedule_c_get) | **GET** /schedules/schedule_c/ | 
[**schedules_schedule_c_sub_id_get**](LoansApi.md#schedules_schedule_c_sub_id_get) | **GET** /schedules/schedule_c/{sub_id}/ | 


# **schedules_schedule_c_get**
> InlineResponseDefault3 schedules_schedule_c_get(api_key, last_index=last_index, min_payment_to_date=min_payment_to_date, sort=sort, max_amount=max_amount, max_incurred_date=max_incurred_date, min_image_number=min_image_number, candidate_name=candidate_name, loan_source_name=loan_source_name, sort_nulls_last=sort_nulls_last, sort_hide_null=sort_hide_null, line_number=line_number, committee_id=committee_id, max_payment_to_date=max_payment_to_date, per_page=per_page, min_amount=min_amount, min_incurred_date=min_incurred_date, image_number=image_number, page=page, sort_null_only=sort_null_only, max_image_number=max_image_number)



 Schedule C shows all loans, endorsements and loan guarantees a committee receives or makes.  The committee continues to report the loan until it is repaid. 

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
api_instance = swagger_client.LoansApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
last_index = 56 # int | Index of last result from previous page (optional)
min_payment_to_date = 56 # int |  Minimum payment to date  (optional)
sort = '-incurred_date' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -incurred_date)
max_amount = 'max_amount_example' # str |  Filter for all amounts less than a value.  (optional)
max_incurred_date = '2013-10-20' # date |  Maximum incurred date  (optional)
min_image_number = 'min_image_number_example' # str |  (optional)
candidate_name = ['candidate_name_example'] # list[str] | Name of candidate running for office (optional)
loan_source_name = ['loan_source_name_example'] # list[str] | Source of the loan (i.e., bank loan, brokerage account, credit card, home equity line of credit,               other line of credit, or personal funds of the candidate (optional)
sort_nulls_last = true # bool | Toggle that sorts null values last (optional) (default to true)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
line_number = 'line_number_example' # str |  Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`.  (optional)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
max_payment_to_date = 56 # int |  Maximum payment to date  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
min_amount = 'min_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
min_incurred_date = '2013-10-20' # date |  Minimum incurred date  (optional)
image_number = ['image_number_example'] # list[str] |  An unique identifier for each page where the electronic or paper filing is reported.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)
max_image_number = 'max_image_number_example' # str |  (optional)

try:
    api_response = api_instance.schedules_schedule_c_get(api_key, last_index=last_index, min_payment_to_date=min_payment_to_date, sort=sort, max_amount=max_amount, max_incurred_date=max_incurred_date, min_image_number=min_image_number, candidate_name=candidate_name, loan_source_name=loan_source_name, sort_nulls_last=sort_nulls_last, sort_hide_null=sort_hide_null, line_number=line_number, committee_id=committee_id, max_payment_to_date=max_payment_to_date, per_page=per_page, min_amount=min_amount, min_incurred_date=min_incurred_date, image_number=image_number, page=page, sort_null_only=sort_null_only, max_image_number=max_image_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoansApi->schedules_schedule_c_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **last_index** | **int**| Index of last result from previous page | [optional] 
 **min_payment_to_date** | **int**|  Minimum payment to date  | [optional] 
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] [default to -incurred_date]
 **max_amount** | **str**|  Filter for all amounts less than a value.  | [optional] 
 **max_incurred_date** | **date**|  Maximum incurred date  | [optional] 
 **min_image_number** | **str**|  | [optional] 
 **candidate_name** | [**list[str]**](str.md)| Name of candidate running for office | [optional] 
 **loan_source_name** | [**list[str]**](str.md)| Source of the loan (i.e., bank loan, brokerage account, credit card, home equity line of credit,               other line of credit, or personal funds of the candidate | [optional] 
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to true]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **line_number** | **str**|  Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;.  | [optional] 
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **max_payment_to_date** | **int**|  Maximum payment to date  | [optional] 
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **min_amount** | **str**|  Filter for all amounts greater than a value.  | [optional] 
 **min_incurred_date** | **date**|  Minimum incurred date  | [optional] 
 **image_number** | [**list[str]**](str.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] 
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **max_image_number** | **str**|  | [optional] 

### Return type

[**InlineResponseDefault3**](InlineResponseDefault3.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_schedule_c_sub_id_get**
> InlineResponseDefault3 schedules_schedule_c_sub_id_get(api_key, sub_id, page=page, per_page=per_page, sort_nulls_last=sort_nulls_last, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)



 Schedule C shows all loans, endorsements and loan guarantees a committee receives or makes.  The committee continues to report the loan until it is repaid. 

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
api_instance = swagger_client.LoansApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
sub_id = 'sub_id_example' # str | 
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
sort_nulls_last = false # bool | Toggle that sorts null values last (optional) (default to false)
sort = 'sort_example' # str | Provide a field to sort by. Use - for descending order. (optional)
sort_hide_null = false # bool | Hide null values on sorted column(s). (optional) (default to false)
sort_null_only = false # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to false)

try:
    api_response = api_instance.schedules_schedule_c_sub_id_get(api_key, sub_id, page=page, per_page=per_page, sort_nulls_last=sort_nulls_last, sort=sort, sort_hide_null=sort_hide_null, sort_null_only=sort_null_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoansApi->schedules_schedule_c_sub_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **sub_id** | **str**|  | 
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to false]
 **sort** | **str**| Provide a field to sort by. Use - for descending order. | [optional] 
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]

### Return type

[**InlineResponseDefault3**](InlineResponseDefault3.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

