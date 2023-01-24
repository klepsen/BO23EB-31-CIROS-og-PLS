import importlib
import Ciros
import random
import sys
import CirosMESCom
#importlib.reload(CirosMESCom)

verbose = False
def log( txtList ):
	if verbose:
		print(txtList)

env = Ciros.Environment()
		
#Teilnummern
# Spezielle Teilenummern für CIROS
# 90, 91, 92, 93: Front- und Rückschale, lose aufeinander gestapelt (Bereit zum Verpressen) in sw, gr, bl, und rt
# 10, 120, 121, 122, 123: nur Platzhalter, ersetzen mit echter MES ID für Drehteil und Platine

PN_Palette = [25]

PN_Drehteil = [10] 

PN_Front_Roh_sw = [101]
PN_Front_Roh_gr = [102]
PN_Front_Roh_bl = [103]
PN_Front_Roh_rt = [104]

PN_Front_Lochlos_sw = [110]
PN_Front_Lochlos_gr = [109]
PN_Front_Lochlos_bl = [108]
PN_Front_Lochlos_rt = [107]

PN_Front_sw = [90, 210, 211, 212, 213, 214, 1210, 1211, 1212, 1213, 1214]
PN_Front_gr = [91, 310, 311, 312, 313, 314, 1310, 1311, 1312, 1313, 1314]
PN_Front_bl = [92, 410, 411, 412, 413, 414, 1410, 1411, 1412, 1413, 1414]
PN_Front_rt = [93, 510, 511, 512, 513, 514, 1510, 1511, 1512, 1513, 1514]

PN_Back_sw = [1210, 1211, 1212, 1213, 1214]
PN_Back_gr = [1310, 1311, 1312, 1313, 1314]
PN_Back_bl = [1410, 1411, 1412, 1413, 1414]
PN_Back_rt = [1510, 1511, 1512, 1513, 1514]

PN_Platine = [120, 121, 122,123, 211, 311, 411, 511, 212, 312, 412, 512, 213, 313, 413, 513, 214, 314, 414, 514, 1211, 1311, 1411, 1511, 1212, 1312, 1412, 1512, 1213, 1313, 1413, 1513, 1214, 1314, 1414, 1514 ]

PN_Sicherung_A = [121, 123, 212, 312, 412, 512, 214, 314, 414, 514, 1212, 1312, 1412, 1512, 1214, 1314, 1414, 1514]

PN_Sicherung_B = [122, 123, 213, 313, 413, 513, 214, 314, 414, 514, 1213, 1313, 1413, 1513, 1214, 1314, 1414, 1514]

#Farbcodierung (Vereinfachung für manuelle Erzeugung von WS
PN_by_color = [\
	[90, 91, 92, 93],\
	[101, 102, 103, 104],\
	[110, 109, 108, 107],\
	[111, 112, 113, 114],\
	[210, 310, 410, 510],\
	[211, 311, 411, 511],\
	[212, 312, 412, 512],\
	[213, 313, 413, 513],\
	[214, 314, 414, 514],\
	[1210, 1310, 1410, 1510],\
	[1211, 1311, 1411, 1511],\
	[1212, 1312, 1412, 1512],\
	[1213, 1313, 1413, 1513],\
	[1214, 1314, 1414, 1514],\
	]
	
Box_Type_Templates = [	[1, "Kiste_Inlay_Drehteil"], 
						[2, "Kiste_Inlay_Palette"],
						[3, "Kiste_Inlay_Platinen"],
						[4,  "Kiste_Inlay_WS"]]
			
