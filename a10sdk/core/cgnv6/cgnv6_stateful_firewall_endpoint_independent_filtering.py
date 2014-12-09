from a10sdk.common.A10BaseClass import A10BaseClass


class EndpointIndependentFiltering(A10BaseClass):
    
    """Class Description::
    Configure Endpoint-Independent-Filtering Behavior .

    Class endpoint-independent-filtering supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/stateful-firewall/endpoint-independent-filtering`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "endpoint-independent-filtering"
        self.a10_url="/axapi/v3/cgnv6/stateful-firewall/endpoint-independent-filtering"
        self.DeviceProxy = ""
        self.udp = {}
        self.tcp = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)

