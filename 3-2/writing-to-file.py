date = "930106"

# vectorq.exec
print("#!/bin/csh")
print("")
print("")
print("set dir = ./test/")
print("set fileinfo = {$dir}info_pr.dat")
print("set filedh =  {$dir}dynamic_height_"+date+".gr")
print("set filest =  {$dir}density_"+date+".gr")
print("set filestm = {$dir}ss1_st0.dat")
print("set filequ =  {$dir}ss1a2qu.gr")
print("set fileqv =  {$dir}ss1a2qv.gr")
print("set fileqdi = {$dir}ss1a2qdi.gr")
print("")
print("./vectorq.exe << !")
print("'$fileinfo'	#>>>>>Escribe info file info.dat:")
print("'$filedh'	#>>>>>Escribe fichero de altura Dinamica:")
print("'$filest'	#>>>>>Escribe fichero de densidad:")
print("'$filestm'	#>>>>>Escribe fichero de densidad promedio:")
print("'$filequ'	#>>>>>Escribe fichero Qu:")
print("'$fileqv'	#>>>>>Escribe fichero Qv:")
print("'$fileqdi'	#>>>>>Escribe fichero Qdi:")
print("!")

print("\n---\n")

# omegainve.exec
print("#!/bin/csh")
print("")
print("set dir = ./test/")
print("set fileinfo = {$dir}info_pr.dat")
print("set filestm = {$dir}ss1_st0.dat")
print("set fileqdi = {$dir}ss1a2qdi.gr")
print("set filew =   {$dir}ss1a2ww.gr")
print("")
print("./omegainv.exe << !")
print("'$fileinfo' 	#>>>>>Escribe info file info.dat:")
print("'$fileqdi' 	#>>>>>Escribe fichero de Div Q:")
print("'$filestm'   	#>>>>>Escribe fichero de densidad promedio:")
print("'ominput.dat'  #>>>>>Escribe fichero parametros (ominput.dat):")
print("'$filew'	#>>>>>Escribe fichero Salida W:")
print("!")