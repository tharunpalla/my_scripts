from mil.army.usace.hec.vortex.convert import GridToPointConverter
from mil.army.usace.hec.vortex import Options
from mil.army.usace.hec.vortex.io import DataReader
import os
from glob import glob
from java.nio.file import Path
from java.nio.file import Paths

#DSS Grid Files to convert to time series
d_files = glob('C:/Users/chand/Downloads/automation_1.dss')

#Output DSS File
output_dss = Paths.get("C:\Users\chand\Downloads\grib2point.dss")

#Shapefile
clip_shp = Paths.get("C:\Users\chand\Downloads\HEC_DSS_Automation\Vortex\examples\src\main\jython\grib2\Basins.shp")

#Shapefile attribute for zonal statistics
name = 'NAME'

#Output DSS file path partA
basin = 'RIVER BASIN'
ds = 'UA_sanitized'

#Loop through each dss file
for dss_file in d_files:

    #Get dss pathnames
    sourceGrids = DataReader.getVariables(dss_file)

    #Output DSS wite options
    write_options = Options.create()
    write_options.add('partF', ds )
    write_options.add('partA', 'SHG')
    write_options.add('partB', basin)

    #Convert the Data
    myImport = GridToPointConverter.builder()\
            .pathToGrids(dss_file)\
            .variables(sourceGrids)\
            .pathToFeatures(clip_shp)\
            .field(name)\
            .destination(output_dss)\
            .writeOptions(write_options).build()
    myImport.convert()
