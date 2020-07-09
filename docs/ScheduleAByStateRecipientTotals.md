# schedule_a_by_state_recipient_totals.ScheduleAByStateRecipientTotals

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**committee_type** | **str, none_type** | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional]
**committee_type_full** | **str, none_type** | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional]
**count** | **int, none_type** | Number of records making up the total. | [optional]
**cycle** | **int, none_type** |  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  | [optional]
**state** | **str, none_type** | US state or territory | [optional]
**state_full** | **str, none_type** | US state or territory | [optional]
**total** | **float, none_type** | The calculated total. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
