# schedule_b_by_recipient_id.ScheduleBByRecipientID

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**committee_id** | **str** |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  |
**cycle** | **int** |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  |
**recipient_id** | **str** | The FEC identifier should be represented here if the entity receiving the disbursement is registered with the FEC. |
**committee_name** | **str** |  | [optional]
**count** | **int, none_type** |  Number of records making up the total.  | [optional]
**memo_count** | **int, none_type** |  Number of records making up the total.  | [optional]
**memo_total** | **float, none_type** |  Schedule B disbursements aggregated by memoed items only  | [optional]
**recipient_name** | **str** |  | [optional]
**total** | **float, none_type** |  Schedule B disbursements aggregated by non-memoed items only  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
