# V1alpha1KubernetesWatchRef

KubernetesWatchRef is similar to v1.ObjectReference from the Kubernetes API and is used to determine what objects should be reported on based on discovery.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name is the Kubernetes object name.  This is not directly used in discovery; it is extra metadata. | [optional] 
**namespace** | **str** | Namespace is the Kubernetes namespace for discovery. Required. | 
**uid** | **str** | UID is a Kubernetes object UID.  It should either be the exact object UID or the transitive owner. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


