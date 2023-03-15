import Ciros

class MESCommunication( object ):
	def __init__( self, fakeID ):
		self.id = fakeID
		
	def getContent( self, ans, name ):
		start = ans.find( "["+name+":" )
		if start == -1:
			return( int(0) )
		else: 
			start += len(name)+2
		
		end = ans.find("]", start )
		
		return( int(ans[start:end]) )
		
	def getParameter( self, ans, parNr ):
		return( self.getContent(ans, "Parameter"+str(parNr)))
		
	def GetBufferContent(self, mesId, bufferNo, maxRecords):
		# GetPartsInBufCiros (IN real : resourceId; IN real : bufNo; IN real : bufPos; IN real : maxRecords);
		# 	O_MClass := 150;
		# 	O_MNo := 16;
		# 	O_ResourceID := resourceId;
		# 	O_BufNo := bufNo;	
		# 	O_BufPos := starBufPos;	
		# 	O_MaxRecords := maxRecords;
		req = "[TcpIdent:1][RequestID:" + str(self.id) + "][MClass:150][MNo:16][ResourceID:" + str(mesId)+ "][BufNo:" + str(bufferNo)+ "][BufPos:1][MaxRecords:"+str(maxRecords)+"]"
		env = Ciros.Environment()
		ans = env.sendMESMessage(req)
		del env
		
		ret = []
		for i in range(maxRecords):
			ret.append( self.getParameter(ans, i))
			
		return( ret )
		
	def GetBoxPosAll(self, boxId, boxPNo, maxRecords):
		req = "[RequestID:" + str(self.id) + "][MClass:150][MNo:71][BoxID:" + str(boxId)+ "][BoxPNo:" + str(boxPNo)+ "][MaxRecords:"+str(maxRecords)+"]"
		env = Ciros.Environment()
		ans = env.sendMESMessage(req)
		del env
		
		ret = []
		for i in range(maxRecords):
			ret.append( self.getParameter(ans, i))
			
		return( ret )