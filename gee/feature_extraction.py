import ee

def add_ndvi(img):
    ndvi = img.normalizedDifference(['B8','B4']).rename('ndvi')
    return img.addBands(ndvi)

def add_cndvi(img, TP=0.00002):
    contrast = (img.select('B8')
                .toInt()
                .glcmTexture(1)
                .select('B8_contrast'))

    ndvi = img.normalizedDifference(['B8','B4'])

    cndvi = ndvi.multiply(
        ee.Image(1).subtract(contrast.multiply(-TP).exp())
    ).rename('cndvi')

    return img.addBands([contrast, cndvi])

def add_sar(img):
    sar = img.select('VV').add(img.select('VH')).rename('sar')
    return img.addBands(sar)