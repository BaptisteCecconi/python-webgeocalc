# -*- coding: utf-8 -*-
'''WebGeoCalc varibales.'''

API_URL = 'https://wgc2.jpl.nasa.gov:8443/webgeocalc/api'

CALCULATION_FAILED_PHASES = [
    'FAILED',
    'CANCELLED',
    'DISPATCHED',
    'EXPIRED',
]

CALCULATION_TYPE = [
    'STATE_VECTOR',
    'ANGULAR_SEPARATION',
    'ANGULAR_SIZE',
    'SUB_OBSERVER_POINT',
    'SUB_SOLAR_POINT',
    'ILLUMINATION_ANGLES',
    'SURFACE_INTERCEPT_POINT',
    'OSCULATING_ELEMENTS',
    'FRAME_TRANSFORMATION',
    'GF_COORDINATE_SEARCH',
    'GF_ANGULAR_SEPARATION_SEARCH',
    'GF_DISTANCE_SEARCH',
    'GF_SUB_POINT_SEARCH',
    'GF_OCCULTATION_SEARCH',
    'GF_TARGET_IN_INSTRUMENT_FOV_SEARCH',
    'GF_SURFACE_INTERCEPT_POINT_SEARCH',
    'GF_RAY_IN_FOV_SEARCH',
    'TIME_CONVERSION',
]

TIME_SYSTEM = [
    'UTC',
    'TDB',
    'TDT',
    'SPACECRAFT_CLOCK',
]

TIME_FORMAT = [
    'CALENDAR',
    'JULIAN',
    'SECONDS_PAST_J2000',
    'SPACECRAFT_CLOCK_TICKS',
    'SPACECRAFT_CLOCK_STRING',
]

OUTPUT_TIME_FORMAT = [
    'CALENDAR',
    'CALENDAR_YMD',
    'CALENDAR_DOY',
    'JULIAN',
    'SECONDS_PAST_J2000',
    'SPACECRAFT_CLOCK_STRING',
    'SPACECRAFT_CLOCK_TICKS',
    'CUSTOM',
]

TIME_STEP_UNITS = [
    'SECONDS',
    'MINUTES',
    'HOURS',
    'DAYS',
    'EQUAL_INTERVALS',
]

INTERVALS = [
    "array([startTime, endTime])",
    "dict({'startTime': startTime, 'endTime': endTime})",
    "array([ interval1, interval2, … ])",
]

ABERRATION_CORRECTION = [
    'NONE',
    'LT',
    'LT+S',
    'CN',
    'CN+S',
    'XLT',
    'XLT+S',
    'XCN',
    'XCN+S',
]

STATE_REPRESENTATION = [
    'RECTANGULAR',
    'RA_DEC',
    'LATITUDINAL',
    'PLANETODETIC',
    'PLANETOGRAPHIC',
    'CYLINDRICAL',
    'SPHERICAL',
]

SHAPE = [
    'POINT',
    'SPHERE',
    'ELLIPSOID',
    'DSK ',
]

TIME_LOCATION = [
    'FRAME1',
    'FRAME2',
]

ORIENTATION_REPRESENTATION = [
    'EULER_ANGLES',
    'ANGLE_AND_AXIS',
    'SPICE_QUATERNION',
    'OTHER_QUATERNION',
    'MATRIX_ROW_BY_ROW',
    'MATRIX_FLAGGED',
    'MATRIX_ALL_ONE_ROW',
]

ANGULAR_VELOCITY_REPRESENTATION = [
    'NOT_INCLUDED',
    'VECTOR_IN_FRAME1',
    'VECTOR_IN_FRAME2',
    'EULER_ANGLE_DERIVATIVES',
    'MATRIX',
]

AXIS = [
    'X',
    'Y',
    'Z',
]

ANGULAR_UNITS = [
    'deg',
    'rad',
]

ANGULAR_VELOCITY_UNITS = [
    'deg/s',
    'rad/s',
    'RPM',
    'Unitary',
]

COORDINATE_REPRESENTATION = [
    'LATITUDINAL',
    'PLANETODETIC',
    'PLANETOGRAPHIC',
]

SUB_POINT_TYPE = [
    'Near point: ellipsoid',
    'Intercept: ellipsoid',
    'NADIR/DSK/UNPRIORITIZED',
    'INTERCEPT/DSK/UNPRIORITIZED',
]

DIRECTION_VECTOR_TYPE = [
    'INSTRUMENT_BORESIGHT',
    'INSTRUMENT_FOV_BOUNDARY_VECTORS',
    'REFERENCE_FRAME_AXIS',
    'VECTOR_IN_INSTRUMENT_FOV',
    'VECTOR_IN_REFERENCE_FRAME',
]
