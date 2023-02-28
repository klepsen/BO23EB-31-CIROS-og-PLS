import sys
import importlib

#Eigenes Verzeichnis im Suchpfad ergänzen (Standardmäßig ist das CIROS.exe Verzeichnis eingetragen)
import os;
sys.path.append( os.path.dirname( sys.argv[0] ))

import CirosReplicator
#importlib.reload(CirosReplicator)

import CirosMESCom
#importlib.reload(CirosMESCom)
		
mesCom = CirosMESCom.MESCommunication(0)

boxId = 0
boxType = 0
maxPlaces = 15
partIds = []

cpr = CirosReplicator.PartNr(sys.argv[1])		

if( boxId != 0 ):
	#boxType
	partIds = mesCom.GetBoxPosAll( boxId, boxType, maxPlaces )
	print( "TBI: Abfrage des Boxtyps und Inhalts vom MES" )
else:
	boxType = cpr.replObj.getInput( "BoxTyp" )
	for pos in range(maxPlaces):
		inputName = "Fach_%s" % (pos+1)
		partIds.append( cpr.replObj.getInput( inputName ))

env = Ciros.Environment()
env.muteGUI(True)

ret = cpr.createInlay( boxType )

if ret != None:
	inlayRepl = CirosReplicator.PartNr(ret)		
	skipPalette = boxType != 2
	root_gpp = "Bauchlage_"
	if boxType == 3: 
		root_gpp = "GPP_Platine_"
	for pos, partId in zip(range( maxPlaces ), partIds):
		gpp = root_gpp + str(pos) + "_Inlay"
		inlayRepl.replicateAt(skipPalette, partId, gpp )
	
del env