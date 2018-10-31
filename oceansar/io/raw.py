
import time
from netCDF4 import Dataset
from oceansar.io.netcdf import NETCDFHandler

class SkimRawFile(NETCDFHandler):
    """ Raw data file generated by the OASIS Simulator

        :param file_name: File name
        :param mode: Access mode (w = write, r = read, r+ = read + append)
        :param raw_dim: Raw data dimensions
        :param format: netCDF format

        .. note::
            Refer to netCDF4 Python library for details on access mode and
            available formats
    """
    def __init__(self, file_name, mode, raw_dim=None, format='NETCDF4'):

        self.__file__ = Dataset(file_name, mode, format)

        # If writing, define file
        if mode == 'w':
            # Set file attributes
            self.__file__.description = 'OASIS SAR Raw Data File'
            self.__file__.history = 'Created ' + time.ctime(time.time())
            self.__file__.source = 'OASIS Simulator'

            # Dimensions
            if not raw_dim:
                raise ValueError('Raw data dimensions are needed when creating a new file!')


            # For SKIM, not very nice to decide this like this, but ok
            self.__file__.createDimension('pol_dim', raw_dim[0])
            self.__file__.createDimension('az_dim', raw_dim[1])
            self.__file__.createDimension('rg_dim', raw_dim[2])
            raw_data_r = self.__file__.createVariable('raw_data_r',
                                                      'f8',
                                                      ('pol_dim',
                                                       'az_dim',
                                                       'rg_dim'))
            raw_data_i = self.__file__.createVariable('raw_data_i',
                                                      'f8',
                                                      ('pol_dim',
                                                       'az_dim',
                                                       'rg_dim'))
            dop_ref = self.__file__.createVariable('dop_ref', 'f8', ('rg_dim',))
            dop_ref.units = '[Hz]'
        # Variables
            inc_angle = self.__file__.createVariable('inc_angle', 'f8')
            inc_angle.units = '[deg]'
            f0 = self.__file__.createVariable('f0', 'f8')
            f0.units = '[Hz]'

            ant_L = self.__file__.createVariable('ant_L', 'f8')
            ant_L.units = '[m]'
            prf = self.__file__.createVariable('prf', 'f8')
            prf.units = '[Hz]'
            v_ground = self.__file__.createVariable('v_ground', 'f8')
            v_ground.units = '[m/s]'
            orbit_alt = self.__file__.createVariable('orbit_alt', 'f8')
            orbit_alt.units = '[m]'
            sr0 = self.__file__.createVariable('sr0', 'f8')
            sr0.units = '[m]'
            rg_sampling = self.__file__.createVariable('rg_sampling', 'f8')
            rg_sampling.units = '[Hz]'
            rg_bw = self.__file__.createVariable('rg_bw', 'f8')
            rg_bw.units = '[Hz]'
            azimuth = self.__file__.createVariable('azimuth', 'f8')
            azimuth.units = '[deg]'


            raw_data_r.units = '[]'
            raw_data_i.units = '[]'
            NRCS_avg = self.__file__.createVariable('NRCS_avg',
                                                    'f8',
                                                    ('pol_dim', 'az_dim'))
            NRCS_avg.units = '[]'

class RawFile(NETCDFHandler):
    """ Raw data file generated by the OASIS Simulator

        :param file_name: File name
        :param mode: Access mode (w = write, r = read, r+ = read + append)
        :param raw_dim: Raw data dimensions
        :param format: netCDF format

        .. note::
            Refer to netCDF4 Python library for details on access mode and
            available formats
    """
    def __init__(self, file_name, mode, raw_dim=None, format='NETCDF4'):

        self.__file__ = Dataset(file_name, mode, format)

        # If writing, define file
        if mode == 'w':
            # Set file attributes
            self.__file__.description = 'OASIS SAR Raw Data File'
            self.__file__.history = 'Created ' + time.ctime(time.time())
            self.__file__.source = 'OASIS Simulator'

            # Dimensions
            if not raw_dim:
                raise ValueError('Raw data dimensions are needed when creating a new file!')
            if len(raw_dim) == 4:
                self.__file__.createDimension('pol_dim', raw_dim[0])
                self.__file__.createDimension('ch_dim', raw_dim[1])
                self.__file__.createDimension('az_dim', raw_dim[2])
                self.__file__.createDimension('rg_dim', raw_dim[3])
                num_ch = self.__file__.createVariable('num_ch', 'i4')
                num_ch.units = '[]'
                raw_data_r = self.__file__.createVariable('raw_data_r',
                                                          'f8',
                                                          ('pol_dim',
                                                           'ch_dim',
                                                           'az_dim',
                                                           'rg_dim'))
                raw_data_i = self.__file__.createVariable('raw_data_i',
                                                          'f8',
                                                          ('pol_dim',
                                                           'ch_dim',
                                                           'az_dim',
                                                           'rg_dim'))
            else:
                # For SKIM, not very nice to decide this like this, but ok
                self.__file__.createDimension('pol_dim', raw_dim[0])
                self.__file__.createDimension('az_dim', raw_dim[1])
                self.__file__.createDimension('rg_dim', raw_dim[2])
                raw_data_r = self.__file__.createVariable('raw_data_r',
                                                          'f8',
                                                          ('pol_dim',
                                                           'az_dim',
                                                           'rg_dim'))
                raw_data_i = self.__file__.createVariable('raw_data_i',
                                                          'f8',
                                                          ('pol_dim',
                                                           'az_dim',
                                                           'rg_dim'))
            # Variables
            inc_angle = self.__file__.createVariable('inc_angle', 'f8')
            inc_angle.units = '[deg]'
            f0 = self.__file__.createVariable('f0', 'f8')
            f0.units = '[Hz]'

            ant_L = self.__file__.createVariable('ant_L', 'f8')
            ant_L.units = '[m]'
            prf = self.__file__.createVariable('prf', 'f8')
            prf.units = '[Hz]'
            v_ground = self.__file__.createVariable('v_ground', 'f8')
            v_ground.units = '[m/s]'
            orbit_alt = self.__file__.createVariable('orbit_alt', 'f8')
            orbit_alt.units = '[m]'
            sr0 = self.__file__.createVariable('sr0', 'f8')
            sr0.units = '[m]'
            rg_sampling = self.__file__.createVariable('rg_sampling', 'f8')
            rg_sampling.units = '[Hz]'
            rg_bw = self.__file__.createVariable('rg_bw', 'f8')
            rg_bw.units = '[Hz]'


            raw_data_r.units = '[]'
            raw_data_i.units = '[]'
            NRCS_avg = self.__file__.createVariable('NRCS_avg',
                                                    'f8',
                                                    ('pol_dim', 'az_dim'))
            NRCS_avg.units = '[]'

