def getNetAddress(ip, mascara):
    # Convierte la dirección IP y la máscara de subred a una lista de números
    ipList = [int(x) for x in ip.split('.')]
    maskList = [int(x) for x in mascara.split('.')]
    # Realiza la operación bitwise AND en cada par de números de las listas
    netList = [a & b for a, b in zip(ipList, maskList)]
    # Convierte la lista de números de la dirección de red a una cadena
    netAddress = '.'.join(map(str, netList))
    return netAddress

# Ejemplo de uso
ip = "192.168.1.10"
mask = "255.255.255.0"

netAddress = getNetAddress(ip, mask)
print(f"La direccion de red para {ip}/{mask} es: {netAddress}")