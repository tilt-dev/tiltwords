# V1alpha1TargetStateTerminated

TargetStateTerminated is a target that finished running, either because it completed successfully or encountered an error.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error is a non-empty string if the target encountered a failure during execution that caused it to stop.  For targets of type TargetTypeServer, this is always populated, as the target is expected to run indefinitely, and thus any termination is an error. | [optional] 
**finish_time** | **datetime** | FinishTime is when the target stopped executing. | 
**start_time** | **datetime** | StartTime is when the target began executing. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


