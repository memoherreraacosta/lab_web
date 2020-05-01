from mpi4py import MPI

comm = MPI.COMM_WORLD
r = comm.Get_rank()
m = "Salu2"

if r == 0:
    m = m + " from node: {}".format(r)
elif r == 1:
    m = m + " from node: {}".format(r)

d = comm.bcast(m, root=0)
print(d)
