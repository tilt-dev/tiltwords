# V1alpha1TargetState

TargetState describes the current execution status for a target.  Either EXACTLY one of Waiting, Active, or Terminated will be populated or NONE of them will be. In the event that all states are null, the target is currently inactive or disabled and should not be expected to execute.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | [**V1alpha1TargetStateActive**](V1alpha1TargetStateActive.md) |  | [optional] 
**terminated** | [**V1alpha1TargetStateTerminated**](V1alpha1TargetStateTerminated.md) |  | [optional] 
**waiting** | [**V1alpha1TargetStateWaiting**](V1alpha1TargetStateWaiting.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


