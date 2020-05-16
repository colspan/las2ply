import numpy as np
import random
from laspy.file import File

class LasFile():
    def __init__(self, filename):
        las = File(filename, mode="r")
        self.obj = las

    # def __del__(self):
        # self.obj.close()

    def toarray(self, skip_rate=0):
        point_records = self.obj.points

        cnt = len(self.obj)
        ptdata = np.zeros((cnt, 7), dtype=np.float64)

        colmap = [
            'X',
            'Y',
            'Z',
            'intensity',
            'red',
            'green',
            'blue',
        ]
        for i, col in enumerate(colmap):
            ptdata[:, i] = point_records['point'][col].astype(np.float64)
        # ptdata = np.vstack(
        #     [point_records['point'][col].astype(np.float64) for col in colmap]).T

        # apply scale and offset for xy
        for i in range(3):
            ptdata[:, i] *= self.obj.header.scale[i]
            ptdata[:, i] += self.obj.header.offset[i]

        # scale colors
        ptdata[:, 3:] /= 65536.0

        if 0 < skip_rate < 1.0:
            idx = np.random.randint(
                ptdata.shape[0], size=int(ptdata.shape[0]*(1-skip_rate)))
            ptdata = ptdata[idx, :]

        return ptdata