class internalPartNr(object):
	def __init__( self, Fehlteile_SicherungA, Fehlteile_SicherungB):
		object.__init__(self)
				
		#Abkürzende Schreibweise...
		root_gpp_list = ['Bauchlage', 'Rueckenlage']
		root_gpp_list_kpl = root_gpp_list +['Komplett_Rueckenlage']
		
		# Zur Erzeugung verwendeter GPP			Templatename					Metaname			Teilnummern			Eingangsliste d. Fehler %		Fehlertemplates
		self.PNList_Template = [\
			['Bauchlage',	 					'Palette', 						'Paletten',			PN_Palette, 		[], 							[]],\
			['Bauchlage',	 					'CP_Drehteil', 					'Drehteile',		PN_Drehteil, 		[], 							[]],\
			[root_gpp_list,						'CP_Frontschale_Rohteil_sw', 	'Frontschalen',		PN_Front_Roh_sw,	[], 							[]],\
			[root_gpp_list,						'CP_Frontschale_Rohteil_gr', 	'Frontschalen',		PN_Front_Roh_gr,	[], 							[]],\
			[root_gpp_list,						'CP_Frontschale_Rohteil_bl', 	'Frontschalen',		PN_Front_Roh_bl,	[], 							[]],\
			[root_gpp_list,						'CP_Frontschale_Rohteil_rt', 	'Frontschalen',		PN_Front_Roh_rt,	[], 							[]],\
			[root_gpp_list,						'CP_Frontschale_Lochlos_sw', 	'Frontschalen',		PN_Front_Lochlos_sw,[], 							[]],\
			[root_gpp_list,						'CP_Frontschale_Lochlos_gr', 	'Frontschalen',		PN_Front_Lochlos_gr,[], 							[]],\
			[root_gpp_list,						'CP_Frontschale_Lochlos_bl', 	'Frontschalen',		PN_Front_Lochlos_bl,[], 							[]],\
			[root_gpp_list,						'CP_Frontschale_Lochlos_rt', 	'Frontschalen',		PN_Front_Lochlos_rt,[], 							[]],\
			[root_gpp_list_kpl,					'CP_Frontschale_sw', 			'Frontschalen',		PN_Front_sw,		[], 							[]],\
			[root_gpp_list_kpl,					'CP_Frontschale_gr', 			'Frontschalen',		PN_Front_gr, 		[], 							[]],\
			[root_gpp_list_kpl,					'CP_Frontschale_bl', 			'Frontschalen',		PN_Front_bl, 		[], 							[]],\
			[root_gpp_list_kpl,					'CP_Frontschale_rt', 			'Frontschalen',		PN_Front_rt, 		[], 							[]],\
			[root_gpp_list,						'CP_Rueckschale_sw', 			'Rueckschalen',		[111],				[], 							[]],\
			[root_gpp_list,						'CP_Rueckschale_gr', 			'Rueckschalen',		[112],				[], 							[]],\
			[root_gpp_list,						'CP_Rueckschale_bl', 			'Rueckschalen',		[113],				[], 							[]],\
			[root_gpp_list,						'CP_Rueckschale_rt', 			'Rueckschalen',		[114],				[], 							[]],\
			[['GPP_Rueckschale'],				'CP_Rueckschale_sw', 			'Rueckschalen',		PN_Back_sw,			[], 							[]],\
			[['GPP_Rueckschale'],				'CP_Rueckschale_gr', 			'Rueckschalen',		PN_Back_gr,			[], 							[]],\
			[['GPP_Rueckschale'],				'CP_Rueckschale_bl', 			'Rueckschalen',		PN_Back_bl,			[], 							[]],\
			[['GPP_Rueckschale'],				'CP_Rueckschale_rt', 			'Rueckschalen',		PN_Back_rt,			[], 							[]],\
			[['Rueckschale_aufgelegt_Palette'],	'CP_Rueckschale_sw', 			'Rueckschalen',		[90],				[], 							[]],\
			[['Rueckschale_aufgelegt_Palette'],	'CP_Rueckschale_gr', 			'Rueckschalen',		[91],				[], 							[]],\
			[['Rueckschale_aufgelegt_Palette'],	'CP_Rueckschale_bl', 			'Rueckschalen',		[92],				[], 							[]],\
			[['Rueckschale_aufgelegt_Palette'],	'CP_Rueckschale_rt', 			'Rueckschalen',		[93],				[], 							[]],\
			[['GPP_Platine'],					'CP_Platine', 					'Platinen',			PN_Platine,			[], 							[]],\
			[['GPP_SicherungA'],				'CP_Schmelzsicherung', 			'Sicherungen',		PN_Sicherung_A,		[Fehlteile_SicherungA], 		['CP_Schmelzsicherung_defekt']],\
			[['GPP_SicherungB'],				'CP_Schmelzsicherung', 			'Sicherungen',		PN_Sicherung_B,		[Fehlteile_SicherungB], 		['CP_Schmelzsicherung_defekt']],\
			]
			
	def replicatePart( self, partNr, gpp_name ):
		log( '    Test: PNo [' + str(partNr) + '] am GPP [' + gpp_name + ']' )
		ret = ''
		
		#Passenden Eintrag suchen
		for entry in self.PNList_Template:
			possible_gpps 	= entry[0]
			partNr_List 	= entry[3]
		
			#Wenn Bauteilnummer am aktuellen GPP erzeugt werden soll
			if partNr in partNr_List:
				for possible_gpp in possible_gpps:
					if gpp_name.startswith( possible_gpp ):
						template_name 	= self.getTemplateNameByErrorGeneration(entry)
						meta_name 		= entry[2]
						
						#Template instantiieren
						#TODO: .modx laden
						ret = env.addObjectFromTemplate( template_name, gpp_name, meta_name )
						log( '        -> [' + ret + '] erzeugt' )
						if( partNr == 25 ):
							break				
						
						#Echte Namen der Folgegreiferpunkte ermitteln
						replObject = Ciros.Object(ret)
						replObjectGPPs = replObject.getGripperNameList()
						for replGPP in replObjectGPPs:
							self.replicatePart( partNr, replGPP )
		return ret 

	def getTemplateNameByErrorGeneration(self, entry ):
		ret = entry[1]
		total = 0
		r = random.random()*100
		index = 0
		for errror_percent in entry[4]:
			if r > total and r < total+errror_percent:
				log( '    Errorpart: [' + entry[1] + '] ersetzt durch [' + entry[5][index] + ']' )
				ret = entry[5][index]
			total += errror_percent
			index += 1

		#sanity check
		if total > 100:
			print( 'Replikator [' + self.replObj + ']: Mehr als 100% Fehlteile konfiguriert!' )
		
		return( ret )

