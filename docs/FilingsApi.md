# openfec_sdk.FilingsApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**candidate_candidate_id_filings_get**](FilingsApi.md#candidate_candidate_id_filings_get) | **GET** /candidate/{candidate_id}/filings/ |
[**committee_committee_id_filings_get**](FilingsApi.md#committee_committee_id_filings_get) | **GET** /committee/{committee_id}/filings/ |
[**filings_get**](FilingsApi.md#filings_get) | **GET** /filings/ |
[**operations_log_get**](FilingsApi.md#operations_log_get) | **GET** /operations-log/ |


# **candidate_candidate_id_filings_get**
> filings_page.FilingsPage candidate_candidate_id_filings_get(candidate_id)



 All official records and reports filed by or delivered to the FEC.  Note: because the filings data includes many records, counts for large result sets are approximate; you will want to page through the records until no records are returned.

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
    api_instance = openfec_sdk.FilingsApi(api_client)
    candidate_id = 'candidate_id_example' # str |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.
    page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
form_type = ['form_type_example'] # [str] | The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  (optional)
amendment_indicator = ['amendment_indicator_example'] # [str] | Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment.  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
filer_type = 'filer_type_example' # str | The method used to file with the FEC, either electronic or on paper. (optional)
most_recent = True # bool |  Report is either new or is the most-recently filed amendment  (optional)
sort = ["-receipt_date"] # [str], none_type | Provide a field to sort by. Use - for descending order. (optional) if omitted the server will use the default value of ["-receipt_date"]
office = ['office_example'] # [str] | Federal office candidate runs for: H, S or P (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
cycle = [56] # [int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
report_year = [56] # [int] |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  (optional)
form_category = ['form_category_example'] # [str] |  The forms filed are categorized based on the nature of the filing:     - REPORT F3, F3X, F3P, F3L, F4, F5, F7, F13     - NOTICE F5, F24, F6, F9, F10, F11     - STATEMENT F1, F2     - OTHER F1M, F8, F99, F12, FRQ  (optional)
min_receipt_date = '2013-10-20' # date |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
is_amended = True # bool |  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  (optional)
party = ['party_example'] # [str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
committee_type = 'committee_type_example' # str | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
district = ['district_example'] # [str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
document_type = ['document_type_example'] # [str] |  The type of document for documents other than reports:     - 2 24 Hour Contribution Notice     - 4 48 Hour Contribution Notice     - A Debt Settlement Statement     - B Acknowledgment of Receipt of Debt Settlement Statement     - C RFAI: Debt Settlement First Notice     - D Commission Debt Settlement Review     - E Commission Response TO Debt Settlement Request     - F Administrative Termination     - G Debt Settlement Plan Amendment     - H Disavowal Notice     - I Disavowal Response     - J Conduit Report     - K Termination Approval     - L Repeat Non-Filer Notice     - M Filing Frequency Change Notice     - N Paper Amendment to Electronic Report     - O Acknowledgment of Filing Frequency Change     - S RFAI: Debt Settlement Second     - T Miscellaneous Report TO FEC     - V Repeat Violation Notice (441A OR 441B)     - P Notice of Paper Filing     - R F3L Filing Frequency Change Notice     - Q Acknowledgment of F3L Filing Frequency Change     - U Unregistered Committee Notice  (optional)
state = ['state_example'] # [str] | US state or territory where a candidate runs for office (optional)
request_type = ['request_type_example'] # [str] | Requests for additional information (RFAIs) sent to filers. The request type is based on the type of document filed:     - 1 Statement of Organization     - 2 Report of Receipts and Expenditures (Form 3 and 3X)     - 3 Second Notice - Reports     - 4 Request for Additional Information     - 5 Informational - Reports     - 6 Second Notice - Statement of Organization     - 7 Failure to File     - 8 From Public Disclosure     - 9 From Multi Candidate Status  (optional)
beginning_image_number = ['beginning_image_number_example'] # [str] |  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  (optional)
primary_general_indicator = ['primary_general_indicator_example'] # [str] |  Primary, general or special election indicator.  (optional)
file_number = [56] # [int] | Filing ID number (optional)
max_receipt_date = '2013-10-20' # date |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
report_type = ['report_type_example'] # [str] | Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.candidate_candidate_id_filings_get(candidate_id)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling FilingsApi->candidate_candidate_id_filings_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.candidate_candidate_id_filings_get(candidate_id, page=page, sort_nulls_last=sort_nulls_last, form_type=form_type, amendment_indicator=amendment_indicator, per_page=per_page, filer_type=filer_type, most_recent=most_recent, sort=sort, office=office, sort_hide_null=sort_hide_null, cycle=cycle, report_year=report_year, form_category=form_category, min_receipt_date=min_receipt_date, is_amended=is_amended, party=party, committee_type=committee_type, sort_null_only=sort_null_only, district=district, document_type=document_type, state=state, request_type=request_type, beginning_image_number=beginning_image_number, primary_general_indicator=primary_general_indicator, file_number=file_number, max_receipt_date=max_receipt_date, report_type=report_type)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling FilingsApi->candidate_candidate_id_filings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **candidate_id** | **str**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  |
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **form_type** | **[str]**| The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  | [optional]
 **amendment_indicator** | **[str]**| Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment.  | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **filer_type** | **str**| The method used to file with the FEC, either electronic or on paper. | [optional]
 **most_recent** | **bool**|  Report is either new or is the most-recently filed amendment  | [optional]
 **sort** | **[str], none_type**| Provide a field to sort by. Use - for descending order. | [optional] if omitted the server will use the default value of ["-receipt_date"]
 **office** | **[str]**| Federal office candidate runs for: H, S or P | [optional]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **cycle** | **[int]**|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional]
 **report_year** | **[int]**|  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional]
 **form_category** | **[str]**|  The forms filed are categorized based on the nature of the filing:     - REPORT F3, F3X, F3P, F3L, F4, F5, F7, F13     - NOTICE F5, F24, F6, F9, F10, F11     - STATEMENT F1, F2     - OTHER F1M, F8, F99, F12, FRQ  | [optional]
 **min_receipt_date** | **date**|  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **is_amended** | **bool**|  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  | [optional]
 **party** | **[str]**| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional]
 **committee_type** | **str**| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **district** | **[str]**| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional]
 **document_type** | **[str]**|  The type of document for documents other than reports:     - 2 24 Hour Contribution Notice     - 4 48 Hour Contribution Notice     - A Debt Settlement Statement     - B Acknowledgment of Receipt of Debt Settlement Statement     - C RFAI: Debt Settlement First Notice     - D Commission Debt Settlement Review     - E Commission Response TO Debt Settlement Request     - F Administrative Termination     - G Debt Settlement Plan Amendment     - H Disavowal Notice     - I Disavowal Response     - J Conduit Report     - K Termination Approval     - L Repeat Non-Filer Notice     - M Filing Frequency Change Notice     - N Paper Amendment to Electronic Report     - O Acknowledgment of Filing Frequency Change     - S RFAI: Debt Settlement Second     - T Miscellaneous Report TO FEC     - V Repeat Violation Notice (441A OR 441B)     - P Notice of Paper Filing     - R F3L Filing Frequency Change Notice     - Q Acknowledgment of F3L Filing Frequency Change     - U Unregistered Committee Notice  | [optional]
 **state** | **[str]**| US state or territory where a candidate runs for office | [optional]
 **request_type** | **[str]**| Requests for additional information (RFAIs) sent to filers. The request type is based on the type of document filed:     - 1 Statement of Organization     - 2 Report of Receipts and Expenditures (Form 3 and 3X)     - 3 Second Notice - Reports     - 4 Request for Additional Information     - 5 Informational - Reports     - 6 Second Notice - Statement of Organization     - 7 Failure to File     - 8 From Public Disclosure     - 9 From Multi Candidate Status  | [optional]
 **beginning_image_number** | **[str]**|  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  | [optional]
 **primary_general_indicator** | **[str]**|  Primary, general or special election indicator.  | [optional]
 **file_number** | **[int]**| Filing ID number | [optional]
 **max_receipt_date** | **date**|  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **report_type** | **[str]**| Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  | [optional]

