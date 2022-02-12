import pygrib
# import grib2io
# from ncepgrib2 import Grib2Encode
import eccodes



# grbs = pygrib.open('backup/GaugeCorr_QPE_01H_00.00_20200606-000000-1.grib2')
# grb1 = pygrib.open('backup/GaugeCorr_QPE_01H_00.00_20200606-000000.g.grib2')
grbs = pygrib.open('../abc/GaugeCorr_QPE_01H_00.00_20220204-000000.grib2')
grb1 = pygrib.open('../abc/GaugeCorr_QPE_01H_00.00_20220204-600000.grib2')

for g in grbs:
    # print(g.typeOfLevel, g.level, g.name, g.validDate, g.analDate, g.forecastTime)
    # g['forecastTime'] = 240
    # g['analDate'] = 20200505
    print(g.typeOfLevel, g.level, g.name, "Data Date", g.dataDate, "Valid Date", g.validDate,
          "Anal Date", g.analDate, "Forecast Date", g.forecastTime)

for g in grb1:
    # print(g.typeOfLevel, g.level, g.name, g.validDate, g.analDate, g.forecastTime)
    # g['forecastTime'] = 240
    # g['analDate'] = 20200505
    print(g.typeOfLevel, g.level, g.name, "Data Date", g.dataDate, "Valid Date", g.validDate,
          "Anal Date", g.analDate, "Forecast Date", g.forecastTime)

# g2 = grbs.select()[0]
# print(g2)
# print(grbs)

# for g in grb1:
#     print(g)
#     print(g.typeOfLevel, g.level, g.name, g.validDate, g.analDate, g.forecastTime)




# filename = open("GaugeCorr_QPE_01H_00.00_20220211-600000.grib2")
#
# gid = eccodes.codes_grib_new_from_file(filename)
# # if gid is None:
# #     exit()
#
# key1 = 'validityDate'
# print(eccodes.codes_get(gid, key1))
#
# # clone_id = eccodes.codes_clone(gid)
#
# # key2 = 'dayOfEndOfOverallTimeInterval'
# # eccodes.codes_set(gid, key2, 11)
#
# with open("GaugeCorr_QPE_01H_00.00_20220211-600000.grib2", "wb") as output:
#      eccodes.codes_write(gid, output)
#
# eccodes.codes_release(gid)


# filename.write(str(eccodes.codes_get_message(gid)))
# filename.flush()


# print(eccodes.codes_get(gid, key1))

# with gribapi.GribFile(filename) as grib:
# eccodes.codes_set_key_vals
# eccodes.codes_index_write(gid, "./GaugeCorr_QPE_01H_00.00_20220211-600000.grib2")
# eccodes.codes_release()