# V1alpha1Container

Container is an init or application container within a pod.  The Tilt API representation mirrors the Kubernetes API very closely. Irrelevant data is not included, and some fields might be simplified.  There might also be Tilt-specific status fields.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID is the normalized container ID (the &#x60;docker://&#x60; prefix is stripped). | 
**image** | **str** | Image is the image the container is running. | 
**name** | **str** | Name is the name of the container as defined in Kubernetes. | 
**ports** | **list[int]** | Ports are exposed ports as extracted from the Pod spec.  This is added by Tilt for convenience when managing port forwards. | 
**ready** | **bool** | Ready is true if the container is passing readiness checks (or has none defined). | 
**restarts** | **int** | Restarts is the number of times the container has restarted.  This includes restarts before the Tilt daemon was started if the container was already running. | 
**state** | [**V1alpha1ContainerState**](V1alpha1ContainerState.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


