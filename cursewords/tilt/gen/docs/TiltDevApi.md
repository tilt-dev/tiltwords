# tilt-dev/python-kubernetes.client.TiltDevApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_group**](TiltDevApi.md#get_api_group) | **GET** /apis/tilt.dev/ | 


# **get_api_group**
> V1APIGroup get_api_group()



get information of a group

### Example

```python
from __future__ import print_function
import time
import tilt_dev.python-kubernetes.client
from tilt-dev/python-kubernetes.client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API kubernetes.client
with tilt-dev/python-kubernetes.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tilt-dev/python-kubernetes.client.TiltDevApi(api_client)
    
    try:
        api_response = api_instance.get_api_group()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TiltDevApi->get_api_group: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1APIGroup**](V1APIGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

