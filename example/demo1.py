from pysimulator import Device, Simctl

new_device = Device.create('demo01-device',
                           device_type_name=Simctl.list_devicetypes().filter('iPhone X').first().identifier,
                           runtime_name=Simctl.list_runtimes().filter('13.5').first().identifier
                           )
print(new_device)