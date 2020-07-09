# openfec_sdk.LegalApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**legal_search_get**](LegalApi.md#legal_search_get) | **GET** /legal/search/ |


# **legal_search_get**
> inline_response_default1.InlineResponseDefault1 legal_search_get()



 Search legal documents by type, or across all document types using keywords, parameter values and ranges.

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
    api_instance = openfec_sdk.LegalApi(api_client)
    case_no = ['case_no_example'] # [str] | Enforcement matter case number (optional)
af_min_rtb_date = '2013-10-20' # date | Filter cases by earliest Reason to Believe date (optional)
af_rtb_fine_amount = 56 # int | Filter cases by Reason to Believe fine amount (optional)
case_document_category = ['case_document_category_example'] # [str] | Filter cases by category of associated documents (optional)
case_election_cycles = 56 # int | Filter cases by election cycles (optional)
af_name = ['af_name_example'] # [str] | Admin fine committee name (optional)
hits_returned = 56 # int | Number of results to return (max 10). (optional)
case_min_close_date = '2013-10-20' # date | Filter cases by earliest date closed (optional)
type = 'type_example' # str | Document type to refine search by (optional)
case_min_open_date = '2013-10-20' # date | Filter cases by earliest date opened (optional)
ao_min_issue_date = '2013-10-20' # date | Earliest issue date of advisory opinion (optional)
ao_status = 'ao_status_example' # str | Status of AO (pending, withdrawn, or final) (optional)
af_max_fd_date = '2013-10-20' # date | Filter cases by latest Final Determination date (optional)
ao_requestor = 'ao_requestor_example' # str | The requestor of the advisory opinion (optional)
from_hit = 56 # int | Get results starting from this index. (optional)
af_min_fd_date = '2013-10-20' # date | Filter cases by earliest Final Determination date (optional)
ao_citation_require_all = True # bool | Require all citations to be in document (default behavior is any) (optional)
af_max_rtb_date = '2013-10-20' # date | Filter cases by latest Reason to Believe date (optional)
ao_max_request_date = '2013-10-20' # date | Latest request date of advisory opinion (optional)
af_committee_id = 'af_committee_id_example' # str | Admin fine committee ID (optional)
af_report_year = 'af_report_year_example' # str | Admin fine report year (optional)
case_dispositions = ['case_dispositions_example'] # [str] | Filter cases by dispositions (optional)
ao_no = ['ao_no_example'] # [str] | Force advisory opinion number (optional)
case_max_close_date = '2013-10-20' # date | Filter cases by latest date closed (optional)
ao_name = ['ao_name_example'] # [str] | Force advisory opinion name (optional)
af_fd_fine_amount = 56 # int | Filter cases by Final Determination fine amount (optional)
ao_regulatory_citation = ['ao_regulatory_citation_example'] # [str] | Search for regulatory citations (optional)
ao_category = ['ao_category_example'] # [str] | Category of the document (optional)
case_respondents = 'case_respondents_example' # str | Filter cases by respondents (optional)
case_max_open_date = '2013-10-20' # date | Filter cases by latest date opened (optional)
ao_is_pending = True # bool | AO is pending (optional)
ao_requestor_type = [56] # [int] | Code of the advisory opinion requestor type. (optional)
ao_statutory_citation = ['ao_statutory_citation_example'] # [str] | Search for statutory citations (optional)
ao_entity_name = ['ao_entity_name_example'] # [str] | Search by name of commenter or representative (optional)
q = 'q_example' # str | Text to search legal documents for. (optional)
ao_max_issue_date = '2013-10-20' # date | Latest issue date of advisory opinion (optional)
ao_min_request_date = '2013-10-20' # date | Earliest request date of advisory opinion (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.legal_search_get()
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling LegalApi->legal_search_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.legal_search_get(case_no=case_no, af_min_rtb_date=af_min_rtb_date, af_rtb_fine_amount=af_rtb_fine_amount, case_document_category=case_document_category, case_election_cycles=case_election_cycles, af_name=af_name, hits_returned=hits_returned, case_min_close_date=case_min_close_date, type=type, case_min_open_date=case_min_open_date, ao_min_issue_date=ao_min_issue_date, ao_status=ao_status, af_max_fd_date=af_max_fd_date, ao_requestor=ao_requestor, from_hit=from_hit, af_min_fd_date=af_min_fd_date, ao_citation_require_all=ao_citation_require_all, af_max_rtb_date=af_max_rtb_date, ao_max_request_date=ao_max_request_date, af_committee_id=af_committee_id, af_report_year=af_report_year, case_dispositions=case_dispositions, ao_no=ao_no, case_max_close_date=case_max_close_date, ao_name=ao_name, af_fd_fine_amount=af_fd_fine_amount, ao_regulatory_citation=ao_regulatory_citation, ao_category=ao_category, case_respondents=case_respondents, case_max_open_date=case_max_open_date, ao_is_pending=ao_is_pending, ao_requestor_type=ao_requestor_type, ao_statutory_citation=ao_statutory_citation, ao_entity_name=ao_entity_name, q=q, ao_max_issue_date=ao_max_issue_date, ao_min_request_date=ao_min_request_date)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling LegalApi->legal_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **case_no** | **[str]**| Enforcement matter case number | [optional]
 **af_min_rtb_date** | **date**| Filter cases by earliest Reason to Believe date | [optional]
 **af_rtb_fine_amount** | **int**| Filter cases by Reason to Believe fine amount | [optional]
 **case_document_category** | **[str]**| Filter cases by category of associated documents | [optional]
 **case_election_cycles** | **int**| Filter cases by election cycles | [optional]
 **af_name** | **[str]**| Admin fine committee name | [optional]
 **hits_returned** | **int**| Number of results to return (max 10). | [optional]
 **case_min_close_date** | **date**| Filter cases by earliest date closed | [optional]
 **type** | **str**| Document type to refine search by | [optional]
 **case_min_open_date** | **date**| Filter cases by earliest date opened | [optional]
 **ao_min_issue_date** | **date**| Earliest issue date of advisory opinion | [optional]
 **ao_status** | **str**| Status of AO (pending, withdrawn, or final) | [optional]
 **af_max_fd_date** | **date**| Filter cases by latest Final Determination date | [optional]
 **ao_requestor** | **str**| The requestor of the advisory opinion | [optional]
 **from_hit** | **int**| Get results starting from this index. | [optional]
 **af_min_fd_date** | **date**| Filter cases by earliest Final Determination date | [optional]
 **ao_citation_require_all** | **bool**| Require all citations to be in document (default behavior is any) | [optional]
 **af_max_rtb_date** | **date**| Filter cases by latest Reason to Believe date | [optional]
 **ao_max_request_date** | **date**| Latest request date of advisory opinion | [optional]
 **af_committee_id** | **str**| Admin fine committee ID | [optional]
 **af_report_year** | **str**| Admin fine report year | [optional]
 **case_dispositions** | **[str]**| Filter cases by dispositions | [optional]
 **ao_no** | **[str]**| Force advisory opinion number | [optional]
 **case_max_close_date** | **date**| Filter cases by latest date closed | [optional]
 **ao_name** | **[str]**| Force advisory opinion name | [optional]
 **af_fd_fine_amount** | **int**| Filter cases by Final Determination fine amount | [optional]
 **ao_regulatory_citation** | **[str]**| Search for regulatory citations | [optional]
 **ao_category** | **[str]**| Category of the document | [optional]
 **case_respondents** | **str**| Filter cases by respondents | [optional]
 **case_max_open_date** | **date**| Filter cases by latest date opened | [optional]
 **ao_is_pending** | **bool**| AO is pending | [optional]
 **ao_requestor_type** | **[int]**| Code of the advisory opinion requestor type. | [optional]
 **ao_statutory_citation** | **[str]**| Search for statutory citations | [optional]
 **ao_entity_name** | **[str]**| Search by name of commenter or representative | [optional]
 **q** | **str**| Text to search legal documents for. | [optional]
 **ao_max_issue_date** | **date**| Latest issue date of advisory opinion | [optional]
 **ao_min_request_date** | **date**| Earliest request date of advisory opinion | [optional]

### Return type

[**inline_response_default1.InlineResponseDefault1**](InlineResponseDefault1.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Legal search results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
