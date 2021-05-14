# V1alpha1UIResourceStatus

UIResourceStatus defines the observed state of UIResource
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_history** | [**list[V1alpha1UIBuildTerminated]**](V1alpha1UIBuildTerminated.md) | Past completed builds. | [optional] 
**current_build** | [**V1alpha1UIBuildRunning**](V1alpha1UIBuildRunning.md) |  | [optional] 
**endpoint_links** | [**list[V1alpha1UIResourceLink]**](V1alpha1UIResourceLink.md) | Links attached to this resource. | [optional] 
**has_pending_changes** | **bool** | True if the build was put in the pending queue due to file changes. | [optional] 
**k8s_resource_info** | [**V1alpha1UIResourceKubernetes**](V1alpha1UIResourceKubernetes.md) |  | [optional] 
**last_deploy_time** | **datetime** | The last time this resource was deployed. | [optional] 
**local_resource_info** | [**V1alpha1UIResourceLocal**](V1alpha1UIResourceLocal.md) |  | [optional] 
**pending_build_since** | **datetime** | When the build was put in the pending queue. | [optional] 
**queued** | **bool** | Queued is a simple indicator of whether the resource is queued for an update. | [optional] 
**runtime_status** | **str** | The RuntimeStatus is a simple, high-level summary of the runtime state of a server.  Not all resources run servers. | [optional] 
**specs** | [**list[V1alpha1UIResourceTargetSpec]**](V1alpha1UIResourceTargetSpec.md) | Information about all the target specs that this resource summarizes. | [optional] 
**trigger_mode** | **int** | Bit mask representing whether this resource is run when: 1) When a file changes 2) When the resource initializes | [optional] 
**update_status** | **str** | The UpdateStatus is a simple, high-level summary of any update tasks to bring the resource up-to-date.  If the resource runs a server, this may include both build tasks and live-update syncing. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


