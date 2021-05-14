# V1alpha1UISessionStatus

UISessionStatus defines the observed state of UISession
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fatal_error** | **str** | A FatalError is an error that forces Tilt to stop its control loop. The API server will stay up and continue to serve the UI, but no further builds will happen. | 
**feature_flags** | [**list[V1alpha1UIFeatureFlag]**](V1alpha1UIFeatureFlag.md) | FeatureFlags reports a list of experimental features that have been enabled. | 
**needs_analytics_nudge** | **bool** | NeedsAnalyticsNudge reports whether the UI hasn&#39;t opted in or out of analytics, and the UI should nudge them to do so. | 
**running_tilt_build** | [**V1alpha1TiltBuild**](V1alpha1TiltBuild.md) |  | 
**suggested_tilt_version** | **str** | SuggestedTiltVersion tells the UI the recommended version for this user. If the version is different than what&#39;s running, the UI may display a prompt to upgrade. | 
**tilt_cloud_scheme_host** | **str** | TiltCloudSchemeHost reports the base URL of the Tilt Cloud instance associated with this Tilt process. Usually https://cloud.tilt.dev | 
**tilt_cloud_team_id** | **str** | TiltCloudTeamID reports the unique team id if the user is signed into TiltCloud and the Tiltfile declares a team. | 
**tilt_cloud_team_name** | **str** | TiltCloudUsername reports the human-readable team name if the user is signed into TiltCloud and the Tiltfile declares a team. | 
**tilt_cloud_username** | **str** | TiltCloudUsername reports the username if the user is signed into TiltCloud. | 
**tilt_start_time** | **datetime** | The time that this instance of tilt started. Clients can use this to determine if the API server has restarted and all the objects need to be refreshed. | 
**tiltfile_key** | **str** | An identifier for the Tiltfile that is running. Clients can use this to store data associated with a particular project in LocalStorage or other persistent storage. | 
**version_settings** | [**V1alpha1VersionSettings**](V1alpha1VersionSettings.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


