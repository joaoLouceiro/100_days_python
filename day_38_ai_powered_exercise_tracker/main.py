import docs_api
import exercise
import exercise_api

u_input = input('Tell me which exercises you did: ')

req = exercise_api.post(u_input)

for item in req.json()["exercises"]:
    ex = exercise.Exercise(name=item["name"], duration=item["duration_min"], calories=item["nf_calories"])
    docs_api.post(ex)