import re,sys,os,parse
from Token import *

run=True
DEBUG = True
ERRORNAME = True
sys.path.append(os.getcwd())

with open("a.a") as rd:
	sc = rd.read()

if "#DEBUG 0" in sc:
	DEBUG=False
if "#ERRORNAME 0" in sc:
	ERRORNAME=False

#Lexer
def char_change(tp):
	return "@char|"+tp.group()+"@"

def sent_change(tp):
	return "@sent|"+tp.group()+"@"

def num_change(tp):
	return "@number|"+tp.group()+"@"

def sym_change(tp):
	return "@symbol|"+tp.group()+"@"

def space_change(tp):
	return "@space|"+tp.group()+"@"
sc = sc.replace("\\n","\n")
result = re.sub("\".*\"",char_change,sc,re.M)
result = re.sub("print",sent_change,result,re.M)
result = re.sub("\\d+",num_change,result,re.M)
result = re.sub("\\+|-|\\*|/",sym_change,result,re.M)
result = re.sub("\\n",space_change,result,re.M)
if sc.count("\"") % 2 != 0:
	if DEBUG and ERRORNAME:
		print("Error(QuotationMarksNumberError[2]):\"str or str\" is not be allowed.")
		print("Exception:Error.LexicalAnalysisError.QuotationMarksNumberError,\nDEBUG=\"TRUE\",ERRORNAME=\"TRUE\"")
		run=False
		sys.exit(-1)
	elif not DEBUG:
		print("1 Error in LexicalAnalysis but turn into warning,\nINFORMATION:DEBUG=\"FALSE\",ERRORNAME=\"NULL\"")
	elif DEBUG and not ERRORNAME:
		print("Error(QuotationMarksNumberError[2]):\"str or str\" is not be allowed.")
		print("Exception:ERRORNAME_ISNOT_OPEN_WARNING(1),\nINFORMATION:DEBUG=\"TRUE\",ERRORNAME=\"FALSE\"")
		run=False
		sys.exit(-1)

result = result.split("@")
res = []
tokens=[]
for i in result:
	if i[0:4] == "sent":
		if i[5:] == "print":
			tokens.append(Token("print","sent"))
	elif i[0:4] == "char":
		val = i.split('|')
		tokens.append(Token(val[1][1:-1],"char"))
	elif i[0:5] == "space":
		val = i.split('|')
		if val == "\\n":
			tokens.append(Token("\\n","space"))
	elif i[0:6] == "number":
		val = i.split('|')
		tokens.append(Token(int(val[1]),"number"))
	elif i[0:6] == "symbol":
		val = i.split('|')
		tokens.append(Token(val[1],"symbol"))
if run:
	parse.parse(tokens)
	sys.exit(0)