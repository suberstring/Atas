import Token,sys

def parse(lst,DEBUG,ERRORNAME):
	state="Default"
	stack=[]
	efg=[]
	v=0
	#Main Loop
	for i in lst:
		if i.typ == "sent":
			if i.value == "print":
				state = "Io"
		elif i.typ == "char":
			if state == "Io":
				print(i.value)
		elif i.typ == "number":
			stack.append(i)
			if len(stack) == 3:
				if stack[1].value == "+":
					v = stack[0].value+stack[2].value
				if stack[1].value == "-":
					v = stack[0].value-stack[2].value
				if stack[1].value == "*":
					v = stack[0].value*stack[2].value
				if stack[1].value == "/":
					v = stack[0].value/stack[2].value
				if stack[1].value == "%":
					v = stack[0].value%stack[2].value
				stack = []
				if state == "Io":
					print(v)
		elif i.typ == "symbol":
			stack.append(i)
		elif i.typ == "space":
			pass
			state = "Default"
		else:
			if DEBUG and ERRORNAME:
				print("Error(NameUnknownError[1]):Unknown Value or Keyword.")
				print("Exception:Error.LexicalAnalysisError.QuotationMarksNumberError,\nDEBUG=\"TRUE\",ERRORNAME=\"TRUE\"")
				run=False
				#-1:ERROR,0:RUN_SUCCESSFULLY,1:WARNING_ONLY
				sys.exit(-1)
			elif not DEBUG:
				print("1 Error in LexicalAnalysis but turn into warning,\nINFORMATION:DEBUG=\"FALSE\",ERRORNAME=\"NULL\"")
			elif DEBUG and not ERRORNAME:
				print("Error(NameUnknownError[1]):Unknown Value or Keyword.")
				print("Exception:ERRORNAME_ISNOT_OPEN_WARNING(1),\nINFORMATION:DEBUG=\"TRUE\",ERRORNAME=\"FALSE\"")
				sys.exit(-1)