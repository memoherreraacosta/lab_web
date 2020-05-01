from mpi4py import MPI

comm = MPI.COMM_WORLD
r = comm.Get_rank()

if r == 0:
    print("Escribe un numero entero positivo \nque quieras obtener su factorial")
    x= int(input())
    print(x)
    fact=1
    for i in range(1, x//2+1 ):
        fact*=i
    dic = {"input": x, "fact": fact}
    s=comm.send(dic, dest=1)
    print("Nodo {}: valor de factorial {}".format(r, fact))
    print("Nodo {}: valor de factorial {} \n".format(r, comm.recv(source=1)))
elif r == 1:
    s = comm.recv(source=0)
    fact=s["input"]//2 +1
    print(fact)
    for i in range(s["input"]//2+2, s["input"]+1):
        fact*=i
    res = fact*s["fact"]
    print("Nodo {}: valor de factorial {}".format(r, fact))
    print("Nodo {}: valor de factorial {}".format(r, res))
    s=comm.send(res, dest=0)