# %%
import consisTent

seed = ["the cat sat on the mat", "the feline layed on the carpet", ...]


consisTent.ConsistencyValidator(seed_size=2).validate(
    seed=seed,
    model_output="the dog sat on the mat",
)
consisTent.ConsistencyValidator(seed_size=2).validate()
consisTent.LabelsValidator().validate()
consisTent.JsonValidator().validate()
consisTent.JsValidator().validate()
consisTent.YamlValidator().validate()
consisTent.PydanticValidator().validate()
consisTent.PyValidator().validate()

# %%
