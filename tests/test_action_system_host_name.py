"""Generated test for checking pynos based actions
"""
import xml.etree.ElementTree as ET
from st2tests.base import BaseActionTestCase
from system_host_name import system_host_name

__all__ = [
    'TestSystemHostName'
]


class MockCallback(object):  # pylint:disable=too-few-public-methods
    """Class to hold mock callback and result
    """
    returned_data = None

    def callback(self, call, **kwargs):  # pylint:disable=unused-argument
        """Mock callback method
        """
        xml_result = ET.tostring(call)
        self.returned_data = xml_result


class TestSystemHostName(BaseActionTestCase):
    """Test holder class
    """
    action_cls = system_host_name

    def test_action(self):
        """Generated test to check action
        """
        action = self.get_action_instance()
        mock_callback = MockCallback()
        kwargs = {
            'username': '',
            'rbridge_id': '224',
            'get': False,
            'ip': '',
            'password': '',
            'port': '22',
            'host_name': 'test',
            'test': True,
            'callback': mock_callback.callback
        }

        action.run(**kwargs)

        expected_xml = (
            '<config><rbridge-id xmlns="urn:brocade.com:mgmt:brocade-rbridge">'
            '<rbridge-id>224</rbridge-id><switch-attributes><host-name>test</h'
            'ost-name></switch-attributes></rbridge-id></config>'
        )

        self.assertTrue(expected_xml, mock_callback.returned_data)
