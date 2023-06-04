

def validation(request):
    if 'text' in request and 'created_date' in request and 'rubrics' in request:
        if isinstance(request['text'], str) and isinstance(request['created_date'], str) and isinstance(request['rubrics'], list):
            return True
    return False
