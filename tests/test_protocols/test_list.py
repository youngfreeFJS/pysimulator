import pytest
from pysimulator.protocols.simctl import Simctl, ListTypes
from pysimulator.protocols.runtime import RunTime, RunTimeList
from pysimulator.protocols.device import Device, DeviceList


@pytest.fixture
def setup_new_device():
    new_device = Device.create('demo01-device1',
                               device_type=Simctl.list_devicetypes().filter('iPhone X').first().identifier,
                               runtime=Simctl.list_runtimes().filter('iOS').first().identifier
                               )
    assert len(new_device.udid) == 36
    assert new_device.name == 'demo01-device1'
    yield new_device
    new_device.delete()


def test_runtime_list():
    runtime_list = Simctl.list_runtimes()
    for runtime in runtime_list:
        assert isinstance(runtime, RunTime)
        assert runtime.name != None


def test_device_list():
    device_list = Simctl.list_devices()
    for device in device_list:
        assert isinstance(device, Device)
        assert device.name != None
        assert len(device.udid) == 36


def test_device_list_filter(setup_new_device: Device):
    device_list = Simctl.list_devices()
    devices_filter = device_list.filter(setup_new_device.name)
    assert len(devices_filter) == 1


def test_device_list_first(setup_new_device: Device):
    device_list = Simctl.list_devices()
    device = device_list.filter(setup_new_device.name).first()
    assert isinstance(device, Device)
    assert device.name == setup_new_device.name


def test_device_type_list():
    device_type_list = Simctl.list_devicetypes()
    assert len(device_type_list) > 0
