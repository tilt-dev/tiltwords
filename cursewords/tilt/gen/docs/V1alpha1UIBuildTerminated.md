# V1alpha1UIBuildTerminated

UIBuildRunning respresents a finished build/update in the user interface.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | A non-empty string if the build failed with an error. | [optional] 
**finish_time** | **datetime** | The time when the build finished. | [optional] 
**is_crash_rebuild** | **bool** | A crash rebuild happens when Tilt live-updated a container, then the pod crashed, wiping out the live-updates. Tilt does a full build+deploy to reset the pod state to what&#39;s on disk. | [optional] 
**span_id** | **str** | The log span where the build logs are stored in the logstore. | [optional] 
**start_time** | **datetime** | The time when the build started. | [optional] 
**warnings** | **list[str]** | A list of warnings encountered while running the build. These warnings will also be printed to the build&#39;s log. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


