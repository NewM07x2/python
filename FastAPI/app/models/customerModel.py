from pydantic import BaseModel

class CustomerModel(BaseModel):
    id: int = None
    name: str = ""
    email: str = ""

    def get_id(self) -> int:
        return self.id

    def set_id(self, id: int):
        self.id = id

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_email(self) -> str:
        return self.email

    def set_email(self, email: str):
        self.email = email