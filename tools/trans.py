import sys
import os
import indic_transliteration as it
from indic_transliteration import sanscript as sn

schemes = {
	'ben':sn.BENGALI,
	'dev':sn.DEVANAGARI,
	'guj':sn.GUJARATI,
	'gur':sn.GURMUKHI,
	'kan':sn.KANNADA,
	'mal':sn.MALAYALAM,
	'ori':sn.ORIYA,
	'tam':sn.TAMIL,
	'tel':sn.TELUGU,
	'hk':sn.HK,
	'iast':sn.IAST,
	'itrans':sn.ITRANS,
	'kolkata':sn.KOLKATA,
	'slp1':sn.SLP1,
	'velthuis':sn.VELTHUIS,
	'wx':sn.WX,
}

def lookupscheme(name):
	print("Looking up", name)
	name = name.lower()
	if name in schemes:
		return schemes[name]
	elif name[:3] in schemes:
		return schemes[name[:3]]
	else:
		raise("Unknown Language:", name)

def transfile(fname, frm, to, outfname):
	with open(fname) as fp:
		data = fp.read()

	newdata = sn.transliterate(data, frm, to)

	with open(outfname, "w") as ofp:
		ofp.write(newdata)

if __name__ == "__main__":

	if len(sys.argv) < 4:
		print("""
				Usage:
				{} <from> <to> filename.txt [outputdir]
				from and to are language codes like "telugu, kannada, devanagari, etc."
				""".format(sys.argv[0]))
		sys.exit()

	frm = lookupscheme(sys.argv[1])
	to = lookupscheme(sys.argv[2])
	fname = sys.argv[3]

	basename = os.path.basename(fname)
	try:
		outdir = sys.argv[4]
		assert(os.path.isdir(outdir))
	except:
		outdir = "."

	outfname = os.path.join(outdir, basename)

	transfile(fname, frm, to, outfname)
