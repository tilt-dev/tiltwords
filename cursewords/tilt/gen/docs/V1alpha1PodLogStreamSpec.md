# V1alpha1PodLogStreamSpec

PodLogStreamSpec defines the desired state of PodLogStream  Translated into a PodLog query to the current Kubernetes cluster: https://pkg.go.dev/k8s.io/api/core/v1#PodLogOptions  which Kubernetes context to use?
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ignore_containers** | **list[str]** | The names of containers to exclude from the stream.  If &#x60;onlyContainers&#x60; and &#x60;ignoreContainers&#x60; are not set, will watch all containers in the pod. | [optional] 
**namespace** | **str** | The namespace of the pod to watch. Defaults to the kubecontext default namespace. | [optional] 
**only_containers** | **list[str]** | The names of containers to include in the stream.  If &#x60;onlyContainers&#x60; and &#x60;ignoreContainers&#x60; are not set, will watch all containers in the pod. | [optional] 
**pod** | **str** | The name of the pod to watch. Required. | [optional] 
**since_time** | **datetime** | An RFC3339 timestamp from which to show logs. If this value precedes the time a pod was started, only logs since the pod start will be returned. If this value is in the future, no logs will be returned.  Translates directly to the underlying PodLogOptions. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


