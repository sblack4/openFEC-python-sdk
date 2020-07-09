# calendar_date.CalendarDate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_day** | **bool, none_type** |  | [optional]
**calendar_category_id** | **int, none_type** |  Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29  | [optional]
**category** | **str, none_type** |  Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29  | [optional]
**description** | **str** |  | [optional]
**end_date** | **str** |  | [optional]
**event_id** | **int** | An unique ID for an event. Useful for downloading a single event to your calendar. This ID is not a permanent, persistent ID. | [optional]
**location** | **str, none_type** |  Can be state address or room.  | [optional]
**start_date** | **str** |  | [optional]
**state** | **[str], none_type** | The state field only applies to election dates and reporting deadlines, reporting periods and all other dates do not have the array of states to filter on | [optional]
**summary** | **str** |  | [optional]
**url** | **str, none_type** |  A url for that event  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
