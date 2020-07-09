# candidate_history_total.CandidateHistoryTotal

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidate_id** | **str** |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office.  |
**cycle** | **int** |  |
**is_election** | **bool** |  |
**two_year_period** | **int** |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  |
**active_through** | **int, none_type** | Last year a candidate was active. This field is specific to the candidate_id so if the same person runs for another office, there may be a different record for them. | [optional]
**address_city** | **str, none_type** | City of candidate&#39;s address, as reported on their Form 2. | [optional]
**address_state** | **str, none_type** | State of candidate&#39;s address, as reported on their Form 2. | [optional]
**address_street_1** | **str, none_type** | Street of candidate&#39;s address, as reported on their Form 2. | [optional]
**address_street_2** | **str, none_type** | Additional street information of candidate&#39;s address, as reported on their Form 2. | [optional]
**address_zip** | **str, none_type** | Zip code of candidate&#39;s address, as reported on their Form 2. | [optional]
**candidate_election_year** | **int, none_type** | The last year of the cycle for this election. | [optional]
**candidate_inactive** | **bool, none_type** |  True indicates that a candidate is inactive.  | [optional]
**candidate_status** | **str, none_type** | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  | [optional]
**cash_on_hand_end_period** | **float, none_type** |  | [optional]
**coverage_end_date** | **date, none_type** | Ending date of the reporting period | [optional]
**coverage_start_date** | **date, none_type** | Beginning date of the reporting period | [optional]
**cycles** | **[int], none_type** |  Two-year election cycle in which a candidate runs for office. Calculated from FEC Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To see data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | [optional]
**debts_owed_by_committee** | **float, none_type** |  | [optional]
**disbursements** | **float, none_type** |  | [optional]
**district** | **str, none_type** | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional]
**district_number** | **int, none_type** | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  | [optional]
**election_districts** | **[str], none_type** | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional]
**election_year** | **int** |  | [optional]
**election_years** | **[int], none_type** | Years in which a candidate ran for office. | [optional]
**fec_cycles_in_election** | **[int], none_type** | FEC cycles are included in candidate election years. | [optional]
**federal_funds_flag** | **bool, none_type** | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. | [optional]
**first_file_date** | **date, none_type** | The day the FEC received the candidate&#39;s first filing. This is a F2 candidate registration. | [optional]
**flags** | **str, none_type** |  | [optional]
**has_raised_funds** | **bool, none_type** | A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) | [optional]
**incumbent_challenge** | **str, none_type** | One-letter code (&#39;I&#39;, &#39;C&#39;, &#39;O&#39;) explaining if the candidate is an incumbent, a challenger, or if the seat is open. | [optional]
**incumbent_challenge_full** | **str, none_type** | Explains if the candidate is an incumbent, a challenger, or if the seat is open. | [optional]
**last_f2_date** | **date, none_type** | The day the FEC received the candidate&#39;s most recent Form 2 | [optional]
**last_file_date** | **date, none_type** | The day the FEC received the candidate&#39;s most recent filing | [optional]
**load_date** | **datetime, none_type** | Date the information was loaded into the FEC systems. This can be affected by reseting systems and other factors, refer to receipt_date for the day that the FEC received the paper or electronic document. Keep in mind that paper filings take more time to process and there can be a lag between load_date and receipt_date. This field can be helpful to identify paper records that have been processed recently. | [optional]
**name** | **str, none_type** | Name of candidate running for office | [optional]
**office** | **str, none_type** | Federal office candidate runs for: H, S or P | [optional]
**office_full** | **str, none_type** | Federal office candidate runs for: House, Senate or presidential | [optional]
**party** | **str, none_type** | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional]
**party_full** | **str, none_type** | Party affiliated with a candidate or committee | [optional]
**receipts** | **float, none_type** |  | [optional]
**rounded_election_years** | **[int], none_type** | Rounded election years in which a candidate ran for office | [optional]
**state** | **str, none_type** | US state or territory where a candidate runs for office | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
