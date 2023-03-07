from get_check import ScanCheck
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    qrraw = 't=20230306T1324&s=59.98&fn=7281440500232639&i=8355&fp=3680124697&n=1'
    client = ScanCheck()
    check_json = client.get_json(qrraw)
    client.save_check_to_json()
