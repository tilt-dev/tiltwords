# V1alpha1FileWatchStatus

FileWatchStatus defines the observed state of FileWatch
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error is set if there is a problem with the filesystem watch. If non-empty, consumers should assume that no filesystem events will be seen and that the file watcher is in a failed state. | [optional] 
**file_events** | [**list[V1alpha1FileEvent]**](V1alpha1FileEvent.md) | FileEvents summarizes batches of file changes (create, modify, or delete) that have been seen in ascending chronological order. Only the most recent 20 events are included. | [optional] 
**last_event_time** | **datetime** | LastEventTime is the timestamp of the most recent file event. It is zero if no events have been seen yet.  If the specifics of which files changed are not important, this field can be used as a watermark without needing to inspect FileEvents. | [optional] 
**monitor_start_time** | **datetime** | MonitorStartTime is the timestamp of when filesystem monitor was started. It is zero if the monitor has not been started yet. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


