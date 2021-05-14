# V1alpha1KubernetesDiscoverySpec

KubernetesDiscoverySpec defines the desired state of KubernetesDiscovery
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra_selectors** | [**list[V1LabelSelector]**](V1LabelSelector.md) | ExtraSelectors are label selectors that will force discovery of a Pod even if it does not match the AncestorUID.  This should only be necessary in the event that a CRD creates Pods but does not set an owner reference to itself. | [optional] 
**watches** | [**list[V1alpha1KubernetesWatchRef]**](V1alpha1KubernetesWatchRef.md) | Watches determine what resources are discovered.  If a discovered resource (e.g. Pod) matches the KubernetesWatchRef UID exactly, it will be reported. If a discovered resource is transitively owned by the KubernetesWatchRef UID, it will be reported. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


