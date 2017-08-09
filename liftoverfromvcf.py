import os
import sys
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("vcf")
parser.add_argument("chain")
parser.add_argument("--out","-o",nargs="?",default="LIFTEDOVER.vcf")
parser.add_argument("--chr",help="Using --chr adds the prefix 'chr' to the bed file")

args = parser.parse_args()
#print args.vcf
#print args.chain
#if args.out:
#	print args.out

if args.chr:
	command = 'grep -v "^#" ' + args.vcf+ '| ' + " awk '{print \"chr\"$1\" \"$2-1\" \"$2}'"+ ' > old.bed'
else:
	command = 'grep -v "^#" ' + args.vcf+ '| ' + " awk '{print $1\" \"$2-1\" \"$2}'"+ ' > old.bed'

print("Reading VCF...may take a few minutes for large VCFs...")
#return_code = os.system(command)

command = "./liftOver old.bed " + args.chain + " new.bed unmapped.txt"
#os.system(command)

print("Reading in unmapped co-ordinates...")
unmapped = dict()
unMappedfile = open("unmapped.txt")
for line in unMappedfile:
        line = line.rstrip()
        if line[0] == '#':
                continue

        temp = line.split()
        unmapped[temp[0] + ":" + temp[1]] = 1

unMappedfile.close()

print("Reading in new coordinates...")
#mapped file
mapped = open("new.bed")
mappedpos = []
for line in mapped:
#       print(line)
        line = line.rstrip()
        temp = line.split()
        mappedpos.append(temp[0] + "\t" + str(int(temp[1])+1))

mapped.close()

print("Creating new VCF...\n")
allold = open(args.vcf)
writenewvcf = open(args.out ,"w")

#print("Here")
NEWINDEX = 0
for line in allold:
        if line[0] == '#':
                writenewvcf.write(line)
        else:
                line = line.rstrip()
                temp = line.split()
                pos = temp[0] + ":" + str(int(temp[1])-1)
                if unmapped.has_key(pos):

                        donothing=1
                else:
                        writenewvcf.write(mappedpos[NEWINDEX] + "\t".join(temp[2:]) + "\n")
                        NEWINDEX += 1

allold.close()
writenewvcf.close()

print("Done!")
