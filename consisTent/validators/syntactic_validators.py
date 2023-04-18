import json
import yaml
import ast
import js2py

from jsonschema import validate as js_validate
from pydantic import BaseModel

from .base_validator import Validator


class JsonValidator(Validator):
    @staticmethod
    def validate(
        model_output: str,
        schema: BaseModel = None,
    ):
        parsed_json = json.loads(model_output)
        if schema:
            js_validate(
                parsed_json,
                schema.schema(),
            )


class YamlValidator(Validator):
    @staticmethod
    def validate(
        model_output: str,
        schema: BaseModel,
    ):
        parsed_yaml = yaml.safe_load(model_output)
        js_validate(
            parsed_yaml,
            schema.schema(),
        )


class PyValidator(Validator):
    @staticmethod
    def validate(
        model_output: str,
    ):
        ast.parse(model_output)


class JsValidator(Validator):
    @staticmethod
    def validate(
        model_output: str,
    ):
        js2py.parse_js(model_output)
