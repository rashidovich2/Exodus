from secrets import token_bytes
from typing import Dict, Any

from src.util.json_util import dict_to_json_str


# Messages must follow this format
# Message = { "command" "command_name",
#             "data" : {...},
#             "request_id": "bytes_32",
#             "destination": "service_name",
#             "origin": "service_name"
#           }


def format_response(incoming_msg: Dict[str, Any], response_data: Dict[str, Any]) -> str:
    """
    Formats the response into standard format.
    """
    response = {
        "command": incoming_msg["command"],
        "ack": True,
        "data": response_data,
        "request_id": incoming_msg["request_id"],
        "destination": incoming_msg["origin"],
        "origin": incoming_msg["destination"],
    }

    return dict_to_json_str(response)


def create_payload(
    command: str, data: Dict[str, Any], origin: str, destination: str, string=True
):
    response = {
        "command": command,
        "ack": False,
        "data": data,
        "request_id": token_bytes().hex(),
        "destination": destination,
        "origin": origin,
    }

    return dict_to_json_str(response) if string else response


def pong():
    return {"success": True}
