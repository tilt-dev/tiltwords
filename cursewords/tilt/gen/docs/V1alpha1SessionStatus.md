# V1alpha1SessionStatus

SessionStatus defines the observed state of Session
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**done** | **bool** | Done indicates whether this Session has completed its work and is ready to exit. | 
**error** | **str** | Error is a non-empty string when the Session is Done but encountered a failure as defined by the ExitCondition from the SessionSpec. | [optional] 
**pid** | **int** | PID is the process identifier for this instance of Tilt. | 
**start_time** | **datetime** | StartTime is when the Tilt engine was first started. | 
**targets** | [**list[V1alpha1Target]**](V1alpha1Target.md) | Targets are normalized representations of the servers/jobs managed by this Session.  A resource from a Tiltfile might produce one or more targets. A target can also be shared across multiple resources (e.g. an image referenced by multiple K8s pods). | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


