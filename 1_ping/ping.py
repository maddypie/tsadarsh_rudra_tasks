import os


def main(address: str, count: int=10):
    command = f"ping {address} -c {count}"
    res = os.popen(command).read()
    return res


if __name__ == "__main__":
    address = input("Enter url/ip address to ping: ")
    output = main(address)
    print(output)
