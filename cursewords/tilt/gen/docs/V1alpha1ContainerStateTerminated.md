# V1alpha1ContainerStateTerminated

ContainerStateTerminated is a terminated state of a container.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exit_code** | **int** | ExitCode is the exit status from the termination of the container.  Any non-zero value indicates an error during termination. | 
**finished_at** | **datetime** | FinishedAt is the time the container stopped running. | 
**reason** | **str** | Reason is a (brief) reason the container stopped running. | [optional] 
**started_at** | **datetime** | StartedAt is the time the container began running. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