### Return type

[**filings_page.FilingsPage**](FilingsPage.md)

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

# **committee_committee_id_filings_get**
> filings_page.FilingsPage committee_committee_id_filings_get(committee_id)



 All official records and reports filed by or delivered to the FEC.  Note: because the filings data includes many records, counts for large result sets are approximate; you will want to page through the records until no records are returned.

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
    api_instance = openfec_sdk.FilingsApi(api_client)
    committee_id = 'committee_id_example' # str |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.
    page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
form_type = ['form_type_example'] # [str] | The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  (optional)
amendment_indicator = ['amendment_indicator_example'] # [str] | Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment.  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
filer_type = 'filer_type_example' # str | The method used to file with the FEC, either electronic or on paper. (optional)
most_recent = True # bool |  Report is either new or is the most-recently filed amendment  (optional)
sort = ["-receipt_date"] # [str], none_type | Provide a field to sort by. Use - for descending order. (optional) if omitted the server will use the default value of ["-receipt_date"]
office = ['office_example'] # [str] | Federal office candidate runs for: H, S or P (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
cycle = [56] # [int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
report_year = [56] # [int] |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  (optional)
form_category = ['form_category_example'] # [str] |  The forms filed are categorized based on the nature of the filing:     - REPORT F3, F3X, F3P, F3L, F4, F5, F7, F13     - NOTICE F5, F24, F6, F9, F10, F11     - STATEMENT F1, F2     - OTHER F1M, F8, F99, F12, FRQ  (optional)
min_receipt_date = '2013-10-20' # date |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
is_amended = True # bool |  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  (optional)
party = ['party_example'] # [str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
committee_type = 'committee_type_example' # str | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
district = ['district_example'] # [str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
document_type = ['document_type_example'] # [str] |  The type of document for documents other than reports:     - 2 24 Hour Contribution Notice     - 4 48 Hour Contribution Notice     - A Debt Settlement Statement     - B Acknowledgment of Receipt of Debt Settlement Statement     - C RFAI: Debt Settlement First Notice     - D Commission Debt Settlement Review     - E Commission Response TO Debt Settlement Request     - F Administrative Termination     - G Debt Settlement Plan Amendment     - H Disavowal Notice     - I Disavowal Response     - J Conduit Report     - K Termination Approval     - L Repeat Non-Filer Notice     - M Filing Frequency Change Notice     - N Paper Amendment to Electronic Report     - O Acknowledgment of Filing Frequency Change     - S RFAI: Debt Settlement Second     - T Miscellaneous Report TO FEC     - V Repeat Violation Notice (441A OR 441B)     - P Notice of Paper Filing     - R F3L Filing Frequency Change Notice     - Q Acknowledgment of F3L Filing Frequency Change     - U Unregistered Committee Notice  (optional)
state = ['state_example'] # [str] | US state or territory where a candidate runs for office (optional)
request_type = ['request_type_example'] # [str] | Requests for additional information (RFAIs) sent to filers. The request type is based on the type of document filed:     - 1 Statement of Organization     - 2 Report of Receipts and Expenditures (Form 3 and 3X)     - 3 Second Notice - Reports     - 4 Request for Additional Information     - 5 Informational - Reports     - 6 Second Notice - Statement of Organization     - 7 Failure to File     - 8 From Public Disclosure     - 9 From Multi Candidate Status  (optional)
beginning_image_number = ['beginning_image_number_example'] # [str] |  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  (optional)
primary_general_indicator = ['primary_general_indicator_example'] # [str] |  Primary, general or special election indicator.  (optional)
file_number = [56] # [int] | Filing ID number (optional)
max_receipt_date = '2013-10-20' # date |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
report_type = ['report_type_example'] # [str] | Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.committee_committee_id_filings_get(committee_id)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling FilingsApi->committee_committee_id_filings_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.committee_committee_id_filings_get(committee_id, page=page, sort_nulls_last=sort_nulls_last, form_type=form_type, amendment_indicator=amendment_indicator, per_page=per_page, filer_type=filer_type, most_recent=most_recent, sort=sort, office=office, sort_hide_null=sort_hide_null, cycle=cycle, report_year=report_year, form_category=form_category, min_receipt_date=min_receipt_date, is_amended=is_amended, party=party, committee_type=committee_type, sort_null_only=sort_null_only, district=district, document_type=document_type, state=state, request_type=request_type, beginning_image_number=beginning_image_number, primary_general_indicator=primary_general_indicator, file_number=file_number, max_receipt_date=max_receipt_date, report_type=report_type)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling FilingsApi->committee_committee_id_filings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **committee_id** | **str**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  |
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **form_type** | **[str]**| The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  | [optional]
 **amendment_indicator** | **[str]**| Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment.  | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **filer_type** | **str**| The method used to file with the FEC, either electronic or on paper. | [optional]
 **most_recent** | **bool**|  Report is either new or is the most-recently filed amendment  | [optional]
 **sort** | **[str], none_type**| Provide a field to sort by. Use - for descending order. | [optional] if omitted the server will use the default value of ["-receipt_date"]
 **office** | **[str]**| Federal office candidate runs for: H, S or P | [optional]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **cycle** | **[int]**|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional]
 **report_year** | **[int]**|  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional]
 **form_category** | **[str]**|  The forms filed are categorized based on the nature of the filing:     - REPORT F3, F3X, F3P, F3L, F4, F5, F7, F13     - NOTICE F5, F24, F6, F9, F10, F11     - STATEMENT F1, F2     - OTHER F1M, F8, F99, F12, FRQ  | [optional]
 **min_receipt_date** | **date**|  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **is_amended** | **bool**|  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  | [optional]
 **party** | **[str]**| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional]
 **committee_type** | **str**| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **district** | **[str]**| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional]
 **document_type** | **[str]**|  The type of document for documents other than reports:     - 2 24 Hour Contribution Notice     - 4 48 Hour Contribution Notice     - A Debt Settlement Statement     - B Acknowledgment of Receipt of Debt Settlement Statement     - C RFAI: Debt Settlement First Notice     - D Commission Debt Settlement Review     - E Commission Response TO Debt Settlement Request     - F Administrative Termination     - G Debt Settlement Plan Amendment     - H Disavowal Notice     - I Disavowal Response     - J Conduit Report     - K Termination Approval     - L Repeat Non-Filer Notice     - M Filing Frequency Change Notice     - N Paper Amendment to Electronic Report     - O Acknowledgment of Filing Frequency Change     - S RFAI: Debt Settlement Second     - T Miscellaneous Report TO FEC     - V Repeat Violation Notice (441A OR 441B)     - P Notice of Paper Filing     - R F3L Filing Frequency Change Notice     - Q Acknowledgment of F3L Filing Frequency Change     - U Unregistered Committee Notice  | [optional]
 **state** | **[str]**| US state or territory where a candidate runs for office | [optional]
 **request_type** | **[str]**| Requests for additional information (RFAIs) sent to filers. The request type is based on the type of document filed:     - 1 Statement of Organization     - 2 Report of Receipts and Expenditures (Form 3 and 3X)     - 3 Second Notice - Reports     - 4 Request for Additional Information     - 5 Informational - Reports     - 6 Second Notice - Statement of Organization     - 7 Failure to File     - 8 From Public Disclosure     - 9 From Multi Candidate Status  | [optional]
 **beginning_image_number** | **[str]**|  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  | [optional]
 **primary_general_indicator** | **[str]**|  Primary, general or special election indicator.  | [optional]
 **file_number** | **[int]**| Filing ID number | [optional]
 **max_receipt_date** | **date**|  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **report_type** | **[str]**| Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  | [optional]

