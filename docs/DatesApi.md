# openapi_client.DatesApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calendar_dates_export_get**](DatesApi.md#calendar_dates_export_get) | **GET** /calendar-dates/export/ |
[**calendar_dates_get**](DatesApi.md#calendar_dates_get) | **GET** /calendar-dates/ |
[**election_dates_get**](DatesApi.md#election_dates_get) | **GET** /election-dates/ |
[**reporting_dates_get**](DatesApi.md#reporting_dates_get) | **GET** /reporting-dates/ |


# **calendar_dates_export_get**
> calendar_date_page.CalendarDatePage calendar_dates_export_get()



 Returns CSV or ICS for downloading directly into calendar applications like Google, Outlook or other applications.  Combines the election and reporting dates with Commission meetings, conferences, outreach, Advisory Opinions, rules, litigation dates and other events into one calendar.  State filtering now applies to elections, reports and reporting periods.  Presidential pre-primary report due dates are not shown on even years. Filers generally opt to file monthly rather than submit over 50 pre-primary election reports. All reporting deadlines are available at /reporting-dates/ for reference.  This is [the sql function](https://github.com/fecgov/openFEC/blob/develop/data/migrations/V40__omnibus_dates.sql) that creates the calendar.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DatesApi(api_client)
    page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
min_start_date = '2013-10-20' # date |  The minimum start date.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
description = ['description_example'] # [str] | Brief description of event (optional)
min_end_date = '2013-10-20' # date |  The minimum end date.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
event_id = 56 # int | An unique ID for an event. Useful for downloading a single event to your calendar. This ID is not a permanent, persistent ID. (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
max_end_date = '2013-10-20' # date |  The maximum end date.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
renderer = 'ics' # str |  (optional) if omitted the server will use the default value of 'ics'
summary = ['summary_example'] # [str] | Longer description of event (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
calendar_category_id = [56] # [int] |  Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29  (optional)
sort = '-start_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of '-start_date'
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
max_start_date = '2013-10-20' # date |  The maximum start date.(MM/DD/YYYY or YYYY-MM-DD)  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.calendar_dates_export_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DatesApi->calendar_dates_export_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.calendar_dates_export_get(page=page, min_start_date=min_start_date, description=description, min_end_date=min_end_date, event_id=event_id, sort_null_only=sort_null_only, max_end_date=max_end_date, sort_nulls_last=sort_nulls_last, renderer=renderer, summary=summary, per_page=per_page, calendar_category_id=calendar_category_id, sort=sort, sort_hide_null=sort_hide_null, max_start_date=max_start_date)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DatesApi->calendar_dates_export_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **min_start_date** | **date**|  The minimum start date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **description** | **[str]**| Brief description of event | [optional]
 **min_end_date** | **date**|  The minimum end date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **event_id** | **int**| An unique ID for an event. Useful for downloading a single event to your calendar. This ID is not a permanent, persistent ID. | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **max_end_date** | **date**|  The maximum end date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **renderer** | **str**|  | [optional] if omitted the server will use the default value of 'ics'
 **summary** | **[str]**| Longer description of event | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **calendar_category_id** | **[int]**|  Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29  | [optional]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of '-start_date'
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **max_start_date** | **date**|  The maximum start date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional]

### Return type

[**calendar_date_page.CalendarDatePage**](CalendarDatePage.md)

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

# **calendar_dates_get**
> calendar_date_page.CalendarDatePage calendar_dates_get()



 Combines the election and reporting dates with Commission meetings, conferences, outreach, Advisory Opinions, rules, litigation dates and other events into one calendar.  State and report type filtering is no longer available.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DatesApi(api_client)
    page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
min_start_date = '2013-10-20' # date |  The minimum start date.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
description = ['description_example'] # [str] | Brief description of event (optional)
min_end_date = '2013-10-20' # date |  The minimum end date.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
event_id = 56 # int | An unique ID for an event. Useful for downloading a single event to your calendar. This ID is not a permanent, persistent ID. (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
max_end_date = '2013-10-20' # date |  The maximum end date.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
summary = ['summary_example'] # [str] | Longer description of event (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
calendar_category_id = [56] # [int] |  Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29  (optional)
sort = '-start_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of '-start_date'
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
max_start_date = '2013-10-20' # date |  The maximum start date.(MM/DD/YYYY or YYYY-MM-DD)  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.calendar_dates_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DatesApi->calendar_dates_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.calendar_dates_get(page=page, min_start_date=min_start_date, description=description, min_end_date=min_end_date, event_id=event_id, sort_null_only=sort_null_only, max_end_date=max_end_date, sort_nulls_last=sort_nulls_last, summary=summary, per_page=per_page, calendar_category_id=calendar_category_id, sort=sort, sort_hide_null=sort_hide_null, max_start_date=max_start_date)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DatesApi->calendar_dates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **min_start_date** | **date**|  The minimum start date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **description** | **[str]**| Brief description of event | [optional]
 **min_end_date** | **date**|  The minimum end date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **event_id** | **int**| An unique ID for an event. Useful for downloading a single event to your calendar. This ID is not a permanent, persistent ID. | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **max_end_date** | **date**|  The maximum end date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **summary** | **[str]**| Longer description of event | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **calendar_category_id** | **[int]**|  Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29  | [optional]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of '-start_date'
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **max_start_date** | **date**|  The maximum start date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional]

### Return type

[**calendar_date_page.CalendarDatePage**](CalendarDatePage.md)

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

# **election_dates_get**
> inline_response_default.InlineResponseDefault election_dates_get()



 FEC election dates since 1995.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DatesApi(api_client)
    election_type_id = ['election_type_id_example'] # [str] |  Election type id  (optional)
page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
election_state = ['election_state_example'] # [str] |  State or territory of the office sought.  (optional)
election_party = ['election_party_example'] # [str] |  Party, if applicable.  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
office_sought = ['office_sought_example'] # [str] |  House, Senate or presidential office.  (optional)
election_year = ['election_year_example'] # [str] | Year of election (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
max_update_date = '2013-10-20' # date |  The maximum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
min_update_date = '2013-10-20' # date |  The minimum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
sort = '-election_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of '-election_date'
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
max_primary_general_date = '2013-10-20' # date |  The maximum date of primary or general election.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
max_create_date = '2013-10-20' # date |  The maximum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
election_district = ['election_district_example'] # [str] |  House district of the office sought, if applicable.  (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
min_primary_general_date = '2013-10-20' # date |  The minimum date of primary or general election.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
min_election_date = '2013-10-20' # date |  The minimum date of election.  (optional)
min_create_date = '2013-10-20' # date |  The minimum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
max_election_date = '2013-10-20' # date |  The maximum date of election.  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.election_dates_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DatesApi->election_dates_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.election_dates_get(election_type_id=election_type_id, page=page, election_state=election_state, election_party=election_party, sort_nulls_last=sort_nulls_last, office_sought=office_sought, election_year=election_year, per_page=per_page, max_update_date=max_update_date, min_update_date=min_update_date, sort=sort, sort_hide_null=sort_hide_null, max_primary_general_date=max_primary_general_date, max_create_date=max_create_date, election_district=election_district, sort_null_only=sort_null_only, min_primary_general_date=min_primary_general_date, min_election_date=min_election_date, min_create_date=min_create_date, max_election_date=max_election_date)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DatesApi->election_dates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **election_type_id** | **[str]**|  Election type id  | [optional]
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **election_state** | **[str]**|  State or territory of the office sought.  | [optional]
 **election_party** | **[str]**|  Party, if applicable.  | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **office_sought** | **[str]**|  House, Senate or presidential office.  | [optional]
 **election_year** | **[str]**| Year of election | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **max_update_date** | **date**|  The maximum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **min_update_date** | **date**|  The minimum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of '-election_date'
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **max_primary_general_date** | **date**|  The maximum date of primary or general election.(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **max_create_date** | **date**|  The maximum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **election_district** | **[str]**|  House district of the office sought, if applicable.  | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **min_primary_general_date** | **date**|  The minimum date of primary or general election.(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **min_election_date** | **date**|  The minimum date of election.  | [optional]
 **min_create_date** | **date**|  The minimum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **max_election_date** | **date**|  The maximum date of election.  | [optional]

### Return type

[**inline_response_default.InlineResponseDefault**](InlineResponseDefault.md)

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

# **reporting_dates_get**
> inline_response_default2.InlineResponseDefault2 reporting_dates_get()



 FEC election dates since 1995.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyQueryAuth):
* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import openapi_client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'X-Api-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: ApiKeyQueryAuth
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: apiKey
configuration = openapi_client.Configuration(
    host = "http://localhost/v1",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DatesApi(api_client)
    page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
min_due_date = '2013-10-20' # date |  The minimum date the report is due.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
max_due_date = '2013-10-20' # date |  The maximum date the report is due.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
max_update_date = '2013-10-20' # date |  The maximum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
report_year = [56] # [int] |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  (optional)
min_update_date = '2013-10-20' # date |  The minimum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
sort = '-due_date' # str | Provide a field to sort by. Use `-` for descending order.  (optional) if omitted the server will use the default value of '-due_date'
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
min_create_date = '2013-10-20' # date |  The minimum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
max_create_date = '2013-10-20' # date |  The maximum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  (optional)
report_type = ['report_type_example'] # [str] | Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.reporting_dates_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DatesApi->reporting_dates_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.reporting_dates_get(page=page, min_due_date=min_due_date, max_due_date=max_due_date, sort_null_only=sort_null_only, sort_nulls_last=sort_nulls_last, per_page=per_page, max_update_date=max_update_date, report_year=report_year, min_update_date=min_update_date, sort=sort, sort_hide_null=sort_hide_null, min_create_date=min_create_date, max_create_date=max_create_date, report_type=report_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DatesApi->reporting_dates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **min_due_date** | **date**|  The minimum date the report is due.(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **max_due_date** | **date**|  The maximum date the report is due.(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **max_update_date** | **date**|  The maximum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **report_year** | **[int]**|  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional]
 **min_update_date** | **date**|  The minimum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **sort** | **str**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] if omitted the server will use the default value of '-due_date'
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **min_create_date** | **date**|  The minimum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **max_create_date** | **date**|  The maximum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **report_type** | **[str]**| Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  | [optional]

### Return type

[**inline_response_default2.InlineResponseDefault2**](InlineResponseDefault2.md)

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
