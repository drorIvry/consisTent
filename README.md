<img align="center" src="./logo.png">

consisTent is a full blows testing framework for prompts. The goal of consisTent is to create reproducible tests for LLM based applications regardless of the FM used.


## Installation

```sh
pip install consistent
```

## Concepts

consisTent comes with 2 types of validators (testers)

### syntactic validators

This type of validators is used to do static assertions of the LLM output. for example validating if the output is in a certain JSON format and assert the schema.
You can also use syntactic validators to assert something is a valid piece of code (JS or Python are supported at the moment)


**Syntactic validators are used to assert the FORM of the response**

### example

```python
consisTent.JsValidator().validate('console.log("Im a JS program!")')

consisTent.PyValidator().validate('print("Im a python program!")')

consisTent.JsonValidator().validate('"question": {"is this a valid JSON?"}')
```

### syntactic validators

This type of validators is used to assert the quality of the response with more "soft" parameters for example, check if something is factually correct, check for hallucinations, check for labels like "funny"/"interesting" etc... another type of semantic validator is the semantic consistency validator where you provide a seed of validated input and a threshold, and the test will assert the semantic distance of the new output from the seed cluster.

**Semantic validators are used to assert the CONTENT of the response**

### example

```python
seed = [
    'the cat sat on the mat',
    'the feline layed on the carpet',
    ...
]


consisTent.ConsistencyValidator().validate(
    seed=seed,
    model_output='the dog sat on the mat',
)

```
