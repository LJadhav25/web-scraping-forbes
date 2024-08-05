import pandas as pd
import requests

headers = {
    "accept": "application/json, text/plain, */*",
    "referer": "https://www.forbes.com/lists/global2000/#23d5375d335d",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36",
}

cookies = {
    "notice_behavior": "expressed,eu",
    "notice_gdpr_prefs": "0,1,2:1a8b5228dd7ff0717196863a5d28ce6c",
}
api_url = "https://www.forbes.com/forbesapi/org/global2000/2020/position/true.json?limit=2000"
response = requests.get(api_url, headers=headers, cookies=cookies).json()
if "organizationList" in response and "organizationsLists" in response["organizationList"]:
    organizations = response["organizationList"]["organizationsLists"]
    sorted_organizations = sorted(organizations, key=lambda k: k["position"])
    sample_table = [
        [
            item.get("organizationName", ""),
            item.get("country", ""),
            item.get("revenue", ""),
            item.get("profits", ""),
            item.get("assets", ""),
            item.get("marketValue", "")
        ]
        for item in sorted_organizations
    ]
    df = pd.DataFrame(sample_table, columns=["Company", "Country", "Sales", "Profits", "Assets", "Market Value"])
    df.to_csv("forbes_2020.csv", index=False)
else:
    print("Expected keys not found in JSON response")
