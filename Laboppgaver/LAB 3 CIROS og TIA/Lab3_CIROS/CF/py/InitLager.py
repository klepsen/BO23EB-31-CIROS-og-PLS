import sys
import importlib
import Ciros

#Eigenes Verzeichnis im Suchpfad ergänzen (Standardmäßig ist das CIROS.exe Verzeichnis eingetragen)
import os;
sys.path.append( os.path.dirname( sys.argv[0] ))

import CirosReplicator
importlib.reload(CirosReplicator)

	
cpr = CirosReplicator.LagerReplicator(sys.argv[1])

env = Ciros.Environment()
env.muteGUI(True)

cpr.initialize()
	
del env	
		