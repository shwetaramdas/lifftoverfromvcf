# liftoverfromvcf
Code to liftover VCF from one genome build to another. Uses the UCSC liftOver tool, but performs all the steps necessary to convert one VCF to another (and generates the intermediate bed files.)

## Download the relevant gzipped chain files into your directory from:
http://hgdownload.cse.ucsc.edu/downloads.html#liftover

## To run:
Run from the folder containing the liftoverfromvcf.py folder (and the liftOver tool).

python liftoverfromvcf.py oldvcf chainfile

## Optional Arguments:
--out : Output vcf file name. If not provided, default output is LIFTEDOVER.vcf.
--chr : If the chain file has the 'chr' prefix, and the input VCF file does not have it, use this option.

## Example Usage:
$ python liftoverfromvcf.py All8Rats-rn4_gVCFpool.4nt.Pooled.vcf rn4ToRn6.over.chain.gz --out out.vcf
