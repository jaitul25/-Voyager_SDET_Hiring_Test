from Stub_Github import Github_Stub
import unittest
from pretend import stub

class Testsuite(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.gh_stub_obj = Github_Stub()
        cls.user1 = stub(user = 'jaitul25')
        cls.user2 = stub(user = 'tanmayb123')

        

    def testing_user_api(self) -> None:

        self.gh_stub_obj.get_user_info(self.user1)
        self.gh_stub_obj.get_user_info(self.user2)


    def testing_user_repo_api(self) -> None:
        
        self.gh_stub_obj.get_user_repo_info(self.user1)
        self.gh_stub_obj.get_user_repo_info(self.user2)

    def testing_gateway_response_check(self) -> None:

        self.gh_stub_obj.gateway_response_check(self.user1)
        self.gh_stub_obj.gateway_response_check(self.user2)
        
        
    def testing_response_status_check(self) -> None:

        self.gh_stub_obj.response_status_check(self.user1)
        self.gh_stub_obj.response_status_check(self.user2)
    


        


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