### Return type

[**filings_page.FilingsPage**](FilingsPage.md)

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

# **filings_get**
> filings_page.FilingsPage filings_get()



 All official records and reports filed by or delivered to the FEC.  Note: because the filings data includes many records, counts for large result sets are approximate; you will want to page through the records until no records are returned.

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
    api_instance = openfec_sdk.FilingsApi(api_client)
    page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
committee_id = ['committee_id_example'] # [str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
form_type = ['form_type_example'] # [str] | The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  (optional)
amendment_indicator = ['amendment_indicator_example'] # [str] | Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment.  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
filer_type = 'filer_type_example' # str | The method used to file with the FEC, either electronic or on paper. (optional)
most_recent = True # bool |  Report is either new or is the most-recently filed amendment  (optional)
sort = ["-receipt_date"] # [str], none_type | Provide a field to sort by. Use - for descending order. (optional) if omitted the server will use the default value of ["-receipt_date"]
office = ['office_example'] # [str] | Federal office candidate runs for: H, S or P (optional)
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
candidate_id = ['candidate_id_example'] # [str] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  (optional)
cycle = [56] # [int] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  (optional)
report_year = [56] # [int] |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  (optional)
form_category = ['form_category_example'] # [str] |  The forms filed are categorized based on the nature of the filing:     - REPORT F3, F3X, F3P, F3L, F4, F5, F7, F13     - NOTICE F5, F24, F6, F9, F10, F11     - STATEMENT F1, F2     - OTHER F1M, F8, F99, F12, FRQ  (optional)
min_receipt_date = '2013-10-20' # date |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
is_amended = True # bool |  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  (optional)
party = ['party_example'] # [str] | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. (optional)
committee_type = 'committee_type_example' # str | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
district = ['district_example'] # [str] | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. (optional)
document_type = ['document_type_example'] # [str] |  The type of document for documents other than reports:     - 2 24 Hour Contribution Notice     - 4 48 Hour Contribution Notice     - A Debt Settlement Statement     - B Acknowledgment of Receipt of Debt Settlement Statement     - C RFAI: Debt Settlement First Notice     - D Commission Debt Settlement Review     - E Commission Response TO Debt Settlement Request     - F Administrative Termination     - G Debt Settlement Plan Amendment     - H Disavowal Notice     - I Disavowal Response     - J Conduit Report     - K Termination Approval     - L Repeat Non-Filer Notice     - M Filing Frequency Change Notice     - N Paper Amendment to Electronic Report     - O Acknowledgment of Filing Frequency Change     - S RFAI: Debt Settlement Second     - T Miscellaneous Report TO FEC     - V Repeat Violation Notice (441A OR 441B)     - P Notice of Paper Filing     - R F3L Filing Frequency Change Notice     - Q Acknowledgment of F3L Filing Frequency Change     - U Unregistered Committee Notice  (optional)
state = ['state_example'] # [str] | US state or territory where a candidate runs for office (optional)
request_type = ['request_type_example'] # [str] | Requests for additional information (RFAIs) sent to filers. The request type is based on the type of document filed:     - 1 Statement of Organization     - 2 Report of Receipts and Expenditures (Form 3 and 3X)     - 3 Second Notice - Reports     - 4 Request for Additional Information     - 5 Informational - Reports     - 6 Second Notice - Statement of Organization     - 7 Failure to File     - 8 From Public Disclosure     - 9 From Multi Candidate Status  (optional)
beginning_image_number = ['beginning_image_number_example'] # [str] |  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  (optional)
primary_general_indicator = ['primary_general_indicator_example'] # [str] |  Primary, general or special election indicator.  (optional)
file_number = [56] # [int] | Filing ID number (optional)
max_receipt_date = '2013-10-20' # date |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
report_type = ['report_type_example'] # [str] | Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.filings_get()
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling FilingsApi->filings_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.filings_get(page=page, committee_id=committee_id, sort_nulls_last=sort_nulls_last, form_type=form_type, amendment_indicator=amendment_indicator, per_page=per_page, filer_type=filer_type, most_recent=most_recent, sort=sort, office=office, sort_hide_null=sort_hide_null, candidate_id=candidate_id, cycle=cycle, report_year=report_year, form_category=form_category, min_receipt_date=min_receipt_date, is_amended=is_amended, party=party, committee_type=committee_type, sort_null_only=sort_null_only, district=district, document_type=document_type, state=state, request_type=request_type, beginning_image_number=beginning_image_number, primary_general_indicator=primary_general_indicator, file_number=file_number, max_receipt_date=max_receipt_date, report_type=report_type)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling FilingsApi->filings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **committee_id** | **[str]**|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **form_type** | **[str]**| The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  | [optional]
 **amendment_indicator** | **[str]**| Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment.  | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **filer_type** | **str**| The method used to file with the FEC, either electronic or on paper. | [optional]
 **most_recent** | **bool**|  Report is either new or is the most-recently filed amendment  | [optional]
 **sort** | **[str], none_type**| Provide a field to sort by. Use - for descending order. | [optional] if omitted the server will use the default value of ["-receipt_date"]
 **office** | **[str]**| Federal office candidate runs for: H, S or P | [optional]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **candidate_id** | **[str]**|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional]
 **cycle** | **[int]**|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional]
 **report_year** | **[int]**|  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional]
 **form_category** | **[str]**|  The forms filed are categorized based on the nature of the filing:     - REPORT F3, F3X, F3P, F3L, F4, F5, F7, F13     - NOTICE F5, F24, F6, F9, F10, F11     - STATEMENT F1, F2     - OTHER F1M, F8, F99, F12, FRQ  | [optional]
 **min_receipt_date** | **date**|  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **is_amended** | **bool**|  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  | [optional]
 **party** | **[str]**| Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional]
 **committee_type** | **str**| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **district** | **[str]**| Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional]
 **document_type** | **[str]**|  The type of document for documents other than reports:     - 2 24 Hour Contribution Notice     - 4 48 Hour Contribution Notice     - A Debt Settlement Statement     - B Acknowledgment of Receipt of Debt Settlement Statement     - C RFAI: Debt Settlement First Notice     - D Commission Debt Settlement Review     - E Commission Response TO Debt Settlement Request     - F Administrative Termination     - G Debt Settlement Plan Amendment     - H Disavowal Notice     - I Disavowal Response     - J Conduit Report     - K Termination Approval     - L Repeat Non-Filer Notice     - M Filing Frequency Change Notice     - N Paper Amendment to Electronic Report     - O Acknowledgment of Filing Frequency Change     - S RFAI: Debt Settlement Second     - T Miscellaneous Report TO FEC     - V Repeat Violation Notice (441A OR 441B)     - P Notice of Paper Filing     - R F3L Filing Frequency Change Notice     - Q Acknowledgment of F3L Filing Frequency Change     - U Unregistered Committee Notice  | [optional]
 **state** | **[str]**| US state or territory where a candidate runs for office | [optional]
 **request_type** | **[str]**| Requests for additional information (RFAIs) sent to filers. The request type is based on the type of document filed:     - 1 Statement of Organization     - 2 Report of Receipts and Expenditures (Form 3 and 3X)     - 3 Second Notice - Reports     - 4 Request for Additional Information     - 5 Informational - Reports     - 6 Second Notice - Statement of Organization     - 7 Failure to File     - 8 From Public Disclosure     - 9 From Multi Candidate Status  | [optional]
 **beginning_image_number** | **[str]**|  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  | [optional]
 **primary_general_indicator** | **[str]**|  Primary, general or special election indicator.  | [optional]
 **file_number** | **[int]**| Filing ID number | [optional]
 **max_receipt_date** | **date**|  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **report_type** | **[str]**| Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  | [optional]

