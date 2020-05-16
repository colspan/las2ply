import argparse
import las2ply.convert.las2ply


def las2ply_cmd():
    parser = argparse.ArgumentParser(description='las2ply')
    parser.add_argument('lasfiles', metavar='XXX.las', type=str, nargs='+',
                        help='input las file list')
    parser.add_argument('output', metavar='output.ply', type=str,
                        help='output ply file')
    parser.add_argument('--voxel-size', type=float, default=None,
                        help='voxel down size')
    parser.add_argument('--skip-rate', type=float, default=0.8,
                        help='skip rate')

    args = parser.parse_args()

    las2ply.convert.las2ply.las2ply(args.lasfiles, args.output,
                                    skip_rate=args.skip_rate, voxel_size=args.voxel_size)


if __name__ == "__main__":
    las2ply_cmd()