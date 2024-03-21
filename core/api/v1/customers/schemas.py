from ninja import Schema


class AuthInSchema(Schema):
    phone: str


class AuthOutSchema(Schema):
    message: str


class TokenInSchema(Schema):
    phone: str
    code: str


class TokenOutSchema(Schema):
    token: str
