import pytest
from datetime import datetime

@pytest.mark.usefixtures("setup_and_teardown")
class BaseTest:
    def generate_email_with_timestamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "ahrnot" + time_stamp + "@ukr.net"