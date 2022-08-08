from flask import Flask
from flask_restful import Api
from src.resources.available import AvailablePreConfigs
from src.resources.analysis import (
    Analysis,
    CalculateMeasures,
    CalculateSubcharacteristics,
    CalculateCharacteristics,
)


app = Flask(__name__)
api = Api(app)

api.add_resource(AvailablePreConfigs, "/available-pre-configs")

api.add_resource(Analysis, "/analysis")

api.add_resource(
    CalculateMeasures,
    "/calculate-measures/",
)

api.add_resource(
    CalculateSubcharacteristics,
    "/calculate-subcharacteristics/",
)

api.add_resource(
    CalculateCharacteristics,
    "/calculate-characteristics/",
)
