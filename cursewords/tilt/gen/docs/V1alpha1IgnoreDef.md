# V1alpha1IgnoreDef

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_path** | **str** | BasePath is the base path for the patterns. It cannot be empty.  If no patterns are specified, everything under it will be recursively ignored. | 
**patterns** | **list[str]** | Patterns are dockerignore style rules. Absolute-style patterns will be rooted to the BasePath.  See https://docs.docker.com/engine/reference/builder/#dockerignore-file. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


