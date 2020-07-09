# openfec_sdk.AuditApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**audit_case_get**](AuditApi.md#audit_case_get) | **GET** /audit-case/ |
[**audit_category_get**](AuditApi.md#audit_category_get) | **GET** /audit-category/ |
[**audit_primary_category_get**](AuditApi.md#audit_primary_category_get) | **GET** /audit-primary-category/ |
[**names_audit_candidates_get**](AuditApi.md#names_audit_candidates_get) | **GET** /names/audit_candidates/ |
[**names_audit_committees_get**](AuditApi.md#names_audit_committees_get) | **GET** /names/audit_committees/ |


# **audit_case_get**
> audit_case_page.AuditCasePage audit_case_get()



 This endpoint contains Final Audit Reports approved by the Commission since inception. The search can be based on information about the audited committee (Name, FEC ID Number, Type,  Election Cycle) or the issues covered in the report.

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
    api_instance = openfec_sdk.AuditApi(api_client)
    audit_case_id = ['audit_case_id_example'] # [str] |  Primary/foreign key for audit tables  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
sub_category_id = 'all' # str |  The finding id of an audit. Finding are a category of broader issues. Each category has an unique ID.  (optional) if omitted the server will use the default value of 'all'
committee_id = ['committee_id_example'] # [str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
sort = ["-cycle","committee_name"] # [str], none_type | Provide a field to sort by. Use - for descending order. (optional) if omitted the server will use the default value of ["-cycle","committee_name"]
candidate_id = ['candidate_id_example'] # [str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
committee_designation = 'committee_designation_example' # str | Type of committee:         - H or S - Congressional         - P - Presidential         - X or Y or Z - Party         - N or Q - PAC         - I - Independent expenditure         - O - Super PAC   (optional)
min_election_cycle = 56 # int |  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  (optional)
cycle = [56] # [int] |  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  (optional)
qq = ['qq_example'] # [str] | Name of candidate running for office (optional)
committee_type = ['committee_type_example'] # [str] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
primary_category_id = 'all' # str |  Audit category ID (table PK)  (optional) if omitted the server will use the default value of 'all'
audit_id = [56] # [int] |  The audit issue. Each subcategory has an unique ID  (optional)
max_election_cycle = 56 # int |  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  (optional)
q = ['q_example'] # [str] | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.audit_case_get()
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling AuditApi->audit_case_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.audit_case_get(audit_case_id=audit_case_id, page=page, sub_category_id=sub_category_id, committee_id=committee_id, sort_nulls_last=sort_nulls_last, per_page=per_page, sort=sort, candidate_id=candidate_id, sort_hide_null=sort_hide_null, committee_designation=committee_designation, min_election_cycle=min_election_cycle, cycle=cycle, qq=qq, committee_type=committee_type, sort_null_only=sort_null_only, primary_category_id=primary_category_id, audit_id=audit_id, max_election_cycle=max_election_cycle, q=q)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling AuditApi->audit_case_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **audit_case_id** | **[str]**|  Primary/foreign key for audit tables  | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **sub_category_id** | **str**|  The finding id of an audit. Finding are a category of broader issues. Each category has an unique ID.  | [optional] if omitted the server will use the default value of 'all'
 **committee_id** | **[str]**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **sort** | **[str], none_type**| Provide a field to sort by. Use - for descending order. | [optional] if omitted the server will use the default value of ["-cycle","committee_name"]
 **candidate_id** | **[str]**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **committee_designation** | **str**| Type of committee:         - H or S - Congressional         - P - Presidential         - X or Y or Z - Party         - N or Q - PAC         - I - Independent expenditure         - O - Super PAC   | [optional]
 **min_election_cycle** | **int**|  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  | [optional]
 **cycle** | **[int]**|  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  | [optional]
 **qq** | **[str]**| Name of candidate running for office | [optional]
 **committee_type** | **[str]**| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **primary_category_id** | **str**|  Audit category ID (table PK)  | [optional] if omitted the server will use the default value of 'all'
 **audit_id** | **[int]**|  The audit issue. Each subcategory has an unique ID  | [optional]
 **max_election_cycle** | **int**|  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  | [optional]
 **q** | **[str]**| The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. | [optional]

### Return type

[**audit_case_page.AuditCasePage**](AuditCasePage.md)

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

# **audit_category_get**
> audit_category_page.AuditCategoryPage audit_category_get()



 This lists the options for the categories and subcategories available in the /audit-search/ endpoint.

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
    api_instance = openfec_sdk.AuditApi(api_client)
    page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
primary_category_id = ['primary_category_id_example'] # [str] |  Audit category ID (table PK)  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
sort = 'primary_category_name' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of 'primary_category_name'
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
primary_category_name = ['primary_category_name_example'] # [str] | Primary Audit Category     - No Findings or Issues/Not a Committee     - Net Outstanding Campaign/Convention Expenditures/Obligations     - Payments/Disgorgements     - Allocation Issues     - Prohibited Contributions     - Disclosure     - Recordkeeping     - Repayment to US Treasury     - Other     - Misstatement of Financial Activity     - Excessive Contributions     - Failure to File Reports/Schedules/Notices     - Loans     - Referred Findings Not Listed  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.audit_category_get()
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling AuditApi->audit_category_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.audit_category_get(page=page, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, primary_category_id=primary_category_id, per_page=per_page, sort=sort, sort_hide_null=sort_hide_null, primary_category_name=primary_category_name)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling AuditApi->audit_category_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **primary_category_id** | **[str]**|  Audit category ID (table PK)  | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of 'primary_category_name'
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **primary_category_name** | **[str]**| Primary Audit Category     - No Findings or Issues/Not a Committee     - Net Outstanding Campaign/Convention Expenditures/Obligations     - Payments/Disgorgements     - Allocation Issues     - Prohibited Contributions     - Disclosure     - Recordkeeping     - Repayment to US Treasury     - Other     - Misstatement of Financial Activity     - Excessive Contributions     - Failure to File Reports/Schedules/Notices     - Loans     - Referred Findings Not Listed  | [optional]

### Return type

[**audit_category_page.AuditCategoryPage**](AuditCategoryPage.md)

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

# **audit_primary_category_get**
> audit_primary_category_page.AuditPrimaryCategoryPage audit_primary_category_get()



 This lists the options for the primary categories available in the /audit-search/ endpoint.

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
    api_instance = openfec_sdk.AuditApi(api_client)
    page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
primary_category_id = ['primary_category_id_example'] # [str] |  Audit category ID (table PK)  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
sort = 'primary_category_name' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of 'primary_category_name'
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
primary_category_name = ['primary_category_name_example'] # [str] | Primary Audit Category     - No Findings or Issues/Not a Committee     - Net Outstanding Campaign/Convention Expenditures/Obligations     - Payments/Disgorgements     - Allocation Issues     - Prohibited Contributions     - Disclosure     - Recordkeeping     - Repayment to US Treasury     - Other     - Misstatement of Financial Activity     - Excessive Contributions     - Failure to File Reports/Schedules/Notices     - Loans     - Referred Findings Not Listed  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.audit_primary_category_get()
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling AuditApi->audit_primary_category_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.audit_primary_category_get(page=page, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, primary_category_id=primary_category_id, per_page=per_page, sort=sort, sort_hide_null=sort_hide_null, primary_category_name=primary_category_name)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling AuditApi->audit_primary_category_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **primary_category_id** | **[str]**|  Audit category ID (table PK)  | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of 'primary_category_name'
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **primary_category_name** | **[str]**| Primary Audit Category     - No Findings or Issues/Not a Committee     - Net Outstanding Campaign/Convention Expenditures/Obligations     - Payments/Disgorgements     - Allocation Issues     - Prohibited Contributions     - Disclosure     - Recordkeeping     - Repayment to US Treasury     - Other     - Misstatement of Financial Activity     - Excessive Contributions     - Failure to File Reports/Schedules/Notices     - Loans     - Referred Findings Not Listed  | [optional]

### Return type

[**audit_primary_category_page.AuditPrimaryCategoryPage**](AuditPrimaryCategoryPage.md)

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

# **names_audit_candidates_get**
> audit_candidate_search_list.AuditCandidateSearchList names_audit_candidates_get(q)



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
    api_instance = openfec_sdk.AuditApi(api_client)
    q = ['q_example'] # [str] | Name (candidate or committee) to search for

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.names_audit_candidates_get(q)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling AuditApi->names_audit_candidates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **[str]**| Name (candidate or committee) to search for |
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'

### Return type

[**audit_candidate_search_list.AuditCandidateSearchList**](AuditCandidateSearchList.md)

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

# **names_audit_committees_get**
> audit_committee_search_list.AuditCommitteeSearchList names_audit_committees_get(q)



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
    api_instance = openfec_sdk.AuditApi(api_client)
    q = ['q_example'] # [str] | Name (candidate or committee) to search for

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.names_audit_committees_get(q)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling AuditApi->names_audit_committees_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **[str]**| Name (candidate or committee) to search for |
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'

### Return type

[**audit_committee_search_list.AuditCommitteeSearchList**](AuditCommitteeSearchList.md)

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
