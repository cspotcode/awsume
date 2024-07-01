from posixpath import basename
import sys
from awsume.configure import main as configure_main
from awsume.awsumepy import main as awsume_py_main
from awsume.autoawsume import main as autoawsume_main
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
    
    bin = basename(sys.argv[0])
    # bin = basename(sys.argv[1]) if len(sys.argv) > 1 else ""
    # print(sys.argv)
    # bin = "autoawsume"

    if bin == 'awsumepy':
        awsume_py_main.main()
    elif bin == 'awsume-configure':
        configure_main.main()
    elif bin == 'autoawsume':
        autoawsume_main.main()
    elif bin == 'awsume-autocomplete':
        awsume_autocomplete.awsume_autocomplete.main()
    else:
        print(f"Unable to determine which binary to execute from argv: {bin}", file=sys.stderr)
        exit(1)

main()
