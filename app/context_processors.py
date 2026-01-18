# frontend/context_processors.py
import requests
from pro.settings import BACKEND_API_BASE

def api_user(request):
    token = request.session.get("access")
    if not token:
        return {}
    headers = {"Authorization": f"Bearer {token}"}
    try:
        r = requests.get(f"{BACKEND_API_BASE}me/", headers=headers)
        if r.status_code == 200:
            return {"api_user": r.json()}
    except:
        pass
    return {}
