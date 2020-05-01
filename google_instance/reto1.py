from mpi4py import MPI

comm = MPI.COMM_WORLD
r = comm.Get_rank()

if r == 0:
    m = {"Avisa en 0": 24}
    s = comm.sendrecv(m, dest=1, source=1)
    print("Mensaje de {}: {}".format(r, s))
elif r == 1:
    m = {"Avisa en 1": 8}
    comm.send(m, dest=0)
    s = comm.sendrecv(m, dest=0, source=0)
    print("Mensaje de {}: {}".format(r, s))