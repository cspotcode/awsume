from posixpath import basename
from sys import argv
import sys
import awsume.configure.main
import awsume.awsumepy.main
import awsume.autoawsume.main
import awsume_autocomplete.awsume_autocomplete

def main():
    # TODO Replace this logic with Nuitka's multidist feature?
    # https://nuitka.net/user-documentation/use-cases.html#use-case-6-multidist

    #################
    # Console Scripts
    # from setup.py
    #################
    # 'awsumepy=awsume.awsumepy.main:main',
    # 'autoawsume=awsume.autoawsume.main:main',
    # 'awsume-configure=awsume.configure.main:main',
    # 'awsume-autocomplete=awsume_autocomplete:main',
    bin = basename(argv[1])
    if bin == 'awsume-configure':
        awsume.configure.main.main()
    elif bin == 'awsumepy':
        awsume.awsumepy.main.main()
    elif bin == 'autoawsume':
        awsume.autoawsume.main.main()
    elif bin == 'awsume-autocomplete':
        awsume_autocomplete.awsume_autocomplete.main()
    else:
        print(f"Unable to determine which binary to execute from argv: {bin}", file=sys.stderr)
        exit(1)

main()
