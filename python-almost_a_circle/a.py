#!/usr/bin/python3
from models.base import Base
from_json_str = Base.from_json_string('[{ "id": 89 }]')
print("Result ", from_json_str)
