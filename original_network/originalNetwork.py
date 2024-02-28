NetMask = {
    "8": "255.0.0.0",
    "9": "255.128.0.0",
    "10": "255.192.0.0",
    "11": "255.224.0.0",
    "12": "255.240.0.0",
    "13": "255.248.0.0",
    "14": "255.252.0.0",
    "15": "255.254.0.0",
    "16": "255.255.0.0",
    "17": "255.255.128.0",
    "18": "255.255.192.0",
    "19": "255.255.224.0",
    "20": "255.255.240.0",
    "21": "255.255.248.0",
    "22": "255.255.252.0",
    "23": "255.255.254.0",
    "24": "255.255.255.0",
    "25": "255.255.255.128",
    "26": "255.255.255.192",
    "27": "255.255.255.224",
    "28": "255.255.255.240",
    "29": "255.255.255.248",
    "30": "255.255.255.252",
    "31": "255.255.255.254",
    "32": "255.255.255.255"
}

Hosts = {
    "8": "16777216",
    "9": "8388608",
    "10": "4194304",
    "11": "2097152",
    "12": "1048573",
    "13": "524288",
    "14": "262144",
    "15": "131072",
    "16": "65536",
    "17": "32768",
    "18": "16384",
    "19": "8192",
    "20": "4096",
    "21": "2048",
    "22": "1024",
    "23": "512",
    "24": "256",
    "25": "128",
    "26": "64",
    "27": "32",
    "28": "16",
    "29": "8",
    "30": "4",
    "31": "2",
    "32": "1"
}

def getNetAddress(ip, mask):
    try:
        # Convierte la dirección IP y la máscara de subred a una lista de números
        ipList = [int(x) for x in ip.split('.')]
        maskList = [int(x) for x in mask.split('.')]
        #Verificar datos ingresados por el usuario
        if len(ipList) != 4:
            raise TypeError("Error: The IP address must have 4 octets.")
        for element in ipList:
            if element > 255:
                raise TypeError("Error: The IP address octets have a limit value of 255.")
        # Realiza la operación bitwise AND en cada par de números de las listas
        netList = [a & b for a, b in zip(ipList, maskList)]
        # Convierte la lista de números de la dirección de red a una cadena
        netAddress = '.'.join(map(str, netList))
        return netAddress
    except ValueError:
        print("Error: Enter a valid IP address and/or a valid subnet mask.")
        return None
    except Exception as e:
        print(e)
        return None

def main():
    try:
        #Obtener inputs del usuario
        print("\n-------------------\n")
        ip = input("Enter the ip: ") 
        mask = input("Enter the subnet mask(prefix 8-32): ")
        print("\n-------------------\n")
        #Obtener información de la mascara de red
        netMask = NetMask[mask]
        hosts = Hosts[mask]
        netAddress = getNetAddress(ip, netMask)
        if netAddress is not None:
            #Imprimir resultado
            print(f"The network address {ip}/{mask} is: {netAddress} and has a total of {hosts} hosts.")
            print("\n-------------------\n")
    except:
        print("Error: Subnet mask not valid.")

if __name__ == "__main__":
    main()