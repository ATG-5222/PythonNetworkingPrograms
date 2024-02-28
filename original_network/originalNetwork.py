from netmask_dict import NetMask
from hosts_dict import Hosts

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