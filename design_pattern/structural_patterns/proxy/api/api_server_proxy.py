from .api_server import APIServer
from .api_server_interface import APIServerInterface


class APIServerProxy(APIServerInterface):
    def __init__(self, api_server: APIServer) -> None:
        self._api_server = api_server

    def create_loan(self, loan_id: int) -> None:
        self._api_server.create_loan(loan_id)
        self.log_request()

    def get_loan(self, loan_id: int) -> dict:
        result = dict()
        if self.authorize_account():
            result = self._api_server.get_loan(loan_id)
        self.log_request()
        return result

    def delete_loan(self, loan_id: int) -> None:
        self._api_server.delete_loan(loan_id)
        self.log_request()

    def get_all_loans(self) -> dict:
        result = dict()
        if self.authorize_account():
            result = self._api_server.get_all_loans()
        self.log_request()
        return result

    def authorize_account(self) -> bool:
        return True

    def log_request(self) -> None:
        print('Logged request')
