from pycparser.c_ast import Return


def animals(poulet,vach,pigs):
    poulet*2
    vach*4
    pigs*4
    return animals(poulet,vach,pigs)
print(animals(2,3,4))