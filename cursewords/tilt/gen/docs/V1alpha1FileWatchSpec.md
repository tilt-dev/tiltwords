# V1alpha1FileWatchSpec

FileWatchSpec defines the desired state of FileWatch
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ignores** | [**list[V1alpha1IgnoreDef]**](V1alpha1IgnoreDef.md) | Ignores are optional rules to filter out a subset of changes matched by WatchedPaths. | [optional] 
**watched_paths** | **list[str]** | WatchedPaths are paths of directories or files to watch for changes to. It cannot be empty. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


