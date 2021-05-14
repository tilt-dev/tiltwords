# V1alpha1ContainerLogStreamStatus

ContainerLogStreamStatus defines the current status of each individual container log stream.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | True when the stream is set up and streaming logs properly. | [optional] 
**error** | **str** | The last error message encountered while streaming.  Empty when the stream is actively streaming or successfully terminated. | [optional] 
**name** | **str** | The name of the container. | [optional] 
**terminated** | **bool** | True when the logs are done stream and the container is terminated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


