# TotalsCommittee

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliated_committee_name** | **str** |  Affiliated committee or connected organization  | [optional] 
**candidate_ids** | **list[str]** |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  | [optional] 
**cash_on_hand_end_period** | **float** |  | [optional] 
**city** | **str** |  City of committee as reported on the Form 1  | [optional] 
**committee_id** | **str** |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | 
**committee_type** | **str** | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
**committee_type_full** | **str** | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditor (person or group)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
**cycle** | **int** |  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.  | 
**cycles** | **list[int]** |  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s) The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
**cycles_has_activity** | **list[int]** |  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1), and the committee has filling activity during the cycle  | [optional] 
**cycles_has_financial** | **list[int]** |  A two year election cycle that the committee was active- (after original registration date but before expiration date in FEC Form 1s), and the commitee files the financial reports (&#39;F3&#39;, &#39;F3X&#39;, &#39;F3P&#39;, &#39;F3L&#39;, &#39;F4&#39;, &#39;F5&#39;, &#39;F7&#39;, &#39;F13&#39;) during this cycle.  | [optional] 
**debts_owed_by_committee** | **float** |  | [optional] 
**designation** | **str** | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
**designation_full** | **str** | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
**disbursements** | **float** |  | [optional] 
**filing_frequency** | **str** | The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived  | [optional] 
**independent_expenditures** | **float** |  | [optional] 
**is_active** | **bool** |  True indicates that a committee is active.  | [optional] 
**last_cycle_has_activity** | **int** |  The latest two year election cycle that the committee has filings  | [optional] 
**last_cycle_has_financial** | **int** |  The latest two year election cycle that the committee files the financial reports (&#39;F3&#39;, &#39;F3X&#39;, &#39;F3P&#39;, &#39;F3L&#39;, &#39;F4&#39;, &#39;F5&#39;, &#39;F7&#39;, &#39;F13&#39;).  | [optional] 
**name** | **str** | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. | [optional] 
**organization_type** | **str** | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] 
**organization_type_full** | **str** | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] 
**party** | **str** | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
**party_full** | **str** | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
**receipts** | **float** |  | [optional] 
**state** | **str** |  State of the committee&#39;s address as filed on the Form 1  | [optional] 
**state_full** | **str** |  State of committee as reported on the Form 1  | [optional] 
**street_1** | **str** |  Street address of committee as reported on the Form 1  | [optional] 
**street_2** | **str** |  Second line of street address of committee as reported on the Form 1  | [optional] 
**treasurer_name** | **str** | Name of the Committee&#39;s treasurer. If multiple treasurers for the committee, the most recent treasurer will be shown. | [optional] 
**zip** | **str** |  Zip code of committee as reported on the Form 1  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


