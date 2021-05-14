# V1alpha1Target

Target is a server or job whose execution is managed as part of this Session.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name is the name of the target; this is auto-generated from Tiltfile resources. | 
**resources** | **list[str]** | Resources are one or more Tiltfile resources that this target is associated with. | 
**state** | [**V1alpha1TargetState**](V1alpha1TargetState.md) |  | 
**type** | **str** | Type is the execution profile for this resource.  Job targets run to completion (e.g. a build script or database migration script). Server targets run indefinitely (e.g. an HTTP server). | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