class PartNr( object ):
	def __init__( self, objectname ):
		#Aktuelles Replikatorobjekt
		self.objectname = objectname
		self.replObj = Ciros.Object(objectname)
		#Lage		
		self.ventral = True #self.replObj.getInput('Bauchlage')

		#Fehlteilgenerierung
		#Fehlteilgenerierung nur aktivieren falls ein neuer Random Seed erzeugt werden kann. 
		self.Fehlteile_SicherungA = 0
		self.Fehlteile_SicherungB = 0
		self.Fehlteil_verdreht = 0;
		input_names = self.replObj.getInputNameList()
		if 'RandomSeedFromSimulation' in input_names:
			random.seed( self.replObj.getInput('RandomSeedFromSimulation'))
			if 'Fehlteile_SicherungA' in input_names:
				self.Fehlteile_SicherungA = self.replObj.getInput('Fehlteile_SicherungA')
			if 'Fehlteile_SicherungB' in input_names:
				self.Fehlteile_SicherungB = self.replObj.getInput('Fehlteile_SicherungB')
			if 'Fehlteil_verdreht' in input_names:
				self.Fehlteil_verdreht = self.replObj.getInput('Fehlteil_verdreht')
	
	def checkForRepl(self):
		#zu erzeugende TeileNr
		partNr = self.replObj.getInput( 'TeilNr' )
		deleteFirst = self.replObj.getInput( 'ErstLoeschen' )
		
		#Für Schwarzteil / Farbe Kombination die korrekte Teilnummer finden
		if partNr == 0:
			#zu erzeugende TeileNr (in schwarz)
			partNr_sw = self.replObj.getInput( 'TeilNr_sw' )
			#Farbe der zu erzeugenden partNr_sw
			farbe = int(self.replObj.getInput( 'Farbe' ))
		
			if (farbe < 0) or (farbe > 3):
				print( 'Replikator [' + replObj + ']: Farbe ' + str(farbe) + ' nicht hinterlegt!' )
				sys.exit(0)
			partNr = partNr_sw
			for colors in PN_by_color:
				if colors[0] == partNr_sw:
					partNr = colors[farbe]
		

		partNrReplicator = internalPartNr(self.Fehlteile_SicherungA, self.Fehlteile_SicherungB)
				
		if deleteFirst:
			log( '    Teil am GPP "Bauchlage" löschen' )
			self.deleteAtGripper('Bauchlage')
		else:
			log( '    Löschen überspringen' )

		#Palette erzeugen falls gewünscht
		if self.replObj.getInput( 'Palette' ):
			ventral_gpp =self.findGPPStartingWith( 'Bauchlage')
			palName = partNrReplicator.replicatePart( 25, ventral_gpp )
			del self.replObj;
			self.replObj = Ciros.Object(palName)
			
			#Wenn nur eine Palette erzeugt werden sollte -> Fertig, keine Fehlermeldung
			if( partNr == 25 ):
				partNr = 0
			
		#instantiierten GPP für diesen Replikator/diese Palette finden
		gppStartName = self.findRootGPPName(partNr) # bauchlage / Rücklage
		#Sonderbehandlung für Platinen mit und ohne Sicherung
		if partNr >= 120 and partNr <= 125 :
			gppStartName = "GPP_Platine"
		#Sonderbehandlung für aufgelegte Rückschalen
		if partNr >= 90 and partNr <= 93:
			gppStartName = self.findGPPStartingWith( 'Rueckschale_aufgelegt_Palette')
		#GPP Instanz finden
		root_gpp =self.findGPPStartingWith(gppStartName )

		log('Replicate: Obj:[' + self.objectname+'] GPP:['+  root_gpp + '] PNo:['+str(partNr)+']' )
		ret = partNrReplicator.replicatePart( partNr, root_gpp )
		if( ret == '' and partNr != 0  ):
			env.addObjectFromTemplate( "CP_Unbekannt", root_gpp, "Frontschalen" )
			#print( 'Replikator [' + self.objectname + ']: Konnte TeilNr [' + str(partNr) + '] nicht erzeugen' )

		
	def createInlay( self, boxType ):
		root_gpp =self.findGPPStartingWith( "GPP_Inlay" )
		self.deleteAtGripper(root_gpp)

		ret = None
		#Find inlay
		for i in Box_Type_Templates:
			if i[0] == boxType:
				ret = env.addObjectFromTemplate( i[1], root_gpp, "Inlays" )
		return( ret )
		
	def deleteAtGripper(self, gpp):
		gpp_name = self.findGPPStartingWith(gpp)
		object_and_gpp = env.findGrippableObjectForGripper( gpp_name )
		if object_and_gpp[0]:
			log( '    Delete: Am GPP [' + gpp_name + '] das Objekt ['+object_and_gpp[0] +']'		)
			env.deleteObject(object_and_gpp[0] )
		
	def findRootGPPName(self, partNr):
		turnOver = not self.ventral
		r = random.random()*100
		if r < self.Fehlteil_verdreht:
				turnOver = not turnOver
				log( '    Errorpart: Teil verdreht' )
			
		ret = 'Bauchlage'
		if turnOver:
			if partNr > 1000:
				ret = 'Komplett_Rueckenlage'
			else:	
				ret = 'Rueckenlage'
		return( ret )			

	def findGPPStartingWith( self, gpp_start ):
		for GPP in self.replObj.getGripperNameList():
			if GPP.startswith(gpp_start):
				return( GPP )
		return( '' )	
		
		
