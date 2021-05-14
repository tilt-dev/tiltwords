# V1alpha1CmdSpec

CmdSpec defines how to run a local command.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **list[str]** | Command-line arguments. Must have length at least 1. | [optional] 
**dir** | **str** | Process working directory.  If the working directory is not specified, the command is run in the default Tilt working directory. | [optional] 
**env** | **list[str]** | Additional variables process environment.  Expressed as a C-style array of strings of the form [\&quot;KEY1&#x3D;VALUE1\&quot;, \&quot;KEY2&#x3D;VALUE2\&quot;, ...].  Environment variables are layered on top of the environment variables that Tilt runs with. | [optional] 
**readiness_probe** | [**V1alpha1Probe**](V1alpha1Probe.md) |  | [optional] 
**restart_on** | [**V1alpha1RestartOnSpec**](V1alpha1RestartOnSpec.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


