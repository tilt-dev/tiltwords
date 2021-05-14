# V1alpha1PodCondition

PodCondition is a lifecycle condition for a Pod.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_transition_time** | **datetime** | LastTransitionTime is the last time the status changed. | [optional] 
**message** | **str** | Message is a human-readable description of the last status change. | [optional] 
**reason** | **str** | Reason is a unique, one-word, CamelCase value for the cause of the last status change. | [optional] 
**status** | **str** | Status is the current state of the condition (True, False, or Unknown).  Valid values for this are v1.PodConditionStatus values from the Kubernetes API. | 
**type** | **str** | Type is the type of condition.  Valid values for this are v1.PodConditionType values from the Kubernetes API. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


