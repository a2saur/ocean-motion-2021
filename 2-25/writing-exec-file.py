import sys

open("vectorq.exec", "w").write("")
open("omegainv.exec", "w").write("")

vectorq = open("vectorq.exec", "a")
omegainv = open("omegainv.exec", "a")

date = sys.argv[1]
print(date)

vectorq.write("#!/bin/csh\n")
vectorq.write("\n")
vectorq.write("\n")
vectorq.write("set dir = ./test/\n")
vectorq.write("set dhdir = /Users/brownscholar/Desktop/A2_Internship/data/dynamic-height/\n")
vectorq.write("set dendir = /Users/brownscholar/Desktop/A2_Internship/data/density/\n")
vectorq.write("set auxdir = /Users/brownscholar/Desktop/A2_Internship/data/aux/\n")
vectorq.write("set outdir = /Users/brownscholar/Desktop/A2_Internship/data/omega/\n")
vectorq.write("set fileinfo = {$dir}info_pr.dat\n")
vectorq.write("set filedh =  {$dhdir}/dynamic_height_"+date+".gr\n")
vectorq.write("set filest =  {$dendir}/density_"+date+".gr\n")
vectorq.write("set filestm = {$auxdir}/st0/"+date+"_st0.dat\n")
vectorq.write("set filequ =  {$outdir}/u/"+date+"_qu.gr\n")
vectorq.write("set fileqv =  {$outdir}/v/"+date+"_qv.gr\n")
vectorq.write("set fileqdi = {$auxdir}/qdi/"+date+"_qdi.gr\n")
vectorq.write("\n")
vectorq.write("./vectorq.exe << !\n")
vectorq.write("'$fileinfo'	#>>>>>Escribe info file info.dat:\n")
vectorq.write("'$filedh'	#>>>>>Escribe fichero de altura Dinamica:\n")
vectorq.write("'$filest'	#>>>>>Escribe fichero de densidad:\n")
vectorq.write("'$filestm'	#>>>>>Escribe fichero de densidad promedio:\n")
vectorq.write("'$filequ'	#>>>>>Escribe fichero Qu:\n")
vectorq.write("'$fileqv'	#>>>>>Escribe fichero Qv:\n")
vectorq.write("'$fileqdi'	#>>>>>Escribe fichero Qdi:")

# -----------------------

omegainv.write("#!/bin/csh\n")
omegainv.write("\n")
omegainv.write("\n")
omegainv.write("set dir = ./test/\n")
omegainv.write("set fileinfo = {$dir}info_pr.dat\n")
omegainv.write("set outdir = /Users/brownscholar/Desktop/A2_Internship/data/omega/\n")
omegainv.write("set auxdir = /Users/brownscholar/Desktop/A2_Internship/data/aux/\n")
omegainv.write("set filestm = {$auxdir}/st0/"+date+"_st0.dat\n")
omegainv.write("set fileqdi = {$auxdir}/qdi/"+date+"_qdi.gr\n")
omegainv.write("set filew =  {$outdir}w/"+date+"_ww.gr\n")
omegainv.write("\n")
omegainv.write("./omegainv.exe << !\n")
omegainv.write("'$fileinfo' 	#>>>>>Escribe info file info.dat:\n")
omegainv.write("'$fileqdi' 	#>>>>>Escribe fichero de Div Q:\n")
omegainv.write("'$filestm'   	#>>>>>Escribe fichero de densidad promedio:\n")
omegainv.write("'ominput.dat'  #>>>>>Escribe fichero parametros (ominput.dat):\n")
omegainv.write("'$filew'	#>>>>>Escribe fichero Salida W:\n")
omegainv.write("\n")



