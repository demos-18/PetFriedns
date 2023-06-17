import json
from jsonschema import validate


class ResponseHandler:

    def __init__(self, response):
        self.response = response
        self.response_status = response.status_code
        self.parsed_object = None
        try:
            try:
                self.response_json = response.json().get("pets")
                if self.response_json is None:
                    raise ValueError
            except ValueError:
                self.response_json = response.json()
        except json.decoder.JSONDecodeError:
            self.response_text = response.text

    def validate_pydantic(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.parse_obj(item)
        else:
            schema.parse_obj(self.response_json)
            return self

    def validate_json(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                validate(item, schema)
        else:
            validate(self.response_json, schema)
            return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, self
        else:
            assert self.response_status == status_code, self
            return self

    def parsed_obj(self, value):
        self.parsed_object = self.response_json.get(value)
        return self.parsed_object

    def __str__(self):
        return \
            f"Status code {self.response_status} \n \"" \
            f"Requested url {self.response.url} \n \"" \
            f"Response body {self.response_json}"

