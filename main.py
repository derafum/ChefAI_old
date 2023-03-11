from get_check import ScanCheck

if __name__ == "__main__":
    qrraw = 't=20230306T1341&s=128.97&fn=9960440302156797&i=74284&fp=1765630299&n=1'
    client = ScanCheck()
    check_json = client.get_json(qrraw)
    client.save_check_to_json()

