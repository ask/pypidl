import sys
import optparse
from pypidl import download_package


OPTION_LIST = (
        optparse.make_option('-i', '--index', default=None,
            action="store", dest="index", type="str",
            help="Use a custom PyPI index server.",
        ),
        optparse.make_option('-V', '--version', default=None,
            action="store",
            help="Specify a version to download.",
        ),
        optparse.make_option('-e', '--egg', default=False,
            action="store_true", dest="egg",
            help="Fetch the egg package (otherwise the source)",
        ),
        optparse.make_option('-u', '--unlink', default=False,
            action="store_true", dest="unlink",
            help="Remove existing files.",
        ),
        optparse.make_option('-d', '--dest', default=".",
            action="store", type="str",
            help="Destination directory (default is: current directory).",
        ),
)


def parse_options(arguments):
    """Parse available options."""
    parser = optparse.OptionParser(option_list=OPTION_LIST)
    options, values = parser.parse_args(arguments)
    return options, values


def main(package, dest=None, unlink=None, version=None, index=None, egg=None):
    download_package(package, directory=dest, unlink=unlink, version=version,
                     index=index, source=not egg)


if __name__ == "__main__":
    options, args = parse_options(sys.argv[:1])
    if not len(args) >= 2:
        sys.stderr.write("Must specify package name")
    print("ARGS: %s" % str(args))
    main(args[2], **vars(options))
