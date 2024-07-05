import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(url: str, mock: bool = False):
    """scrape linkedin profile data from url"""

    if mock:
        url = "https://gist.githubusercontent.com/Nikeshh/5d9bc3a94facf9a3a89ee540c9b45d73/raw/d977a9c23c1dc942ee22f53bf4488f3430cf4571/nikeshh-linkedin.json"
        response = requests.get(
            url,
            timeout=10,
        )
    else:
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response = requests.get(
            api_endpoint,
            params={"url": url},
            headers=header_dic,
            timeout=10,
        )

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    """if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")"""

    return data