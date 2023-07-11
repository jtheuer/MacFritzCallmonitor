

def parse_call_log(event_string):
    fields = event_string.split(";")
    if len(fields) < 4:
        return None
    elif fields[1] == "RING" and len(fields) == 7:
        return {
            "type": fields[1],
            "from": fields[3],
            "to": fields[4],
            "time": fields[0]
        }
    elif fields[1] == "CALL" and len(fields) == 8:
        return {
            "type": fields[1],
            "from": fields[4],
            "to": fields[5],
            "time": fields[0]
        }
    return None
