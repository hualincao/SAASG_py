import ee

def load_s2(start_date, end_date, roi):
    s2 = (ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
          .filterBounds(roi)
          .filterDate(start_date, end_date))

    # 去云
    s2 = s2.map(lambda img:
        img.updateMask(img.select('MSK_CLDPRB').lt(20))
    )

    return s2


def load_s1(start_date, end_date, roi):
    s1 = (ee.ImageCollection("COPERNICUS/S1_GRD")
          .filterBounds(roi)
          .filterDate(start_date, end_date)
          .filter(ee.Filter.eq('instrumentMode', 'IW'))
          .filter(ee.Filter.eq('orbitProperties_pass', 'ASCENDING')))

    # 简单滤波
    def lee(img):
        return img.focal_mean(1).copyProperties(img, ['system:time_start'])

    return s1.map(lee)