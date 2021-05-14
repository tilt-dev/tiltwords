# V1alpha1UIResourceKubernetes

UIResourceKubernetes contains status information specific to Kubernetes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_containers_ready** | **bool** | Whether all the containers in the pod are currently healthy and have passed readiness checks. | [optional] 
**display_names** | **list[str]** | The list of all resources deployed in the Kubernetes deploy for this resource. | [optional] 
**pod_creation_time** | **datetime** | The creation time of the active pod. | [optional] 
**pod_name** | **str** | The name of the active pod.  The active pod tends to be what Tilt defaults to for port-forwards, live-updates, etc. | [optional] 
**pod_restarts** | **int** | The number of pod restarts. | [optional] 
**pod_status** | **str** | The status of the active pod. | [optional] 
**pod_status_message** | **str** | Extra error messaging around the current status of the active pod. | [optional] 
**pod_update_start_time** | **datetime** | The last update time of the active pod | [optional] 
**span_id** | **str** | The span where this pod stores its logs in the Tilt logstore. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


