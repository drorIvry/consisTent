import json
from typing import List
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.chat_models import ChatOpenAI

from ..base_validator import Validator


class OpenAIValidator(Validator):
    def __init__(
        self,
        openai_key: str,
    ):
        self._model = ChatOpenAI(
            temperature=0,
            openai_api_key=openai_key,
            max_tokens=1000,
        )

        response_schemas = [
            ResponseSchema(
                name="criteria",
                description="This is the input_criteria from the user",
            ),
            ResponseSchema(
                name="passed",
                description="This is the validation result of the input against this criteria",  # noqa E501
            ),
            ResponseSchema(
                name="match_score",
                description="A score 0-100 of how close you think the match is between user input and your match",  # noqa E501
            ),
            ResponseSchema(
                name="reason",
                description="Why did the input failed / passed this criteria",
            ),
        ]

        output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
        format_instructions = output_parser.get_format_instructions()

        self._template = """
        you are an input validator.
        given a set of criteria your goal is to decide
        if the input matches the given criteria.

        {format_instructions}

        Wrap your final output with closed and open brackets (a list of json objects)

        CRITERIA:
        {criteria}

        INPUT:
        {user_input}

        YOUR RESPONSE:
            """

        self._prompt = ChatPromptTemplate(
            messages=[HumanMessagePromptTemplate.from_template(self._template)],
            input_variables=["criteria", "user_input"],
            partial_variables={"format_instructions": format_instructions},
        )

    def validate(
        self,
        criteria: List[str],
        model_output: str,
    ):
        parsed_criteria = ", ".join(criteria)

        _input = self._prompt.format_prompt(
            criteria=parsed_criteria,
            user_input=model_output,
        )

        output = self._model(_input.to_messages())

        structured_data = json.loads(output.content)

        for entry in structured_data:
            assert (
                entry["passed"] is True
            ), f"llm validation check validation failed on {entry['criteria']} for {entry['reason']}"  # noqa: E501
