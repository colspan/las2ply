import numpy as np
import open3d as o3d

from las2ply.format.las import LasFile
from las2ply.format.ply import PlyFile


def las2ply(input_paths, out_path, skip_rate=0.5, voxel_size=None):
    las_files = map(LasFile, input_paths)
    lasdataset = map(lambda x: x.toarray(skip_rate=skip_rate), las_files)
    lasdata = np.concatenate(list(lasdataset))

    plydata = PlyFile(data=lasdata)
    pcd = plydata.obj

    # 指定したvoxelサイズでダウンサンプリング
    if voxel_size is not None:
        pcd = o3d.geometry.PointCloud.voxel_down_sample(
            pcd, voxel_size=voxel_size)

    o3d.io.write_point_cloud(out_path, pcd)
