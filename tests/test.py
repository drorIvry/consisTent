# %%
import consisTent

seed = [
    "the cat sat on the mat",
    "the feline layed on the carpet",
]


# consisTent.ConsistencyValidator(
#     seed_size=2,
# ).validate(
#     seed=seed,
#     model_output="the dog sat on the mat",
# )
# consisTent.ConsistencyValidator(seed_size=2).validate()
OPENAI_KEY = "XXXXXX"

consisTent.LabelsValidator(openai_key=OPENAI_KEY).validate(
    labels=[
        "funny",
        "short",
        "about rabbits",
    ],
    model_output="What do you call a rabbit that tells jokes? A funny bunny!",
)
# consisTent.JsonValidator().validate()
# consisTent.JsValidator().validate()
# consisTent.YamlValidator().validate()
# consisTent.PydanticValidator().validate()
# consisTent.PyValidator().validate()

# %%
