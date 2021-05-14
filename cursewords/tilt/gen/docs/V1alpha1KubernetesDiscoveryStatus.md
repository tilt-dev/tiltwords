# V1alpha1KubernetesDiscoveryStatus

KubernetesDiscoveryStatus defines the observed state of KubernetesDiscovery
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitor_start_time** | **datetime** | MonitorStartTime is the timestamp of when Kubernetes resource discovery was started.  It is zero if discovery has not been started yet. | [optional] 
**pods** | [**list[V1alpha1Pod]**](V1alpha1Pod.md) | Pods that have been discovered based on the criteria in the spec. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


