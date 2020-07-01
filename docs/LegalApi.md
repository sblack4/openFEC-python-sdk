# swagger_client.LegalApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**legal_search_get**](LegalApi.md#legal_search_get) | **GET** /legal/search/ | 


# **legal_search_get**
> InlineResponseDefault1 legal_search_get(api_key, case_dispositions=case_dispositions, ao_requestor_type=ao_requestor_type, af_report_year=af_report_year, ao_name=ao_name, case_min_open_date=case_min_open_date, ao_entity_name=ao_entity_name, q=q, case_respondents=case_respondents, ao_statutory_citation=ao_statutory_citation, ao_max_issue_date=ao_max_issue_date, af_max_rtb_date=af_max_rtb_date, case_election_cycles=case_election_cycles, case_document_category=case_document_category, type=type, case_max_open_date=case_max_open_date, af_name=af_name, ao_min_issue_date=ao_min_issue_date, af_fd_fine_amount=af_fd_fine_amount, af_rtb_fine_amount=af_rtb_fine_amount, af_max_fd_date=af_max_fd_date, ao_category=ao_category, ao_regulatory_citation=ao_regulatory_citation, ao_min_request_date=ao_min_request_date, af_min_rtb_date=af_min_rtb_date, case_max_close_date=case_max_close_date, ao_citation_require_all=ao_citation_require_all, case_min_close_date=case_min_close_date, ao_max_request_date=ao_max_request_date, from_hit=from_hit, af_committee_id=af_committee_id, ao_requestor=ao_requestor, ao_status=ao_status, ao_is_pending=ao_is_pending, case_no=case_no, af_min_fd_date=af_min_fd_date, ao_no=ao_no, hits_returned=hits_returned)



 Search legal documents by type, or across all document types using keywords, parameter values and ranges. 

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
api_instance = swagger_client.LegalApi(swagger_client.ApiClient(configuration))
api_key = 'DEMO_KEY' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
case_dispositions = ['case_dispositions_example'] # list[str] | Filter cases by dispositions (optional)
ao_requestor_type = [56] # list[int] | Code of the advisory opinion requestor type. (optional)
af_report_year = 'af_report_year_example' # str | Admin fine report year (optional)
ao_name = ['ao_name_example'] # list[str] | Force advisory opinion name (optional)
case_min_open_date = '2013-10-20' # date | Filter cases by earliest date opened (optional)
ao_entity_name = ['ao_entity_name_example'] # list[str] | Search by name of commenter or representative (optional)
q = 'q_example' # str | Text to search legal documents for. (optional)
case_respondents = 'case_respondents_example' # str | Filter cases by respondents (optional)
ao_statutory_citation = ['ao_statutory_citation_example'] # list[str] | Search for statutory citations (optional)
ao_max_issue_date = '2013-10-20' # date | Latest issue date of advisory opinion (optional)
af_max_rtb_date = '2013-10-20' # date | Filter cases by latest Reason to Believe date (optional)
case_election_cycles = 56 # int | Filter cases by election cycles (optional)
case_document_category = ['case_document_category_example'] # list[str] | Filter cases by category of associated documents (optional)
type = 'type_example' # str | Document type to refine search by (optional)
case_max_open_date = '2013-10-20' # date | Filter cases by latest date opened (optional)
af_name = ['af_name_example'] # list[str] | Admin fine committee name (optional)
ao_min_issue_date = '2013-10-20' # date | Earliest issue date of advisory opinion (optional)
af_fd_fine_amount = 56 # int | Filter cases by Final Determination fine amount (optional)
af_rtb_fine_amount = 56 # int | Filter cases by Reason to Believe fine amount (optional)
af_max_fd_date = '2013-10-20' # date | Filter cases by latest Final Determination date (optional)
ao_category = ['ao_category_example'] # list[str] | Category of the document (optional)
ao_regulatory_citation = ['ao_regulatory_citation_example'] # list[str] | Search for regulatory citations (optional)
ao_min_request_date = '2013-10-20' # date | Earliest request date of advisory opinion (optional)
af_min_rtb_date = '2013-10-20' # date | Filter cases by earliest Reason to Believe date (optional)
case_max_close_date = '2013-10-20' # date | Filter cases by latest date closed (optional)
ao_citation_require_all = true # bool | Require all citations to be in document (default behavior is any) (optional)
case_min_close_date = '2013-10-20' # date | Filter cases by earliest date closed (optional)
ao_max_request_date = '2013-10-20' # date | Latest request date of advisory opinion (optional)
from_hit = 56 # int | Get results starting from this index. (optional)
af_committee_id = 'af_committee_id_example' # str | Admin fine committee ID (optional)
ao_requestor = 'ao_requestor_example' # str | The requestor of the advisory opinion (optional)
ao_status = 'ao_status_example' # str | Status of AO (pending, withdrawn, or final) (optional)
ao_is_pending = true # bool | AO is pending (optional)
case_no = ['case_no_example'] # list[str] | Enforcement matter case number (optional)
af_min_fd_date = '2013-10-20' # date | Filter cases by earliest Final Determination date (optional)
ao_no = ['ao_no_example'] # list[str] | Force advisory opinion number (optional)
hits_returned = 56 # int | Number of results to return (max 10). (optional)

