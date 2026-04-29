import ee
import numpy as np
from scipy.interpolate import interp1d
from scipy.signal import savgol_filter

from gee.data_preprocess import load_s2
from gee.feature_extraction import add_ndvi, add_cndvi

ee.Initialize()

# ===== 参数 =====
START = '2024-03-01'
END   = '2024-11-30'

local_file = "../data/2024_调研点_整理.shp"

# ===== 读取样本 =====
points = geemap.shp_to_ee(local_file)

# ===== Sentinel-2 =====
s2 = load_s2(START, END, points.geometry())
s2 = s2.map(add_ndvi)
s2 = s2.map(add_cndvi)

# ===== 时间标记 =====
def add_time(img):
    date = ee.Date(img.get('system:time_start'))
    doy = date.getRelative('day', 'year')
    return img.set('doy', doy)

s2 = s2.map(add_time)

# ===== 采样函数 =====
def sample_image(img):
    samples = img.select('ndvi').sampleRegions(
        collection=points,
        scale=10
    )
    return samples.map(lambda f: f.set('time', img.get('doy')))

# ===== 提取时序 =====
fc = s2.map(sample_image).flatten()
data = fc.getInfo()

# ===== 转 Python =====
result = {}
for f in data['features']:
    pid = f['properties'].get('system:index')
    t = f['properties']['time']
    v = f['properties']['ndvi']

    if pid not in result:
        result[pid] = {'time':[], 'ndvi':[]}

    result[pid]['time'].append(t)
    result[pid]['ndvi'].append(v)

# ===== 插值 + 平均 =====
common_time = np.arange(90,280,5)

all_series = []

for k in result:
    t = np.array(result[k]['time'])
    v = np.array(result[k]['ndvi'])

    if len(t) < 5:
        continue

    f = interp1d(t, v, bounds_error=False, fill_value=np.nan)
    all_series.append(f(common_time))

all_series = np.array(all_series)

mean_curve = np.nanmean(all_series, axis=0)
std_curve  = np.nanstd(all_series, axis=0)

# SG滤波
mean_curve = savgol_filter(mean_curve, 11, 2)

np.save("../results/mean_curve.npy", mean_curve)
np.save("../results/time.npy", common_time)

print("S-MPFC 构建完成")