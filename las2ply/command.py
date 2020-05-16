import argparse
import las2ply.convert.las2ply


def las2ply_cmd():
    parser = argparse.ArgumentParser(description='las2ply')
    parser.add_argument('lasfiles', metavar='XXX.las', type=str, nargs='+',
                        help='input las file list')
    parser.add_argument('--output', '-o', metavar='<outputname>.ply', type=str,
                        help='output ply file', required=True)
    parser.add_argument('--voxel-size', type=float, default=None,
                        help='voxel down size')
    parser.add_argument('--skip-rate', type=float, default=0.8,
                        help='skip rate')
    parser.add_argument('--estimate-normals', type=bool, default=True,
                        help='estimate normal vectors')
    parser.add_argument('--write-ascii', type=bool, default=False,
                        help='write by ascii format')

    args = parser.parse_args()

    las2ply.convert.las2ply.las2ply(args.lasfiles, args.output,
                                    skip_rate=args.skip_rate,
                                    voxel_size=args.voxel_size,
                                    estimate_normals=args.estimate_normals,
                                    write_ascii=args.write_ascii)


if __name__ == "__main__":
    las2ply_cmd()
