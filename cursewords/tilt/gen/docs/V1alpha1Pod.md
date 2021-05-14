# V1alpha1Pod

Pod is a collection of containers that can run on a host.  The Tilt API representation mirrors the Kubernetes API very closely. Irrelevant data is not included, and some fields might be simplified.  There might also be Tilt-specific status fields.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ancestor_uid** | **str** | AncestorUID is the UID from the WatchRef that matched this Pod.  If the Pod matched based on extra label selectors, this will be empty. | [optional] 
**baseline_restart_count** | **int** | BaselineRestartCount is the number of restarts across all containers before Tilt started observing the Pod.  This is used to ignore restarts for a Pod that was already executing before the Tilt daemon started. | 
**conditions** | [**list[V1alpha1PodCondition]**](V1alpha1PodCondition.md) | Conditions are various lifecycle conditions for this Pod.  See also v1.PodCondition in the Kubernetes API. | [optional] 
**containers** | [**list[V1alpha1Container]**](V1alpha1Container.md) | Containers are the containers belonging to the Pod. | 
**created_at** | **datetime** | CreatedAt is when the Pod was created. | 
**deleting** | **bool** | Deleting indicates that the Pod is in the process of being removed. | 
**errors** | **list[str]** | Errors are aggregated error messages for the Pod and its containers. | 
**init_containers** | [**list[V1alpha1Container]**](V1alpha1Container.md) | InitContainers are containers executed prior to the Pod containers being executed. | [optional] 
**name** | **str** | Name is the Pod name within the K8s cluster. | 
**namespace** | **str** | Namespace is the Pod namespace within the K8s cluster. | 
**phase** | **str** | Phase is where the Pod is at in its current lifecycle.  Valid values for this are v1.PodPhase values from the Kubernetes API. | 
**pod_template_spec_hash** | **str** | PodTemplateSpecHash is a hash of the Pod template spec.  Tilt uses this to associate Pods with the build that triggered them. | [optional] 
**status** | **str** | Status is a concise description for the Pod&#39;s current state.  This is based off the status output from &#x60;kubectl get pod&#x60; and is not an \&quot;enum-like\&quot; value. | 
**uid** | **str** | UID is the unique Pod UID within the K8s cluster. | 
**update_started_at** | **datetime** | UpdateStartedAt is when Tilt started a deployment update for this Pod. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


