from mpi4py import MPI

comm = MPI.COMM_WORLD
r = comm.Get_rank()

if r == 0:
    m = sum(range(0, 51))
    s = comm.sendrecv(m, dest=1, source=1)
    print("Suma en nodo {}= {}".format(r, m))
    sm = m + s
    print("Suma total en nodo {}= {}".format(r, sm))
elif r == 1:
    m = sum(range(51, 101))
    s = comm.sendrecv(m, dest=0, source=0)
    print("Suma en nodo {}= {}".format(r, m))