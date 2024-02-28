from abc import ABC, abstractmethod


class APIServerInterface(ABC):
    @abstractmethod
    def create_loan(self, loan_id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_loan(self, loan_id: int) -> dict:
        raise NotImplementedError

    @abstractmethod
    def delete_loan(self, loan_id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_all_loans(self) -> dict:
        raise NotImplementedError
