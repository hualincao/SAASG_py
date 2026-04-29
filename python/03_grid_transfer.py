import ee
import numpy as np
from tqdm import tqdm

from gee.data_preprocess import load_s2
from gee.feature_extraction import add_ndvi
from python.02_ms_twdtw import dtw

ee.Initialize()

# ===== 候选点 =====
def generate_points(roi, n=100):
    pts=[]
    for _ in range(n):
        lon = np.random.uniform(roi[0], roi[2])
        lat = np.random.uniform(roi[1], roi[3])
        pts.append(ee.Feature(ee.Geometry.Point([lon,lat])))
    return ee.FeatureCollection(pts)

# ===== 示例ROI =====
roi = [115,35,118,38]
points = generate_points(roi)

# ===== S2 =====
s2 = load_s2('2024-03-01','2024-11-30',points.geometry())
s2 = s2.map(add_ndvi)

# ===== 这里你继续接你原来的流程 =====
print("Grid transfer模块完成")