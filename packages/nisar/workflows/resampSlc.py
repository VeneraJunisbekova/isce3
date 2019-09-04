#!/usr/bin/env python3
#
# Author: Liang Yu
# Copyright 2019-

import os
import gdal
from nisar.products.readers import SLC
from isce3.image.ResampSlc import ResampSlc
from isce3.io.Raster import Raster

def cmdLineParse():
    """
    Command line parser.
    """
    parser = argparse.ArgumentParser(description="""
        Run resampSlc.""")

    # Required arguments
    parser.add_argument('product', type=str,
            help='Input HDF5 to be resampled.')
    parser.add_argument('frequency', type=str,
            help='Frequency of SLC.')
    parser.add_argument('polarization', type=str,
            help='Polarization of SLC.')

    # Optional arguments
    parser.add_argument('outdir', type=str, action='store', default='resampSlc',
            help='Output directory. Default: offsets.')
    parser.add_argument('offsetdir', type=str, action='store', default='offsets',
            help='Input offset directory. Default: offsets.')
    parser.add_argument('linesPerTile', type=int, action='store', default=0,
            help='Number of lines resampled per iteration. Default: 0')

    # Parse and return
    return parser.parse_args()


def main(opts):
    """
    resample SLC
    """

    # prep SLC dataset input
    productSlc = SLC(hdf5file=opts.product)

    # get grids needed for resamp object instantiation
    productGrid = productSlc.getRadarGrid(opts.frequency)

    # instantiate resamp object
    resamp = ResampSlc(productGrid,
            productSlc.getDopplerCentroid(),
            productGrid.wavelength)
    
    # set number of lines per tile if arg > 0
    if opts.linesPerTile:
        resamp.linesPerTile = opts.linesPerTile

    # Prepare input rasters
    inSlcDataset = productSlc.getGdalSlcDataset(opts.frequency, opts.polarization)
    inSlcRaster = Raster('', dataset=inSlcDataset)
    azOffsetRaster = Raster(filename=os.path.join(opts.offsetdir, 'azimuth.off'))
    rgOffsetRaster = Raster(filename=os.path.join(opts.offsetdir, 'range.off'))

    # Init output directory
    if opts.outdir and not os.path.isdir(opts.outdir):
        os.mkdir(opts.outdir)

    # Prepare output raster
    driver = gdal.GetDriverByName('ISCE')
    slcName = 'resamp_{}_{}.slc'.format(opts.frequency, opts.polarization)
    outds = driver.Create(os.path.join(opts.outdir, slcName), rgOffsetRaster.width,
                          rgOffsetRaster.length, 1, gdal.GDT_CFloat32)
    outSlcRaster = Raster('', dataset=outds)

    # Run resamp
    resamp.resamp(inSlc=inSlcRaster,
            outSlc=outSlcRaster,
            rgoffRaster=rgOffsetRaster,
            azoffRaster=azOffsetRaster)


if __name__ == '__main__':
    opts = cmdLineParse()
    main(opts)

# end of file
