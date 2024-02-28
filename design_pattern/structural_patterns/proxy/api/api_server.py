from .api_server_interface import APIServerInterface


class APIServer(APIServerInterface):
    def get_loan(self, loan_id: int) -> dict:
        return {'loan_id': loan_id}

    def delete_loan(self, loan_id: int) -> None:
        print('deleting loan', loan_id)

    def get_all_loans(self) -> dict:
        return {'loans': list()}

    def create_loan(self, loan_id: int) -> None:
        print(f'Creating loan with id {loan_id}')
