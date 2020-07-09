# openfec_sdk.LoansApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schedules_schedule_c_get**](LoansApi.md#schedules_schedule_c_get) | **GET** /schedules/schedule_c/ |
[**schedules_schedule_c_sub_id_get**](LoansApi.md#schedules_schedule_c_sub_id_get) | **GET** /schedules/schedule_c/{sub_id}/ |


# **schedules_schedule_c_get**
> InlineResponseDefault3 schedules_schedule_c_get(api_key, min_image_number=min_image_number, sort=sort, min_payment_to_date=min_payment_to_date, sort_nulls_last=sort_nulls_last, min_amount=min_amount, max_amount=max_amount, last_index=last_index, sort_null_only=sort_null_only, candidate_name=candidate_name, min_incurred_date=min_incurred_date, loan_source_name=loan_source_name, sort_hide_null=sort_hide_null, per_page=per_page, max_payment_to_date=max_payment_to_date, image_number=image_number, max_incurred_date=max_incurred_date, committee_id=committee_id, page=page, max_image_number=max_image_number, line_number=line_number)



 Schedule C shows all loans, endorsements and loan guarantees a committee receives or makes.  The committee continues to report the loan until it is repaid.

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
    api_instance = openfec_sdk.LoansApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
min_image_number = 'min_image_number_example' # str |  (optional)
sort = '-incurred_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-incurred_date')
min_payment_to_date = 56 # int |  Minimum payment to date  (optional)
sort_nulls_last = True # bool | Toggle that sorts null values last (optional) (default to True)
min_amount = 'min_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
max_amount = 'max_amount_example' # str |  Filter for all amounts less than a value.  (optional)
last_index = 56 # int | Index of last result from previous page (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
candidate_name = ['candidate_name_example'] # list[str] | Name of candidate running for office (optional)
min_incurred_date = '2013-10-20' # date |  Minimum incurred date  (optional)
loan_source_name = ['loan_source_name_example'] # list[str] | Source of the loan (i.e., bank loan, brokerage account, credit card, home equity line of credit,               other line of credit, or personal funds of the candidate (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
max_payment_to_date = 56 # int |  Maximum payment to date  (optional)
image_number = ['image_number_example'] # list[str] |  An unique identifier for each page where the electronic or paper filing is reported.  (optional)
max_incurred_date = '2013-10-20' # date |  Maximum incurred date  (optional)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
max_image_number = 'max_image_number_example' # str |  (optional)
line_number = 'line_number_example' # str |  Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`.  (optional)

    try:
        api_response = api_instance.schedules_schedule_c_get(api_key, min_image_number=min_image_number, sort=sort, min_payment_to_date=min_payment_to_date, sort_nulls_last=sort_nulls_last, min_amount=min_amount, max_amount=max_amount, last_index=last_index, sort_null_only=sort_null_only, candidate_name=candidate_name, min_incurred_date=min_incurred_date, loan_source_name=loan_source_name, sort_hide_null=sort_hide_null, per_page=per_page, max_payment_to_date=max_payment_to_date, image_number=image_number, max_incurred_date=max_incurred_date, committee_id=committee_id, page=page, max_image_number=max_image_number, line_number=line_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoansApi->schedules_schedule_c_get: %s\n" % e)
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
    api_instance = openfec_sdk.LoansApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
min_image_number = 'min_image_number_example' # str |  (optional)
sort = '-incurred_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-incurred_date')
min_payment_to_date = 56 # int |  Minimum payment to date  (optional)
sort_nulls_last = True # bool | Toggle that sorts null values last (optional) (default to True)
min_amount = 'min_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
max_amount = 'max_amount_example' # str |  Filter for all amounts less than a value.  (optional)
last_index = 56 # int | Index of last result from previous page (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
candidate_name = ['candidate_name_example'] # list[str] | Name of candidate running for office (optional)
min_incurred_date = '2013-10-20' # date |  Minimum incurred date  (optional)
loan_source_name = ['loan_source_name_example'] # list[str] | Source of the loan (i.e., bank loan, brokerage account, credit card, home equity line of credit,               other line of credit, or personal funds of the candidate (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
max_payment_to_date = 56 # int |  Maximum payment to date  (optional)
image_number = ['image_number_example'] # list[str] |  An unique identifier for each page where the electronic or paper filing is reported.  (optional)
max_incurred_date = '2013-10-20' # date |  Maximum incurred date  (optional)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
max_image_number = 'max_image_number_example' # str |  (optional)
line_number = 'line_number_example' # str |  Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`.  (optional)

    try:
        api_response = api_instance.schedules_schedule_c_get(api_key, min_image_number=min_image_number, sort=sort, min_payment_to_date=min_payment_to_date, sort_nulls_last=sort_nulls_last, min_amount=min_amount, max_amount=max_amount, last_index=last_index, sort_null_only=sort_null_only, candidate_name=candidate_name, min_incurred_date=min_incurred_date, loan_source_name=loan_source_name, sort_hide_null=sort_hide_null, per_page=per_page, max_payment_to_date=max_payment_to_date, image_number=image_number, max_incurred_date=max_incurred_date, committee_id=committee_id, page=page, max_image_number=max_image_number, line_number=line_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoansApi->schedules_schedule_c_get: %s\n" % e)
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
    api_instance = openfec_sdk.LoansApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
min_image_number = 'min_image_number_example' # str |  (optional)
sort = '-incurred_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to '-incurred_date')
min_payment_to_date = 56 # int |  Minimum payment to date  (optional)
sort_nulls_last = True # bool | Toggle that sorts null values last (optional) (default to True)
min_amount = 'min_amount_example' # str |  Filter for all amounts greater than a value.  (optional)
max_amount = 'max_amount_example' # str |  Filter for all amounts less than a value.  (optional)
last_index = 56 # int | Index of last result from previous page (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
candidate_name = ['candidate_name_example'] # list[str] | Name of candidate running for office (optional)
min_incurred_date = '2013-10-20' # date |  Minimum incurred date  (optional)
loan_source_name = ['loan_source_name_example'] # list[str] | Source of the loan (i.e., bank loan, brokerage account, credit card, home equity line of credit,               other line of credit, or personal funds of the candidate (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)
max_payment_to_date = 56 # int |  Maximum payment to date  (optional)
image_number = ['image_number_example'] # list[str] |  An unique identifier for each page where the electronic or paper filing is reported.  (optional)
max_incurred_date = '2013-10-20' # date |  Maximum incurred date  (optional)
committee_id = ['committee_id_example'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
max_image_number = 'max_image_number_example' # str |  (optional)
line_number = 'line_number_example' # str |  Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`.  (optional)

    try:
        api_response = api_instance.schedules_schedule_c_get(api_key, min_image_number=min_image_number, sort=sort, min_payment_to_date=min_payment_to_date, sort_nulls_last=sort_nulls_last, min_amount=min_amount, max_amount=max_amount, last_index=last_index, sort_null_only=sort_null_only, candidate_name=candidate_name, min_incurred_date=min_incurred_date, loan_source_name=loan_source_name, sort_hide_null=sort_hide_null, per_page=per_page, max_payment_to_date=max_payment_to_date, image_number=image_number, max_incurred_date=max_incurred_date, committee_id=committee_id, page=page, max_image_number=max_image_number, line_number=line_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoansApi->schedules_schedule_c_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **min_image_number** | **str**|  | [optional]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-incurred_date&#39;]
 **min_payment_to_date** | **int**|  Minimum payment to date  | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to True]
 **min_amount** | **str**|  Filter for all amounts greater than a value.  | [optional]
 **max_amount** | **str**|  Filter for all amounts less than a value.  | [optional]
 **last_index** | **int**| Index of last result from previous page | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **candidate_name** | [**list[str]**](str.md)| Name of candidate running for office | [optional]
 **min_incurred_date** | **date**|  Minimum incurred date  | [optional]
 **loan_source_name** | [**list[str]**](str.md)| Source of the loan (i.e., bank loan, brokerage account, credit card, home equity line of credit,               other line of credit, or personal funds of the candidate | [optional]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **max_payment_to_date** | **int**|  Maximum payment to date  | [optional]
 **image_number** | [**list[str]**](str.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional]
 **max_incurred_date** | **date**|  Maximum incurred date  | [optional]
 **committee_id** | [**list[str]**](str.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **max_image_number** | **str**|  | [optional]
 **line_number** | **str**|  Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;.  | [optional]

### Return type

[**InlineResponseDefault3**](InlineResponseDefault3.md)

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
> InlineResponseDefault3 schedules_schedule_c_sub_id_get(api_key, sub_id, sort_nulls_last=sort_nulls_last, page=page, sort=sort, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, per_page=per_page)



 Schedule C shows all loans, endorsements and loan guarantees a committee receives or makes.  The committee continues to report the loan until it is repaid.

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
    api_instance = openfec_sdk.LoansApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
sub_id = 'sub_id_example' # str |
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)

    try:
        api_response = api_instance.schedules_schedule_c_sub_id_get(api_key, sub_id, sort_nulls_last=sort_nulls_last, page=page, sort=sort, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoansApi->schedules_schedule_c_sub_id_get: %s\n" % e)
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
    api_instance = openfec_sdk.LoansApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
sub_id = 'sub_id_example' # str |
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)

    try:
        api_response = api_instance.schedules_schedule_c_sub_id_get(api_key, sub_id, sort_nulls_last=sort_nulls_last, page=page, sort=sort, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoansApi->schedules_schedule_c_sub_id_get: %s\n" % e)
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
    api_instance = openfec_sdk.LoansApi(api_client)
    api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to 'DEMO_KEY')
sub_id = 'sub_id_example' # str |
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) (default to False)
page = 1 # int | For paginating through results, starting at page 1 (optional) (default to 1)
sort = 'null' # str | Provide a field to sort by. Use `-` for descending order.  (optional) (default to 'null')
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) (default to False)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) (default to False)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) (default to 20)

    try:
        api_response = api_instance.schedules_schedule_c_sub_id_get(api_key, sub_id, sort_nulls_last=sort_nulls_last, page=page, sort=sort, sort_null_only=sort_null_only, sort_hide_null=sort_hide_null, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoansApi->schedules_schedule_c_sub_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **sub_id** | **str**|  |
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] [default to False]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;null&#39;]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to False]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] [default to False]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]

### Return type

[**InlineResponseDefault3**](InlineResponseDefault3.md)

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