### Return type

[**filings_page.FilingsPage**](FilingsPage.md)

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

# **operations_log_get**
> operations_log_page.OperationsLogPage operations_log_get()



 The Operations log contains details of each report loaded into the database. It is primarily used as status check to determine when all of the data processes, from initial entry through review are complete.

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
    api_instance = openfec_sdk.FilingsApi(api_client)
    page = 1 # int | For paginating through results, starting at page 1 (optional) if omitted the server will use the default value of 1
max_transaction_data_complete_date = '2013-10-20' # date |  Select all filings processed completely before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
sort_nulls_last = False # bool | Toggle that sorts null values last (optional) if omitted the server will use the default value of False
form_type = ['form_type_example'] # [str] | The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  (optional)
amendment_indicator = ['amendment_indicator_example'] # [str] | Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment.  (optional)
per_page = 20 # int | The number of results returned per page. Defaults to 20. (optional) if omitted the server will use the default value of 20
max_coverage_end_date = '2013-10-20' # date |  Ending date of the reporting period before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
sort = ["-report_year"] # [str], none_type | Provide a field to sort by. Use - for descending order. (optional) if omitted the server will use the default value of ["-report_year"]
sort_hide_null = False # bool | Hide null values on sorted column(s). (optional) if omitted the server will use the default value of False
report_year = [56] # [int] |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  (optional)
candidate_committee_id = ['candidate_committee_id_example'] # [str] |  A unique identifier of the registered filer.  (optional)
min_coverage_end_date = '2013-10-20' # date |  Ending date of the reporting period after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
min_receipt_date = '2013-10-20' # date |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
sort_null_only = False # bool | Toggle that filters out all rows having sort column that is non-null (optional) if omitted the server will use the default value of False
beginning_image_number = ['beginning_image_number_example'] # [str] |  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  (optional)
status_num = ['status_num_example'] # [str] |  Status of the transactional report.     -0- Transaction is entered            into the system.           But not verified.     -1- Transaction is verified.  (optional)
min_transaction_data_complete_date = '2013-10-20' # date |  Select all filings processed completely after this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
max_receipt_date = '2013-10-20' # date |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  (optional)
report_type = ['report_type_example'] # [str] | Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.operations_log_get()
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling FilingsApi->operations_log_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.operations_log_get(page=page, max_transaction_data_complete_date=max_transaction_data_complete_date, sort_nulls_last=sort_nulls_last, form_type=form_type, amendment_indicator=amendment_indicator, per_page=per_page, max_coverage_end_date=max_coverage_end_date, sort=sort, sort_hide_null=sort_hide_null, report_year=report_year, candidate_committee_id=candidate_committee_id, min_coverage_end_date=min_coverage_end_date, min_receipt_date=min_receipt_date, sort_null_only=sort_null_only, beginning_image_number=beginning_image_number, status_num=status_num, min_transaction_data_complete_date=min_transaction_data_complete_date, max_receipt_date=max_receipt_date, report_type=report_type)
        pprint(api_response)
    except openfec_sdk.ApiException as e:
        print("Exception when calling FilingsApi->operations_log_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | defaults to 'DEMO_KEY'
 **page** | **int**| For paginating through results, starting at page 1 | [optional] if omitted the server will use the default value of 1
 **max_transaction_data_complete_date** | **date**|  Select all filings processed completely before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **sort_nulls_last** | **bool**| Toggle that sorts null values last | [optional] if omitted the server will use the default value of False
 **form_type** | **[str]**| The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information  | [optional]
 **amendment_indicator** | **[str]**| Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment.  | [optional]
 **per_page** | **int**| The number of results returned per page. Defaults to 20. | [optional] if omitted the server will use the default value of 20
 **max_coverage_end_date** | **date**|  Ending date of the reporting period before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **sort** | **[str], none_type**| Provide a field to sort by. Use - for descending order. | [optional] if omitted the server will use the default value of ["-report_year"]
 **sort_hide_null** | **bool**| Hide null values on sorted column(s). | [optional] if omitted the server will use the default value of False
 **report_year** | **[int]**|  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional]
 **candidate_committee_id** | **[str]**|  A unique identifier of the registered filer.  | [optional]
 **min_coverage_end_date** | **date**|  Ending date of the reporting period after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **min_receipt_date** | **date**|  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **sort_null_only** | **bool**| Toggle that filters out all rows having sort column that is non-null | [optional] if omitted the server will use the default value of False
 **beginning_image_number** | **[str]**|  Unique identifier for the electronic or paper report. This number is used to construct PDF URLs to the original document.  | [optional]
 **status_num** | **[str]**|  Status of the transactional report.     -0- Transaction is entered            into the system.           But not verified.     -1- Transaction is verified.  | [optional]
 **min_transaction_data_complete_date** | **date**|  Select all filings processed completely after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **max_receipt_date** | **date**|  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional]
 **report_type** | **[str]**| Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  | [optional]

### Return type

[**operations_log_page.OperationsLogPage**](OperationsLogPage.md)

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
