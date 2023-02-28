import sys
import importlib

#Eigenes Verzeichnis im Suchpfad ergänzen (Standardmäßig ist das CIROS.exe Verzeichnis eingetragen)
import os;
sys.path.append( os.path.dirname( sys.argv[0] ))

import CirosReplicator
#importlib.reload(CirosReplicator)

cpr = CirosReplicator.PartNr(sys.argv[1])
cpr.checkForRepl()

#import CirosMESCom
#importlib.reload(CirosMESCom)
		
#mesCom = CirosMESCom.MESCommunication(0)
#print( mesCom.GetBufferContent( 100, 1, 50 ))
	
	
	
		