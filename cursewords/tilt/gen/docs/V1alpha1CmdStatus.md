# V1alpha1CmdStatus

CmdStatus defines the observed state of Cmd  Based loosely on ContainerStatus in Kubernetes
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ready** | **bool** | Specifies whether the command has passed its readiness probe.  Terminating the command does not change its Ready state.  Is always true when no readiness probe is defined. | [optional] 
**running** | [**V1alpha1CmdStateRunning**](V1alpha1CmdStateRunning.md) |  | [optional] 
**terminated** | [**V1alpha1CmdStateTerminated**](V1alpha1CmdStateTerminated.md) |  | [optional] 
**waiting** | [**V1alpha1CmdStateWaiting**](V1alpha1CmdStateWaiting.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


