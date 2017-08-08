from subprocess import check_call


def init_parser(parser):
    parser.add_argument('name', type=str, help='Cluster name.')


def main(args):
    print("Stopping cluster '{}'...".format(args.name))

    check_call(['gcloud', 'dataproc', 'clusters', 'delete', '--quiet', args.name])
