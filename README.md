# lifftoverfromvcf
Code to liftover VCF from one genome build to another

## Download gzipped chain files into your directory from:
http://hgdownload.cse.ucsc.edu/downloads.html#liftover

## To run:
python liftoverfromvcf.py oldvcf chainfile

## Optional Arguments:
--out : Output vcf file name

## Example Usage:
$ python liftoverfromvcf.py All8Rats-rn4_gVCFpool.4nt.Pooled.vcf rn4ToRn6.over.chain.gz --out out.vcf
