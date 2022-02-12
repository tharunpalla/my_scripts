import os
from mil.army.usace.hec.vortex.io import DataReader
from mil.army.usace.hec.vortex.math import Shifter


def convert_grib2_to_dss():

    path = 'C:\Users\chand\Downloads\HEC_DSS_Automation\Vortex\examples\src\main\jython\grib2\GaugeCorr_QPE_01H_00.00_20220211-020000.grib2'

    variables = set()

    for file in os.scandir(path):
        vars = DataReader.getVariables(file)
        for s in vars:
            variables.add(str(s))

    variables = list(variables)

    print(variables)

    destination = 'C:/Users/chand/Downloads/automation_1.dss'

    write_options = {'partF': 'my script import'}

    # myImport = BatchImporter.builder() \
    #     .inFiles(in_files) \
    #     .variables(variables) \
    #     .geoOptions(geo_options) \
    #     .destination(destination) \
    #     .writeOptions(write_options) \
    #     .build()

    interval = {
        "Duration": "5"
    }

    Shifter
    shifter = Shifter.builder() \
        .shift(interval) \
        .pathToFile(path) \
        .grids(variables) \
        .destination(path) \
        .writeOptions(write_options) \
        .build();

    shifter.shift()
