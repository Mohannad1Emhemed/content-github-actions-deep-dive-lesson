from github import Github

def lambda_handler(event, context):
    """Lambda function wrapper
    Args:
        event: trigger event dict
        context: lambda methods and properties
    Returns:
        string: greeting response
    """
    print('Starting functions\n---------------------------------------------')

    if "input" not in event:
        raise ValueError("Input not provided in the event")

    input_value = event["input"]


    if event["input"] == "Hi":
        
        return "Hi There"


    if input_value == "Hello":
        return "World"

    else:
        raise ValueError(f"Unsupported input value: {input_value}")