try:
    api_response = api_instance.legal_search_get(api_key, case_dispositions=case_dispositions, ao_requestor_type=ao_requestor_type, af_report_year=af_report_year, ao_name=ao_name, case_min_open_date=case_min_open_date, ao_entity_name=ao_entity_name, q=q, case_respondents=case_respondents, ao_statutory_citation=ao_statutory_citation, ao_max_issue_date=ao_max_issue_date, af_max_rtb_date=af_max_rtb_date, case_election_cycles=case_election_cycles, case_document_category=case_document_category, type=type, case_max_open_date=case_max_open_date, af_name=af_name, ao_min_issue_date=ao_min_issue_date, af_fd_fine_amount=af_fd_fine_amount, af_rtb_fine_amount=af_rtb_fine_amount, af_max_fd_date=af_max_fd_date, ao_category=ao_category, ao_regulatory_citation=ao_regulatory_citation, ao_min_request_date=ao_min_request_date, af_min_rtb_date=af_min_rtb_date, case_max_close_date=case_max_close_date, ao_citation_require_all=ao_citation_require_all, case_min_close_date=case_min_close_date, ao_max_request_date=ao_max_request_date, from_hit=from_hit, af_committee_id=af_committee_id, ao_requestor=ao_requestor, ao_status=ao_status, ao_is_pending=ao_is_pending, case_no=case_no, af_min_fd_date=af_min_fd_date, ao_no=ao_no, hits_returned=hits_returned)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegalApi->legal_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to DEMO_KEY]
 **case_dispositions** | [**list[str]**](str.md)| Filter cases by dispositions | [optional] 
 **ao_requestor_type** | [**list[int]**](int.md)| Code of the advisory opinion requestor type. | [optional] 
 **af_report_year** | **str**| Admin fine report year | [optional] 
 **ao_name** | [**list[str]**](str.md)| Force advisory opinion name | [optional] 
 **case_min_open_date** | **date**| Filter cases by earliest date opened | [optional] 
 **ao_entity_name** | [**list[str]**](str.md)| Search by name of commenter or representative | [optional] 
 **q** | **str**| Text to search legal documents for. | [optional] 
 **case_respondents** | **str**| Filter cases by respondents | [optional] 
 **ao_statutory_citation** | [**list[str]**](str.md)| Search for statutory citations | [optional] 
 **ao_max_issue_date** | **date**| Latest issue date of advisory opinion | [optional] 
 **af_max_rtb_date** | **date**| Filter cases by latest Reason to Believe date | [optional] 
 **case_election_cycles** | **int**| Filter cases by election cycles | [optional] 
 **case_document_category** | [**list[str]**](str.md)| Filter cases by category of associated documents | [optional] 
 **type** | **str**| Document type to refine search by | [optional] 
 **case_max_open_date** | **date**| Filter cases by latest date opened | [optional] 
 **af_name** | [**list[str]**](str.md)| Admin fine committee name | [optional] 
 **ao_min_issue_date** | **date**| Earliest issue date of advisory opinion | [optional] 
 **af_fd_fine_amount** | **int**| Filter cases by Final Determination fine amount | [optional] 
 **af_rtb_fine_amount** | **int**| Filter cases by Reason to Believe fine amount | [optional] 
 **af_max_fd_date** | **date**| Filter cases by latest Final Determination date | [optional] 
 **ao_category** | [**list[str]**](str.md)| Category of the document | [optional] 
 **ao_regulatory_citation** | [**list[str]**](str.md)| Search for regulatory citations | [optional] 
 **ao_min_request_date** | **date**| Earliest request date of advisory opinion | [optional] 
 **af_min_rtb_date** | **date**| Filter cases by earliest Reason to Believe date | [optional] 
 **case_max_close_date** | **date**| Filter cases by latest date closed | [optional] 
 **ao_citation_require_all** | **bool**| Require all citations to be in document (default behavior is any) | [optional] 
 **case_min_close_date** | **date**| Filter cases by earliest date closed | [optional] 
 **ao_max_request_date** | **date**| Latest request date of advisory opinion | [optional] 
 **from_hit** | **int**| Get results starting from this index. | [optional] 
 **af_committee_id** | **str**| Admin fine committee ID | [optional] 
 **ao_requestor** | **str**| The requestor of the advisory opinion | [optional] 
 **ao_status** | **str**| Status of AO (pending, withdrawn, or final) | [optional] 
 **ao_is_pending** | **bool**| AO is pending | [optional] 
 **case_no** | [**list[str]**](str.md)| Enforcement matter case number | [optional] 
 **af_min_fd_date** | **date**| Filter cases by earliest Final Determination date | [optional] 
 **ao_no** | [**list[str]**](str.md)| Force advisory opinion number | [optional] 
 **hits_returned** | **int**| Number of results to return (max 10). | [optional] 

### Return type

[**InlineResponseDefault1**](InlineResponseDefault1.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

