from design_pattern.structural_patterns.proxy.api.api_server import APIServer
from design_pattern.structural_patterns.proxy.api.api_server_proxy import APIServerProxy


class Client:
    def __init__(self, _api_server: APIServer) -> None:
        self.api_server = _api_server

    def get_loan(self, loan_id: int) -> dict:
        return self.api_server.get_loan(loan_id)

    def delete_loan(self, loan_id: int) -> None:
        self.api_server.delete_loan(loan_id)

    def get_all_loans(self) -> dict:
        return self.api_server.get_all_loans()

    def create_loan(self, loan_id: int) -> None:
        self.api_server.create_loan(loan_id)


if __name__ == '__main__':
    api_server = APIServer()
    proxy = APIServerProxy(api_server)
    client = Client(proxy)

    client.create_loan(1)