class LagerReplicator( PartNr ):
	def __init__( self, objectname ):
		PartNr.__init__(self, objectname)
		
		resId = self.replObj.getInput( "MyResourceId" )
		self.nrOfPlaces = int(self.replObj.getInput( "AnzahlFächer" ))
		self.skipPalette = bool(self.replObj.getInput( "OhnePalette" ))
		self.partIds = []

		if( resId != 0 ):
			mesCom = CirosMESCom.MESCommunication(0)
			self.partIds = mesCom.GetBufferContent( resId, 1, self.nrOfPlaces )
			del mesCom
		else:
			for pos in range( self.nrOfPlaces ):
				inputName = "Fach_%s" % (pos+1)
				self.partIds.append( self.replObj.getInput( inputName ))
				
	def initialize( self ):
		for pos, partNr in zip(range( self.nrOfPlaces ), self.partIds):
		
			print( pos, partNr )
		
			gpp_name = "Bauchlage_" + str(pos) + "_Lager"
	
			root_gpp =self.findGPPStartingWith( gpp_name )
			if( root_gpp == '' ):
				return
			self.deleteAtGripper( gpp_name)
			
			if( partNr == 0 ):
				return
					
			partNrReplicator = internalPartNr(self.Fehlteile_SicherungA, self.Fehlteile_SicherungB)
			saveObj =  self.replObj;

			if not self.skipPalette:
				ret = partNrReplicator.replicatePart( 25, root_gpp )
				self.replObj = Ciros.Object(ret)
				if( partNr == 25 ):
					partNr = 0
				#instantiierten GPP für diesen Replikator/diese Palette finden
				root_gpp =self.findGPPStartingWith( self.findRootGPPName(partNr))

			log('Replicate: Obj:[' + self.objectname+'] GPP:['+  root_gpp + '] PNo:['+str(partNr)+']' )
			ret = partNrReplicator.replicatePart( partNr, root_gpp )
			if( ret == '' and partNr != 0  ):
				env.addObjectFromTemplate( "CP_Unbekannt", root_gpp, "Frontschalen" )
				#print( 'Replikator [' + self.objectname + ']: Konnte TeilNr [' + str(partNr) + '] nicht erzeugen' )	
				
			self.replObj = saveObj;		