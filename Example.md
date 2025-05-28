# Curl Command to Run the Model

## Local 
`curl http://localhost:5001/`

## Depolyed (Run command in terminal)
`curl -H "Content-Type: application/json" -X POST -d '{"cyl":"4","disp":"160","vs":"1"}' "https://mpg-api-48417636379.europe-west1.run.app/predict_mpg"`


# Example Output: 

{
  "predict mpg": 24.998446152729784
}
