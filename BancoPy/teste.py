from models.cliente import Cliente
from models.conta import Conta

felicity: Cliente = Cliente('Felicity Jones', 'felicity@gmail.com', '046.821.136-96', '08/07/1986')
angelina: Cliente = Cliente('Angelina Jolie', 'angelina@gmail.com', '058.348.820-20', '10/12/1983')

# print(felicity)
# print(angelina)

conta1: Conta = Conta(felicity)
conta2: Conta = Conta(angelina)

print(conta1)

