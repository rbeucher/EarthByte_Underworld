# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ImportersToolbox', [dirname(__file__)])
        except ImportError:
            import _ImportersToolbox
            return _ImportersToolbox
        if fp is not None:
            try:
                _mod = imp.load_module('_ImportersToolbox', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ImportersToolbox = swig_import_helper()
    del swig_import_helper
else:
    import _ImportersToolbox
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


import StGermain
import StgDomain
import StgFEM
import PICellerator
import Underworld
import gLucifer
class VoxelFieldVariable(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VoxelFieldVariable, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VoxelFieldVariable, name)
    __repr__ = _swig_repr
    __swig_setmethods__["_sizeOfSelf"] = _ImportersToolbox.VoxelFieldVariable__sizeOfSelf_set
    __swig_getmethods__["_sizeOfSelf"] = _ImportersToolbox.VoxelFieldVariable__sizeOfSelf_get
    if _newclass:_sizeOfSelf = _swig_property(_ImportersToolbox.VoxelFieldVariable__sizeOfSelf_get, _ImportersToolbox.VoxelFieldVariable__sizeOfSelf_set)
    __swig_setmethods__["_deleteSelf"] = _ImportersToolbox.VoxelFieldVariable__deleteSelf_set
    __swig_getmethods__["_deleteSelf"] = _ImportersToolbox.VoxelFieldVariable__deleteSelf_get
    if _newclass:_deleteSelf = _swig_property(_ImportersToolbox.VoxelFieldVariable__deleteSelf_get, _ImportersToolbox.VoxelFieldVariable__deleteSelf_set)
    __swig_setmethods__["type"] = _ImportersToolbox.VoxelFieldVariable_type_set
    __swig_getmethods__["type"] = _ImportersToolbox.VoxelFieldVariable_type_get
    if _newclass:type = _swig_property(_ImportersToolbox.VoxelFieldVariable_type_get, _ImportersToolbox.VoxelFieldVariable_type_set)
    __swig_setmethods__["nRefs"] = _ImportersToolbox.VoxelFieldVariable_nRefs_set
    __swig_getmethods__["nRefs"] = _ImportersToolbox.VoxelFieldVariable_nRefs_get
    if _newclass:nRefs = _swig_property(_ImportersToolbox.VoxelFieldVariable_nRefs_get, _ImportersToolbox.VoxelFieldVariable_nRefs_set)
    __swig_setmethods__["_delete"] = _ImportersToolbox.VoxelFieldVariable__delete_set
    __swig_getmethods__["_delete"] = _ImportersToolbox.VoxelFieldVariable__delete_get
    if _newclass:_delete = _swig_property(_ImportersToolbox.VoxelFieldVariable__delete_get, _ImportersToolbox.VoxelFieldVariable__delete_set)
    __swig_setmethods__["_print"] = _ImportersToolbox.VoxelFieldVariable__print_set
    __swig_getmethods__["_print"] = _ImportersToolbox.VoxelFieldVariable__print_get
    if _newclass:_print = _swig_property(_ImportersToolbox.VoxelFieldVariable__print_get, _ImportersToolbox.VoxelFieldVariable__print_set)
    __swig_setmethods__["_copy"] = _ImportersToolbox.VoxelFieldVariable__copy_set
    __swig_getmethods__["_copy"] = _ImportersToolbox.VoxelFieldVariable__copy_get
    if _newclass:_copy = _swig_property(_ImportersToolbox.VoxelFieldVariable__copy_get, _ImportersToolbox.VoxelFieldVariable__copy_set)
    __swig_setmethods__["name"] = _ImportersToolbox.VoxelFieldVariable_name_set
    __swig_getmethods__["name"] = _ImportersToolbox.VoxelFieldVariable_name_get
    if _newclass:name = _swig_property(_ImportersToolbox.VoxelFieldVariable_name_get, _ImportersToolbox.VoxelFieldVariable_name_set)
    __swig_setmethods__["nameAllocationType"] = _ImportersToolbox.VoxelFieldVariable_nameAllocationType_set
    __swig_getmethods__["nameAllocationType"] = _ImportersToolbox.VoxelFieldVariable_nameAllocationType_get
    if _newclass:nameAllocationType = _swig_property(_ImportersToolbox.VoxelFieldVariable_nameAllocationType_get, _ImportersToolbox.VoxelFieldVariable_nameAllocationType_set)
    __swig_setmethods__["_defaultConstructor"] = _ImportersToolbox.VoxelFieldVariable__defaultConstructor_set
    __swig_getmethods__["_defaultConstructor"] = _ImportersToolbox.VoxelFieldVariable__defaultConstructor_get
    if _newclass:_defaultConstructor = _swig_property(_ImportersToolbox.VoxelFieldVariable__defaultConstructor_get, _ImportersToolbox.VoxelFieldVariable__defaultConstructor_set)
    __swig_setmethods__["_construct"] = _ImportersToolbox.VoxelFieldVariable__construct_set
    __swig_getmethods__["_construct"] = _ImportersToolbox.VoxelFieldVariable__construct_get
    if _newclass:_construct = _swig_property(_ImportersToolbox.VoxelFieldVariable__construct_get, _ImportersToolbox.VoxelFieldVariable__construct_set)
    __swig_setmethods__["_build"] = _ImportersToolbox.VoxelFieldVariable__build_set
    __swig_getmethods__["_build"] = _ImportersToolbox.VoxelFieldVariable__build_get
    if _newclass:_build = _swig_property(_ImportersToolbox.VoxelFieldVariable__build_get, _ImportersToolbox.VoxelFieldVariable__build_set)
    __swig_setmethods__["_initialise"] = _ImportersToolbox.VoxelFieldVariable__initialise_set
    __swig_getmethods__["_initialise"] = _ImportersToolbox.VoxelFieldVariable__initialise_get
    if _newclass:_initialise = _swig_property(_ImportersToolbox.VoxelFieldVariable__initialise_get, _ImportersToolbox.VoxelFieldVariable__initialise_set)
    __swig_setmethods__["_execute"] = _ImportersToolbox.VoxelFieldVariable__execute_set
    __swig_getmethods__["_execute"] = _ImportersToolbox.VoxelFieldVariable__execute_get
    if _newclass:_execute = _swig_property(_ImportersToolbox.VoxelFieldVariable__execute_get, _ImportersToolbox.VoxelFieldVariable__execute_set)
    __swig_setmethods__["_destroy"] = _ImportersToolbox.VoxelFieldVariable__destroy_set
    __swig_getmethods__["_destroy"] = _ImportersToolbox.VoxelFieldVariable__destroy_get
    if _newclass:_destroy = _swig_property(_ImportersToolbox.VoxelFieldVariable__destroy_get, _ImportersToolbox.VoxelFieldVariable__destroy_set)
    __swig_setmethods__["isConstructed"] = _ImportersToolbox.VoxelFieldVariable_isConstructed_set
    __swig_getmethods__["isConstructed"] = _ImportersToolbox.VoxelFieldVariable_isConstructed_get
    if _newclass:isConstructed = _swig_property(_ImportersToolbox.VoxelFieldVariable_isConstructed_get, _ImportersToolbox.VoxelFieldVariable_isConstructed_set)
    __swig_setmethods__["isBuilt"] = _ImportersToolbox.VoxelFieldVariable_isBuilt_set
    __swig_getmethods__["isBuilt"] = _ImportersToolbox.VoxelFieldVariable_isBuilt_get
    if _newclass:isBuilt = _swig_property(_ImportersToolbox.VoxelFieldVariable_isBuilt_get, _ImportersToolbox.VoxelFieldVariable_isBuilt_set)
    __swig_setmethods__["isInitialised"] = _ImportersToolbox.VoxelFieldVariable_isInitialised_set
    __swig_getmethods__["isInitialised"] = _ImportersToolbox.VoxelFieldVariable_isInitialised_get
    if _newclass:isInitialised = _swig_property(_ImportersToolbox.VoxelFieldVariable_isInitialised_get, _ImportersToolbox.VoxelFieldVariable_isInitialised_set)
    __swig_setmethods__["hasExecuted"] = _ImportersToolbox.VoxelFieldVariable_hasExecuted_set
    __swig_getmethods__["hasExecuted"] = _ImportersToolbox.VoxelFieldVariable_hasExecuted_get
    if _newclass:hasExecuted = _swig_property(_ImportersToolbox.VoxelFieldVariable_hasExecuted_get, _ImportersToolbox.VoxelFieldVariable_hasExecuted_set)
    __swig_setmethods__["isDestroyed"] = _ImportersToolbox.VoxelFieldVariable_isDestroyed_set
    __swig_getmethods__["isDestroyed"] = _ImportersToolbox.VoxelFieldVariable_isDestroyed_get
    if _newclass:isDestroyed = _swig_property(_ImportersToolbox.VoxelFieldVariable_isDestroyed_get, _ImportersToolbox.VoxelFieldVariable_isDestroyed_set)
    __swig_setmethods__["constructType"] = _ImportersToolbox.VoxelFieldVariable_constructType_set
    __swig_getmethods__["constructType"] = _ImportersToolbox.VoxelFieldVariable_constructType_get
    if _newclass:constructType = _swig_property(_ImportersToolbox.VoxelFieldVariable_constructType_get, _ImportersToolbox.VoxelFieldVariable_constructType_set)
    __swig_setmethods__["buildType"] = _ImportersToolbox.VoxelFieldVariable_buildType_set
    __swig_getmethods__["buildType"] = _ImportersToolbox.VoxelFieldVariable_buildType_get
    if _newclass:buildType = _swig_property(_ImportersToolbox.VoxelFieldVariable_buildType_get, _ImportersToolbox.VoxelFieldVariable_buildType_set)
    __swig_setmethods__["initialiseType"] = _ImportersToolbox.VoxelFieldVariable_initialiseType_set
    __swig_getmethods__["initialiseType"] = _ImportersToolbox.VoxelFieldVariable_initialiseType_get
    if _newclass:initialiseType = _swig_property(_ImportersToolbox.VoxelFieldVariable_initialiseType_get, _ImportersToolbox.VoxelFieldVariable_initialiseType_set)
    __swig_setmethods__["executeType"] = _ImportersToolbox.VoxelFieldVariable_executeType_set
    __swig_getmethods__["executeType"] = _ImportersToolbox.VoxelFieldVariable_executeType_get
    if _newclass:executeType = _swig_property(_ImportersToolbox.VoxelFieldVariable_executeType_get, _ImportersToolbox.VoxelFieldVariable_executeType_set)
    __swig_setmethods__["destroyType"] = _ImportersToolbox.VoxelFieldVariable_destroyType_set
    __swig_getmethods__["destroyType"] = _ImportersToolbox.VoxelFieldVariable_destroyType_get
    if _newclass:destroyType = _swig_property(_ImportersToolbox.VoxelFieldVariable_destroyType_get, _ImportersToolbox.VoxelFieldVariable_destroyType_set)
    __swig_setmethods__["context"] = _ImportersToolbox.VoxelFieldVariable_context_set
    __swig_getmethods__["context"] = _ImportersToolbox.VoxelFieldVariable_context_get
    if _newclass:context = _swig_property(_ImportersToolbox.VoxelFieldVariable_context_get, _ImportersToolbox.VoxelFieldVariable_context_set)
    __swig_setmethods__["_interpolateValueAt"] = _ImportersToolbox.VoxelFieldVariable__interpolateValueAt_set
    __swig_getmethods__["_interpolateValueAt"] = _ImportersToolbox.VoxelFieldVariable__interpolateValueAt_get
    if _newclass:_interpolateValueAt = _swig_property(_ImportersToolbox.VoxelFieldVariable__interpolateValueAt_get, _ImportersToolbox.VoxelFieldVariable__interpolateValueAt_set)
    __swig_setmethods__["_getMinGlobalFieldMagnitude"] = _ImportersToolbox.VoxelFieldVariable__getMinGlobalFieldMagnitude_set
    __swig_getmethods__["_getMinGlobalFieldMagnitude"] = _ImportersToolbox.VoxelFieldVariable__getMinGlobalFieldMagnitude_get
    if _newclass:_getMinGlobalFieldMagnitude = _swig_property(_ImportersToolbox.VoxelFieldVariable__getMinGlobalFieldMagnitude_get, _ImportersToolbox.VoxelFieldVariable__getMinGlobalFieldMagnitude_set)
    __swig_setmethods__["_getMaxGlobalFieldMagnitude"] = _ImportersToolbox.VoxelFieldVariable__getMaxGlobalFieldMagnitude_set
    __swig_getmethods__["_getMaxGlobalFieldMagnitude"] = _ImportersToolbox.VoxelFieldVariable__getMaxGlobalFieldMagnitude_get
    if _newclass:_getMaxGlobalFieldMagnitude = _swig_property(_ImportersToolbox.VoxelFieldVariable__getMaxGlobalFieldMagnitude_get, _ImportersToolbox.VoxelFieldVariable__getMaxGlobalFieldMagnitude_set)
    __swig_setmethods__["_cacheMinMaxGlobalFieldMagnitude"] = _ImportersToolbox.VoxelFieldVariable__cacheMinMaxGlobalFieldMagnitude_set
    __swig_getmethods__["_cacheMinMaxGlobalFieldMagnitude"] = _ImportersToolbox.VoxelFieldVariable__cacheMinMaxGlobalFieldMagnitude_get
    if _newclass:_cacheMinMaxGlobalFieldMagnitude = _swig_property(_ImportersToolbox.VoxelFieldVariable__cacheMinMaxGlobalFieldMagnitude_get, _ImportersToolbox.VoxelFieldVariable__cacheMinMaxGlobalFieldMagnitude_set)
    __swig_setmethods__["_getMinAndMaxLocalCoords"] = _ImportersToolbox.VoxelFieldVariable__getMinAndMaxLocalCoords_set
    __swig_getmethods__["_getMinAndMaxLocalCoords"] = _ImportersToolbox.VoxelFieldVariable__getMinAndMaxLocalCoords_get
    if _newclass:_getMinAndMaxLocalCoords = _swig_property(_ImportersToolbox.VoxelFieldVariable__getMinAndMaxLocalCoords_get, _ImportersToolbox.VoxelFieldVariable__getMinAndMaxLocalCoords_set)
    __swig_setmethods__["_getMinAndMaxGlobalCoords"] = _ImportersToolbox.VoxelFieldVariable__getMinAndMaxGlobalCoords_set
    __swig_getmethods__["_getMinAndMaxGlobalCoords"] = _ImportersToolbox.VoxelFieldVariable__getMinAndMaxGlobalCoords_get
    if _newclass:_getMinAndMaxGlobalCoords = _swig_property(_ImportersToolbox.VoxelFieldVariable__getMinAndMaxGlobalCoords_get, _ImportersToolbox.VoxelFieldVariable__getMinAndMaxGlobalCoords_set)
    __swig_setmethods__["extensionMgr"] = _ImportersToolbox.VoxelFieldVariable_extensionMgr_set
    __swig_getmethods__["extensionMgr"] = _ImportersToolbox.VoxelFieldVariable_extensionMgr_get
    if _newclass:extensionMgr = _swig_property(_ImportersToolbox.VoxelFieldVariable_extensionMgr_get, _ImportersToolbox.VoxelFieldVariable_extensionMgr_set)
    __swig_setmethods__["fieldComponentCount"] = _ImportersToolbox.VoxelFieldVariable_fieldComponentCount_set
    __swig_getmethods__["fieldComponentCount"] = _ImportersToolbox.VoxelFieldVariable_fieldComponentCount_get
    if _newclass:fieldComponentCount = _swig_property(_ImportersToolbox.VoxelFieldVariable_fieldComponentCount_get, _ImportersToolbox.VoxelFieldVariable_fieldComponentCount_set)
    __swig_setmethods__["dim"] = _ImportersToolbox.VoxelFieldVariable_dim_set
    __swig_getmethods__["dim"] = _ImportersToolbox.VoxelFieldVariable_dim_get
    if _newclass:dim = _swig_property(_ImportersToolbox.VoxelFieldVariable_dim_get, _ImportersToolbox.VoxelFieldVariable_dim_set)
    __swig_setmethods__["communicator"] = _ImportersToolbox.VoxelFieldVariable_communicator_set
    __swig_getmethods__["communicator"] = _ImportersToolbox.VoxelFieldVariable_communicator_get
    if _newclass:communicator = _swig_property(_ImportersToolbox.VoxelFieldVariable_communicator_get, _ImportersToolbox.VoxelFieldVariable_communicator_set)
    __swig_setmethods__["fieldVariable_Register"] = _ImportersToolbox.VoxelFieldVariable_fieldVariable_Register_set
    __swig_getmethods__["fieldVariable_Register"] = _ImportersToolbox.VoxelFieldVariable_fieldVariable_Register_get
    if _newclass:fieldVariable_Register = _swig_property(_ImportersToolbox.VoxelFieldVariable_fieldVariable_Register_get, _ImportersToolbox.VoxelFieldVariable_fieldVariable_Register_set)
    __swig_setmethods__["isCheckpointedAndReloaded"] = _ImportersToolbox.VoxelFieldVariable_isCheckpointedAndReloaded_set
    __swig_getmethods__["isCheckpointedAndReloaded"] = _ImportersToolbox.VoxelFieldVariable_isCheckpointedAndReloaded_get
    if _newclass:isCheckpointedAndReloaded = _swig_property(_ImportersToolbox.VoxelFieldVariable_isCheckpointedAndReloaded_get, _ImportersToolbox.VoxelFieldVariable_isCheckpointedAndReloaded_set)
    __swig_setmethods__["isSavedData"] = _ImportersToolbox.VoxelFieldVariable_isSavedData_set
    __swig_getmethods__["isSavedData"] = _ImportersToolbox.VoxelFieldVariable_isSavedData_get
    if _newclass:isSavedData = _swig_property(_ImportersToolbox.VoxelFieldVariable_isSavedData_get, _ImportersToolbox.VoxelFieldVariable_isSavedData_set)
    __swig_setmethods__["cachedTimestep"] = _ImportersToolbox.VoxelFieldVariable_cachedTimestep_set
    __swig_getmethods__["cachedTimestep"] = _ImportersToolbox.VoxelFieldVariable_cachedTimestep_get
    if _newclass:cachedTimestep = _swig_property(_ImportersToolbox.VoxelFieldVariable_cachedTimestep_get, _ImportersToolbox.VoxelFieldVariable_cachedTimestep_set)
    __swig_setmethods__["magnitudeMin"] = _ImportersToolbox.VoxelFieldVariable_magnitudeMin_set
    __swig_getmethods__["magnitudeMin"] = _ImportersToolbox.VoxelFieldVariable_magnitudeMin_get
    if _newclass:magnitudeMin = _swig_property(_ImportersToolbox.VoxelFieldVariable_magnitudeMin_get, _ImportersToolbox.VoxelFieldVariable_magnitudeMin_set)
    __swig_setmethods__["magnitudeMax"] = _ImportersToolbox.VoxelFieldVariable_magnitudeMax_set
    __swig_getmethods__["magnitudeMax"] = _ImportersToolbox.VoxelFieldVariable_magnitudeMax_get
    if _newclass:magnitudeMax = _swig_property(_ImportersToolbox.VoxelFieldVariable_magnitudeMax_get, _ImportersToolbox.VoxelFieldVariable_magnitudeMax_set)
    __swig_setmethods__["theScaling"] = _ImportersToolbox.VoxelFieldVariable_theScaling_set
    __swig_getmethods__["theScaling"] = _ImportersToolbox.VoxelFieldVariable_theScaling_get
    if _newclass:theScaling = _swig_property(_ImportersToolbox.VoxelFieldVariable_theScaling_get, _ImportersToolbox.VoxelFieldVariable_theScaling_set)
    __swig_setmethods__["o_units"] = _ImportersToolbox.VoxelFieldVariable_o_units_set
    __swig_getmethods__["o_units"] = _ImportersToolbox.VoxelFieldVariable_o_units_get
    if _newclass:o_units = _swig_property(_ImportersToolbox.VoxelFieldVariable_o_units_get, _ImportersToolbox.VoxelFieldVariable_o_units_set)
    __swig_setmethods__["useCacheMaxMin"] = _ImportersToolbox.VoxelFieldVariable_useCacheMaxMin_set
    __swig_getmethods__["useCacheMaxMin"] = _ImportersToolbox.VoxelFieldVariable_useCacheMaxMin_get
    if _newclass:useCacheMaxMin = _swig_property(_ImportersToolbox.VoxelFieldVariable_useCacheMaxMin_get, _ImportersToolbox.VoxelFieldVariable_useCacheMaxMin_set)
    __swig_setmethods__["_setupDataArray"] = _ImportersToolbox.VoxelFieldVariable__setupDataArray_set
    __swig_getmethods__["_setupDataArray"] = _ImportersToolbox.VoxelFieldVariable__setupDataArray_get
    if _newclass:_setupDataArray = _swig_property(_ImportersToolbox.VoxelFieldVariable__setupDataArray_get, _ImportersToolbox.VoxelFieldVariable__setupDataArray_set)
    __swig_setmethods__["_testDataArray"] = _ImportersToolbox.VoxelFieldVariable__testDataArray_set
    __swig_getmethods__["_testDataArray"] = _ImportersToolbox.VoxelFieldVariable__testDataArray_get
    if _newclass:_testDataArray = _swig_property(_ImportersToolbox.VoxelFieldVariable__testDataArray_get, _ImportersToolbox.VoxelFieldVariable__testDataArray_set)
    __swig_setmethods__["_setArrayValue"] = _ImportersToolbox.VoxelFieldVariable__setArrayValue_set
    __swig_getmethods__["_setArrayValue"] = _ImportersToolbox.VoxelFieldVariable__setArrayValue_get
    if _newclass:_setArrayValue = _swig_property(_ImportersToolbox.VoxelFieldVariable__setArrayValue_get, _ImportersToolbox.VoxelFieldVariable__setArrayValue_set)
    __swig_setmethods__["_getArrayIndexIJK"] = _ImportersToolbox.VoxelFieldVariable__getArrayIndexIJK_set
    __swig_getmethods__["_getArrayIndexIJK"] = _ImportersToolbox.VoxelFieldVariable__getArrayIndexIJK_get
    if _newclass:_getArrayIndexIJK = _swig_property(_ImportersToolbox.VoxelFieldVariable__getArrayIndexIJK_get, _ImportersToolbox.VoxelFieldVariable__getArrayIndexIJK_set)
    __swig_setmethods__["voxelDataHandler"] = _ImportersToolbox.VoxelFieldVariable_voxelDataHandler_set
    __swig_getmethods__["voxelDataHandler"] = _ImportersToolbox.VoxelFieldVariable_voxelDataHandler_get
    if _newclass:voxelDataHandler = _swig_property(_ImportersToolbox.VoxelFieldVariable_voxelDataHandler_get, _ImportersToolbox.VoxelFieldVariable_voxelDataHandler_set)
    __swig_setmethods__["decompositionMesh"] = _ImportersToolbox.VoxelFieldVariable_decompositionMesh_set
    __swig_getmethods__["decompositionMesh"] = _ImportersToolbox.VoxelFieldVariable_decompositionMesh_get
    if _newclass:decompositionMesh = _swig_property(_ImportersToolbox.VoxelFieldVariable_decompositionMesh_get, _ImportersToolbox.VoxelFieldVariable_decompositionMesh_set)
    __swig_setmethods__["localCrdMin"] = _ImportersToolbox.VoxelFieldVariable_localCrdMin_set
    __swig_getmethods__["localCrdMin"] = _ImportersToolbox.VoxelFieldVariable_localCrdMin_get
    if _newclass:localCrdMin = _swig_property(_ImportersToolbox.VoxelFieldVariable_localCrdMin_get, _ImportersToolbox.VoxelFieldVariable_localCrdMin_set)
    __swig_setmethods__["localCrdMax"] = _ImportersToolbox.VoxelFieldVariable_localCrdMax_set
    __swig_getmethods__["localCrdMax"] = _ImportersToolbox.VoxelFieldVariable_localCrdMax_get
    if _newclass:localCrdMax = _swig_property(_ImportersToolbox.VoxelFieldVariable_localCrdMax_get, _ImportersToolbox.VoxelFieldVariable_localCrdMax_set)
    __swig_setmethods__["localStartCrd"] = _ImportersToolbox.VoxelFieldVariable_localStartCrd_set
    __swig_getmethods__["localStartCrd"] = _ImportersToolbox.VoxelFieldVariable_localStartCrd_get
    if _newclass:localStartCrd = _swig_property(_ImportersToolbox.VoxelFieldVariable_localStartCrd_get, _ImportersToolbox.VoxelFieldVariable_localStartCrd_set)
    __swig_setmethods__["arraySize"] = _ImportersToolbox.VoxelFieldVariable_arraySize_set
    __swig_getmethods__["arraySize"] = _ImportersToolbox.VoxelFieldVariable_arraySize_get
    if _newclass:arraySize = _swig_property(_ImportersToolbox.VoxelFieldVariable_arraySize_get, _ImportersToolbox.VoxelFieldVariable_arraySize_set)
    __swig_setmethods__["voxelDataArray"] = _ImportersToolbox.VoxelFieldVariable_voxelDataArray_set
    __swig_getmethods__["voxelDataArray"] = _ImportersToolbox.VoxelFieldVariable_voxelDataArray_get
    if _newclass:voxelDataArray = _swig_property(_ImportersToolbox.VoxelFieldVariable_voxelDataArray_get, _ImportersToolbox.VoxelFieldVariable_voxelDataArray_set)
    __swig_setmethods__["dataType"] = _ImportersToolbox.VoxelFieldVariable_dataType_set
    __swig_getmethods__["dataType"] = _ImportersToolbox.VoxelFieldVariable_dataType_get
    if _newclass:dataType = _swig_property(_ImportersToolbox.VoxelFieldVariable_dataType_get, _ImportersToolbox.VoxelFieldVariable_dataType_set)
    __swig_setmethods__["localMin"] = _ImportersToolbox.VoxelFieldVariable_localMin_set
    __swig_getmethods__["localMin"] = _ImportersToolbox.VoxelFieldVariable_localMin_get
    if _newclass:localMin = _swig_property(_ImportersToolbox.VoxelFieldVariable_localMin_get, _ImportersToolbox.VoxelFieldVariable_localMin_set)
    __swig_setmethods__["localMax"] = _ImportersToolbox.VoxelFieldVariable_localMax_set
    __swig_getmethods__["localMax"] = _ImportersToolbox.VoxelFieldVariable_localMax_get
    if _newclass:localMax = _swig_property(_ImportersToolbox.VoxelFieldVariable_localMax_get, _ImportersToolbox.VoxelFieldVariable_localMax_set)
    __swig_setmethods__["zSliceCoord"] = _ImportersToolbox.VoxelFieldVariable_zSliceCoord_set
    __swig_getmethods__["zSliceCoord"] = _ImportersToolbox.VoxelFieldVariable_zSliceCoord_get
    if _newclass:zSliceCoord = _swig_property(_ImportersToolbox.VoxelFieldVariable_zSliceCoord_get, _ImportersToolbox.VoxelFieldVariable_zSliceCoord_set)
    __swig_setmethods__["useNearestCell"] = _ImportersToolbox.VoxelFieldVariable_useNearestCell_set
    __swig_getmethods__["useNearestCell"] = _ImportersToolbox.VoxelFieldVariable_useNearestCell_get
    if _newclass:useNearestCell = _swig_property(_ImportersToolbox.VoxelFieldVariable_useNearestCell_get, _ImportersToolbox.VoxelFieldVariable_useNearestCell_set)
    __swig_setmethods__["useExternalArray"] = _ImportersToolbox.VoxelFieldVariable_useExternalArray_set
    __swig_getmethods__["useExternalArray"] = _ImportersToolbox.VoxelFieldVariable_useExternalArray_get
    if _newclass:useExternalArray = _swig_property(_ImportersToolbox.VoxelFieldVariable_useExternalArray_get, _ImportersToolbox.VoxelFieldVariable_useExternalArray_set)
    __swig_setmethods__["errorStream"] = _ImportersToolbox.VoxelFieldVariable_errorStream_set
    __swig_getmethods__["errorStream"] = _ImportersToolbox.VoxelFieldVariable_errorStream_get
    if _newclass:errorStream = _swig_property(_ImportersToolbox.VoxelFieldVariable_errorStream_get, _ImportersToolbox.VoxelFieldVariable_errorStream_set)
    __swig_setmethods__["minMaxCached"] = _ImportersToolbox.VoxelFieldVariable_minMaxCached_set
    __swig_getmethods__["minMaxCached"] = _ImportersToolbox.VoxelFieldVariable_minMaxCached_get
    if _newclass:minMaxCached = _swig_property(_ImportersToolbox.VoxelFieldVariable_minMaxCached_get, _ImportersToolbox.VoxelFieldVariable_minMaxCached_set)
    def __init__(self): 
        this = _ImportersToolbox.new_VoxelFieldVariable()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ImportersToolbox.delete_VoxelFieldVariable
    __del__ = lambda self : None;
VoxelFieldVariable_swigregister = _ImportersToolbox.VoxelFieldVariable_swigregister
VoxelFieldVariable_swigregister(VoxelFieldVariable)
cvar = _ImportersToolbox.cvar
VoxelFieldVariable_Type = cvar.VoxelFieldVariable_Type


def _VoxelFieldVariable_DefaultNew(*args):
  return _ImportersToolbox._VoxelFieldVariable_DefaultNew(*args)
_VoxelFieldVariable_DefaultNew = _ImportersToolbox._VoxelFieldVariable_DefaultNew

def _VoxelFieldVariable_New(*args):
  return _ImportersToolbox._VoxelFieldVariable_New(*args)
_VoxelFieldVariable_New = _ImportersToolbox._VoxelFieldVariable_New

def _VoxelFieldVariable_AssignFromXML(*args):
  return _ImportersToolbox._VoxelFieldVariable_AssignFromXML(*args)
_VoxelFieldVariable_AssignFromXML = _ImportersToolbox._VoxelFieldVariable_AssignFromXML

def _VoxelFieldVariable_Build(*args):
  return _ImportersToolbox._VoxelFieldVariable_Build(*args)
_VoxelFieldVariable_Build = _ImportersToolbox._VoxelFieldVariable_Build

def _VoxelFieldVariable_Destroy(*args):
  return _ImportersToolbox._VoxelFieldVariable_Destroy(*args)
_VoxelFieldVariable_Destroy = _ImportersToolbox._VoxelFieldVariable_Destroy

def _VoxelFieldVariable_Initialise(*args):
  return _ImportersToolbox._VoxelFieldVariable_Initialise(*args)
_VoxelFieldVariable_Initialise = _ImportersToolbox._VoxelFieldVariable_Initialise

def _VoxelFieldVariable_InterpolateValueAt(*args):
  return _ImportersToolbox._VoxelFieldVariable_InterpolateValueAt(*args)
_VoxelFieldVariable_InterpolateValueAt = _ImportersToolbox._VoxelFieldVariable_InterpolateValueAt

def _VoxelFieldVariable_GetMinGlobalFieldMagnitude(*args):
  return _ImportersToolbox._VoxelFieldVariable_GetMinGlobalFieldMagnitude(*args)
_VoxelFieldVariable_GetMinGlobalFieldMagnitude = _ImportersToolbox._VoxelFieldVariable_GetMinGlobalFieldMagnitude

def _VoxelFieldVariable_GetMaxGlobalFieldMagnitude(*args):
  return _ImportersToolbox._VoxelFieldVariable_GetMaxGlobalFieldMagnitude(*args)
_VoxelFieldVariable_GetMaxGlobalFieldMagnitude = _ImportersToolbox._VoxelFieldVariable_GetMaxGlobalFieldMagnitude

def _VoxelFieldVariable_CacheMinMaxGlobalFieldMagnitude(*args):
  return _ImportersToolbox._VoxelFieldVariable_CacheMinMaxGlobalFieldMagnitude(*args)
_VoxelFieldVariable_CacheMinMaxGlobalFieldMagnitude = _ImportersToolbox._VoxelFieldVariable_CacheMinMaxGlobalFieldMagnitude

def _VoxelFieldVariable_GetMinAndMaxLocalCoords(*args):
  return _ImportersToolbox._VoxelFieldVariable_GetMinAndMaxLocalCoords(*args)
_VoxelFieldVariable_GetMinAndMaxLocalCoords = _ImportersToolbox._VoxelFieldVariable_GetMinAndMaxLocalCoords

def _VoxelFieldVariable_GetMinAndMaxGlobalCoords(*args):
  return _ImportersToolbox._VoxelFieldVariable_GetMinAndMaxGlobalCoords(*args)
_VoxelFieldVariable_GetMinAndMaxGlobalCoords = _ImportersToolbox._VoxelFieldVariable_GetMinAndMaxGlobalCoords

def _VoxelFieldVariable_SetupDataArray(*args):
  return _ImportersToolbox._VoxelFieldVariable_SetupDataArray(*args)
_VoxelFieldVariable_SetupDataArray = _ImportersToolbox._VoxelFieldVariable_SetupDataArray

def _VoxelFieldVariable_TestDataArray(*args):
  return _ImportersToolbox._VoxelFieldVariable_TestDataArray(*args)
_VoxelFieldVariable_TestDataArray = _ImportersToolbox._VoxelFieldVariable_TestDataArray

def _VoxelFieldVariable_SetArrayValue(*args):
  return _ImportersToolbox._VoxelFieldVariable_SetArrayValue(*args)
_VoxelFieldVariable_SetArrayValue = _ImportersToolbox._VoxelFieldVariable_SetArrayValue

def _VoxelFieldVariable_GetArrayIndexIJK(*args):
  return _ImportersToolbox._VoxelFieldVariable_GetArrayIndexIJK(*args)
_VoxelFieldVariable_GetArrayIndexIJK = _ImportersToolbox._VoxelFieldVariable_GetArrayIndexIJK
# This file is compatible with both classic and new-style classes.


