# V1alpha1FileEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seen_files** | **list[str]** | SeenFiles is a list of paths which changed (create, modify, or delete). | 
**time** | **datetime** | Time is an approximate timestamp for a batch of file changes.  This will NOT exactly match any inode attributes (e.g. ctime, mtime) at the filesystem level and is purely informational or for use as an opaque watermark. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


