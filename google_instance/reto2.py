from mpi4py import MPI

comm = MPI.COMM_WORLD
r = comm.Get_rank()

m ="Ganaron todos"
d=comm.bcast(m, root=0)
print (d)