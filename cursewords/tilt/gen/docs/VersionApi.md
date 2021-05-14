# tilt-dev/python-kubernetes.client.VersionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_code**](VersionApi.md#get_code) | **GET** /version/ | 


# **get_code**
> VersionInfo get_code()



get the code version

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
    api_instance = tilt-dev/python-kubernetes.client.VersionApi(api_client)
    
    try:
        api_response = api_instance.get_code()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VersionApi->get_code: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VersionInfo**](VersionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

