from pysimulator.protocols.device import Device
from pysimulator.protocols.simctl import Simctl


def test_create_device():
    new_device = Device.create('demo01-device1',
                               device_type=Simctl.list_devicetypes().filter('iPhone X').first().identifier,
                               runtime=Simctl.list_runtimes().filter('13.5').first().identifier
                               )
    assert len(new_device.udid) == 36
    assert new_device.name == 'demo01-device1'

    new_device.delete()
